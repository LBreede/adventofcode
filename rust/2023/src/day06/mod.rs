use std::iter::zip;
use std::time::Instant;
use thousands::Separable;

pub fn run() {
    println!("Day 6: Wait For It");
    let input = include_str!("input.txt");

    let now = Instant::now();
    let result = part_one(input);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        result.separate_with_commas(),
        elapsed
    );

    println!("Part 2: Skipped!");
    // let now = Instant::now();
    // let result part_two(input);
    // let elapsed = now.elapsed();
    // println!("Part 2: {} ({:.2?})", result.separate_with_commas(), elapsed);
    
    println!();
}

fn record_beat_count(time: u64, record_dist: u64) -> usize {
    (0..=time)
        .map(|n| (time - n) * n)
        .filter(|n| *n > record_dist)
        .count()
}

fn part_one(input: &str) -> usize {
    let mut iter = input.lines().map(|line| {
        line.split_whitespace()
            .skip(1)
            .map(|n| n.parse::<u64>().unwrap())
            .collect::<Vec<u64>>()
    });
    let times = iter.next().unwrap();
    let record_distances = iter.next().unwrap();

    zip(times, record_distances)
        .map(|(time, record_dist)| record_beat_count(time, record_dist))
        .product()
}
fn part_two(input: &str) -> usize {
    let mut iter = input.lines().map(|line| {
        line.chars()
            .filter(|ch| ch.is_ascii_digit())
            .collect::<String>()
            .parse::<u64>()
            .unwrap()
    });
    let time = iter.next().unwrap();
    let record_dist = iter.next().unwrap();
    record_beat_count(time, record_dist)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 288);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 449_820);
    }

    #[test]
    fn test_part_two_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_two(input), 71_503);
    }

    // #[test]
    // fn test_part_two() {
    //     let input = include_str!("input.txt");
    //     assert_eq!(part_two(input), 42_250_895);
    // }
}
