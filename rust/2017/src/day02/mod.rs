use std::time::Instant;

const INPUT: &str = include_str!("input.txt");

pub fn main() {
    println!("Day 2: Corruption Checksum");
    let now = Instant::now();
    let result = part_one(INPUT);
    let elapsed = now.elapsed();
    println!("Part 1: {} ({:.2?})", result, elapsed);

    let now = Instant::now();
    let result = part_two(INPUT);
    let elapsed = now.elapsed();
    println!("Part 2: {} ({:.2?})\n", result, elapsed);
}

fn part_one(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let numbers = line
                .split_whitespace()
                .map(|x| x.parse::<u32>().expect("should have been a number"));
            let max = numbers.clone().max().unwrap();
            let min = numbers.min().unwrap();
            max - min
        })
        .sum()
}

fn part_two(input: &str) -> u32 {
    let mut result = 0;
    for line in input.lines() {
        let numbers = line
            .split_whitespace()
            .map(|x| x.parse::<u32>().expect("should have been a number"))
            .collect::<Vec<u32>>();
        for (i, a) in numbers.iter().enumerate() {
            for (j, b) in numbers.iter().enumerate() {
                if i != j && a % b == 0 {
                    result += a / b;
                }
            }
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        let example = include_str!("example.txt");
        assert_eq!(part_one(example), 18);
    }

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(INPUT), 36_174);
    }

    #[test]
    fn test_part_two_example() {
        let example = include_str!("example2.txt");
        assert_eq!(part_two(example), 9);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(INPUT), 244);
    }
}
