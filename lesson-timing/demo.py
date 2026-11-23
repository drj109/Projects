"""Estimate activity duration and inspect residuals on unseen activity templates."""
import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def sample():
    rng = np.random.default_rng(82)
    groups = np.repeat(np.arange(80), 5)
    words = rng.integers(50, 1000, 80)[groups]
    questions = rng.integers(1, 12, 80)[groups]
    discussion = rng.integers(0, 2, 80)[groups]
    minutes = (2 + words / 130 + .75 * questions + 4 * discussion
               + rng.normal(0, 1.3, 80)[groups] + rng.normal(0, 1, len(groups)))
    return np.column_stack((words, questions, discussion)), minutes, groups


def main():
    x, y, groups = sample()
    train, test = next(GroupShuffleSplit(n_splits=1, test_size=.25, random_state=12).split(x, groups=groups))
    model = make_pipeline(StandardScaler(), Ridge()).fit(x[train], y[train])
    baseline = DummyRegressor(strategy="median").fit(x[train], y[train])
    pred = model.predict(x[test])
    print(f"Median baseline MAE: {mean_absolute_error(y[test], baseline.predict(x[test])):.2f} min")
    print(f"Ridge MAE: {mean_absolute_error(y[test], pred):.2f} min")
    worst = np.argmax(abs(y[test] - pred))
    print(f"Largest miss: template {groups[test[worst]]}, actual {y[test][worst]:.1f}, predicted {pred[worst]:.1f} min")
    print(f"Example with 400 words, 5 questions and discussion: {model.predict([[400, 5, 1]])[0]:.1f} min")


if __name__ == "__main__":
    main()
