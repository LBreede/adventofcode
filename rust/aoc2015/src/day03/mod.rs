use std::collections::HashSet;

pub fn main() {
    use std::time::Instant;
    use thousands::Separable;

    println!("Day 3: Perfectly Spherical Houses in a Vacuum");
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

#[derive(Debug, Hash, Eq, PartialEq, Copy, Clone)]
struct Coord(i32, i32);

impl Coord {
    fn new(x: i32, y: i32) -> Self {
        Self(x, y)
    }

    fn move_step(&mut self, direction: char) {
        match direction {
            '^' => self.1 += 1,
            '>' => self.0 += 1,
            'v' => self.1 -= 1,
            '<' => self.0 -= 1,
            _ => panic!("Unknown direction '{}'", direction),
        }
    }
}

fn part_one(input: &str) -> u32 {
    let mut coord = Coord::new(0, 0);
    let mut visited: HashSet<Coord> = HashSet::new();
    visited.insert(coord);
    for c in input.chars() {
        coord.move_step(c);
        visited.insert(coord);
    }
    visited.len().try_into().unwrap()
}

fn part_two(input: &str) -> u32 {
    let mut coord_santa = Coord::new(0, 0);
    let mut coord_robo = Coord::new(0, 0);
    let mut visited: HashSet<Coord> = HashSet::new();
    visited.insert(coord_santa);
    for (i, c) in input.chars().enumerate() {
        if i % 2 == 0 {
            coord_santa.move_step(c);
            visited.insert(coord_santa);
        } else {
            coord_robo.move_step(c);
            visited.insert(coord_robo);
        }
    }
    visited.len().try_into().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_examples() {
        assert_eq!(part_one(">"), 2);
        assert_eq!(part_one("^>v<"), 4);
        assert_eq!(part_one("^v^v^v^v^v"), 2);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 2_572);
    }

    #[test]
    fn test_part_two_examples() {
        assert_eq!(part_two("^v"), 3);
        assert_eq!(part_two("^>v<"), 3);
        assert_eq!(part_two("^v^v^v^v^v"), 11);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 2_631);
    }
}
