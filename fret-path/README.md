# Fret path
One pitch can appear in several places on a guitar. Given a melody in MIDI note numbers, this C++17 CLI searches standard tuning up to fret 20 for the sequence with the least total fret and string movement. Each fret or string of movement costs one point. The first position is free.

With GCC on Windows run:
```powershell
g++ -std=c++17 -O2 main.cpp -o fret-path.exe
.\fret-path.exe 40 41 43
```
Expect string 6 at frets 0, 1 and 3, for a movement score of 3. Try `64 67 69 67 64` for a melody with multiple fingerings. On Linux or macOS compile with `c++ -std=c++17 main.cpp -o fret-path` and run `./fret-path`.

Each candidate position retains its cheapest predecessor. Backtracking recovers the tabs. The cost ignores hand position changes when ringing open strings.

**Make it yours.** Transcribe a riff you play, evaluate the suggested fingering on your guitar, and adjust the cost of crossing strings. Save both outputs and explain your preference.
