#include "common.h"
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

std::vector<std::string> split_lines(const std::string &s) {
  std::vector<std::string> lines;
  size_t start = 0;
  while (start < s.size()) {
    size_t end = s.find('\n', start);
    if (end == std::string::npos)
      end = s.size();
    lines.push_back(s.substr(start, end - start));
    start = end + 1;
  }
  return lines;
}

bool is_numeric(const std::string &s) {
  return !s.empty() && std::all_of(s.begin(), s.end(), [](unsigned char c) {
    return std::isdigit(c);
  });
}

bool process(std::string expr, std::string var,
             std::unordered_map<std::string, uint16_t> &vars) {

  switch (std::count(expr.begin(), expr.end(), ' ')) {
  case 0: {
    uint16_t value = std::stoi(expr);
    vars[var] = value;
    return true;
  }
  case 1: {
    std::string s = expr.substr(expr.find(' ') + 1);
    if (vars.find(s) == vars.end()) {
      return false;
    }
    uint16_t value = vars[s];
    vars[var] = ~value;
    return true;
  }

  case 2: {
    size_t first = expr.find(' ');
    size_t second = expr.find(' ', first + 1);
    std::string lhs = expr.substr(0, first);
    std::string rhs = expr.substr(second + 1);

    uint16_t value;

    switch (expr[first + 1]) {
    case 'A': {
      if (vars.find(lhs) == vars.end()) {
        return false;
      }
      if (vars.find(rhs) == vars.end()) {
        return false;
      }
      value = vars[lhs] & vars[rhs];
      break;
    }
    case 'O': {
      if (vars.find(lhs) == vars.end()) {
        return false;
      }
      if (vars.find(rhs) == vars.end()) {
        return false;
      }
      value = vars[lhs] | vars[rhs];
      break;
    }
    case 'L': {
      if (vars.find(lhs) == vars.end()) {
        return false;
      }
      value = vars[lhs] << std::stoi(rhs);
      break;
    }
    case 'R': {
      if (vars.find(lhs) == vars.end()) {
        return false;
      }
      value = vars[lhs] >> std::stoi(rhs);
      break;
    }
    }
    vars[var] = value;

    return true;
  }
  }
  return false; // unreachable

  if (is_numeric(expr)) {
    int value = std::stoi(expr);
    vars[var] = value;
    return true;
  }
  return false;
}

int part1(const std::string &input) {

  std::vector<std::string> lines = split_lines(input);

  std::string delimiter = " -> ";
  std::unordered_map<std::string, uint16_t> vars;

  size_t i = 0;

  while (!lines.empty()) {
    std::string s = lines[i];
    size_t pos = s.find(delimiter);
    if (pos == std::string::npos) {
      i = (i + 1) % lines.size();
      continue;
    }

    std::string lhs = s.substr(0, pos);
    std::string rhs = s.substr(pos + delimiter.size());

    if (process(lhs, rhs, vars)) {
      lines.erase(lines.begin() + i);
      if (!lines.empty() && i >= lines.size())
        i = 0;
    } else {
      i = (i + 1) % lines.size();
    }
  }

  for (const auto &[key, value] : vars) {
    std::cout << key << ": " << value << '\n';
  }
  return 1;
}

int part2(const std::string &input) { return 2; }

int main() {
  const unsigned int day = 7;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::string example = R"(123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i)";

  part1(example);

  std::cout << "Result = " << part1(input) << "\n";

  // std::cout << "\n=== Part 2 ===\n";
  //
  // std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
