# Handwritten Digit Reader

Recognize a single digit in a scanned math response.

## Run

Install the shared dependencies using the root README, then run `python digit-reader/demo.py` from the root with that environment active.

## Data and evaluation

The bundled scikit-learn digits dataset contains 8×8 samples of human handwriting. The stratified split holds out images. Writer identities are unavailable here, so cross-writer performance is unknown.

## Recorded run

```text
Majority accuracy: 10.2%
Original: 96.7% accuracy; most common mix-up 1 read as 8 (3 times)
One pixel right: 47.8% accuracy; most common mix-up 6 read as 1 (33 times)
```

## Extend the experiment

Translate each test image one pixel right with zero padding. Which digits get confused? Try adding shifted examples to training only and compare both conditions.
