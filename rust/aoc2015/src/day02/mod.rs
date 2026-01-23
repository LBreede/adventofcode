use std::time::Instant;

use thousands::Separable;

pub fn day02() {
    println!("Day 2: I Was Told There Would Be No Math");
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

#[derive(Debug)]
struct Package {
    length: u32,
    width: u32,
    height: u32,
}

impl Package {
    fn from(string: &str) -> Self {
        let dims: Vec<u32> = string
            .split("x")
            .map(|x| x.parse::<u32>().unwrap())
            .collect();
        Self {
            length: dims[0],
            width: dims[1],
            height: dims[2],
        }
    }

    fn wrapping_paper(&self) -> u32 {
        let lw = self.length * self.width;
        let wh = self.width * self.height;
        let hl = self.height * self.length;
        let min = lw.min(wh).min(hl);
        2 * lw + 2 * wh + 2 * hl + min
    }
    fn ribbon(&self) -> u32 {
        let a = (2 * self.length + 2 * self.width)
            .min(2 * self.width + 2 * self.height)
            .min(2 * self.height + 2 * self.length);
        let b = self.length * self.width * self.height;
        a + b
    }
}

fn part_one(input: &str) -> u32 {
    input
        .lines()
        .map(|x| Package::from(x).wrapping_paper())
        .sum()
}

fn part_two(input: &str) -> u32 {
    input.lines().map(|x| Package::from(x).ribbon()).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_examples() {
        assert_eq!(part_one("2x3x4"), 58);
        assert_eq!(part_one("1x1x10"), 43);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 1_586_300);
    }

    #[test]
    fn test_part_two_examples() {
        assert_eq!(part_two("2x3x4"), 34);
        assert_eq!(part_two("1x1x10"), 14);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 3_737_498);
    }
}
