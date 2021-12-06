from collections import Counter

import numpy as np
from tqdm import tqdm


def count_fishes(starting_fishes, nr_days):
    fish_dict = Counter(starting_fishes)
    for _ in tqdm(range(nr_days)):
        new_fish_dict = {}
        for key, value in fish_dict.items():
            if key == 0:
                new_fish_dict[8] = value
                new_fish_dict[6] = new_fish_dict.get(6, 0) + value
            else:
                shift_key = key - 1
                if shift_key == 6:
                    new_fish_dict[shift_key] = new_fish_dict.get(shift_key, 0) + value
                else:
                    new_fish_dict[shift_key] = value
        fish_dict = new_fish_dict.copy()
    return sum(fish_dict.values())


def read_input(path: str):
    with open(path, "r") as f:
        fishes = list(map(lambda x: int(x), f.read().split(",")))
    return fishes


if __name__ == "__main__":
    instruction_input = read_input("./input.txt")
    output1 = count_fishes(np.array(instruction_input), 80)
    output2 = count_fishes(np.array(instruction_input), 256)
    print(f"The answer to day 6 puzzle 1: {output1}")
    print(f"The answer to day 6 puzzle 2: {output2}")
