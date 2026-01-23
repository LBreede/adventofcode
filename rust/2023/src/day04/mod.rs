use std::collections::{HashMap, HashSet};
use std::time::Instant;
use thousands::Separable;

pub fn run() {
    println!("Day 4: Scratchcards");
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
    // part_two(input);
    // let elapsed = now.elapsed();
    // println!("Part 2: {} ({:.2?})", result.separate_with_commas(), elapsed);

    println!();
}

#[derive(Debug, Clone)]
struct Card {
    id: u32,
    winning_numbers: Vec<u32>,
    numbers: Vec<u32>,
}

impl Card {
    fn from(s: &str) -> Self {
        let (id, numbers) = s.split_once(": ").unwrap();
        let (a, b) = numbers.split_once(" | ").unwrap();
        Self {
            id: id.split_whitespace().collect::<Vec<&str>>()[1]
                .parse()
                .expect("invalid number"),
            winning_numbers: a
                .split_whitespace()
                .map(|n| n.parse().expect("invalid number"))
                .collect(),
            numbers: b
                .split_whitespace()
                .map(|n| n.parse().expect("invalid number"))
                .collect(),
        }
    }
    fn count_wins(&self) -> usize {
        let winning_set: HashSet<u32> = self.winning_numbers.iter().copied().collect();
        let numbers_set: HashSet<u32> = self.numbers.iter().copied().collect();

        winning_set
            .intersection(&numbers_set)
            .copied()
            .collect::<Vec<u32>>()
            .len()
    }
}

fn part_one(input: &str) -> u32 {
    let mut score = 0;
    for line in input.lines() {
        let card = Card::from(line);
        let num_wins = card.count_wins();
        score += if num_wins == 0 {
            0
        } else {
            2_u32.pow((num_wins - 1).try_into().unwrap())
        }
    }
    score
}
fn part_two(input: &str) -> u32 {
    let mut cards: Vec<Card> = Vec::new();
    let mut cards_map: HashMap<u32, Card> = HashMap::new();
    for line in input.lines() {
        let card = Card::from(line);
        cards.push(card.clone());
        let id = card.id;
        cards_map.entry(id).or_insert(card);
    }
    let mut j = 0;
    while !cards.is_empty() {
        let card = cards.swap_remove(0);
        let num_wins = card.count_wins();

        for k in 0..num_wins {
            if let Some(next_card) = cards_map.get(&(card.id + k as u32 + 1)) {
                cards.push(next_card.clone());
            }
        }
        j += 1;
    }
    j
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 13);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 21_568);
    }

    #[test]
    fn test_part_two_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_two(input), 30);
    }

    // #[test]
    // fn test_part_two() {
    //     let input = include_str!("input.txt");
    //     assert_eq!(part_two(input), 11_827_296);
    // }
}
