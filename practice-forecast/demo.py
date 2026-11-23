"""Forecast the next simulated practice response using previous attempts only."""
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss


def simulate(seed, learners):
    rng = np.random.default_rng(seed)
    rows, results = [], []
    for _ in range(learners):
        ability = rng.normal()
        correct = 0
        for attempt in range(16):
            difficulty = rng.choice([-1., 0., 1.])
            past_rate = (correct + 1) / (attempt + 2)
            rows.append([past_rate, attempt, difficulty])
            chance = 1 / (1 + np.exp(-(ability + .07 * attempt - difficulty)))
            outcome = int(rng.random() < chance)
            results.append(outcome)
            correct += outcome
    return np.array(rows), np.array(results)


def main():
    x, y = simulate(8, 250)
    test, actual = simulate(18, 100)
    model = LogisticRegression().fit(x, y)
    baseline = DummyClassifier(strategy="prior").fit(x, y)
    for name, estimator in [("Training prevalence", baseline), ("Logistic model", model)]:
        p = estimator.predict_proba(test)[:, 1]
        print(f"{name} Brier score: {brier_score_loss(actual, p):.3f} (lower is better)")
    probabilities = model.predict_proba(test)[:, 1]
    for low, high in [(0, .25), (.25, .5), (.5, .75), (.75, 1.01)]:
        subset = (probabilities >= low) & (probabilities < high)
        if subset.any():
            print(f"{subset.sum()} attempts: predicted {probabilities[subset].mean():.1%}, observed {actual[subset].mean():.1%}")


if __name__ == "__main__":
    main()
