#include <cassert>
#include <iostream>
#include <string>

#include "common.h"

int part1(const std::string &input) {
  int floor = 0;
  for (const char c : input) {
    if (c == '(') {
      ++floor;
    } else if (c == ')') {
      --floor;
    }
  }
  return floor;
}

int part2(const std::string &input) {
  int floor = 0;
  for (std::size_t i = 0; i < input.size(); ++i) {
    const char c = input[i];
    if (c == '(') {
      ++floor;
    } else if (c == ')') {
      --floor;
    }
    if (floor < 0) {
      return i + 1;
    }
  }
  return 0;
}

int main() {
  int day = 1;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  assert(part1("(())") == 0);
  assert(part1("()()") == 0);
  assert(part1("(((") == 3);
  assert(part1("(()(()(") == 3);
  assert(part1("))(((((") == 3);
  assert(part1("())") == -1);
  assert(part1("))(") == -1);
  assert(part1(")))") == -3);
  assert(part1(")())())") == -3);

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  assert(part2(")") == 1);
  assert(part2("()())") == 5);

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
