# Practice Forecast

Estimate the chance that a fictional learner answers the next question correctly.

## Run

Install the shared dependencies using the root README, then run `python practice-forecast/demo.py` from the root with that environment active.

## Data and evaluation

All learners and attempts are simulated. Input features are past accuracy, attempt number and current question difficulty. Past accuracy is computed before updating with the current answer. A fresh group of simulated learners forms the test set.

## Recorded run

```text
Training prevalence Brier score: 0.245 (lower is better)
Logistic model Brier score: 0.198 (lower is better)
164 attempts: predicted 20.3%, observed 23.2%
508 attempts: predicted 38.2%, observed 40.4%
532 attempts: predicted 63.1%, observed 63.9%
396 attempts: predicted 83.8%, observed 84.3%
```

## Extend the experiment

Compare predicted and observed success rates in each probability band. Change how quickly the test population learns and see which bands drift.
