# Lesson Timing

Estimate how many minutes to budget for a lesson activity.

## Run

Install the shared dependencies using the root README, then run `python lesson-timing/demo.py` from the root with that environment active.

## Data and evaluation

A seeded simulator creates 80 activity templates with five noisy timing observations each. All observations for a template stay together when splitting. The target formula is approximately linear.

## Recorded run

```text
Median baseline MAE: 3.31 min
Ridge MAE: 1.60 min
Largest miss: template 21, actual 12.2, predicted 17.3 min
Example with 400 words, 5 questions and discussion: 12.8 min
```

## Extend the experiment

Inspect the worst residual. Try removing the discussion feature and compare the change in mean absolute error, measured in minutes.
