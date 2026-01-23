use adv_code_2024::*;
use anyhow::*;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use itertools::Itertools;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "02";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const TEST: &str = "\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let answer = reader
            .lines()
            .map_while(Result::ok)
            .map(|line| {
                line.split_whitespace()
                    .map(|n| n.parse::<i32>().expect("should only have numbers"))
                    .collect::<Vec<i32>>()
            })
            .filter(|ns| safe_report(ns))
            .count();
        Ok(answer)
    }

    assert_eq!(2, part1(BufReader::new(TEST.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let mut answer = 0;
        'outer: for line in reader.lines().map_while(Result::ok) {
            let numbers: Vec<i32> = line
                .split_whitespace()
                .map(|n| n.parse::<i32>().expect("should only have number"))
                .collect();

            if safe_report(&numbers) {
                answer += 1;
                continue 'outer;
            }

            for i in 0..numbers.len() {
                let new_numbers: Vec<i32> = numbers
                    .iter()
                    .copied()
                    .enumerate()
                    .filter_map(|(j, val)| if j == i { None } else { Some(val) })
                    .collect();
                if safe_report(&new_numbers) {
                    answer += 1;
                    continue 'outer;
                }
            }
        }
        Ok(answer)
    }

    assert_eq!(4, part2(BufReader::new(TEST.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

fn safe_report(report: &[i32]) -> bool {
    let differences: Vec<i32> = report.iter().tuple_windows().map(|(a, b)| b - a).collect();
    (differences.iter().all(|&x| x > 0) || differences.iter().all(|&x| x < 0))
        && differences.iter().all(|&x| x.abs() >= 1 && x.abs() <= 3)
}
