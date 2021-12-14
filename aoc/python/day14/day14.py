from typing import List, Tuple


def match_instruction_counts(polymer: str, instructions: dict, steps: int) -> dict:
    duo_counts_dict = {}
    char_counts_dict = {}
    for i in range(len(polymer) - 1):
        char_counts_dict[polymer[i]] = char_counts_dict.get(polymer[i], 0) + 1
        char_duo = polymer[i:i + 2]
        if char_duo in duo_counts_dict:
            duo_counts_dict[char_duo] += 1
        else:
            duo_counts_dict[char_duo] = 1
    char_counts_dict[polymer[-1]] = char_counts_dict.get(polymer[-1], 0) + 1
    for i in range(steps):
        new_counts_dict = {}
        for key in duo_counts_dict.keys():
            if key in instructions.keys():
                char_duo_1 = key[0] + instructions[key]
                char_duo_2 = instructions[key] + key[1]
                new_counts_dict[char_duo_1] = new_counts_dict.get(char_duo_1, 0) + duo_counts_dict[key]
                new_counts_dict[char_duo_2] = new_counts_dict.get(char_duo_2, 0) + duo_counts_dict[key]
                char_counts_dict[instructions[key]] = char_counts_dict.get(instructions[key], 0) + duo_counts_dict[
                    key]
            else:
                new_counts_dict[key] = new_counts_dict.get(key, 0) + duo_counts_dict[key]
        duo_counts_dict = new_counts_dict.copy()
    return char_counts_dict


def puzzle(polymer: str, instructions: dict, steps=10) -> List[Tuple[str, int]]:
    char_counts_dict = match_instruction_counts(polymer, instructions, steps)
    return sorted(char_counts_dict.items(), key=lambda item: item[1], reverse=True)


def read_input(path: str) -> (str, dict):
    with open(path, "r") as f:
        inputs = f.readlines()
        start_list = inputs[0].strip()
        instructions = {}
        for line in inputs[2:]:
            splitted = line.split(' -> ')
            instructions[splitted[0].strip()] = splitted[1].strip()
        return start_list, instructions


if __name__ == "__main__":
    start_list, instructions_dict = read_input("./input.txt")
    answer1 = puzzle(start_list, instructions_dict, 10)
    answer2 = puzzle(start_list, instructions_dict, 40)
    print(f"The answer to day 14 puzzle 1: {answer1[0][1] - answer1[-1][1]}")
    print(f"The answer to day 14 puzzle 2: {answer2[0][1] - answer2[-1][1]}")
