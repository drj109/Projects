# Rush hour
Find the earliest minute when a community center had the most simultaneous visitors. The sample is synthetic. Go validates a same-day CSV and emits integer minute pairs. Rust sums arrivals and departures at each minute, then scans for the first peak. A departure frees its place immediately.

With Go 1.21+ and stable Rust installed, run from this folder in PowerShell:
```powershell
rustc peak.rs -o peak.exe
rustc --test peak.rs -o checks.exe
.\checks.exe
go run normalize.go visits.csv | .\peak.exe
```
Expected output: **Peak: 3 visitors at 12:07**. On Unix use `./peak.exe` for the executable. Run the Go stage alone to inspect the intermediate records. A malformed CSV makes that stage exit with an error before emitting any records.

**Make it yours.** Extend the Rust report to return every time span at peak occupancy. Test two separate periods tied for the same peak.
