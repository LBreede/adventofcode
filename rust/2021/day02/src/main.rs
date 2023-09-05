fn part_one(input: String) -> u32 {
    let mut horizontal = 0;
    let mut depth = 0;

    for line in input.lines() {
        let parts = line.split(" ").collect::<Vec<&str>>();
        let dir = parts[0];
        let dist = parts[1].parse::<u32>().unwrap();

        match dir {
            "forward" => {
                horizontal += dist;
            }
            "up" => {
                depth -= dist;
            }
            "down" => {
                depth += dist;
            }
            _ => {}
        }
    }
    horizontal * depth
}
fn part_two(input: String) -> u32 {
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;

    for line in input.lines() {
        let parts = line.split(" ").collect::<Vec<&str>>();
        let dir = parts[0];
        let dist = parts[1].parse::<u32>().unwrap();

        match dir {
            "down" => {
                aim += dist;
            }
            "up" => {
                aim -= dist;
            }
            "forward" => {
                horizontal += dist;
                depth += aim * dist;
            }
            _ => {}
        }
    }
    horizontal * depth
}
fn main() {
    let input = include_str!("../input.txt");
    println!("Part One: {}", part_one(input.to_string()));
    println!("Part Two: {}", part_two(input.to_string()));
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = include_str!("../example.txt");
    const INPUT: &str = include_str!("../input.txt");

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(EXAMPLE.to_string()), 150);
        assert_eq!(part_one(INPUT.to_string()), 1762050);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(EXAMPLE.to_string()), 900);
        assert_eq!(part_two(INPUT.to_string()), 1855892637);
    }
}
