fn score_char(c: char) -> u32 {
    if c.is_ascii_lowercase() {
        c as u32 - 'a' as u32 + 1
    } else {
        c as u32 - 'A' as u32 + 27
    }
}

pub fn process_part1(input: &str) -> u32 {
    let mut result = 0;
    for line in input.lines() {
        let len = line.len();
        let first = &line[..len / 2];
        let second = &line[len / 2..];
        if let Some(common) = second.chars().find(|&c| first.contains(c)) {
            result += score_char(common);
        }
    }
    result
    // input.lines().fold(0, |acc, line| {
    //     let len = line.len();
    //     let first = &line[..len / 2];
    //     let second = &line[len / 2..];
    //     acc + second
    //         .chars()
    //         .find(|&c| first.contains(c))
    //         .map(|c| score_char(c))
    //         .unwrap_or(0)
    // })
}
pub fn process_part2(input: &str) -> u32 {
    let lines: Vec<&str> = input.lines().collect();
    let len = lines.len() / 3;

    let mut result = 0;

    for i in 0..len {
        let a = lines[i * 3];
        let b = lines[i * 3 + 1];
        let c = lines[i * 3 + 2];

        for ch in ('a'..='z').chain('A'..='Z') {
            let a_count = a.chars().filter(|&x| x == ch).count();
            let b_count = b.chars().filter(|&x| x == ch).count();
            let c_count = c.chars().filter(|&x| x == ch).count();

            if a_count > 0 && b_count > 0 && c_count > 0 {
                result += score_char(ch);
            }
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";

    #[test]
    fn part_one_works() {
        let result = process_part1(EXAMPLE);
        assert_eq!(result, 157)
    }

    #[test]
    fn part_two_works() {
        let result = process_part2(EXAMPLE);
        assert_eq!(result, 70)
    }
}
