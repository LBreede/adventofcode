use itertools::izip;
use std::time::Instant;
use thousands::Separable;

pub fn run() {
    println!("Day 5: If You Give A Seed A Fertilizer");
    let input = include_str!("input.txt");

    let now = Instant::now();
    let result = part_one(input);
    let elapsed = now.elapsed();
    println!(
        "Part 1: {} ({:.2?})",
        result.separate_with_commas(),
        elapsed
    );

    println!("Part 2: Skipped!");
    // let now = Instant::now();
    // let result = part_two(input);
    // let elapsed = now.elapsed();
    // println!("Part 2: {} ({:.2?})", result.separate_with_commas(), elapsed);

    println!();
}

#[derive(Default, Debug)]
struct Map {
    dst_start_vec: Vec<u64>,
    src_start_vec: Vec<u64>,
    range_len_vec: Vec<u64>,
}

impl Map {
    fn from(s: &str) -> Self {
        let mut m = Self::default();
        for line in s.lines() {
            let abc: Vec<u64> = line
                .split_whitespace()
                .map(|n| n.parse::<u64>().expect("invalid number"))
                .collect();
            m.push_dst_start(abc[0]);
            m.push_src_start(abc[1]);
            m.push_range_len(abc[2]);
        }
        m
    }

    fn push_dst_start(&mut self, value: u64) {
        self.dst_start_vec.push(value);
    }
    fn push_src_start(&mut self, value: u64) {
        self.src_start_vec.push(value);
    }
    fn push_range_len(&mut self, value: u64) {
        self.range_len_vec.push(value);
    }
    fn convert(&self, src: u64) -> u64 {
        for (src_start, dst_start, range_len) in izip!(
            self.src_start_vec.clone(),
            self.dst_start_vec.clone(),
            self.range_len_vec.clone()
        ) {
            if src >= src_start && src < src_start + range_len {
                return dst_start + (src - src_start);
            }
        }
        src
    }
}

fn part_one(input: &str) -> u64 {
    let mut iter = input.split("\n\n").collect::<Vec<&str>>().into_iter();
    let seeds: Vec<u64> = iter
        .next()
        .unwrap()
        .split_once(": ")
        .unwrap()
        .1
        .split_whitespace()
        .map(|n| n.parse::<u64>().expect("invalid number"))
        .collect();
    let seed_to_soil_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let soil_to_fert_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let fert_to_watr_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let watr_to_lght_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let lght_to_temp_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let temp_to_humi_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let humi_to_locn_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);

    seeds
        .into_iter()
        .map(|seed| {
            let mut loc = seed_to_soil_map.convert(seed);
            loc = soil_to_fert_map.convert(loc);
            loc = fert_to_watr_map.convert(loc);
            loc = watr_to_lght_map.convert(loc);
            loc = lght_to_temp_map.convert(loc);
            loc = temp_to_humi_map.convert(loc);
            humi_to_locn_map.convert(loc)
        })
        .min()
        .expect("should have found a min")
}

/// Solve part 2
///
/// Takes ages, it's ridiculous!
/// TODO: Make fast one day!
fn part_two(input: &str) -> u64 {
    let mut iter = input.split("\n\n").collect::<Vec<&str>>().into_iter();
    let seeds: Vec<u64> = iter
        .next()
        .unwrap()
        .split_once(": ")
        .unwrap()
        .1
        .split_whitespace()
        .map(|n| n.parse::<u64>().expect("invalid number"))
        .collect();
    let seed_to_soil_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let soil_to_fert_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let fert_to_watr_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let watr_to_lght_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let lght_to_temp_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let temp_to_humi_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);
    let humi_to_locn_map = Map::from(iter.next().unwrap().split_once("\n").unwrap().1);

    let mut all_seeds: Vec<u64> = Vec::new();

    for i in (0..seeds.len()).step_by(2) {
        for j in seeds[i]..(seeds[i] + seeds[i + 1]) {
            all_seeds.push(j);
        }
    }
    let mut min_loc = u64::MAX;
    // let bar = ProgressBar::new(all_seeds.len().try_into().unwrap());
    for seed in all_seeds {
        let mut loc = seed_to_soil_map.convert(seed);
        loc = soil_to_fert_map.convert(loc);
        loc = fert_to_watr_map.convert(loc);
        loc = watr_to_lght_map.convert(loc);
        loc = lght_to_temp_map.convert(loc);
        loc = temp_to_humi_map.convert(loc);
        loc = humi_to_locn_map.convert(loc);
        min_loc = loc.min(min_loc);
        // bar.inc(1);
    }
    min_loc
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_map() {
        let input = r#"50 98 2
52 50 48"#;
        let map = Map::from(input);
        assert_eq!(map.convert(79), 81);
        assert_eq!(map.convert(14), 14);
        assert_eq!(map.convert(55), 57);
        assert_eq!(map.convert(13), 13);
    }

    #[test]
    fn test_part_one_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_one(input), 35);
    }

    #[test]
    fn test_part_one() {
        let input = include_str!("input.txt");
        assert_eq!(part_one(input), 388_071_289);
    }

    #[test]
    fn test_part_two_example() {
        let input = include_str!("example.txt");
        assert_eq!(part_two(input), 46);
    }

    // #[test]
    // fn test_part_two() {
    //     let input = include_str!("input.txt");
    //     assert_eq!(part_two(input), 84_206_669);
    // }
}
