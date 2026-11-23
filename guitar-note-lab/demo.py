"""Learn the six standard open-string labels from synthesized plucks."""
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

NOTES = ["E2", "A2", "D3", "G3", "B3", "E4"]
HZ = [82.41, 110, 146.83, 196, 246.94, 329.63]
RATE = 4096


def examples(seed, count, bright):
    rng = np.random.default_rng(seed)
    time = np.arange(1024) / RATE
    features, labels = [], []
    for label, frequency in zip(NOTES, HZ):
        for _ in range(count):
            fundamental = frequency * 2 ** (rng.uniform(-20, 20) / 1200)
            amplitudes = rng.uniform(.2, .7, 4)
            amplitudes[0] = rng.uniform(.06, .3) if bright else 1
            signal = sum(a * np.sin(2 * np.pi * fundamental * k * time + rng.uniform(0, 2*np.pi))
                         for k, a in enumerate(amplitudes, 1))
            signal *= np.exp(-time * rng.uniform(2, 9))
            signal += rng.normal(0, .07, len(time))
            spectrum = abs(np.fft.rfft(signal * np.hanning(len(time))))[:300]
            features.append(spectrum / np.linalg.norm(spectrum))
            labels.append(label)
    return features, labels


def main():
    x, y = examples(4, 40, False)
    test, actual = examples(41, 30, True)
    model = KNeighborsClassifier(n_neighbors=3).fit(x, y)
    guess = model.predict(test)
    base = DummyClassifier(strategy="most_frequent").fit(x, y)
    print(f"Majority accuracy: {base.score(test, actual):.1%}")
    print(f"Weak-fundamental test accuracy: {accuracy_score(actual, guess):.1%}")
    print("Rows = actual, columns = predicted:", NOTES)
    print(confusion_matrix(actual, guess, labels=NOTES))


if __name__ == "__main__":
    main()
