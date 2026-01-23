use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "11";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "0 1 10 99 999";
const EXAMPLE2: &str = "125 17";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(mut reader: R, iterations: usize) -> Result<usize> {
        let mut content = String::new();
        reader.read_line(&mut content)?;

        let mut numbers: HashMap<usize, usize> = content
            .split_whitespace()
            .map(|s| (s.parse::<usize>().expect("should be a number"), 1))
            .collect();

        for _ in 0..iterations {
            let mut new_numbers = HashMap::new();
            for (&n, &count) in &numbers {
                match n {
                    0 => *new_numbers.entry(1).or_insert(0) += count,
                    n if number_of_digits(n) % 2 == 0 => {
                        let div = 10usize.pow((number_of_digits(n) / 2) as u32);
                        *new_numbers.entry(n / div).or_insert(0) += count;
                        *new_numbers.entry(n % div).or_insert(0) += count;
                    }
                    n => *new_numbers.entry(n * 2024).or_insert(0) += count,
                }
            }
            numbers = new_numbers;
        }
        Ok(numbers.values().sum())
    }

    assert_eq!(7, part1(BufReader::new(EXAMPLE.as_bytes()), 1)?);
    assert_eq!(22, part1(BufReader::new(EXAMPLE2.as_bytes()), 6)?);
    assert_eq!(55312, part1(BufReader::new(EXAMPLE2.as_bytes()), 25)?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file, 25)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    // println!("\n=== Part 2 ===");
    //
    // fn part2<R: BufRead>(reader: R) -> Result<usize> {
    //     Ok(0)
    // }
    //
    // assert_eq!(0, part2(BufReader::new(EXAMPLE.as_bytes()))?);
    //
    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file, 75)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

fn number_of_digits(n: usize) -> usize {
    match n {
        0 => 1,
        n => (n as f64).log10() as usize + 1,
    }
}
