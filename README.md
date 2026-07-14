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
- **`index.html`** — a mobile-first "force" prop: a Stagwell-branded brand
  directory (Prussian-blue + gold palette) presented as an **endless** discovery
  feed of 4,000 partners in random order. The participant scrolls for as long as
  they like; the instant they **stop**, the list smoothly settles onto the same
  ten "Flagship Partners" (the trick brands), each shown with its logo — so any
  stop lands on the ten. The ten stay hidden while scrolling (no tell). Fully
  self-contained (works offline — no venue wifi needed).
- **`vercel.json`** — static-hosting config so the repo deploys to Vercel as-is.

  > Built as an internal performance aid for a Stagwell event. Flagship logos are
  > lightweight inline-SVG recreations in brand colors; swap in official brand
  > assets by editing the `LOGOS` map in `index.html`.

## Deploying to Vercel

The site is a single static `index.html`, so no build step is needed.

**Option A — Vercel dashboard (no CLI):**
1. Go to vercel.com → **Add New… → Project → Import Git Repository**.
2. Select `caras-new-voices/stagwell-brands-magic`.
3. Set the **Production Branch** to `claude/stagwell-brands-magic-trick-x2gz4u`
   (or merge it into `main` first).
4. **Framework Preset: Other**, leave build/output empty → **Deploy**.

**Option B — Vercel CLI (from your machine):**
```bash
git clone <repo> && cd stagwell-brands-magic
npx vercel        # preview deploy
npx vercel --prod # production deploy
```

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
