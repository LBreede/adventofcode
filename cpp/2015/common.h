#pragma once

#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

inline void start_day(int day) {
  std::cout << "Advent of Code 2025 - Day " << std::setw(2) << std::setfill('0')
            << day << "\n\n";
}

inline std::string input_path_for_day(int day) {
  std::ostringstream path_builder;
  path_builder << "./input/" << std::setw(2) << std::setfill('0') << day
               << ".txt";
  return path_builder.str();
}

inline std::string read_file(const char *path) {
  std::ifstream file(path);
  if (!file) {
    return {};
  }
  return {std::istreambuf_iterator<char>(file),
          std::istreambuf_iterator<char>()};
}
