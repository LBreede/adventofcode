package main

import "core:fmt"
import "core:os"
import "core:slice"
import "core:strconv"
import "core:strings"


part1 :: proc(name: string) -> int {
	data, ok := os.read_entire_file(name, context.allocator)
	it := string(data)
	lhs: [dynamic]int
	rhs: [dynamic]int
	for line in strings.split_lines_iterator(&it) {
		s := strings.split(line, " ")
		f :: proc(n: string) -> bool {return n != ""}
		ns := slice.filter(s, f)
		a := strconv.atoi(ns[0])
		b := strconv.atoi(ns[1])
		append(&lhs, a)
		append(&rhs, b)
	}
	slice.sort(lhs[:])
	slice.sort(rhs[:])
	dists := 0
	for num, i in lhs {
		dists += abs(num - rhs[i])
	}
	return dists
}

part2 :: proc(name: string) -> int {
	data, ok := os.read_entire_file(name, context.allocator)
	it := string(data)
	lhs: [dynamic]int
	rhs: [dynamic]int
	for line in strings.split_lines_iterator(&it) {
		s := strings.split(line, " ")
		f :: proc(n: string) -> bool {return n != ""}
		ns := slice.filter(s, f)
		a := strconv.atoi(ns[0])
		b := strconv.atoi(ns[1])
		append(&lhs, a)
		append(&rhs, b)
	}

	dists := 0
	for num in lhs {
		count := 0
		for num2 in rhs {
			if num == num2 {
				count += 1
			}
		}
		dists += num * count
	}
	return dists
}

main :: proc() {
	assert(part1("day01_example.txt") == 11)
	fmt.printfln("Part 1: %i", part1("day01_input.txt"))
	assert(part2("day01_example.txt") == 31)
	fmt.printfln("Part 2: %i", part2("day01_input.txt"))
}
