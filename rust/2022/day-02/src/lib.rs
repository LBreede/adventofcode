use std::convert::TryInto;

#[derive(Debug)]
enum Shape {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

use Shape::*;

#[derive(Debug)]
enum Outcome {
    Win = 6,
    Draw = 3,
    Lose = 0,
}

use Outcome::*;

pub fn process_part1(input: &str) -> String {
    let games: Vec<[Shape; 2]> = input
        .lines()
        .map(|l| {
            l.split_whitespace()
                .map(|s| match s {
                    "A" | "X" => Rock,
                    "B" | "Y" => Paper,
                    "C" | "Z" => Scissors,
                    _ => panic!("Unknown shape"),
                })
                .collect::<Vec<Shape>>()
                .try_into()
                .expect("Incorrect number of shapes")
        })
        .collect();

    let result = games
        .iter()
        .map(|[a, b]| match (b, a) {
            (Rock, Rock) => Draw as u32 + Rock as u32,
            (Rock, Paper) => Lose as u32 + Rock as u32,
            (Rock, Scissors) => Win as u32 + Rock as u32,
            (Paper, Rock) => Win as u32 + Paper as u32,
            (Paper, Paper) => Draw as u32 + Paper as u32,
            (Paper, Scissors) => Lose as u32 + Paper as u32,
            (Scissors, Rock) => Lose as u32 + Scissors as u32,
            (Scissors, Paper) => Win as u32 + Scissors as u32,
            (Scissors, Scissors) => Draw as u32 + Scissors as u32,
        })
        .sum::<u32>();

    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let shapes: Vec<Shape> = input
        .lines()
        .map(|line| line.split_whitespace().nth(0).unwrap())
        .map(|s| match s {
            "A" | "X" => Rock,
            "B" | "Y" => Paper,
            "C" | "Z" => Scissors,
            _ => panic!("Unknown shape"),
        })
        .collect();

    let outcomes: Vec<Outcome> = input
        .lines()
        .map(|line| line.split_whitespace().nth(1).unwrap())
        .map(|s| match s {
            "X" => Lose,
            "Y" => Draw,
            "Z" => Win,
            _ => panic!("Unknown outcome"),
        })
        .collect();

    let mut result: u32 = 0;

    for (shape, outcome) in shapes.iter().zip(outcomes.iter()) {
        match outcome {
            Win => {
                result += Win as u32;
                match shape {
                    Rock => result += Paper as u32,
                    Paper => result += Scissors as u32,
                    Scissors => result += Rock as u32,
                }
            }
            Draw => {
                result += Draw as u32;
                match shape {
                    Rock => result += Rock as u32,
                    Paper => result += Paper as u32,
                    Scissors => result += Scissors as u32,
                }
            }
            Lose => {
                result += Lose as u32;
                match shape {
                    Rock => result += Scissors as u32,
                    Paper => result += Rock as u32,
                    Scissors => result += Paper as u32,
                }
            }
        }
    }

    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "A Y
B X
C Z";

    #[test]
    fn part1_works() {
        let result = process_part1(EXAMPLE);
        assert_eq!(result, "15");
    }
    #[test]
    fn part2_works() {
        let result = process_part2(EXAMPLE);
        assert_eq!(result, "12");
    }
}
