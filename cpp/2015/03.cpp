#include <cassert>
#include <cstdint>
#include <functional>
#include <string>
#include <unordered_set>

#include "common.h"

struct Position {
  int x;
  int y;
};

bool operator==(const Position &lhs, const Position &rhs) {
  return lhs.x == rhs.x && lhs.y == rhs.y;
}

struct PositionHash {
  std::size_t operator()(const Position &pos) const {
    const std::size_t hx =
        std::hash<long long>{}(static_cast<long long>(pos.x));
    const std::size_t hy =
        std::hash<long long>{}(static_cast<long long>(pos.y));
    return hx ^ (hy + 0x9e3779b97f4a7c15ULL + (hx << 6) + (hx >> 2));
  }
};

int part1(const std::string &input) {
  Position position{0, 0};
  std::unordered_set<Position, PositionHash> positions;
  positions.reserve(input.size() + 1);
  positions.insert(position);

  for (const char direction : input) {
    switch (direction) {
    case '<':
      --position.x;
      break;
    case '>':
      ++position.x;
      break;
    case '^':
      ++position.y;
      break;
    case 'v':
      --position.y;
      break;
    default:
      continue;
    }
    positions.insert(position);
  }

  return static_cast<int>(positions.size());
}
int part2(const std::string &input) {
  Position position{0, 0};
  Position robo_position{0, 0};
  std::unordered_set<Position, PositionHash> positions;
  positions.reserve(input.size() + 2);
  positions.insert(position);

  int i = 0;
  for (const char direction : input) {
    Position *current = nullptr;
    switch (direction) {
    case '<':
      current = (i % 2 == 0) ? &position : &robo_position;
      --current->x;
      break;
    case '>':
      current = (i % 2 == 0) ? &position : &robo_position;
      ++current->x;
      break;
    case '^':
      current = (i % 2 == 0) ? &position : &robo_position;
      ++current->y;
      break;
    case 'v':
      current = (i % 2 == 0) ? &position : &robo_position;
      --current->y;
      break;
    default:
      continue;
    }
    positions.insert(*current);
    ++i;
  }

  return static_cast<int>(positions.size());
}

int main() {
  int day = 3;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  assert(part1(">") == 2);
  assert(part1("^>v<") == 4);
  assert(part1("^v^v^v^v^v") == 2);

  const std::string input_path = input_path_for_day(day);
  const std::string input = read_file(input_path.c_str());
  if (input.empty()) {
    std::cerr << "Failed to read " << input_path << "\n";
    return 1;
  }

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  assert(part2("^v") == 3);
  assert(part2("^>v<") == 3);
  assert(part2("^v^v^v^v^v") == 11);

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
