use itertools::Itertools;
use std::cmp::Ordering;
use std::collections::HashMap;
use std::time::Instant;
use thousands::Separable;

pub fn run() {
    println!("Day 7: Camel Cards");
    let input = include_str!("input.txt");

    let now = Instant::now();
    let result = part_one(input);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        result.separate_with_commas(),
        elapsed
    );

    // println!("Part 2: Skipped!");
    let now = Instant::now();
    let result = part_two(input);
    let elapsed = now.elapsed();
    println!(
        "Part 2: {} ({:.2?})",
        result.separate_with_commas(),
        elapsed
    );

    println!();
}

#[derive(Debug, Ord, PartialOrd, Eq, PartialEq)]
enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

#[derive(Debug, Eq, PartialEq)]
struct Hand {
    hand_type: HandType,
    score: u32,
    bid: u32,
}

impl Hand {
    fn new(hand_type: HandType, score: u32, bid: u32) -> Self {
        Self {
            hand_type,
            score,
            bid,
        }
    }
}

impl Ord for Hand {
    fn cmp(&self, other: &Self) -> Ordering {
        let hand_type_cmp = self.hand_type.cmp(&other.hand_type);
        if hand_type_cmp == Ordering::Equal {
            return self.score.cmp(&other.score);
        }
        hand_type_cmp
    }
}
impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}
fn card_value(ch: char) -> u32 {
    match ch {
        '2' => 1,
        '3' => 2,
        '4' => 3,
        '5' => 4,
        '6' => 5,
        '7' => 6,
        '8' => 7,
        '9' => 8,
        'T' => 9,
        'J' => 10,
        'Q' => 11,
        'K' => 12,
        'A' => 13,
        _ => panic!("Invalid card character format"),
    }
}

fn parse_hand(line: &str) -> Hand {
    let (cards, bid) = line.split_once(" ").expect("Invalid format");

    let mut card_counts = HashMap::new();
    for ch in cards.chars() {
        card_counts
            .entry(ch)
            .and_modify(|count| *count += 1)
            .or_insert(1);
    }
    let counts: Vec<u32> = card_counts.values().copied().collect();

    let hand_type = match (
        counts.contains(&5),
        counts.contains(&4),
        counts.contains(&3),
        counts.contains(&2),
        counts.len(),
    ) {
        (true, _, _, _, 1) => HandType::FiveOfAKind,
        (_, true, _, _, 2) => HandType::FourOfAKind,
        (_, _, true, true, 2) => HandType::FullHouse,
        (_, _, true, _, 3) => HandType::ThreeOfAKind,
        (_, _, _, true, 3) => HandType::TwoPair,
        (_, _, _, true, 4) => HandType::OnePair,
        _ => HandType::HighCard,
    };

    let score: u32 = cards
        .chars()
        .map(card_value)
        .fold(0, |acc, n| acc * 100 + n);

    Hand::new(hand_type, score, bid.parse().unwrap())
}
fn part_one(input: &str) -> u32 {
    input
        .lines()
        .map(parse_hand)
        .sorted()
        .enumerate()
        .map(|(i, hand)| hand.bid * (i as u32 + 1))
        .sum()
}
fn part_two(input: &str) -> usize {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_hand_new() {
        assert_eq!(
            Hand::new(HandType::FullHouse, 123, 456),
            Hand {
                hand_type: HandType::FullHouse,
                score: 123,
                bid: 456
            }
        )
    }

    #[test]
    fn test_hand_cmp() {
        assert!(Hand::new(HandType::FiveOfAKind, 123, 0) > Hand::new(HandType::FullHouse, 123, 0));
        assert!(Hand::new(HandType::FullHouse, 456, 0) > Hand::new(HandType::FullHouse, 123, 0));
    }

    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 6_440);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 248_422_077);
    }

    // #[test]
    // fn test_part_two_example() {
    //     let input = include_str!("example.txt");
    //     assert_eq!(part_two(input), 71_503);
    // }

    // #[test]
    // fn test_part_two() {
    //     let input = include_str!("input.txt");
    //     assert_eq!(part_two(input), 42_250_895);
    // }
}
