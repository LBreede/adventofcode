fn part_one(input: &str) -> u32 {
    let mut result: u32 = 0;
    'outer: for line in input.lines() {
        let game_parts: Vec<&str> = line.split(": ").collect();
        for game in game_parts[1].split("; ") {
            let mut red = 0;
            let mut green = 0;
            let mut blue = 0;
            for color_string in game.split(", ") {
                let color_parts: Vec<&str> = color_string.split(" ").collect();
                let color_amount: u32 = color_parts[0].parse().unwrap();
                let color_name: &str = color_parts[1];
                match color_name {
                    "red" => red += color_amount,
                    "green" => green += color_amount,
                    "blue" => blue += color_amount,
                    _ => panic!("Unknown color"),
                }
            }
            // If any color is over the limit, skip this game
            if red > 12 || green > 13 || blue > 14 {
                continue 'outer;
            }
        }
        let game_id = game_parts[0].split(" ").collect::<Vec<&str>>()[1]
            .parse::<u32>()
            .unwrap();
        result += game_id;
    }
    result
}

fn part_two(input: &str) -> u32 {
    let mut result: u32 = 0;
    for line in input.lines() {
        let game_parts: Vec<&str> = line.split(": ").collect();
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        for game in game_parts[1].split("; ") {
            for color_string in game.split(", ") {
                let color_parts: Vec<&str> = color_string.split(" ").collect();
                let color_amount: u32 = color_parts[0].parse().unwrap();
                let color_name: &str = color_parts[1];
                match color_name {
                    "red" => red = red.max(color_amount),
                    "green" => green = green.max(color_amount),
                    "blue" => blue = blue.max(color_amount),
                    _ => panic!("Unknown color"),
                }
            }
        }
        let power = red * green * blue;
        result += power;
    }
    result
}

const INPUT: &str = include_str!("./input.txt");
fn main() {
    println!("Part one: {}", part_one(INPUT));
    println!("Part two: {}", part_two(INPUT));
}

#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(EXAMPLE), 8);
        assert_eq!(part_one(INPUT), 2101);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(EXAMPLE), 2286);
        assert_eq!(part_two(INPUT), 58269);
    }
}
