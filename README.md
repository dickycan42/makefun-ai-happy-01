# makefun-ai-happy-01 — "One Lick for You, One for Me"

Entry for the make.fun competition **ai-happy-01** ("Make the AI judge
happy"). The program writes one image to the grader's output path.

## The image

A warm storybook illustration of a little boy in a red sweater sitting on
a park bench at golden hour, laughing as he shares his ice cream cone with
a tiny orange kitten that stands on its hind legs to lick it. One small,
specific, happy moment: a child sharing his treat with a kitten. Warm
honey-gold light, soft green park background, no text in the image.

## How it works

`main.py` (Python 3.13, standard library only) copies the image stored in
this repository as `entry.png` into the output directory as `entry.png`,
then verifies the copy byte for byte by comparing SHA-256 digests of the
source and the copy. It uses no network, no randomness and no timestamps,
so two runs always write exactly the same bytes.

The image file is a JPEG (told apart by its magic bytes, as the rules
allow) kept under the name `entry.png`, 1024 x 1024 pixels and under 1 MiB.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output`, the grader's
directory.

## Files

- `main.py` — the entry program
- `entry.png` — the image (JPEG bytes, 1024 x 1024, < 1 MiB)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the entry's payout wallet
