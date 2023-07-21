use day_03::process_part2;
use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("Part 2: {}", process_part2(&file));
}
