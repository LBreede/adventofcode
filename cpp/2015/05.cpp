#include <cassert>
#include <regex>
#include <string>

#include "common.h"

bool rule1(const std::string &s) {
  static const std::regex e(R"(([aeiou].*){3,})");
  return std::regex_search(s, e);
}

bool rule2(const std::string &s) {
  static const std::regex e(R"((.)\1)");
  return std::regex_search(s, e);
}

bool rule3(const std::string &s) {
  static const std::regex e(R"(ab|cd|pq|xy)");
  return !std::regex_search(s, e);
}

bool rule4(const std::string &s) {
  static const std::regex e(R"((..).*\1)");
  return std::regex_search(s, e);
}

bool rule5(const std::string &s) {
  static const std::regex e(R"((.).\1)");
  return std::regex_search(s, e);
}

bool is_nice1(const std::string &s) { return rule1(s) && rule2(s) && rule3(s); }
bool is_nice2(const std::string &s) { return rule4(s) && rule5(s); }

std::uint32_t part1(const std::string &input) {
  std::istringstream stream(input);
  std::string line;
  std::uint32_t total = 0;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    total += is_nice1(line);
  }
  return total;
}
std::uint32_t part2(const std::string &input) {
  std::istringstream stream(input);
  std::string line;
  std::uint32_t total = 0;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    total += is_nice2(line);
  }
  return total;
}

int main() {
  const unsigned int day = 5;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  assert(rule1("aei"));
  assert(rule1("xazegov"));
  assert(rule1("aeiouaeiouaeiou"));

  assert(rule2("xx"));
  assert(rule2("abcdde"));
  assert(rule2("aabbccdd"));

  assert(is_nice1("ugknbfddgicrmopn"));
  assert(is_nice1("aaa"));
  assert(!is_nice1("jchzalrnumimnmhp"));
  assert(!is_nice1("haegwjzuvuyypxyu"));
  assert(!is_nice1("dvszwmarrgswjxmb"));

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  assert(rule4("xyxy"));
  assert(rule4("aabcdefgaa"));
  assert(!rule4("aaa"));

  assert(rule5("xyx"));
  assert(rule5("abcdefeghi"));
  assert(rule5("aaa"));

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
