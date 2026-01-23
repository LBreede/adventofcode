# Advent of Code 2024 in Rust :christmas_tree::crab:

My solutions for [Advent of Code](https://adventofcode.com/2024) 2024
in [Rust](https://www.rust-lang.org/).

I was encouraged to use in [RustRover](https://www.jetbrains.com/rust/) after
reading [this blog post](https://blog.jetbrains.com/rust/2024/11/29/advent-of-code-in-rust-for-the-rest-of-us/)
by Vitaly Bragilevsky.

## Progress :star:

| Day | Part 1 | Part 2 |
|:---:|:------:|:------:|
|  1  | :star: | :star: |
|  2  | :star: | :star: |
|  3  | :star: | :star: |
|  4  | :star: | :star: |
|  5  | :star: | :star: |
|  6  | :star: | :star: |
|  7  | :star: | :star: |
|  8  | :star: | :star: |
|  9  | :star: | :star: |
| 10  | :star: | :star: |
| 11  | :star: | :star: |
| 12  | :star: | :star: |
| 13  | :star: |        |

## Timings :stopwatch:

`cargo run --bin <DAY> --profile release`

| Day |   Part 1    |   Part 2    |
|:---:|:-----------:|:-----------:|
|  1  |  `1.593ms`  | `497.182µs` |
|  2  | `502.757µs` |  `1.345ms`  |
|  3  |  `1.676ms`  | `776.282µs` |
|  4  | `979.156µs` | `234.270µs` |
|  5  | `13.677ms`  | `30.662ms`  |
|  6  | `516.75µs`  |  `7.650s`   |
|  7  | `21.319ms`  |  `1.302s`   |
|  8  | `104.208µs` | `224.995µs` |
|  9  | `669.350ms` |  `1.467s`   |
| 10  | `567.317µs` | `334.273µs` |
| 11  | `755.844µs` | `14.271ms`  |
| 12  | `131.339ms` | `155.273ms` |
| 13  | `200.596ms` |     ``      |

***

# Template for solving Advent of Code puzzles in Rust with RustRover

Read
the [blog post](https://blog.jetbrains.com/rust/2024/11/29/advent-of-code-in-rust-for-the-rest-of-us/)
that
explains the structure and rationale behind this template.

## Usage

1. Create a new project from the template repository:
    - Using GitHub’s templating feature: Simply click the Use this
      template [button](https://github.com/new?template_name=advent-of-code-rust-template&template_owner=bravit)
      on the
      repository page, create a new repository, and then open it
      in [RustRover](https://www.jetbrains.com/rust/) by
      selecting *File | New | Project From Version Control…*.
    - Adding the template to RustRover: You can integrate the template directly into
      RustRover and use the regular New
      Project wizard.

2. Whenever you're ready to start solving a new day's puzzle:
    - Open the `bin` folder, copy and paste the `NN.rs` file into it, and give it the
      corresponding name (`01.rs`,
      `02.rs`, etc.).
    - In the `input` folder, create and fill the input data file (`01.txt`, `02.txt`,
      etc.).
    - Fill in the `DAY` constant in the freshly created file.
    - Run the current day's solution to check if it compiles (you can use the gutter
      icon next to the `main` function).
    - Fill in `<TEST-INPUT>`.
    - Write the expected answer for the test data in the `assert_eq` statement in *Part
      1*.
    - Now you're ready to write your solution in the `part1` function (inside `main`).
    - Use `Shift+F10` (Win/Linux) or `Ctrl-R` (macOS) to re-run the same program.

3. When you're done with the first part of the puzzle, use folding to hide *Part 1*.

4. Uncomment *Part 2*, fill in the test data assertion, and start solving it.
