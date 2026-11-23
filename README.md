# Machine learning for classroom tools

Five reproducible experiments for an education software portfolio. Each project trains a model, compares it with a simple baseline and prints an error analysis.

## Run on Windows

From the extracted repository folder in PowerShell (tested with Python 3.12):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python guitar-note-lab/demo.py
```

On macOS or Linux use `python3.12 -m venv .venv` and `.venv/bin/python` for the install and run commands. Once dependencies are installed, all demos run offline on CPU.

| Project | Experiment |
|---|---|
| [Handwritten Digit Reader](digit-reader/) | Recognize a single digit in a scanned math response. |
| [Guitar Note Lab](guitar-note-lab/) | Recognize which standard open-string note a simulated pluck plays. |
| [Lesson Timing](lesson-timing/) | Estimate how many minutes to budget for a lesson activity. |
| [Practice Forecast](practice-forecast/) | Estimate the chance that a fictional learner answers the next question correctly. |
| [Question Tagger](question-tagger/) | Suggest a subject label for an editor reviewing a new practice question. |

## Interpreting results

Digit Reader uses the public handwritten digits dataset distributed with scikit-learn. Question Tagger uses original, hand-written examples. The other three projects simulate their inputs. Their metrics describe these experiments only. Each project README includes measured results and a follow-up experiment.

## Development note

OpenAI Codex generated the initial code, fixtures and documentation.
