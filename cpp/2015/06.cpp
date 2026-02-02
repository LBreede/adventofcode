
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

#include "common.h"

constexpr int W = 1000;
constexpr int H = 1000;

uint32_t &at(std::vector<uint32_t> &grid, int x, int y) {
  return grid[y * W + x];
}

void turn_on(std::vector<uint32_t> &grid, int x, int y) { at(grid, x, y) = 1; }
void turn_off(std::vector<uint32_t> &grid, int x, int y) { at(grid, x, y) = 0; }
void toggle(std::vector<uint32_t> &grid, int x, int y) { at(grid, x, y) ^= 1u; }

void increment(std::vector<uint32_t> &grid, int x, int y) { ++at(grid, x, y); }
void decrement(std::vector<uint32_t> &grid, int x, int y) {
  if (at(grid, x, y) > 0)
    --at(grid, x, y);
}

enum class Op { On, Off, Toggle };

struct Instruction {
  Op op;
  int x1, y1, x2, y2;
};

bool starts_with(const std::string &s, const std::string &prefix) {
  return s.size() >= prefix.size() && s.compare(0, prefix.size(), prefix) == 0;
}

Instruction parse(const std::string &line) {
  Instruction inst;

  if (starts_with(line, "turn on")) {
    inst.op = Op::On;
    std::sscanf(line.c_str(), "turn on %d,%d through %d,%d", &inst.x1, &inst.y1,
                &inst.x2, &inst.y2);
  } else if (starts_with(line, "turn off")) {
    inst.op = Op::Off;
    std::sscanf(line.c_str(), "turn off %d,%d through %d,%d", &inst.x1,
                &inst.y1, &inst.x2, &inst.y2);
  } else if (starts_with(line, "toggle")) {
    inst.op = Op::Toggle;
    std::sscanf(line.c_str(), "toggle %d,%d through %d,%d", &inst.x1, &inst.y1,
                &inst.x2, &inst.y2);
  } else {
    throw std::runtime_error("unknown instruction");
  }

  return inst;
}

void apply(std::vector<uint32_t> &grid, const Instruction &inst) {
  for (int y = inst.y1; y <= inst.y2; ++y) {
    for (int x = inst.x1; x <= inst.x2; ++x) {
      switch (inst.op) {
      case Op::On:
        turn_on(grid, x, y);
        break;
      case Op::Off:
        turn_off(grid, x, y);
        break;
      case Op::Toggle:
        toggle(grid, x, y);
        break;
      }
    }
  }
}
void apply2(std::vector<uint32_t> &grid, const Instruction &inst) {
  for (int y = inst.y1; y <= inst.y2; ++y) {
    for (int x = inst.x1; x <= inst.x2; ++x) {
      switch (inst.op) {
      case Op::On:
        increment(grid, x, y);
        break;
      case Op::Off:
        decrement(grid, x, y);
        break;
      case Op::Toggle:
        at(grid, x, y) += 2;
        break;
      }
    }
  }
}

std::uint32_t part1(const std::string &input) {
  std::vector<uint32_t> grid(W * H, 0);
  std::istringstream stream(input);
  std::string line;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    Instruction inst = parse(line);
    apply(grid, inst);
  }
  return std::accumulate(grid.begin(), grid.end(), 0u);
}
std::uint32_t part2(const std::string &input) {
  std::vector<uint32_t> grid(W * H, 0);
  std::istringstream stream(input);
  std::string line;
  while (std::getline(stream, line)) {
    if (line.empty()) {
      continue;
    }
    Instruction inst = parse(line);
    apply2(grid, inst);
  }
  return std::accumulate(grid.begin(), grid.end(), 0u);
}

int main() {
  const unsigned int day = 6;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
