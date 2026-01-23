use std::cmp;
use std::collections::HashMap;
use std::time::Instant;
use thousands::Separable;

pub fn run() {
    println!("Day 3: Gear Ratios");
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

#[derive(Debug, Clone)]
struct Part {
    number: u32,
    row: usize,
    start: usize,
    end: usize,
}

impl Part {
    fn is_valid(&self, schematic: &Vec<Vec<char>>) -> bool {
        for i in self.row.saturating_sub(1)..=cmp::min(self.row + 1, schematic.len() - 1) {
            for j in self.start.saturating_sub(1)..=cmp::min(self.end + 1, schematic[0].len() - 1) {
                match schematic[i][j] {
                    '0'..='9' => (),
                    '.' => (),
                    _ => return true,
                }
            }
        }
        false
    }
    fn is_adjacent_to(&self, schematic: &Vec<Vec<char>>, symbol: char) -> Option<(usize, usize)> {
        for i in self.row.saturating_sub(1)..=cmp::min(self.row + 1, schematic.len() - 1) {
            for j in self.start.saturating_sub(1)..=cmp::min(self.end + 1, schematic[0].len() - 1) {
                if schematic[i][j] == symbol {
                    return Some((i, j));
                }
            }
        }
        None
    }
}

fn parse_schematics(input: &str) -> Vec<Vec<char>> {
    input.lines().map(|line| line.chars().collect()).collect()
}

fn collect_parts(schematics: Vec<Vec<char>>) -> Vec<Part> {
    let mut parts = Vec::new();
    for (i, _row) in schematics.into_iter().enumerate() {
        let mut row = _row.clone();
        row.push('.');
        let mut number = String::new();
        for (j, val) in row.into_iter().enumerate() {
            if val.is_ascii_digit() {
                number = format!("{}{}", number, val);
            } else {
                if !number.is_empty() {
                    let len = number.len();
                    parts.push(Part {
                        number: number.parse().unwrap(),
                        row: i,
                        start: j - len,
                        end: j - 1,
                    });
                }
                number = String::new();
            }
        }
    }
    parts
}

fn part_one(input: &str) -> u32 {
    let schematics = parse_schematics(input);
    collect_parts(schematics.clone())
        .into_iter()
        .filter(|part| part.is_valid(&schematics))
        .map(|part| part.number)
        .sum()
}
fn part_two(input: &str) -> u32 {
    let schematics = parse_schematics(input);

    let mut map: HashMap<(usize, usize), Vec<Part>> = HashMap::new();

    for part in collect_parts(schematics.clone()) {
        if let Some(loc) = part.is_adjacent_to(&schematics, '*') {
            map.entry(loc)
                .and_modify(|parts| parts.push(part.clone()))
                .or_insert(vec![part]);
        }
    }

    map.iter()
        .filter(|(_, parts)| parts.len() == 2)
        .map(|(_, val)| {
            val.clone()
                .into_iter()
                .map(|part| part.number)
                .product::<u32>()
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 4_361);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 509_115);
    }

    #[test]
    fn test_part_two_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_two(input), 467_835);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 75_220_503);
    }
}
