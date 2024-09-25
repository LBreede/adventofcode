fn process_part_one(input: String) -> i32 {
    input
        .chars()
        .map(|c| match c {
            '(' => 1,
            ')' => -1,
            _ => 0,
        })
        .sum()

    // // GitHub Copilot Chat:
    // input.chars().fold(0, |acc, c| match c {
    //     '(' => acc + 1,
    //     ')' => acc - 1,
    //     _ => acc,
    // })
}

fn process_part_two(input: String) -> i32 {
    let mut floor = 0;

    for (i, c) in input.chars().enumerate() {
        match c {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => (),
        }
        if floor < 0 {
            return (i + 1).try_into().unwrap();
        }
    }
    0
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    let part_one = process_part_one(input.clone());
    println!("Part one: {}", part_one);

    let part_two = process_part_two(input);
    println!("Part two: {}", part_two);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        assert_eq!(process_part_one("(())".to_string()), 0);
        assert_eq!(process_part_one("()()".to_string()), 0);
        assert_eq!(process_part_one("(((".to_string()), 3);
        assert_eq!(process_part_one("(()(()(".to_string()), 3);
        assert_eq!(process_part_one("))(((((".to_string()), 3);
        assert_eq!(process_part_one("())".to_string()), -1);
        assert_eq!(process_part_one("))(".to_string()), -1);
        assert_eq!(process_part_one(")))".to_string()), -3);
        assert_eq!(process_part_one(")())())".to_string()), -3);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(process_part_two(")".to_string()), 1);
        assert_eq!(process_part_two("()())".to_string()), 5);
    }
}
