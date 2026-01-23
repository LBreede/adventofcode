use std::time::Instant;

pub fn run() {
    println!("Day 1: Bathroom Security");

    let input = include_str!("input.txt");

    let now = Instant::now();
    let result = part_one(input);
    let elapsed = now.elapsed();
    println!("Part 1: {:?} ({:.2?})", result, elapsed);

    // println!("Part 2: Skipped!");
    let now = Instant::now();
    let result = part_two(input);
    let elapsed = now.elapsed();
    println!("Part 2: {:?} ({:.2?})", result, elapsed);
    println!();
}

fn part_one(input: &str) -> String {
    let mut number = String::new();
    let mut n: i32 = 5;
    for line in input.lines() {
        for c in line.chars() {
            n = match c {
                'U' => match n {
                    1..=3 => n,
                    _ => n - 3,
                },
                'D' => match n {
                    7..=9 => n,
                    _ => n + 3,
                },
                'L' => match n {
                    1 | 4 | 7 => n,
                    _ => n - 1,
                },
                'R' => match n {
                    3 | 6 | 9 => n,
                    _ => n + 1,
                },
                _ => unreachable!(),
            };
        }
        number = format!("{}{}", number, n);
    }
    number
}

fn part_two(input: &str) -> String {
    let mut number = String::new();
    let mut n: i32 = 5;
    for line in input.lines() {
        for c in line.chars() {
            n = match c {
                'U' => match n {
                    1 | 2 | 4 | 5 | 9 => n,
                    3 | 13 => n - 2,
                    6 | 7 | 8 | 10 | 11 | 12 => n - 4,
                    _ => unreachable!(),
                },
                'D' => match n {
                    5 | 9 | 10 | 12 | 13 => n,
                    1 | 11 => n + 2,
                    2 | 3 | 4 | 6 | 7 | 8 => n + 4,
                    _ => unreachable!(),
                },
                'L' => match n {
                    1 | 2 | 5 | 10 | 13 => n,
                    _ => n - 1,
                },
                'R' => match n {
                    1 | 4 | 9 | 12 | 13 => n,
                    _ => n + 1,
                },
                _ => unreachable!(),
            };
        }
        number = format!("{}{:X}", number, n);
    }
    number
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        let input = r#"ULL
RRDDD
LURDL
UUUUD"#;
        assert_eq!(part_one(input), String::from("1985"));
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), String::from("12578"));
    }

    #[test]
    fn test_part_two_example() {
        let input = r#"ULL
RRDDD
LURDL
UUUUD"#;
        assert_eq!(part_two(input), String::from("5DB3"));
    }

    #[test]
    fn test_part_two() {
        let input = include_str!("input.txt");
        assert_eq!(part_two(input), String::from("516DD"));
    }
}
