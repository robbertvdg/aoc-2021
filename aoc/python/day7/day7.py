import numpy as np


def generate_sums(max_int):
    return [sum(range(i + 1)) for i in range(max_int + 1)]


def puzzle1(crab_positions: np.ndarray):
    min_fuel = 0
    for i in range(crab_positions.max()):
        fuel_sum = np.absolute(crab_positions - i).sum()
        if fuel_sum < min_fuel or min_fuel == 0:
            min_fuel = fuel_sum
    return min_fuel


def puzzle2(crab_positions: np.ndarray):
    min_fuel = 0
    max_crab = crab_positions.max()
    sums = np.array(generate_sums(max_crab))
    for i in range(max_crab):
        shifted_crabs = np.absolute(crab_positions - i)
        fuel_sum = sums[shifted_crabs].sum()
        if fuel_sum < min_fuel or min_fuel == 0:
            min_fuel = fuel_sum
    return min_fuel


def read_input(path: str):
    with open(path, "r") as f:
        crabs = list(map(lambda x: int(x), f.read().split(",")))
    return crabs


if __name__ == "__main__":
    instruction_input = read_input("./input.txt")
    output1 = puzzle1(np.array(instruction_input))
    output2 = puzzle2(np.array(instruction_input))
    print(f"The answer to day 7 puzzle 1: {output1}")
    print(f"The answer to day 7 puzzle 2: {output2}")
