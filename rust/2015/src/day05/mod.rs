use fancy_regex::Regex;

static INPUT: &str = include_str!("input.txt");

pub fn main() {
    use std::time::Instant;
    use thousands::Separable;

    println!("Day 5: Doesn't He Have Intern-Elves For This?");

    let now = Instant::now();
    let day01_result = part_one(INPUT);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        day01_result.separate_with_commas(),
        elapsed
    );

    let now = Instant::now();
    let day02_result = part_two(INPUT);
    let elapsed = now.elapsed();

    println!(
        "Part 2: {} ({:.2?})\n",
        day02_result.separate_with_commas(),
        elapsed
    );
}

#[allow(dead_code)]
fn has_three_vowels(s: &str) -> bool {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    s.chars().filter(|c| vowels.contains(c)).count() >= 3
}

#[allow(dead_code)]
fn has_double_letter(s: &str) -> bool {
    s.as_bytes().windows(2).any(|w| w[0] == w[1])
}

#[allow(dead_code)]
fn has_bad_strings(s: &str) -> bool {
    let bad_pat = ["ab", "cd", "pq", "xy"];
    !bad_pat.iter().any(|pat| s.contains(pat))
}

#[allow(dead_code)]
fn is_nice(s: &str) -> bool {
    has_three_vowels(s) && has_double_letter(s) && has_bad_strings(s)
}

fn part_one(input: &str) -> u32 {
    let re1 = Regex::new(r"(:?[aeiou].*){3}").unwrap();
    let re2 = Regex::new(r"(:?[a-zA-Z])\1").unwrap();
    let re3 = Regex::new(r"ab|cd|pq|xy").unwrap();
    input
        .lines()
        // .filter(|s| is_nice(s))
        .filter(|s| {
            re1.is_match(s).unwrap() && re2.is_match(s).unwrap() && !re3.is_match(s).unwrap()
        })
        .count()
        .try_into()
        .unwrap()
}

fn part_two(input: &str) -> u32 {
    let re1 = Regex::new(r"(..).*\1").unwrap();
    let re2 = Regex::new(r"(.).\1").unwrap();
    input
        .lines()
        .filter(|s| re1.is_match(s).unwrap() && re2.is_match(s).unwrap())
        .count()
        .try_into()
        .unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_has_three_vowels() {
        assert!(has_three_vowels("aei"));
        assert!(has_three_vowels("xazegov"));
        assert!(has_three_vowels("aeiouaeiouaeiou"));
        assert!(!has_three_vowels("dvszwmarrgswjxmb"));
    }

    #[test]
    fn test_has_double_letter() {
        assert!(has_double_letter("xx"));
        assert!(has_double_letter("abcdde"));
        assert!(has_double_letter("aabbccdd"));
        assert!(!has_double_letter("jchzalrnumimnmhp"));
    }

    #[test]
    fn test_has_bad_strings() {
        assert!(!has_bad_strings("haegwjzuvuyypxyu"));
    }

    #[test]
    fn test_is_nice() {
        assert!(is_nice("ugknbfddgicrmopn"));
        assert!(is_nice("aaa"));
        assert!(!is_nice("jchzalrnumimnmhp"));
        assert!(!is_nice("haegwjzuvuyypxyu"));
        assert!(!is_nice("dvszwmarrgswjxmb"));
    }

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(INPUT), 255);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(INPUT), 55);
    }
}
