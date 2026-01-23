use std::cmp;
use std::time::Instant;
use thousands::Separable;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
struct Game(u32, u32, u32);

impl Game {
    fn new(s: &str) -> Self {
        let mut r = 0;
        let mut g = 0;
        let mut b = 0;
        for x in s.split(", ") {
            let (n, color) = x.split_once(" ").expect("Invalid format");
            match color {
                "red" => r += n.parse::<u32>().expect("Invalid number"),
                "green" => g += n.parse::<u32>().expect("Invalid number"),
                "blue" => b += n.parse::<u32>().expect("Invalid number"),
                _ => panic!("Invalid color"),
            }
        }
        Self(r, g, b)
    }

    fn is_possible(&self, red: u32, green: u32, blue: u32) -> u32 {
        if self.0 > red {
            return 0;
        }
        if self.1 > green {
            return 0;
        }
        if self.2 > blue {
            return 0;
        }
        1
    }

    fn max(self, other: Self) -> Self {
        Self(
            cmp::max(self.0, other.0),
            cmp::max(self.1, other.1),
            cmp::max(self.2, other.2),
        )
    }

    fn power(&self) -> u32 {
        self.0 * self.1 * self.2
    }
}

pub fn run() {
    println!("Day 2: Cube Conundrum");
    let input = include_str!("input.txt");

    for i in 1..=2 {
        let now = Instant::now();
        let result = if i % 2 == 1 {
            part_one(input)
        } else {
            part_two(input)
        };
        let elapsed = now.elapsed();
        println!(
            "Part {}: {} ({:.2?})",
            i,
            result.separate_with_commas(),
            elapsed
        );
    }
    println!();
}

fn _part_one(input: &str) -> u32 {
    let mut result: u32 = 0;
    for line in input.lines() {
        let (id, rest) = line.split_once(": ").expect("Invalid format");
        let id = id
            .split_once(" ")
            .unwrap()
            .1
            .parse::<u32>()
            .expect("Invalid format");
        result += rest
            .split("; ")
            .map(Game::new)
            .fold(None, |max, current| match max {
                None => Some(current),
                Some(max) => Some(max.max(current)),
            })
            .unwrap()
            .is_possible(12, 13, 14)
            * id
    }
    result
}
fn part_one(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            line.split_once(": ")
                .expect("Invalid format")
                .1
                .split("; ")
                .map(Game::new)
                .fold(None, |max, current| match max {
                    None => Some(current),
                    Some(max) => Some(max.max(current)),
                })
                .unwrap()
                .is_possible(12, 13, 14)
        })
        .enumerate()
        .map(|(i, x)| (i as u32 + 1) * x)
        .sum()
}
fn part_two(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            line.split_once(": ")
                .expect("Invalid format")
                .1
                .split("; ")
                .map(Game::new)
                .fold(None, |max, current| match max {
                    None => Some(current),
                    Some(max) => Some(max.max(current)),
                })
                .unwrap()
                .power()
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_game() {
        assert_eq!(Game::new("4 green"), Game(0, 4, 0));
        assert_eq!(Game::new("1 red, 6 blue"), Game(1, 0, 6));
        assert_eq!(Game::new("5 green, 2 blue, 9 red"), Game(9, 5, 2));
    }

    #[test]
    fn test_max() {
        assert_eq!(Game(1, 2, 3).max(Game(3, 2, 1)), Game(3, 2, 3));
    }

    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 8);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 2_101);
    }

    #[test]
    fn test_part_two_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_two(input), 2_286);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 58_269);
    }
}
