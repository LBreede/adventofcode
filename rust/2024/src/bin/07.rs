use adv_code_2024::*;
use anyhow::{Context, Result};
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "07";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let mut answer = 0;
        for line in reader.lines().map_while(Result::ok) {
            let (lhs, rhs) = line.split_once(": ").unwrap();
            let target = lhs.parse::<usize>()?;
            let numbers: Vec<usize> = rhs
                .split_whitespace()
                .map(|x| x.parse::<usize>().unwrap())
                .collect();
            answer +=
                calculate(target, numbers, vec![Operation::Add, Operation::Multiply]).unwrap_or(0);
        }
        Ok(answer)
    }

    assert_eq!(3749, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let mut answer = 0;
        for line in reader.lines().map_while(Result::ok) {
            let (lhs, rhs) = line.split_once(": ").unwrap();
            let target = lhs.parse::<usize>()?;
            let numbers: Vec<usize> = rhs
                .split_whitespace()
                .map(|x| x.parse::<usize>().unwrap())
                .collect();
            answer += calculate(
                target,
                numbers,
                vec![Operation::Add, Operation::Multiply, Operation::Concat],
            )
            .unwrap_or(0);
        }
        Ok(answer)
    }

    assert_eq!(11387, part2(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

#[derive(Debug, Copy, Clone)]
enum Operation {
    Add,
    Multiply,
    Concat,
}

/// Generate all possible combinations of operations
fn generate_combinations(n: usize, elements: Vec<Operation>) -> Vec<Vec<Operation>> {
    let length = n - 1;

    if length == 0 {
        return vec![vec![]];
    }

    let mut result = vec![];

    fn helper(
        current: &mut Vec<Operation>,
        result: &mut Vec<Vec<Operation>>,
        elements: &[Operation],
        length: usize,
    ) {
        if current.len() == length {
            result.push(current.clone());
            return;
        }

        for &element in elements {
            current.push(element);
            helper(current, result, elements, length);
            current.pop();
        }
    }

    helper(&mut vec![], &mut result, &elements, length);
    result
}

/// Calculate the target number using the given numbers and operations
/// Returns `None` if the target cannot be reached
fn calculate(target: usize, numbers: Vec<usize>, elements: Vec<Operation>) -> Option<usize> {
    let combinations = generate_combinations(numbers.len(), elements);
    for operations in combinations {
        let mut numbers = numbers.iter();
        let mut result = *numbers.next().unwrap();
        for (num, op) in numbers.zip(operations.iter()) {
            match op {
                Operation::Add => result += num,
                Operation::Multiply => result *= num,
                Operation::Concat => result = concat_digits(result, *num),
            }
        }
        if result == target {
            return Some(result);
        }
    }
    None
}

/// Concatenate two numbers
fn concat_digits(a: usize, b: usize) -> usize {
    a * 10_usize.pow(get_digits(b)) + b
}

/// Get the number of digits in a number
fn get_digits(mut num: usize) -> u32 {
    if num == 0 {
        return 1;
    }
    let mut digits = 0;
    while num > 0 {
        digits += 1;
        num /= 10;
    }
    digits
}
