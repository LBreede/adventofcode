use adv_code_2024::*;
use anyhow::{Context, Result};
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "06";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let map = parse_map(reader);
        let mut guard = find_guard(&map).context("did not find guard")?;

        let mut visited: HashSet<Position> = HashSet::new();
        visited.insert(guard.position); // damn you off-by-one-error!

        while let Ok(peeked) = guard.peek() {
            let line = match map.get(peeked.y) {
                Some(line) => line,
                None => break,
            };
            let byte = match line.get(peeked.x) {
                Some(byte) => byte,
                None => break,
            };
            match byte {
                b'.' | b'^' => guard.advance(),
                b'#' => guard.turn(),
                _ => unreachable!(),
            }
            visited.insert(guard.position);
        }
        Ok(visited.len())
    }

    assert_eq!(41, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let map = parse_map(reader);
        let guard_position = find_guard_position(&map).context("could not find guard")?;

        let mut answer = 0;
        for i in 0..map.len() {
            for j in 0..map[0].len() {
                let mut modified_map = map.clone();

                // technically we could `continue` here if we encounter a `b'#'` or `b'^'`
                modified_map[i][j] = b'O';
                let mut visited: HashSet<Guard> = HashSet::new();
                let mut guard = Guard {
                    position: guard_position,
                    facing: Direction::North,
                };
                visited.insert(guard);

                while let Ok(peeked) = guard.peek() {
                    let line = match modified_map.get(peeked.y) {
                        Some(line) => line,
                        None => break,
                    };
                    let byte = match line.get(peeked.x) {
                        Some(byte) => byte,
                        None => break,
                    };
                    match byte {
                        b'.' | b'^' => guard.advance(),
                        b'#' | b'O' => guard.turn(),
                        _ => unreachable!(),
                    }
                    if visited.contains(&guard) {
                        answer += 1;
                        break;
                    } else {
                        visited.insert(guard);
                    }
                }
            }
        }
        Ok(answer)
    }

    assert_eq!(6, part2(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

fn parse_map<R: BufRead>(reader: R) -> Vec<Vec<u8>> {
    reader
        .lines()
        .map_while(Result::ok)
        .map(|line| line.bytes().collect::<Vec<u8>>())
        .collect()
}

fn find_guard_position(map: &[Vec<u8>]) -> Option<Position> {
    for (y, line) in map.iter().enumerate() {
        if let Some(x) = line.iter().position(|&item| item == b'^') {
            return Some(Position::new(x, y));
        }
    }
    None
}

fn find_guard(map: &[Vec<u8>]) -> Option<Guard> {
    if let Some(position) = find_guard_position(map) {
        return Some(Guard {
            position,
            facing: Direction::North,
        });
    }
    None
}
#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
struct Position {
    x: usize,
    y: usize,
}

impl Position {
    fn new(x: usize, y: usize) -> Self {
        Self { x, y }
    }
}

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
enum Direction {
    North,
    East,
    South,
    West,
}

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
struct Guard {
    position: Position,
    facing: Direction,
}

impl Guard {
    fn peek(&self) -> Result<Position, ()> {
        match self.facing {
            Direction::North => {
                if let Some(y) = self.position.y.checked_sub(1) {
                    Ok(Position::new(self.position.x, y))
                } else {
                    Err(())
                }
            }
            Direction::East => Ok(Position::new(self.position.x + 1, self.position.y)),
            Direction::South => Ok(Position::new(self.position.x, self.position.y + 1)),
            Direction::West => {
                if let Some(x) = self.position.x.checked_sub(1) {
                    Ok(Position::new(x, self.position.y))
                } else {
                    Err(())
                }
            }
        }
    }

    fn advance(&mut self) {
        self.position = self.peek().unwrap();
    }

    fn turn(&mut self) {
        self.facing = match self.facing {
            Direction::North => Direction::East,
            Direction::East => Direction::South,
            Direction::South => Direction::West,
            Direction::West => Direction::North,
        }
    }
}
