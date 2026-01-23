use std::time::Instant;
use thousands::Separable;

pub fn run() {
    println!("Day 1: Trebuchet");
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

fn part_one(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let digits: Vec<u32> = line.chars().filter_map(|ch| ch.to_digit(10)).collect();

            match (digits.first(), digits.last()) {
                (None, _) => 0,
                (Some(n), None) => n * 11,
                (Some(a), Some(b)) => a * 10 + b,
            }
        })
        .sum()
}

fn part_two(input: &str) -> u32 {
    let input = input
        .replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine");
    part_one(input.as_str())
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 142);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 54_708);
    }

    #[test]
    fn test_part_two_example() {
        let input = include_str!("example2.txt");
        assert_eq!(part_two(input), 281);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 54_087);
    }
}
