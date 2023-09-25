# --- Day 7: Recursive Circus ---

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Program:
    name: str
    weight: int
    children: list[Program]

    def get_weight(self) -> int:
        children_weight = sum(child.get_weight() for child in self.children)
        return self.weight + children_weight

    def is_balanced(self) -> bool:
        if not self.children:
            return True
        weights = [child.get_weight() for child in self.children]
        return len(set(weights)) == 1


def get_tower(filename: str) -> Program:
    parsed: list[tuple[str, int, list[str]]] = []
    programs: dict[str, Program] = {}
    with open(filename, encoding="utf-8") as fp:
        for line in fp.read().splitlines():
            parts = line.split(" -> ")
            name = parts[0].split()[0]
            weight = int(parts[0].split()[1][1:-1])
            children = parts[1].split(", ") if len(parts) > 1 else []
            parsed.append((name, weight, children))
    while parsed:
        for name, weight, children in parsed.copy():
            if not children:
                programs[name] = Program(name, weight, [])
                parsed.remove((name, weight, children))
            else:
                if all(child in programs for child in children):
                    programs[name] = Program(
                        name, weight, [programs[child] for child in children]
                    )
                    for child in children:
                        del programs[child]
                    parsed.remove((name, weight, children))

    return programs[list(programs)[0]]


def part_one(tower: Program) -> str:
    return tower.name


def part_two(tower: Program) -> int:
    unbalanced_program = tower
    while True:
        for child in unbalanced_program.children:
            if not child.is_balanced():
                unbalanced_program = child
                break
        else:
            break

    child_weights = [child.get_weight() for child in unbalanced_program.children]
    heavy_child: Optional[Program] = None
    for child in unbalanced_program.children:
        if child_weights.count(child.get_weight()) == 1:
            heavy_child = child
            break
    assert heavy_child is not None

    unique_weights = sorted(list(set(child_weights)))
    difference = unique_weights[1] - unique_weights[0]
    return heavy_child.weight - difference


def main():
    example_tower = get_tower("day07_example.txt")
    assert part_one(example_tower) == "tknk"

    tower = get_tower("day07_input.txt")
    bottom_program = part_one(tower)
    print(f"Part 1: {bottom_program!r}")

    assert part_two(example_tower) == 60

    weight = part_two(tower)
    print(f"Part 2: {weight}")


if __name__ == "__main__":
    main()
