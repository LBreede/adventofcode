from intcode import IntcodeComputer


IC = IntcodeComputer()
IC.load_program("day02_input.txt")

IC.run(noun=12, verb=2)

print("Part 1:", IC.output())

noun, verb = IC.find_output(19690720)
print("Part 2:", 100 * noun + verb)
