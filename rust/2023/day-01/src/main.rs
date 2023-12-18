fn part_one(input: &str) -> u32 {
    let mut result = 0;
    for line in input.lines() {
        let digits = line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect::<Vec<u32>>();
        result += 10 * digits.first().unwrap() + digits.last().unwrap();
    }
    result
}

fn part_two(input: &str) -> u32 {
    let mut result = 0;
    for line in input.lines() {
        let new_line = line
            .replace("one", "o1ne")
            .replace("two", "t2wo")
            .replace("three", "t3hree")
            .replace("four", "f4our")
            .replace("five", "f5ive")
            .replace("six", "s6ix")
            .replace("seven", "s7even")
            .replace("eight", "e8ight")
            .replace("nine", "n9ine");
        let digits = new_line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect::<Vec<u32>>();
        result += 10 * digits.first().unwrap() + digits.last().unwrap();
    }
    result
}

const INPUT: &str = include_str!("./input.txt");
fn main() {
    let result_one = part_one(INPUT);
    println!("Part one: {}", result_one);
    let result_two = part_two(INPUT);
    println!("Part two: {}", result_two);
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_ONE: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

    const EXAMPLE_TWO: &str = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";

    #[test]
    fn part_one_works() {
        assert_eq!(part_one(EXAMPLE_ONE), 142);
        assert_eq!(part_one(INPUT), 54708);
    }

    #[test]
    fn part_two_works() {
        assert_eq!(part_two(EXAMPLE_TWO), 281);
        assert_eq!(part_two(INPUT), 54087);
    }
}
