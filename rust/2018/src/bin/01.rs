use adv_code_2018::*;
use anyhow::*;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "01";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
+1
-2
+3
+1
";

const EXAMPLE_2_1: &str = "\
+1
-1
";

fn main() -> Result<()> {
    start_day(DAY);

    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<i32> {
        reader.lines().map(|line| Ok(line?.parse::<i32>()?)).sum()
    }
    assert_eq!(3, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);

    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<i32> {
        let changes: Vec<i32> = reader
            .lines()
            .map(|l| Ok(l?.parse()?))
            .collect::<Result<_>>()?;

        let mut seen = HashSet::new();
        let mut freq = 0;
        seen.insert(freq);

        for change in changes.iter().cycle() {
            freq += change;
            if !seen.insert(freq) {
                return Ok(freq);
            }
        }

        unreachable!("cycle() is infinite unless input is empty");
    }

    assert_eq!(2, part2(BufReader::new(EXAMPLE.as_bytes()))?);
    assert_eq!(0, part2(BufReader::new(EXAMPLE_2_1.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);

    Ok(())
}
