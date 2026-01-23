use adv_code_2024::*;
use anyhow::Result;
use code_timing_macros::time_snippet;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};

const DAY: &str = "05";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
";

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let lines: Vec<String> = reader.lines().map_while(Result::ok).collect();
        let page_ordering_rules = parse_page_ordering_rules(&lines);
        let pages_to_produce = parse_pages_to_produce(&lines);

        let mut answer = 0;
        for pages in pages_to_produce {
            let mut validity = 1;
            'outer: for (i, &page) in pages.iter().enumerate() {
                for &next_page in pages[i + 1..].iter() {
                    if page_ordering_rules.contains(&[next_page, page]) {
                        validity = 0;
                        break 'outer;
                    }
                }
            }
            answer += pages.get(pages.len().div_euclid(2)).unwrap() * validity;
        }
        Ok(answer)
    }

    assert_eq!(143, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part1(input_file)?);
    println!("Result = {}", result);
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let lines: Vec<String> = reader.lines().map_while(Result::ok).collect();
        let page_ordering_rules = parse_page_ordering_rules(&lines);
        let pages_to_produce = parse_pages_to_produce(&lines);

        let mut answer = 0;
        for mut pages in pages_to_produce {
            let mut k = 0;

            // We loop over a range, rather than the vec itself since we want to mutate the vec
            // while looping over it.
            for i in 0..pages.len() - 1 {
                'inner: loop {
                    for j in (i + 1)..pages.len() {
                        // If `page_order_rules` contains the incorrect ordering, we swap the
                        // incorrect indices, set `k` to 1 to indicate that these pages were changed
                        // and finally `continue` the inner loop to re-check the ordering from the
                        // current `i`, not from the very beginning.
                        if page_ordering_rules.contains(&[pages[j], pages[i]]) {
                            pages.swap(i, j);
                            k = 1;
                            continue 'inner;
                        }
                        // If `j` reaches the end of pages, that means `i` is in the correct place
                        // We can therefore break out of the inner loop, increment `i` and continue
                        // looping.
                        if j == pages.len() - 1 {
                            break 'inner;
                        }
                    }
                }
            }
            answer += pages.get(pages.len().div_euclid(2)).unwrap() * k;
        }
        Ok(answer)
    }

    assert_eq!(123, part2(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let result = time_snippet!(part2(input_file)?);
    println!("Result = {}", result);
    //endregion

    Ok(())
}

/// This function parses the first part of the input. The two parts are separated by an empty line,
/// therefore `take_while` can be used to create an iterator from the beginning until an empty line
/// is reached. That iterator can then be processed using `map` and `split_once("|")`.
fn parse_page_ordering_rules(lines: &[String]) -> Vec<[usize; 2]> {
    lines
        .iter()
        .take_while(|line| !line.is_empty())
        .map(|line| {
            let (x, y) = line
                .split_once("|")
                .expect("Invalid format in page ordering rules");
            [
                x.parse().expect("Invalid number in page ordering rules"),
                y.parse().expect("Invalid number in page ordering rules"),
            ]
        })
        .collect()
}

/// This function parses the second part of the input. The two parts are separated by an empty line,
/// therefore `skip_while` can be used to ignore all items until an empty line is reached. `skip(1)`
/// is used too to ignore the empty line. From there until the end, the iterator can then be
/// processed using `map`, `split`, and `parse`.
fn parse_pages_to_produce(lines: &[String]) -> Vec<Vec<usize>> {
    lines
        .iter()
        .skip_while(|line| !line.is_empty())
        .skip(1)
        .map(|line| {
            line.split(",")
                .map(|x| x.parse().expect("Invalid number in pages to produce"))
                .collect()
        })
        .collect()
}
