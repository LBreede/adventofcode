def run(input_program, first_noun=None, first_verb=None, result_idx=0):

    if isinstance(input_program, list):
        output_program = input_program[:]
    elif isinstance(input_program, tuple):
        output_program = list(input_program)
    else:
        raise TypeError("Input program needs to be a sequence (list, tuple).")

    if first_noun is not None:
        output_program[1] = first_noun
    if first_verb is not None:
        output_program[2] = first_verb

    i = 0

    while True:
        opcode = output_program[i]

        if opcode in (1, 2):
            idx1 = output_program[i + 1]
            idx2 = output_program[i + 2]
            idx3 = output_program[i + 3]

            val1 = output_program[idx1]
            val2 = output_program[idx2]

            if opcode == 1:
                result = val1 + val2
            elif opcode == 2:
                result = val1 * val2

            output_program[idx3] = result

        elif opcode in (3, 4):
            pass

        elif opcode == 99:
            break

        else:
            raise ValueError("Bad opcode!")

        i += 4

    return output_program[result_idx]
