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
  return std::make_tuple(a, b, c);
}
int calcPaperArea(const std::string &dimensions) {
  int l = 0;
  int w = 0;
  int h = 0;
  std::tie(l, w, h) = split_twice(dimensions);
  int lw = l * w;
  int wh = w * h;
  int hl = h * l;
  int slack = std::min({lw, wh, hl});
  return 2 * lw + 2 * wh + 2 * hl + slack;
}

int calcRibbonLength(const std::string &dimensions) {
  int l = 0;
  int w = 0;
  int h = 0;
  std::tie(l, w, h) = split_twice(dimensions);
  int min1 = std::min({l, w, h});
  int min2;
  if (min1 == l) {
    min2 = std::min(w, h);
  } else if (min1 == w) {
    min2 = std::min(l, w);
  } else {
    min2 = std::min(l, w);
  }
  return 2 * min1 + 2 * min2 + l * w * h;
}

int part1(const std::string &input) {
  std::istringstream stream(input);
  std::string line;
  int total = 0;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    total += calcPaperArea(line);
  }
  return total;
}
int part2(const std::string &input) {
  std::istringstream stream(input);
  std::string line;
  int total = 0;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    total += calcRibbonLength(line);
  }
  return total;
}

int main() {
  int day = 2;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  assert(calcPaperArea("2x3x4") == 58);
  assert(calcPaperArea("1x1x10") == 43);

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  assert(calcRibbonLength("2x3x4") == 34);
  assert(calcRibbonLength("1x1x10") == 14);

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
