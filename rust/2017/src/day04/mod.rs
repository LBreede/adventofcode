use std::{collections::HashSet, time::Instant};

const INPUT: &str = include_str!("input.txt");

pub fn main() {
    println!("Day 4: High-Entropy Passphrases");
    let now = Instant::now();
    let result = part_one(INPUT);
    let elapsed = now.elapsed();
    println!("Part 1: {} ({:.2?})", result, elapsed);

    let now = Instant::now();
    let result = part_two(INPUT);
    let elapsed = now.elapsed();
    println!("Part 2: {} ({:.2?})\n", result, elapsed);
}

fn is_valid(passphrase: &str) -> bool {
    let mut words_set = HashSet::new();
    for word in passphrase.split_whitespace() {
        if !words_set.insert(word) {
            return false; // Duplicate found
        }
    }
    true
}

fn part_one(input: &str) -> u32 {
    input.lines().filter(|&line| is_valid(line)).count() as u32
}

fn is_valid2(passphrase: &str) -> bool {
    let mut set = HashSet::new();
    for word in passphrase.split_whitespace() {
        let mut chars: Vec<char> = word.chars().collect();
        chars.sort();
        if !set.insert(chars.iter().collect::<String>()) {
            return false;
        }
    }
    true
}

fn part_two(input: &str) -> u32 {
    input.lines().filter(|&line| is_valid2(line)).count() as u32
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_validity() {
        assert!(is_valid("aa bb cc dd ee"));
        assert!(!is_valid("aa bb cc dd aa"));
        assert!(is_valid("aa bb cc dd aaa"));
    }

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(INPUT), 337);
    }

    #[test]
    fn test_part_two_example() {
        assert!(is_valid2("abcde fghij"));
        assert!(!is_valid2("abcde xyz ecdab"));
        assert!(is_valid2("a ab abc abd abf abj"));
        assert!(is_valid2("iiii oiii ooii oooi oooo"));
        assert!(!is_valid2("oiii ioii iioi iiio"));
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(INPUT), 231);
    }
}
