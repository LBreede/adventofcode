use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "04";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let mut answer = 0;

        let word_search = reader
            .lines()
            .map(|line| line.unwrap().bytes().collect::<Vec<u8>>())
            .collect::<Vec<Vec<u8>>>();
        for (i, row) in word_search.iter().enumerate() {
            for (j, &char) in row.iter().enumerate() {
                if char != b'X' {
                    continue;
                };
                if i.checked_sub(3).is_some() {
                    let a = &word_search[i - 1];
                    let b = &word_search[i - 2];
                    let c = &word_search[i - 3];
                    if j.checked_sub(3).is_some() {
                        if let (b'M', b'A', b'S') = (a[j - 1], b[j - 2], c[j - 3]) {
                            answer += 1;
                        }
                    }
                    if let (b'M', b'A', b'S') = (a[j], b[j], c[j]) {
                        answer += 1;
                    }
                    if let Some(b'S') = c.get(j + 3) {
                        if let (b'M', b'A') = (a[j + 1], b[j + 2]) {
                            answer += 1;
                        }
                    }
                }
                if j.checked_sub(3).is_some() {
                    if let (b'M', b'A', b'S') = (
                        word_search[i][j - 1],
                        word_search[i][j - 2],
                        word_search[i][j - 3],
                    ) {
                        answer += 1
                    }
                }
                if word_search[i].get(j + 3).is_some() {
                    if let (b'M', b'A', b'S') = (
                        word_search[i][j + 1],
                        word_search[i][j + 2],
                        word_search[i][j + 3],
                    ) {
                        answer += 1
                    }
                }
                if word_search.get(i + 3).is_some() {
                    let a = &word_search[i + 1];
                    let b = &word_search[i + 2];
                    let c = &word_search[i + 3];
                    if j.checked_sub(3).is_some() {
                        if let (b'M', b'A', b'S') = (a[j - 1], b[j - 2], c[j - 3]) {
                            answer += 1;
                        }
                    }
                    if let (b'M', b'A', b'S') = (a[j], b[j], c[j]) {
                        answer += 1
                    }
                    if c.get(j + 3).is_some() {
                        if let (b'M', b'A', b'S') = (a[j + 1], b[j + 2], c[j + 3]) {
                            answer += 1;
                        }
                    }
                }
            }
        }
        Ok(answer)
    }

    assert_eq!(18, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let mut answer = 0;

        let word_search = reader
            .lines()
            .map(|line| line.unwrap().bytes().collect::<Vec<u8>>())
            .collect::<Vec<Vec<u8>>>();
        let height = word_search.len();
        for (i, row) in word_search.iter().enumerate() {
            let width = row.len();
            for (j, &char) in row.iter().enumerate() {
                if char != b'A' || i == 0 || i == height - 1 || j == 0 || j == width - 1 {
                    continue;
                }
                match (
                    word_search[i - 1][j - 1],
                    word_search[i - 1][j + 1],
                    word_search[i + 1][j + 1],
                    word_search[i + 1][j - 1],
                ) {
                    (b'M', b'M', b'S', b'S') => answer += 1,
                    (b'M', b'S', b'S', b'M') => answer += 1,
                    (b'S', b'M', b'M', b'S') => answer += 1,
                    (b'S', b'S', b'M', b'M') => answer += 1,
                    _ => continue,
                }
            }
        }
        Ok(answer)
    }

    assert_eq!(9, part2(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}
