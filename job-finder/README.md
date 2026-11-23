# First Shift
A browser-based job explorer for someone writing their first résumé. A Vue form sends skills to Flask. Scikit-learn fits a TF-IDF vocabulary on eight fictional role descriptions and ranks them by cosine similarity. Each result lists the terms contributing most to its score.

## Run on Windows
From this folder, with Python 3.12 installed:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python -m flask --app app run
```
Open http://127.0.0.1:5000. The browser downloads Vue from a pinned CDN URL. Try `scan packages in a warehouse`, then `xylophone` to see the empty-result path.

## Experiment
A driver who says “move boxes” can miss the parcel role because the corpus uses different words. Write ten example queries and expected roles before editing the corpus. Measure how often the expected role ranks first, add synonyms, and report which queries changed. Similarity measures text overlap. This small corpus cannot estimate hiring likelihood.
