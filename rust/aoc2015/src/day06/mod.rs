static INPUT: &str = include_str!("input.txt");

pub fn main() {
    use std::time::Instant;
    use thousands::Separable;

    println!("Day 6: Probably a Fire Hazard");

    let now = Instant::now();
    let day01_result = part_one(INPUT);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        day01_result.separate_with_commas(),
        elapsed
    );

    let now = Instant::now();
    let day02_result = part_two(INPUT);
    let elapsed = now.elapsed();

    println!(
        "Part 2: {} ({:.2?})\n",
        day02_result.separate_with_commas(),
        elapsed
    );
}

#[derive(Debug, PartialEq)]
struct Instruction {
    operation: Operation,
    start: Position,
    end: Position,
}

impl Instruction {
    fn new(operation: Operation, start: Position, end: Position) -> Self {
        Self {
            operation,
            start,
            end,
        }
    }
}

impl From<&str> for Instruction {
    fn from(s: &str) -> Self {
        // turn on 0,0 through 999,999
        let x: Vec<&str> = s
            .split_whitespace()
            .rev()
            .take(4)
            .collect::<Vec<&str>>()
            .into_iter()
            .rev()
            .collect();

        let operation = match x[0] {
            "on" => Operation::TurnOn,
            "off" => Operation::TurnOff,
            "toggle" => Operation::Toggle,
            _ => panic!("couldn't mathc operation"),
        };

        let start = Position::from(x[1]);
        let end = Position::from(x[3]);
        Instruction::new(operation, start, end)
    }
}

#[derive(Debug, PartialEq)]
enum Operation {
    TurnOn,
    TurnOff,
    Toggle,
}

#[derive(Debug, PartialEq)]
struct Position {
    x: usize,
    y: usize,
}

impl Position {
    fn new(x: usize, y: usize) -> Self {
        Position { x, y }
    }
}

impl From<&str> for Position {
    fn from(s: &str) -> Self {
        let (x, y) = s.split_once(",").expect("should have a comma in the &str");
        Self::new(
            x.parse().expect("should be a number"),
            y.parse().expect("should be a number"),
        )
    }
}

#[derive(Clone, Copy)]
struct Light {
    brightness: i32,
}

impl Light {
    fn new() -> Self {
        Self { brightness: 0 }
    }

    fn turn_on(&mut self) {
        self.brightness = 1;
    }
    fn turn_off(&mut self) {
        self.brightness = 0;
    }
    fn toggle(&mut self) {
        self.brightness = 1 - self.brightness;
    }

    fn dim(&mut self, amount: i32) {
        self.brightness = (self.brightness + amount).max(0);
    }
}

struct Grid {
    grid: [[Light; 1000]; 1000],
}

impl Grid {
    fn new() -> Self {
        Self {
            grid: [[Light::new(); 1000]; 1000],
        }
    }

    fn count_lit(&self) -> i32 {
        self.grid
            .iter()
            .flat_map(|inner| inner.iter())
            .map(|&light| light.brightness)
            .sum()
    }

    fn operate_lights(&mut self, instruction: &Instruction) {
        for y in instruction.start.y..=instruction.end.y {
            for x in instruction.start.x..=instruction.end.x {
                match instruction.operation {
                    Operation::TurnOn => self.grid[y][x].turn_on(),
                    Operation::TurnOff => self.grid[y][x].turn_off(),
                    Operation::Toggle => self.grid[y][x].toggle(),
                };
            }
        }
    }
    fn dim_lights(&mut self, instruction: &Instruction) {
        for y in instruction.start.y..=instruction.end.y {
            for x in instruction.start.x..=instruction.end.x {
                match instruction.operation {
                    Operation::TurnOn => self.grid[y][x].dim(1),
                    Operation::TurnOff => self.grid[y][x].dim(-1),
                    Operation::Toggle => self.grid[y][x].dim(2),
                };
            }
        }
    }
}

fn part_one(input: &str) -> i32 {
    let mut grid = Grid::new();
    let instructions: Vec<Instruction> = input.lines().map(Instruction::from).collect();
    for instruction in instructions {
        grid.operate_lights(&instruction)
    }
    grid.count_lit()
}

fn part_two(input: &str) -> i32 {
    let mut grid = Grid::new();
    let instructions: Vec<Instruction> = input.lines().map(Instruction::from).collect();
    for instruction in instructions {
        grid.dim_lights(&instruction)
    }
    grid.count_lit()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_instruction_from() {
        assert_eq!(
            Instruction::from("turn on 0,0 through 999,999"),
            Instruction::new(
                Operation::TurnOn,
                Position::new(0, 0),
                Position::new(999, 999)
            )
        );
        assert_eq!(
            Instruction::from("toggle 0,0 through 999,0"),
            Instruction::new(
                Operation::Toggle,
                Position::new(0, 0),
                Position::new(999, 0)
            )
        );
        assert_eq!(
            Instruction::from("turn off 499,499 through 500,500"),
            Instruction::new(
                Operation::TurnOff,
                Position::new(499, 499),
                Position::new(500, 500)
            )
        );
    }

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(INPUT), 400_410);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(INPUT), 15_343_601);
    }
}
