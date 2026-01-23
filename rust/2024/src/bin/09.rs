use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use itertools::all;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "09";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "2333133121414131402";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let mut filesystem = parse_filesystem(reader);
        loop {
            let first_none = filesystem.iter().position(|x| x.is_none()).unwrap();
            let last_some = filesystem.iter().rposition(|x| x.is_some()).unwrap();
            if first_none < last_some {
                filesystem.swap(first_none, last_some);
            } else {
                break;
            }
        }
        Ok(filesystem
            .iter()
            .take_while(|&&x| x.is_some())
            .enumerate()
            .map(|(i, &x)| i * x.unwrap())
            .sum())
    }

    assert_eq!(1928, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let mut filesystem = parse_filesystem(reader);
        let id = filesystem.iter().filter_map(|x| *x).max().unwrap() + 1;

        // We can skip 0 here since it should always be in its right place
        for i in (1..id).rev() {
            // Find the chunk of files with id == i
            let chunk: Vec<usize> = filesystem
                .iter()
                .enumerate()
                .skip_while(|(_, &x)| x != Some(i))
                .take_while(|(_, &x)| x == Some(i))
                .map(|(i, _)| i)
                .collect();

            // Loop from 0 to the beginning of the chunk
            for j in 0..=chunk[0] - chunk.len() {
                // Check if the chunk fits in the filesystem
                if all(&filesystem[j..j + chunk.len()], |x| x.is_none()) {
                    // Swap the chunk with the empty space
                    for (k, &index) in chunk.iter().enumerate() {
                        filesystem.swap(j + k, index);
                    }
                    break;
                }
            }
        }
        Ok(filesystem
            .iter()
            .enumerate()
            .map(|(i, &x)| i * x.unwrap_or(0))
            .sum())
    }

    assert_eq!(2858, part2(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

fn parse_filesystem<R: BufRead>(reader: R) -> Vec<Option<usize>> {
    let mut filesystem: Vec<Option<usize>> = Vec::new();
    let mut id: usize = 0;
    for (i, n) in reader
        .bytes()
        .map_while(Result::ok)
        .map(|b| b - 48)
        .enumerate()
    {
        if i % 2 == 0 {
            for _ in 0..n {
                filesystem.push(Some(id));
            }
            id += 1
        } else {
            for _ in 0..n {
                filesystem.push(None);
            }
        }
    }
    filesystem
}
