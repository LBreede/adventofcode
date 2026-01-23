use std::time::Instant;

const INPUT: &str = include_str!("input.txt");

pub fn main() {
    println!("Day 5: A Maze of Twisty Trampolines, All Alike");
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
    let mut i: i32 = 0;
    let mut j = 0;

    let mut jumps: Vec<i32> = input
        .split_whitespace()
        .map(|n| n.parse::<i32>().unwrap())
        .collect();

    loop {
        match jumps.get(i as usize) {
            Some(&val) => {
                jumps[i as usize] = val + 1;
                i += val;
                j += 1;
            }
            None => return j,
        };
    }
}

fn part_two(input: &str) -> u32 {
    let mut i: i32 = 0;
    let mut j = 0;

    let mut jumps: Vec<i32> = input
        .split_whitespace()
        .map(|n| n.parse::<i32>().unwrap())
        .collect();

    loop {
        match jumps.get(i as usize) {
            Some(&val) => {
                jumps[i as usize] = if val < 3 { val + 1 } else { val - 1 };
                i += val;
                j += 1;
            }
            None => return j,
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = include_str!("example.txt");

    #[test]
    fn test_part_one_example() {
        assert_eq!(part_one(EXAMPLE), 5);
    }

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(INPUT), 376_976);
    }

    #[test]
    fn test_part_two_example() {
        assert_eq!(part_two(EXAMPLE), 10);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(INPUT), 29_227_751);
    }
}
