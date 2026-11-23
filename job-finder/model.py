import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class JobIndex:
    def __init__(self, path):
        with Path(path).open(encoding="utf-8", newline="") as source:
            self.jobs = list(csv.DictReader(source))
        self.vectorizer = TfidfVectorizer(strip_accents="unicode", ngram_range=(1, 2))
        documents = [job["role"] + " " + job["skills"] for job in self.jobs]
        self.matrix = self.vectorizer.fit_transform(documents)
        self.terms = self.vectorizer.get_feature_names_out()

    def search(self, skills, limit=3):
        query = self.vectorizer.transform([skills])
        scores = linear_kernel(query, self.matrix)[0]
        matches = []
        for i in sorted(range(len(scores)), key=lambda i: -scores[i]):
            if scores[i] <= 0:
                break
            overlap = query.multiply(self.matrix[i]).tocsr()
            terms = sorted(zip(overlap.indices, overlap.data), key=lambda item: -item[1])
            matches.append(dict(role=self.jobs[i]["role"], score=round(float(scores[i]), 4),
                                terms=[self.terms[j] for j, _ in terms[:4]]))
            if len(matches) == limit:
                break
        return matches
