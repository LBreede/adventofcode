#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>

std::tuple<int, int, int> parseDimensions(const std::string& input) {
    int l, w, h;

    std::string dimensions = input;
    for (char& c : dimensions) {
        if (c == 'x') {
            c = ' ';
        }
    }
    std::stringstream ss(dimensions);
    ss >> l >> w >> h;

    return {l, w, h};
}

int measurePaper(const std::string& input) {
    int l, w, h;
    std::tie(l, w, h) = parseDimensions(input);
    int lw = l * w;
    int wh = w * h;
    int hl = h * l;
    int min_side = std::min({lw, wh, hl});
    return 2 * lw + 2 * wh + 2 * hl + min_side;
}

int measureRibbon(const std::string& input) {
    int l, w, h;
    std::tie(l, w, h) = parseDimensions(input);
    std::array<int, 3> lwh = {l, w, h};
    std::sort(std::begin(lwh), std::end(lwh));
    int a = lwh[0];
    int b = lwh[1];
    return 2 * a + 2 * b + l * w * h;
}

int partOne(std::istream& file) {
    std::string line;
    int total = 0;
    while (std::getline(file, line)) {
        total += measurePaper(line);
    }
    return total;
}

int partTwo(std::istream& file) {
    std::string line;
    int total = 0;
    while (std::getline(file, line)) {
        total += measureRibbon(line);
    }
    return total;
}
int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input file>" << std::endl;
        return 1;
    }

    assert(measurePaper("2x3x4") == 58);
    assert(measurePaper("1x1x10") == 43);

    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << argv[1] << std::endl;
        return 1;
    }

    int result_one = partOne(file);
    std::cout << "Part 1: " << result_one << std::endl;

    assert(measureRibbon("2x3x4") == 34);
    assert(measureRibbon("1x1x10") == 14);

    file.clear();
    file.seekg(0);

    int result_two = partTwo(file);
    std::cout << "Part 2: " << result_two << std::endl;

    return 0;
}