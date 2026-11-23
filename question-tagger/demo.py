"""Suggest a subject tag for a curriculum editor."""
import argparse
import csv
from pathlib import Path
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", help="Optional editor-written question")
    args = parser.parse_args()
    with Path(__file__).with_name("questions.tsv").open(encoding="utf8") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    train = [r for r in rows if r["split"] == "train"]
    test = [r for r in rows if r["split"] == "test"]
    model = make_pipeline(TfidfVectorizer(stop_words="english"), MultinomialNB())
    model.fit([r["text"] for r in train], [r["label"] for r in train])
    base = DummyClassifier(strategy="most_frequent").fit([[0]] * len(train), [r["label"] for r in train])
    labels = [r["label"] for r in test]
    predicted = model.predict([r["text"] for r in test])
    for name, tags in [("Majority", base.predict([[0]] * len(test))), ("Naive Bayes", predicted)]:
        print(f"{name} macro F1: {f1_score(labels, tags, average='macro'):.3f}")
    vectorizer = model.steps[0][1]
    for row, guess in zip(test, predicted):
        if row["label"] != guess or not vectorizer.transform([row["text"]]).nnz:
            print(f'{row["text"]} | expected {row["label"]}, raw prediction {guess}')
    if args.text:
        if vectorizer.transform([args.text]).nnz:
            print("Suggested tag:", model.predict([args.text])[0])
        else:
            print("Editor review: no known terms.")


if __name__ == "__main__":
    main()
