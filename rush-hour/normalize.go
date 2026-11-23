package main

import (
    "encoding/csv"
    "fmt"
    "io"
    "os"
    "strconv"
    "time"
)

// Each accepted visit occupies one place during [arrival, departure).
func normalize(source io.Reader, out io.Writer) error {
    reader := csv.NewReader(source)
    header, err := reader.Read()
    if err != nil { return err }
    if len(header) != 2 || header[0] != "arrival" || header[1] != "departure" {
        return fmt.Errorf("expected arrival,departure header")
    }
    type visit struct { start, end int }
    var visits []visit
    minute := func(s string) (int, error) {
        t, err := time.Parse("15:04", s)
        if err != nil { return 0, err }
        return t.Hour()*60 + t.Minute(), nil
    }
    for row := 2; ; row++ {
        fields, err := reader.Read()
        if err == io.EOF { break }
        if err != nil { return fmt.Errorf("row %d: %w", row, err) }
        a, e1 := minute(fields[0])
        b, e2 := minute(fields[1])
        if e1 != nil || e2 != nil || b <= a { return fmt.Errorf("invalid interval on row %d", row) }
        visits = append(visits, visit{a,b})
    }
    for _, v := range visits {
        if _, err := fmt.Fprintf(out, "%d %d\n", v.start, v.end); err != nil { return err }
    }
    return nil
}

func main() {
    if len(os.Args) != 2 { fmt.Fprintln(os.Stderr, "pass the visits CSV path"); os.Exit(2) }
    source, err := os.Open(os.Args[1])
    if err == nil {
        defer source.Close()
        err = normalize(source, os.Stdout)
    }
    if err != nil { fmt.Fprintln(os.Stderr, err); os.Exit(1) }
}
