from typing import List
import re
import time


class IntcodeComputer:
    def __init__(self, program=None, do_log=False):
        self._do_log = do_log

        if program is not None:
            self.load_program(program)
        else:
            self.program = []

    def load_program(self, program):
        if isinstance(program, list):
            self._load_program_from_list(program)
        elif isinstance(program, str):
            if re.search(r"^-*\d+(,\s*-*\d+)+$", program):
                self._load_program_from_string(program)
            elif re.search(r"^.+\.txt$", program):
                self._load_program_from_file(program)
            else:
                raise Exception("unsupported program")
        else:
            raise TypeError(f"unsupported type for program: '{type(program).__name__}'")

    def _load_program_from_list(self, program: List[int]) -> None:
        self.log("loading program from list")
        self._orig_program = program
        self.log("program loaded")
        self.reset()

    def _load_program_from_string(self, string: str) -> None:
        self.log("loading program from string")
        self._load_program_from_list([int(x) for x in string.split(",")])

    def _load_program_from_file(self, file: str) -> None:
        self.log("loading program from file")
        with open(file) as fp:
            self._load_program_from_string(fp.read())

    def reset(self) -> None:
        self.log("resetting memory")
        self.program = self._orig_program.copy()

    def set_noun(self, noun: int) -> None:
        self.log(f"setting noun to {noun}")
        self.program[1] = noun

    def set_verb(self, verb: int) -> None:
        self.log(f"setting verb to {verb}")
        self.program[2] = verb

    def _expand_opcode(self, opcode):
        o = str(opcode).zfill(5)
        return list(map(int, [o[-2:], o[-3], o[-4], o[-5]]))

    def run(self, noun: int = None, verb: int = None, input_=None) -> None:
        self.log("running program")

        self.reset()

        if noun is not None:
            self.set_noun(noun)

        if verb is not None:
            self.set_verb(verb)

        i = 0

        outputs = []

        while True:

            opcode = self.program[i]
            opcode, mode1, mode2, mode3 = self._expand_opcode(self.program[i])
            modes = [mode1, mode2, mode3]

            if opcode == 99:
                break

            if opcode in (1, 2, 7, 8):

                params = self.program[i + 1 : i + 4]
                param1, param2, param3 = params
                vals = self._find_vals(params, modes, self.program)
                val1, val2, val3 = vals

                match opcode:
                    case 1:
                        self.program[param3] = val1 + val2
                    case 2:
                        self.program[param3] = val1 * val2
                    case 7:
                        self.program[param3] = 1 if val1 < val2 else 0
                    case 8:
                        self.program[param3] = 1 if val1 == val2 else 0
                i += 4

            elif opcode in (3, 4):

                param1 = self.program[i + 1]
                val1 = self._find_val(param1, mode1, self.program)

                match opcode:
                    case 3:
                        self.program[param1] = input_
                    case 4:
                        outputs.append(val1)
                i += 2

            elif opcode in (5, 6):

                params = self.program[i + 1 : i + 3]
                param1, param2 = params
                vals = self._find_vals(params, modes, self.program)
                val1, val2 = vals

                match opcode:
                    case 5:
                        i = val2 if val1 != 0 else i + 3
                    case 6:
                        i = val2 if val1 == 0 else i + 3

            else:
                raise OpcodeError(f"unsupported opcode: '{opcode}'")

            print(self.program, i)

        if sum(outputs[:-1]) != 0:
            print("Something might have gone wrong.")

        return outputs

    def _find_vals(self, params, modes, lst):
        vals = []
        for i, param in enumerate(params):
            vals.append(self._find_val(param, modes[i], lst))
        return vals

    def _find_val(self, param, mode, lst):
        return param if mode == 1 else lst[param]

    def find_output(
        self,
        output: int,
        noun_start: int = 0,
        noun_stop: int = 99,
        verb_start: int = 0,
        verb_stop: int = 99,
    ):

        for i in range(noun_start, noun_stop + 1):
            for j in range(verb_start, verb_stop + 1):

                self.run(noun=i, verb=j)

                if self.output() == output:
                    return i, j

    def output(self) -> int:
        return self.program[0]

    def do_log(self, do_log):
        self._do_log = do_log

    def log(self, message):
        if self._do_log:
            print("[INCODE COMPUTER LOG]:", message)


class OpcodeError(Exception):
    pass
