# Stagwell Brands — Mind-Reading Trick

A themed version of the classic "mind-reading shopping list" mentalism routine.
Instead of grocery items, the participant secretly picks one of **ten well-known
brands that work with Stagwell** (real Stagwell clients or clients of Stagwell
network agencies), and the AI "reads their mind."

## What's here

- **`stagwell_brands_mind_reading_trick.md`** — the full performance handoff:
  the brand list, the secret letter sequence, the opening patter, the
  letter-by-letter script, the per-brand "outs," and a copy-paste prompt for a
  fresh session. This is the thing you actually use.
- **`tools/generate_anagram.py`** — the search that produced the routine. It
  finds a valid **progressive anagram** over a pool of confirmed Stagwell brands
  and verifies the result.

## How the trick works (method)

It's a **progressive anagram**. The performer tests letters in a fixed secret
order. Each brand on the list is missing a *different* letter from that
sequence, so the **first letter the participant says "no" to** uniquely
identifies their brand. One brand (United Airlines) contains every test letter,
so "yes to everything" identifies it.

- Brands: PepsiCo, Starbucks, Target, Apple, The Coca-Cola Company, National
  Football League, Stellantis, General Mills, Delta Air Lines, United Airlines
- Secret letter order: **A → E → L → N → I → S → R → D → U**

See the trick file for the full mapping and the verification table.

## Regenerating / customizing

To rebuild the routine (e.g. with a different brand pool):

```bash
python3 tools/generate_anagram.py
```

Edit the `BRANDS` list in that script and rerun. The search maximizes the number
of brands it can chain and prints a verified mapping. Longer, letter-rich
multi-word brand names (e.g. "United Airlines") make longer chains possible.
