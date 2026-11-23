"""Read handwritten digits and measure sensitivity to a horizontal shift."""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def shift_right(images):
    shifted = np.zeros_like(images)
    shifted[:, :, 1:] = images[:, :, :-1]
    return shifted


def main():
    images, labels = load_digits(return_X_y=True)
    train, test, y_train, y_test = train_test_split(
        images, labels, test_size=0.25, stratify=labels, random_state=23)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1500))
    model.fit(train, y_train)
    baseline = DummyClassifier(strategy="most_frequent").fit(train, y_train)
    print(f"Majority accuracy: {baseline.score(test, y_test):.1%}")
    for name, pixels in [("Original", test), ("One pixel right", shift_right(test.reshape(-1, 8, 8)).reshape(-1, 64))]:
        predictions = model.predict(pixels)
        counts = confusion_matrix(y_test, predictions, labels=np.arange(10))
        np.fill_diagonal(counts, 0)
        actual, predicted = np.unravel_index(counts.argmax(), counts.shape)
        print(f"{name}: {accuracy_score(y_test, predictions):.1%} accuracy; most common mix-up "
              f"{actual} read as {predicted} ({counts.max()} times)")


if __name__ == "__main__":
    main()
