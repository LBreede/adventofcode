use adv_code_2024::*;
use anyhow::*;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use itertools::Itertools;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "01";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const TEST: &str = "\
3   4
4   3
2   5
1   3
3   9
3   3
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let (left, right) = split_columns(reader)?;
        let answer: usize = left
            .iter()
            .sorted()
            .zip(right.iter().sorted())
            .map(|(&a, &b)| a.abs_diff(b))
            .sum();

        Ok(answer)
    }

    assert_eq!(11, part1(BufReader::new(TEST.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let (left, right) = split_columns(reader)?;
        let answer = left
            .iter()
            .map(|&a| right.iter().filter(|&b| *b == a).count() * a)
            .sum();

        Ok(answer)
    }

    assert_eq!(31, part2(BufReader::new(TEST.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

fn split_columns<R: BufRead>(reader: R) -> Result<(Vec<usize>, Vec<usize>)> {
    let mut left: Vec<usize> = Vec::new();
    let mut right: Vec<usize> = Vec::new();

    for line in reader.lines().map_while(Result::ok) {
        let (a, b) = line.split_once("   ").unwrap();
        left.push(a.parse()?);
        right.push(b.parse()?);
    }
    Ok((left, right))
}
