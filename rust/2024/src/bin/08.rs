use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use itertools::Itertools;
use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::ops::{Add, Mul, Sub};

const DAY: &str = "08";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
";

const EXAMPLE2: &str = "\
T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let lines = parse_lines(reader);
        let min = Vector::new(0, 0);
        let max = Vector::new(lines.len() as i32, lines[0].len() as i32);
        let antennas = parse_antennas(lines);
        let mut antinodes: HashSet<Vector> = HashSet::new();
        for (_, positions) in antennas {
            for combination in positions.iter().combinations(2) {
                let direction = *combination[0] - *combination[1];
                let a = *combination[0] + direction;
                let b = *combination[0] - direction;
                let c = *combination[1] + direction;
                let d = *combination[1] - direction;
                for antinode in [a, b, c, d] {
                    if !combination.contains(&&antinode) && antinode.is_in_bounds(&min, &max) {
                        antinodes.insert(antinode);
                    }
                }
            }
        }
        Ok(antinodes.len())
    }

    assert_eq!(14, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let lines = parse_lines(reader);
        let min = Vector::new(0, 0);
        let max = Vector::new(lines.len() as i32, lines[0].len() as i32);
        let antennas = parse_antennas(lines);

        let mut antinodes: HashSet<Vector> = HashSet::new();
        for (_, positions) in antennas {
            for combination in positions.iter().combinations(2) {
                let direction = *combination[0] - *combination[1];

                for i in 1.. {
                    let antinode = *combination[0] + direction * i;
                    if !antinode.is_in_bounds(&min, &max) {
                        break;
                    }
                    antinodes.insert(antinode);
                }
                for i in 1.. {
                    let antinode = *combination[0] - direction * i;
                    if !antinode.is_in_bounds(&min, &max) {
                        break;
                    }
                    antinodes.insert(antinode);
                }
                for i in 1.. {
                    let antinode = *combination[1] + direction * i;
                    if !antinode.is_in_bounds(&min, &max) {
                        break;
                    }
                    antinodes.insert(antinode);
                }
                for i in 1.. {
                    let antinode = *combination[1] - direction * i;
                    if !antinode.is_in_bounds(&min, &max) {
                        break;
                    }
                    antinodes.insert(antinode);
                }
            }
        }
        Ok(antinodes.len())
    }

    assert_eq!(9, part2(BufReader::new(EXAMPLE2.as_bytes()))?);
    assert_eq!(34, part2(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash, Default)]
struct Vector {
    x: i32,
    y: i32,
}

impl Vector {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }
    /// Returns true if the vector is within the bounds defined by min and max.
    /// The bounds are inclusive on the min side and exclusive on the max side.
    fn is_in_bounds(&self, min: &Vector, max: &Vector) -> bool {
        self.x >= min.x && self.x < max.x && self.y >= min.y && self.y < max.y
    }
}

impl Add for Vector {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        Self {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl Sub for Vector {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self::Output {
        Self {
            x: self.x - rhs.x,
            y: self.y - rhs.y,
        }
    }
}

impl Mul<i32> for Vector {
    type Output = Self;

    fn mul(self, rhs: i32) -> Self::Output {
        Self {
            x: self.x * rhs,
            y: self.y * rhs,
        }
    }
}

/// Parses the map of antennas and returns a hashmap with the antennas as keys and their positions
/// as values.
fn parse_antennas(map: Vec<Vec<u8>>) -> HashMap<u8, Vec<Vector>> {
    let mut antennas: HashMap<u8, Vec<Vector>> = HashMap::new();
    for (i, line) in map.iter().enumerate() {
        for (j, &byte) in line.iter().enumerate() {
            if byte == b'.' {
                continue;
            }
            let position = Vector {
                x: i as i32,
                y: j as i32,
            };
            antennas
                .entry(byte)
                .and_modify(|pos| pos.push(position))
                .or_insert(vec![position]);
        }
    }
    antennas
}

fn parse_lines<R: BufRead>(reader: R) -> Vec<Vec<u8>> {
    reader
        .lines()
        .map_while(Result::ok)
        .map(|line| line.bytes().collect::<Vec<u8>>())
        .collect()
}
