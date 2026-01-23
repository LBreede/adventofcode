use adv_code_2024::*;
use anyhow::{Context, Result};
use code_timing_macros::time_snippet;
use const_format::concatcp;
use itertools::Itertools;
use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "12";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
AAAA
BBCD
BBCC
EEEC
";

const EXAMPLE2: &str = "\
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
";

const EXAMPLE3: &str = "\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
";

const EXAMPLE4: &str = "\
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
";

const EXAMPLE5: &str = "\
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
";

type Region = HashSet<Position>;

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let regions = find_regions(Grid::from(reader));

        // Calculate price
        let mut price: usize = 0;
        for region in regions {
            let area = region.len();
            let perimeter: usize = region
                .iter()
                .map(|pos| {
                    let mut neighbours = 0;
                    for (x, y) in [(0, -1), (1, 0), (0, 1), (-1, 0)].iter() {
                        if region.iter().contains(&Position {
                            x: pos.x + x,
                            y: pos.y + y,
                        }) {
                            neighbours += 1;
                        }
                    }
                    4 - neighbours
                })
                .sum();
            price += area * perimeter;
        }

        Ok(price)
    }

    assert_eq!(140, part1(BufReader::new(EXAMPLE.as_bytes()))?);
    assert_eq!(772, part1(BufReader::new(EXAMPLE2.as_bytes()))?);
    assert_eq!(1930, part1(BufReader::new(EXAMPLE3.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let regions = find_regions(Grid::from(reader));
        // Calculate price
        let mut price: usize = 0;
        for region in regions {
            let area = region.len();
            let sides: usize = region
                .iter()
                .map(|pos| {
                    let n = region.contains(&Position::new(pos.x, pos.y - 1));
                    let ne = region.contains(&Position::new(pos.x + 1, pos.y - 1));
                    let e = region.contains(&Position::new(pos.x + 1, pos.y));
                    let se = region.contains(&Position::new(pos.x + 1, pos.y + 1));
                    let s = region.contains(&Position::new(pos.x, pos.y + 1));
                    let sw = region.contains(&Position::new(pos.x - 1, pos.y + 1));
                    let w = region.contains(&Position::new(pos.x - 1, pos.y));
                    let nw = region.contains(&Position::new(pos.x - 1, pos.y - 1));

                    let mut corners = 0;
                    for (i, j, k) in [(n, ne, e), (e, se, s), (s, sw, w), (w, nw, n)].into_iter() {
                        corners += match (i, j, k) {
                            (true, false, true) => 1,
                            (false, false, false) => 1,
                            (false, true, false) => 1,
                            _ => 0,
                        }
                    }
                    corners
                })
                .sum();
            price += area * sides;
        }
        Ok(price)
    }

    assert_eq!(80, part2(BufReader::new(EXAMPLE.as_bytes()))?);
    assert_eq!(436, part2(BufReader::new(EXAMPLE2.as_bytes()))?);
    assert_eq!(236, part2(BufReader::new(EXAMPLE4.as_bytes()))?);
    assert_eq!(368, part2(BufReader::new(EXAMPLE5.as_bytes()))?);
    assert_eq!(1206, part2(BufReader::new(EXAMPLE3.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

#[derive(Debug, Eq, PartialEq, Hash)]
struct Position {
    x: i32,
    y: i32,
}

impl Position {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }
}

fn flood_fill(target: u8, x: i32, y: i32, grid: &Grid, mut region: Region) -> Region {
    region.insert(Position { x, y });
    if let Some(north) = grid.get_value(x, y - 1) {
        if north == target && !region.contains(&Position { x, y: y - 1 }) {
            region = flood_fill(target, x, y - 1, grid, region);
        }
    }
    if let Some(east) = grid.get_value(x + 1, y) {
        if east == target && !region.contains(&Position { x: x + 1, y }) {
            region = flood_fill(target, x + 1, y, grid, region);
        }
    }
    if let Some(south) = grid.get_value(x, y + 1) {
        if south == target && !region.contains(&Position { x, y: y + 1 }) {
            region = flood_fill(target, x, y + 1, grid, region);
        }
    }
    if let Some(west) = grid.get_value(x - 1, y) {
        if west == target && !region.contains(&Position { x: x - 1, y }) {
            region = flood_fill(target, x - 1, y, grid, region);
        }
    }
    region
}
fn find_regions(grid: Grid) -> Vec<Region> {
    let mut regions: Vec<Region> = Vec::new();
    for i in 0..grid.height() {
        for j in 0..grid.width() {
            let value = grid
                .get_value(j as i32, i as i32)
                .context("Invalid position")
                .unwrap();
            if !regions.iter().any(|region| {
                region.contains(&Position {
                    x: j as i32,
                    y: i as i32,
                })
            }) {
                let region: Region = HashSet::new();
                let region = flood_fill(value, j as i32, i as i32, &grid, region);
                regions.push(region);
            }
        }
    }
    regions
}
