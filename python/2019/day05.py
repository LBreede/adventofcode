from intcode import IntcodeComputer

"""

def read_opcode(opcode):
    x = str(p[0]).zfill(5)
    return list(map(int, [x[-2:], x[-3], x[-4], x[-5]]))


def find_val(param, mode, lst):
    return param if mode == 1 else p[param]

p = [1101, 100, -1, 4, 0]
full_opcode, a, b, val3 = p[0:4]

opcode, mode1, mode2, mode3 = read_opcode(full_opcode)
# print(opcode, mode1, mode2, mode3)
#

val1 = find_val(a, mode1, p)
val2 = find_val(b, mode2, p)

if opcode == 1:
    p[val3] = val1 + val2
if opcode == 2:
    p[val3] = val1 * val2
print(p)
"""

# print(IC.program)
IC = IntcodeComputer("day05_input.txt")
# IC = IntcodeComputer("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
# print(IC.program, "\n")

outputs = IC.run(input_=5)
if len(outputs) > 0:
    print(outputs[-1], "<=> Outputs:", outputs)
else:
    print("Outputs:", outputs)
