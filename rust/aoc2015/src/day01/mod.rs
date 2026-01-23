use std::time::Instant;

use thousands::Separable;

pub fn day01() {
    println!("Day 1: Not Quite Lisp");
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

fn part_one(input: &str) -> i32 {
    input.chars().fold(0, |acc, x| match x {
        '(' => acc + 1,
        ')' => acc - 1,
        _ => acc,
    })
}

fn part_two(input: &str) -> i32 {
    let mut acc = 0;
    for (i, x) in input.chars().enumerate() {
        acc = match x {
            '(' => acc + 1,
            ')' => acc - 1,
            _ => acc,
        };
        if acc < 0 {
            return (i + 1).try_into().unwrap();
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_examples() {
        assert_eq!(part_one("(())"), 0);
        assert_eq!(part_one("()()"), 0);
        assert_eq!(part_one("((("), 3);
        assert_eq!(part_one("(()(()("), 3);
        assert_eq!(part_one("))((((("), 3);
        assert_eq!(part_one("())"), -1);
        assert_eq!(part_one("))("), -1);
        assert_eq!(part_one(")))"), -3);
        assert_eq!(part_one(")())())"), -3);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 280);
    }

    #[test]
    fn test_part_two_examples() {
        assert_eq!(part_two(")"), 1);
        assert_eq!(part_two("()())"), 5);
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), 1_797);
    }
}
