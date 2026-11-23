# Guitar Note Lab

Recognize which standard open-string note a simulated pluck plays.

## Run

Install the shared dependencies using the root README, then run `python guitar-note-lab/demo.py` from the root with that environment active.

## Data and evaluation

The generator varies tuning, phase, decay, harmonics and noise. Training uses 240 simulated plucks and testing uses 180 fresh plucks whose fundamental is weaker. The six labels cover open strings in standard tuning.

## Recorded run

```text
Majority accuracy: 16.7%
Weak-fundamental test accuracy: 100.0%
Rows = actual, columns = predicted: ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']
[[30  0  0  0  0  0]
 [ 0 30  0  0  0  0]
 [ 0  0 30  0  0  0]
 [ 0  0  0 30  0  0]
 [ 0  0  0  0 30  0]
 [ 0  0  0  0  0 30]]
```

## Extend the experiment

Read the confusion matrix and find the string most often confused with another. Record examples on your Telecaster and reserve an entire recording session for a future test.
