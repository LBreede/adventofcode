#include <algorithm>
#include <cassert>
#include <sstream>
#include <string>
#include <tuple>

#include "common.h"

std::tuple<int, int, int> split_twice(const std::string &s) {
  std::istringstream stream(s);
  int a = 0;
  int b = 0;
  int c = 0;
  char first = '\0';
  char second = '\0';

  stream >> a >> first >> b >> second >> c;
  assert(stream && first == 'x' && second == 'x');
  return std::make_tuple(a, b, c);
}
uint32_t calc_paper_area(const std::string &dimensions) {
  uint32_t l = 0;
  uint32_t w = 0;
  uint32_t h = 0;
  std::tie(l, w, h) = split_twice(dimensions);
  uint32_t lw = l * w;
  uint32_t wh = w * h;
  uint32_t hl = h * l;
  uint32_t slack = std::min({lw, wh, hl});
  return 2 * lw + 2 * wh + 2 * hl + slack;
}

uint32_t calc_ribbon_length(const std::string &dimensions) {
  uint32_t l = 0;
  uint32_t w = 0;
  uint32_t h = 0;
  std::tie(l, w, h) = split_twice(dimensions);
  uint32_t min1 = std::min({l, w, h});
  uint32_t max1 = std::max({l, w, h});
  uint32_t min2 = l + w + h - min1 - max1;
  return 2 * min1 + 2 * min2 + l * w * h;
}

uint32_t part1(const std::string &input) {
  std::istringstream stream(input);
  std::string line;
  uint32_t total = 0;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    total += calc_paper_area(line);
  }
  return total;
}
uint32_t part2(const std::string &input) {
  std::istringstream stream(input);
  std::string line;
  uint32_t total = 0;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    total += calc_ribbon_length(line);
  }
  return total;
}

int main() {
  const unsigned int day = 2;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  assert(calc_paper_area("2x3x4") == 58);
  assert(calc_paper_area("1x1x10") == 43);

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  assert(calc_ribbon_length("2x3x4") == 34);
  assert(calc_ribbon_length("1x1x10") == 14);

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
