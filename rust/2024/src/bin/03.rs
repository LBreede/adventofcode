use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use regex::Regex;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "03";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
const EXAMPLE2: &str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)")?;
        let mut answer = 0;
        for line in reader.lines().map_while(Result::ok) {
            for (_, [lhs, rhs]) in re.captures_iter(line.as_str()).map(|c| c.extract()) {
                let lhs: usize = lhs.parse()?;
                let rhs: usize = rhs.parse()?;
                answer += lhs * rhs;
            }
        }
        Ok(answer)
    }

    assert_eq!(161, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|(don't)\(\)|(do)\(\)")?;
        let mut answer = 0;
        let mut ignore = false;
        for line in reader.lines().map_while(Result::ok) {
            for capture in re.captures_iter(line.as_str()) {
                match capture.get(0).unwrap().as_str() {
                    m if m.starts_with("mul(") => {
                        if !ignore {
                            let lhs: usize = capture.get(1).unwrap().as_str().parse()?;
                            let rhs: usize = capture.get(2).unwrap().as_str().parse()?;
                            answer += lhs * rhs;
                        }
                    }
                    m if m.starts_with("don't(") => {
                        ignore = true;
                    }
                    m if m.starts_with("do(") => {
                        ignore = false;
                    }
                    _ => unreachable!(),
                }
            }
        }
        Ok(answer)
    }

    assert_eq!(48, part2(BufReader::new(EXAMPLE2.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}
