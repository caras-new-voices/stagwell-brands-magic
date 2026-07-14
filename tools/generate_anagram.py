#!/usr/bin/env python3
"""Generate the Stagwell-brands progressive anagram.

Finds the longest chain of brands such that, for a fixed secret letter order,
each brand is uniquely identified by the FIRST letter it is missing (and one
brand contains every test letter -> "yes to all"). Uses a letter-order DFS with
an incremental bipartite matching so every accepted prefix is guaranteed to have
a valid, distinct brand assignment.

Run: python3 tools/generate_anagram.py
"""
import sys
sys.setrecursionlimit(100000)

# Confirmed well-known brands tied to Stagwell agencies (plus richer name variants).
BRANDS = [
    "Starbucks", "PepsiCo", "Target", "Apple", "Delta Air Lines", "Walmart",
    "Dove", "Amazon", "Microsoft", "Yeti", "Adidas", "Bayer", "FIFA", "TikTok",
    "Toyota", "Airbus", "Stellantis", "Coca-Cola", "Netflix", "Nike",
    "T-Mobile", "Warby Parker", "Robinhood", "United Airlines", "Airbnb",
    "American Express", "LEGO", "Google", "Dairy Queen", "La-Z-Boy",
    "McCormick", "JPMorgan Chase", "HBO Max", "Campari", "Tipico",
    "Perdue Farms", "The UPS Store", "NBC", "NFL", "elf Beauty",
    "National Football League", "The Coca-Cola Company", "General Mills",
]

def letters(name):
    return frozenset(c for c in name.upper() if c.isalpha())

LS = {b: letters(b) for b in BRANDS}

overall = {"len": 0, "order": [], "match": {}, "final": None}

def search_final(final):
    universe = sorted(LS[final])
    pool = [b for b in BRANDS if b != final]
    best = {"len": 0, "order": [], "match": {}}

    # match_pos[pos] = brand ; match_brand[brand] = pos
    def try_augment(pos, cand_of, match_pos, match_brand, visited):
        for b in cand_of[pos]:
            if b in visited:
                continue
            visited.add(b)
            if b not in match_brand or try_augment(match_brand[b], cand_of, match_pos, match_brand, visited):
                match_pos[pos] = b
                match_brand[b] = pos
                return True
        return False

    def dfs(P, used_letters, order, cand_of, match_pos, match_brand):
        m = len(order)
        if m > best["len"]:
            best.update(len=m, order=list(order), match=dict(match_pos))
        for L in universe:
            if L in used_letters:
                continue
            # candidates for the new position m: contain P, miss L
            cands = [b for b in pool if L not in LS[b] and P <= LS[b]]
            if not cands:
                continue
            cand_of[m] = cands
            mp, mb = dict(match_pos), dict(match_brand)
            if try_augment(m, cand_of, mp, mb, set()):
                dfs(P | {L}, used_letters | {L}, order + [L], cand_of, mp, mb)
            del cand_of[m]

    dfs(frozenset(), frozenset(), [], {}, {}, {})
    return best

# richest finals first
for final in sorted(BRANDS, key=lambda b: -len(LS[b])):
    if len(LS[final]) < 7:
        break
    b = search_final(final)
    if b["len"] + 1 > overall["len"]:
        overall = {"len": b["len"] + 1, "order": b["order"], "match": b["match"], "final": final}
        print(f"  [+] final={final:18s} items={b['len']+1} letters={''.join(b['order'])}")

order = overall["order"]
match = overall["match"]
final = overall["final"]
print(f"\nBEST items = {overall['len']}")
print(f"Final (all-yes) = {final}")
print(f"Letter sequence = {' -> '.join(order)}\n")
for i, L in enumerate(order):
    b = match[i]
    print(f"  first NO on {L}  ->  {b:22s} (has: {''.join(sorted(LS[b]))})")
print(f"  YES to all       ->  {final:22s} (has: {''.join(sorted(LS[final]))})")

print("\n--- verify ---")
allitems = [match[i] for i in range(len(order))] + [final]
ok = True
for pos, b in enumerate(allitems):
    firstno = next((idx for idx, L in enumerate(order) if L not in LS[b]), None)
    exp = None if b == final else pos
    if firstno != exp:
        print(f"FAIL {b}: firstno {firstno} expected {exp}"); ok = False
if len(set(allitems)) != len(allitems):
    print("FAIL duplicate brand"); ok = False
print("ALL OK" if ok else "PROBLEMS")
