fn main() {
    println!("Hello, world!");
}
#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "1721
979
366
299
675
1456";

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}