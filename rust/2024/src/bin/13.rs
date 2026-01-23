use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "13";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(mut reader: R) -> Result<usize> {
        let mut content = String::new();
        reader.read_to_string(&mut content)?;
        let content = content.replace("\r\n", "\n");

        let mut games: Vec<Game> = Vec::new();

        for s in content.split("\n\n") {
            let mut lines = s.split("\n");

            let (ax, ay) = lines
                .next()
                .unwrap()
                .strip_prefix("Button A: ")
                .unwrap()
                // .trim()
                .split_once(", ")
                .unwrap();

            let a = Vector2::new(
                ax.strip_prefix("X+").unwrap().parse::<usize>()?,
                ay.strip_prefix("Y+").unwrap().parse::<usize>()?,
            );

            let (bx, by) = lines
                .next()
                .unwrap()
                .strip_prefix("Button B: ")
                .unwrap()
                // .trim()
                .split_once(", ")
                .unwrap();
            let b = Vector2::new(
                bx.strip_prefix("X+").unwrap().parse::<usize>()?,
                by.strip_prefix("Y+").unwrap().parse::<usize>()?,
            );

            let (cx, cy) = lines
                .next()
                .unwrap()
                .strip_prefix("Prize: ")
                .unwrap()
                // .trim()
                .split_once(", ")
                .unwrap();
            let c = Vector2::new(
                cx.strip_prefix("X=").unwrap().parse::<usize>()?,
                cy.strip_prefix("Y=").unwrap().parse::<usize>()?,
            );

            let game = Game {
                button_a: a,
                button_b: b,
                prize: c,
            };
            games.push(game);
        }

        let mut tokens_spent = 0;
        for game in games {
            'outer: for a in 0..100 {
                for b in 0..100 {
                    let mut position = Vector2::new(0_usize, 0_usize);
                    for j in 0..a {
                        position += game.button_a;
                        if position == game.prize {
                            tokens_spent += (j + 1) * 3;
                            break 'outer;
                        }
                    }
                    for k in 0..b {
                        position += game.button_b;
                        if position == game.prize {
                            tokens_spent += a * 3 + (k + 1);
                            break 'outer;
                        }
                    }
                    // println!("bi = {:?}, ai = {:?}, position = {:?}", b, a, position);
                }
            }
        }
        Ok(tokens_spent)
    }

    // assert_eq!(480, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    // println!("\n=== Part 2 ===");
    //
    // fn part2<R: BufRead>(reader: R) -> Result<usize> {
    //     Ok(0)
    // }
    //
    // assert_eq!(0, part2(BufReader::new(EXAMPLE.as_bytes()))?);
    //
    // let input_file = BufReader::new(File::open(INPUT_FILE)?);
    // let result = time_snippet!(part2(input_file)?);
    // println!("Result = {}", result);
    //endregion

    Ok(())
}

#[derive(Debug)]
struct Game {
    button_a: Vector2<usize>,
    button_b: Vector2<usize>,
    prize: Vector2<usize>,
}
