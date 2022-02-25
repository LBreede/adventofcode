# --- Day 1: The Tyranny of the Rocket Equation ---

import math


def getModuleMassList(puzzle_input):
    mass_list = open(puzzle_input, "r").read().split("\n")
    mass_list = list(map(int, mass_list))
    return mass_list


def calcModuleFuelList(mass_list):
    fuel_list = []
    for m in mass_list:
        fuel_list.append(math.floor(m / 3) - 2)
    return fuel_list


def calcRecursiveModuelFuelList(mass_list):
    fuel_list = []
    for m in mass_list:
        final_fuel = 0
        fuel = m
        while fuel > 0:
            final_fuel += fuel
            fuel = math.floor(fuel / 3) - 2
        fuel_list.append(final_fuel - m)
    return fuel_list


def accumFuel(fuel_list):
    return sum(fuel_list)


if __name__ == "__main__":
    puzzle_input = "input.txt"
    mass_list = getModuleMassList(puzzle_input)
    # mass_list = [1969]

    fuel_list = calcModuleFuelList(mass_list)
    accum_fuel = accumFuel(fuel_list)
    print("The sum of the fuel requirements: " + str(accum_fuel))

    recursive_fuel_list = calcRecursiveModuelFuelList(mass_list)
    recursive_accum_fuel = accumFuel(recursive_fuel_list)
    print("The sum of the fuel requirements: " + str(recursive_accum_fuel))
