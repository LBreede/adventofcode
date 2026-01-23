use std::time::Instant;

const INPUT: u32 = 368_078;

pub fn main() {
    println!("Day 3: Spiral Memory");
    let now = Instant::now();
    let result = part_one(INPUT);
    let elapsed = now.elapsed();
    println!("Part 1: {} ({:.2?})", result, elapsed);

    let now = Instant::now();
    if let Some(result) = part_two(INPUT) {
        let elapsed = now.elapsed();
        println!("Part 2: {} ({:.2?})\n", result, elapsed);
    } else {
        println!("Part 2: Could not solve");
    }
}

fn part_one(input: u32) -> u32 {
    let mut diameter = (input as f32).sqrt().ceil() as u32;
    if diameter % 2 == 0 {
        diameter += 1;
    }

    let dist_to_corner = (0..5)
        .map(|i| {
            let corner = diameter * diameter - i * (diameter - 1);
            corner.abs_diff(input)
        })
        .min()
        .unwrap();
    diameter - 1 - dist_to_corner
}

fn part_two(input: u32) -> Option<u32> {
    let mut sequence = include_str!("b141481.txt").lines();
    sequence.next();
    sequence.next();
    let mut sequence = sequence.map(|line| {
        let (_, n) = line.split_once(" ").unwrap();
        n.parse::<u32>().unwrap()
    });
    while let Some(n) = sequence.next() {
        if n > input {
            return Some(n);
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        assert_eq!(part_one(1), 0);
        assert_eq!(part_one(12), 3);
        assert_eq!(part_one(23), 2);
        assert_eq!(part_one(1024), 31);
    }

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(INPUT), 371);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(INPUT), Some(369601));
    }
}
