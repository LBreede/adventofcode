# --- Day 10: Cathode-Ray Tube ---


class CathodeRayTube:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.signal = 0
        self.screen = []

    def noop(self):
        self.screen.append("") if self.cycle % 40 == 0 else None
        self.screen[-1] += "██" if self.x - 1 <= self.cycle % 40 <= self.x + 1 else "  "
        self.cycle += 1
        self.signal += self.cycle * self.x if (self.cycle - 20) % 40 == 0 else 0

    def addx(self, val):
        for _ in range(2):
            self.noop()
        self.x += val

    def execute(self, file):
        with open(file) as fp:
            for line in fp:
                cmd = line.rstrip().split()
                if cmd[0] == "noop":
                    self.noop()
                elif cmd[0] == "addx":
                    self.addx(int(cmd[1]))

    def show(self):
        return "\n".join(self.screen)


def main():
    crt = CathodeRayTube()
    crt.execute("input.txt")
    print("Part 1:", crt.signal, "\nPart 2:")
    print(crt.show())


if __name__ == "__main__":
    main()
