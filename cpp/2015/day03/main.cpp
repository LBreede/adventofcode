#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

int partOne(std::istream& file) {
    int x = 0;
    int y = 0;

    std::vector<std::tuple<int, int>> positions = {std::make_tuple(x, y)};

    char ch;
    while (file.get(ch)) {
        if (ch == '^') {
            y++;
        } else if (ch == 'v') {
            y--;
        } else if (ch == '>') {
            x++;
        } else if (ch == '<') {
            x--;
        } else {
            throw std::runtime_error("Invalid character");
        }
        std::tuple<int, int> pos = std::make_tuple(x, y);
        if (std::find(positions.begin(), positions.end(), pos) == positions.end()) {
            positions.push_back(pos);
        }
    }
    return positions.size();
}

int partOne(const std::string& input) {
    std::istringstream stream(input);
    return partOne(stream);
}

int partTwo(std::istream& file) {
    std::vector<std::tuple<int, int>> positions = {std::make_tuple(0, 0)};

    int xa = 0;
    int ya = 0;
    int xb = 0;
    int yb = 0;

    char ch;
    int i = 0;
    while (file.get(ch)) {
        if (ch == '^') {
            if (i % 2 == 0) {
                ya++;
            } else {
                yb++;
            }
        } else if (ch == 'v') {
            if (i % 2 == 0) {
                ya--;
            } else {
                yb--;
            }
        } else if (ch == '>') {
            if (i % 2 == 0) {
                xa++;
            } else {
                xb++;
            }
        } else if (ch == '<') {
            if (i % 2 == 0) {
                xa--;
            } else {
                xb--;
            }
        } else {
            throw std::runtime_error("Invalid character");
        }
        std::tuple<int, int> pos = std::make_tuple(xa, ya);
        if (std::find(positions.begin(), positions.end(), pos) == positions.end()) {
            positions.push_back(pos);
        }
        pos = std::make_tuple(xb, yb);
        if (std::find(positions.begin(), positions.end(), pos) == positions.end()) {
            positions.push_back(pos);
        }
        i++;
    }
    return positions.size();
}

int partTwo(const std::string& input) {
    std::istringstream stream(input);
    return partTwo(stream);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input file>" << std::endl;
        return 1;
    }

    assert(partOne(">") == 2);
    assert(partOne("^>v<") == 4);
    assert(partOne("^v^v^v^v^v") == 2);

    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Cannot open file: " << argv[1] << std::endl;
        return 1;
    }

    std::cout << "Part 1: " << partOne(file) << std::endl;

    assert(partTwo("^v") == 3);
    assert(partTwo("^>v<") == 3);
    assert(partTwo("^v^v^v^v^v") == 11);

    file.clear();
    file.seekg(0);

    std::cout << "Part 2: " << partTwo(file) << std::endl;

    return 0;
}