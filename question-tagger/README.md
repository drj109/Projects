# Question Tagger

Suggest a subject label for an editor reviewing a new practice question.

## Run

Install the shared dependencies using the root README, then run `python question-tagger/demo.py` from the root with that environment active.

## Data and evaluation

The TSV contains 18 original training prompts and nine held-out prompts across math, science and reading. The vocabulary is fit only on the training prompts. Macro F1 gives each subject equal weight.

## Recorded run

```text
Majority macro F1: 0.167
Naive Bayes macro F1: 0.775
How many beats make up half a bar? | expected math, raw prediction math
Where does a seed get what it needs to sprout? | expected science, raw prediction reading
Why might the speaker repeat the final line? | expected reading, raw prediction math
```

## Extend the experiment

Try python demo.py --text "Why does the bulb glow?" from this folder. Test vocabulary gaps, inspect errors and add your own independent questions before changing the model.
