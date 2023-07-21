pub fn process_part1(input: &str) -> String {
    let mut result = 0;
    for line in input.lines() {
        let mut line_iter = line.split_whitespace().map(|s| s.trim());
        let range = line_iter.next().unwrap();
        let mut letter = line_iter.next().unwrap().to_string();
        let password = line_iter.next().unwrap();

        let mut range_iter = range.split("-").map(|n| n.parse::<i32>().unwrap());
        let start = range_iter.next().unwrap();
        let stop = range_iter.next().unwrap();

        letter.pop();

        let count = password.matches(&letter).count();

        if start <= count.try_into().unwrap() && stop >= count.try_into().unwrap() {
            result += 1;
        }
    }
    result.to_string()
}

pub fn process_part2(input: &str) -> String {
    let mut result = 0;

    for line in input.lines() {
        let mut line_iter = line.split_whitespace().map(|s| s.trim());
        let range = line_iter.next().unwrap();
        let mut letter = line_iter.next().unwrap().to_string();
        let password = line_iter.next().unwrap();

        let mut range_iter = range.split("-").map(|n| n.parse::<i32>().unwrap());
        let start = range_iter.next().unwrap();
        let stop = range_iter.next().unwrap();

        letter.pop();
    }

    result.to_string()
}
#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc";

    #[test]
    fn part1_works() {
        let result = process_part1(EXAMPLE);
        assert_eq!(result, "2");
    }
    #[test]
    fn part2_works() {
        let result = process_part2(EXAMPLE);
        assert_eq!(result, "1");
    }
}
