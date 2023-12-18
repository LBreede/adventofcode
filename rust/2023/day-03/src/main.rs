fn part_one(input: &str) -> i32 {
    for line in input.lines() {
        println!("{}", line);
    }
    0
}

fn part_two(input: &str) -> i32 {
    0
}

const INPUT: &str = include_str!("./input.txt");
fn main() {
    println!("Part one: {}", part_one(INPUT));
    println!("Part two: {}", part_two(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = include_str!("./example.txt");

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(EXAMPLE), 14361);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(EXAMPLE), 2);
    }
}
