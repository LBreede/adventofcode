# --- Day 9: Encoding Error ---

from aoc_helper import load_input
from tqdm import trange


def part_1(nums, preample):
    for i in trange(preample, len(nums), desc="Calculating Part 1"):
        num = nums[i]
        lst = nums[i - preample : i]
        terms = set()
        for j in lst:
            for k in lst:
                if j != k and j + k == num:
                    terms.add(j)
                    terms.add(k)
                    break
        if len(terms) == 0:
            return num
            break


def part_2(nums, sum_):

    for i in trange(len(nums), desc="Calculating Part 2"):
        for j in range(len(nums)):
            terms = nums[i:j]
            if len(terms) >= 2 and sum(terms) == sum_:
                return min(terms) + max(terms)


def main():
    numbers = list(map(int, load_input("day09_input.txt")))
    print()
    result_1 = part_1(numbers, 25)
    print(f"\nPart 1: {result_1}\n")
    result_2 = part_2(numbers, result_1)
    print(f"\nPart 2: {result_2}")


if __name__ == "__main__":
    main()
