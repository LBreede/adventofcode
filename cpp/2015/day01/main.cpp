#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>

int partOne(std::istream& file) {
    int x = 0;
    char ch;
    while (file.get(ch)) {
        if (ch == '(') {
            x++;
        } else if (ch == ')') {
            x--;
        }
    }
    return x;
}

int partOne(const std::string& input) {
    std::istringstream stream(input);
    return partOne(stream);
}

int partTwo(std::istream& file) {
    int x = 0;
    int i = 0;
    char ch;
    while (file.get(ch)) {
        i++;
        if (ch == '(') {
            x++;
        } else if (ch == ')') {
            x--;
        }
        if (x < 0) {
            return i;
        }
    }
    return -1;
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

    /*
    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.
    */

    assert(partOne("(())") == 0);
    assert(partOne("()()") == 0);
    assert(partOne("(((") == 3);
    assert(partOne("(()(()(") == 3);
    assert(partOne("))(((((") == 3);
    assert(partOne("())") == -1);
    assert(partOne("))(") == -1);
    assert(partOne(")))") == -3);
    assert(partOne(")())())") == -3);

    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << argv[1] << std::endl;
        return 1;
    }

    int result_one = partOne(file);
    std::cout << "Part 1: " << result_one << std::endl;

    /*
    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.
    */

    assert(partTwo(")") == 1);
    assert(partTwo("()())") == 5);

    file.clear();
    file.seekg(0);

    int result_two = partTwo(file);
    std::cout << "Part 2: " << result_two << std::endl;

    return 0;
}