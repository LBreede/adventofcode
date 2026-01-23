use std::io::BufRead;
use std::ops::{Add, AddAssign};

pub fn start_day(day: &str) {
    println!("Advent of Code 2024 - Day {:0>2}", day);
}

// Additional common functions

#[derive(Debug)]
pub struct Grid {
    pub data: Vec<Vec<u8>>,
}

impl<R: BufRead> From<R> for Grid {
    fn from(reader: R) -> Self {
        Grid {
            data: reader
                .lines()
                .map_while(Result::ok)
                .map(|line| line.bytes().collect::<Vec<u8>>())
                .collect(),
        }
    }
}

impl Grid {
    pub fn height(&self) -> usize {
        self.data.len()
    }
    pub fn width(&self) -> usize {
        self.data[0].len()
    }
    pub fn get_value(&self, x: i32, y: i32) -> Option<u8> {
        if x >= 0 && x < self.width() as i32 && y >= 0 && y < self.height() as i32 {
            Some(self.data[y as usize][x as usize])
        } else {
            None
        }
    }
}

#[derive(Debug, PartialEq, Copy, Clone)]
pub struct Vector2<T> {
    x: T,
    y: T,
}

impl<T> Vector2<T> {
    pub fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl Add for Vector2<usize> {
    type Output = Vector2<usize>;
    fn add(self, rhs: Self) -> Self::Output {
        Vector2::new(self.x + rhs.x, self.y + rhs.y)
    }
}

impl AddAssign for Vector2<usize> {
    fn add_assign(&mut self, other: Self) {
        *self = Self {
            x: self.x + other.x,
            y: self.y + other.y,
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        start_day("00");
    }

    #[test]
    fn add_two_vec_usize() {
        assert_eq!(Vector2::new(2, 3) + Vector2::new(4, 6), Vector2::new(6, 9));
    }
}
