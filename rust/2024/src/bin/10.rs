use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "10";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
";

const EXAMPLE2: &str = "\
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
";

const EXAMPLE3: &str = "\
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
";

const EXAMPLE4: &str = "\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
";

const EXAMPLE5: &str = "\
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
";

const EXAMPLE6: &str = "\
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
";

const EXAMPLE7: &str = "\
012345
123456
234567
345678
4.6789
56789.
";

const EXAMPLE8: &str = "\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let nodes = parse_nodes(reader);
        let start_indices = find_start_indices(&nodes);
        Ok(start_indices
            .into_iter()
            .map(|index| count_paths(&nodes, index, 9))
            .sum())
    }

    assert_eq!(2, part1(BufReader::new(EXAMPLE.as_bytes()))?);
    assert_eq!(4, part1(BufReader::new(EXAMPLE2.as_bytes()))?);
    assert_eq!(3, part1(BufReader::new(EXAMPLE3.as_bytes()))?);
    assert_eq!(36, part1(BufReader::new(EXAMPLE4.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let nodes = parse_nodes(reader);
        let start_indices = find_start_indices(&nodes);
        Ok(start_indices
            .into_iter()
            .map(|index| count_all_paths(&nodes, index, 9))
            .sum())
    }

    assert_eq!(3, part2(BufReader::new(EXAMPLE5.as_bytes()))?);
    assert_eq!(13, part2(BufReader::new(EXAMPLE6.as_bytes()))?);
    assert_eq!(227, part2(BufReader::new(EXAMPLE7.as_bytes()))?);
    assert_eq!(81, part2(BufReader::new(EXAMPLE8.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

#[derive(Debug)]
struct Node {
    value: u8,
    children: Vec<usize>,
}

fn parse_nodes<R: BufRead>(reader: R) -> Vec<Option<Node>> {
    let lines = reader
        .lines()
        .map_while(Result::ok)
        .map(|row| row.bytes().collect::<Vec<u8>>())
        .collect::<Vec<Vec<u8>>>();

    // let height = lines.len();
    let width = lines[0].len();

    let mut nodes: Vec<Option<Node>> = vec![];

    for (i, row) in lines.clone().into_iter().enumerate() {
        for (j, b) in row.into_iter().enumerate() {
            if b == b'.' {
                nodes.push(None);
                continue;
            }

            let value = b - 48;
            let mut children: Vec<usize> = vec![];

            // i-1, j
            if let Some(k) = i.checked_sub(1) {
                let m = lines[k][j];
                if m != b'.' {
                    let m = m - 48;
                    if m == value + 1 {
                        children.push(k * width + j);
                    }
                }
            }
            // i+1, j
            if let Some(k) = lines.get(i + 1) {
                let m = k[j];
                if m != b'.' {
                    let m = m - 48;
                    if m == value + 1 {
                        children.push((i + 1) * width + j);
                    }
                }
            }

            // i, j-1
            if let Some(k) = j.checked_sub(1) {
                let m = lines[i][k];
                if m != b'.' {
                    let m = m - 48;
                    if m == value + 1 {
                        children.push(i * width + k);
                    }
                }
            }

            // i, j+1
            if let Some(k) = lines[i].get(j + 1) {
                let m = *k;
                if m != b'.' {
                    let m = m - 48;
                    if m == value + 1 {
                        children.push(i * width + j + 1);
                    }
                }
            }
            nodes.push(Some(Node { value, children }));
        }
    }

    nodes
}

fn find_start_indices(nodes: &[Option<Node>]) -> Vec<usize> {
    nodes
        .iter()
        .enumerate()
        .filter_map(|(i, &ref x)| {
            if x.is_some() && x.as_ref().unwrap().value == 0 {
                Some(i)
            } else {
                None
            }
        })
        .collect()
}

fn count_paths(nodes: &[Option<Node>], start_index: usize, end_value: u8) -> usize {
    let mut count = 0;
    let mut stack: Vec<usize> = vec![start_index];
    let mut visited: Vec<bool> = vec![false; nodes.len()];

    while let Some(index) = stack.pop() {
        if visited[index] {
            continue;
        }
        visited[index] = true;

        if let Some(node) = &nodes[index] {
            if node.value == end_value {
                count += 1;
            }
            for &child in node.children.iter() {
                stack.push(child);
            }
        }
    }
    count
}

fn count_all_paths(nodes: &[Option<Node>], start_index: usize, end_value: u8) -> usize {
    let mut count = 0;
    let mut stack: Vec<usize> = vec![start_index];

    while let Some(index) = stack.pop() {
        if let Some(node) = &nodes[index] {
            if node.value == end_value {
                count += 1;
                // Don't explore further down this path
                continue;
            }
            for &child in node.children.iter() {
                stack.push(child);
            }
        }
    }
    count
}
