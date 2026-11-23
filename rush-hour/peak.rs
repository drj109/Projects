use std::io::{self, BufRead};

fn peak(input: impl BufRead) -> Result<Option<(i32, usize)>, String> {
    let mut deltas = [0i32; 1441];
    for line in input.lines() {
        let line = line.map_err(|e| e.to_string())?;
        let fields: Vec<_> = line.split_whitespace().collect();
        if fields.len() != 2 { return Err("expected start and end minutes".into()); }
        let parse = |s: &str| s.parse::<usize>().map_err(|_| "invalid minute".to_string());
        let (start, end) = (parse(fields[0])?, parse(fields[1])?);
        if start >= end || end > 1440 { return Err("invalid visit interval".into()); }
        deltas[start] += 1;
        deltas[end] -= 1;
    }
    let (mut current, mut high, mut first) = (0, 0, 0);
    for (minute, delta) in deltas.iter().enumerate() {
        current += *delta;
        if current > high { high = current; first = minute; }
    }
    Ok((high > 0).then_some((high, first)))
}

fn main() {
    match peak(io::stdin().lock()) {
        Ok(Some((count, minute))) => println!("Peak: {} visitors at {:02}:{:02}", count, minute / 60, minute % 60),
        Ok(None) => println!("No visits"),
        Err(message) => { eprintln!("{}", message); std::process::exit(1); }
    }
}

#[test]
fn touching_visits_do_not_overlap() {
    assert_eq!(peak(&b"60 65\n65 70\n"[..]), Ok(Some((1, 60))));
}

#[test]
fn rejects_reversed_interval() {
    assert!(peak(&b"65 60\n"[..]).is_err());
}
