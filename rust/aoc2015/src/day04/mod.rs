use std::time::Instant;
use thousands::Separable;

pub fn main(skip: bool) {
    println!("Day 4: The Ideal Stocking Stuffer");

    if skip {
        println!("Skipped!\n");
        return;
    }
    let input = include_str!("input.txt");

    let now = Instant::now();
    let day01_result = part_one(input);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        day01_result.separate_with_commas(),
        elapsed
    );

    let now = Instant::now();
    let day02_result = part_two(input);
    let elapsed = now.elapsed();

    println!(
        "Part 2: {} ({:.2?})\n",
        day02_result.separate_with_commas(),
        elapsed
    );
}

fn solve(input: &str, n: usize) -> u32 {
    let mut i: u32 = 0;
    loop {
        let digest = format!("{:x}", md5::compute(format!("{}{}", input, i)));
        if digest.chars().take(n).all(|x| x == '0') {
            return i;
        }
        i += 1;
    }
}

fn part_one(input: &str) -> u32 {
    solve(input, 5)
}

fn part_two(input: &str) -> u32 {
    solve(input, 6)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_examples() {
        assert_eq!(part_one("abcdef"), 609_043);
        assert_eq!(part_one("pqrstuv"), 1_048_970);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 282_749);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 9_962_624);
    }
}
