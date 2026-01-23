use std::{collections::HashSet, time::Instant};
use thousands::Separable;

pub fn run() {
    println!("Day 1: No Time for a Taxicab");

    let input = include_str!("input.txt");

    let now = Instant::now();
    let result = part_one(input);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        result.separate_with_commas(),
        elapsed
    );

    // println!("Part 2: Skipped!");
    let now = Instant::now();
    let result = part_two(input);
    let elapsed = now.elapsed();
    println!(
        "Part 2: {} ({:.2?})",
        result.separate_with_commas(),
        elapsed
    );
    println!();
}

#[derive(Debug)]
enum Direction {
    North,
    East,
    South,
    West,
}

impl From<i32> for Direction {
    fn from(index: i32) -> Self {
        match index.rem_euclid(4) {
            0 => Direction::North,
            1 => Direction::East,
            2 => Direction::South,
            3 => Direction::West,
            _ => unreachable!(),
        }
    }
}

impl Direction {
    fn index(&self) -> i32 {
        match self {
            Direction::North => 0,
            Direction::East => 1,
            Direction::South => 2,
            Direction::West => 3,
        }
    }
}

#[derive(Debug, Hash, Eq, PartialEq, Clone, Copy)]
struct Position(i32, i32);

impl Position {
    fn default() -> Self {
        Self(0, 0)
    }

    fn walk(&mut self, direction: &Direction, amount: i32) {
        match direction {
            Direction::North => self.1 += amount,
            Direction::East => self.0 += amount,
            Direction::South => self.1 -= amount,
            Direction::West => self.0 -= amount,
        }
    }

    fn distance(&self) -> u32 {
        self.0.unsigned_abs() + self.1.unsigned_abs()
    }
}

fn part_one(input: &str) -> u32 {
    let mut position = Position::default();
    let mut direction = Direction::North;

    for s in input.trim().split(", ") {
        let mut chars = s.chars();
        let turn = chars.next().expect("should have at least two characters");
        let amount: i32 = chars
            .as_str()
            .parse()
            .expect("this should be able to parsed into i32");
        let idx = direction.index();
        direction = match turn {
            'R' => Direction::from(idx + 1),
            'L' => Direction::from(idx - 1),
            _ => panic!("unknown turn direction {}", turn),
        };
        position.walk(&direction, amount);
    }
    position.distance()
}

fn part_two(input: &str) -> u32 {
    let mut position = Position::default();
    let mut visited: HashSet<Position> = HashSet::new();
    visited.insert(position);

    let mut direction = Direction::North;

    for s in input.trim().split(", ") {
        let mut chars = s.chars();
        let turn = chars.next().expect("should have at least two characters");
        let amount: i32 = chars
            .as_str()
            .parse()
            .expect("this should be able to parsed into i32");
        let idx = direction.index();
        direction = match turn {
            'R' => Direction::from(idx + 1),
            'L' => Direction::from(idx - 1),
            _ => panic!("unknown turn direction {}", turn),
        };
        for _ in 0..amount {
            position.walk(&direction, 1);
            if visited.contains(&position) {
                return position.distance();
            }
            visited.insert(position);
        }
    }
    panic!("did not visit a location twice")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        assert_eq!(part_one("R2, L3"), 5);
        assert_eq!(part_one("R2, R2, R2"), 2);
        assert_eq!(part_one("R5, L5, R5, R3"), 12);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 242);
    }

    #[test]
    fn test_part_two_example() {
        assert_eq!(part_two("R8, R4, R4, R8"), 4);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 150);
    }
}
