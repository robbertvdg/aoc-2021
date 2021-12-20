import json
from copy import deepcopy
from math import floor, ceil
from typing import List, Any

from tqdm import tqdm


def calculate_magnitude(snailfish_number: List[Any]):
    magnitude = 0
    if isinstance(snailfish_number[0], list):
        magnitude += 3 * calculate_magnitude(snailfish_number[0])
    else:
        magnitude += 3 * snailfish_number[0]
    if isinstance(snailfish_number[1], list):
        magnitude += 2 * calculate_magnitude(snailfish_number[1])
    else:
        magnitude += 2 * snailfish_number[1]
    return magnitude


def get_snailfish_by_index(snailfish_number: List[Any], index: List[int]) -> Any:
    if not index:
        return snailfish_number
    elif len(index) == 1:
        return snailfish_number[index[0]]
    elif len(index) == 2:
        return snailfish_number[index[0]][index[1]]
    elif len(index) == 3:
        return snailfish_number[index[0]][index[1]][index[2]]
    else:
        return snailfish_number[index[0]][index[1]][index[2]][index[3]]


def list_depth(snailfish_number: List[Any]) -> int:
    return isinstance(snailfish_number, list) and max(map(list_depth, snailfish_number)) + 1


def get_max_list_number(snailfish_number: List[Any]) -> int:
    if isinstance(snailfish_number, int):
        return snailfish_number
    elif isinstance(snailfish_number[0], list) or isinstance(snailfish_number[1], list):
        return max(map(get_max_list_number, snailfish_number))
    return max(snailfish_number)


def reduce(snailfish_number: List[Any]):
    while True:
        if will_explode(snailfish_number):
            explode(snailfish_number)
        elif will_split(snailfish_number):
            split(snailfish_number)
        else:
            break


def will_explode(snailfish_number: List[Any]) -> bool:
    return list_depth(snailfish_number) > 4


def will_split(snailfish_number: List[Any]) -> bool:
    max_number = get_max_list_number(snailfish_number)
    return max_number > 9


def split(snailfish_number: List[Any]):
    current = snailfish_number
    while True:
        if isinstance(current[0], list) and will_split(current[0]):
            current = current[0]
        elif isinstance(current[0], int) and will_split(current[0]):
            current[0] = [int(floor(current[0] / 2)), int(ceil(current[0] / 2))]
            break
        elif isinstance(current[1], list) and will_split(current[1]):
            current = current[1]
        elif isinstance(current[1], int) and will_split(current[1]):
            current[1] = [int(floor(current[1] / 2)), int(ceil(current[1] / 2))]
            break
        else:
            print("something gone wrong with split, returning")
            return


def explode(snailfish_number: List[Any]):
    depth = list_depth(snailfish_number)
    current_el = snailfish_number
    index = []
    while depth != 0:
        depth -= 1
        for i in range(len(current_el)):
            if list_depth(current_el[i]) > depth:
                current_el = current_el[i]
                index.append(i)
                break
    to_remove = get_snailfish_by_index(snailfish_number, index[:3]).pop(index[3])
    if index[3] == 0:
        snailfish_number[index[0]][index[1]][index[2]] = [0, snailfish_number[index[0]][index[1]][index[2]][0]]
    else:
        snailfish_number[index[0]][index[1]][index[2]] = [snailfish_number[index[0]][index[1]][index[2]][0], 0]

    add_to_left_or_right(snailfish_number, to_remove[0], index, 0)
    add_to_left_or_right(snailfish_number, to_remove[1], index, 1)


def index_exists(snailfish_number: List[Any], index: List[int]) -> bool:
    current = snailfish_number
    for i in index:
        if i < len(current):
            current = current[i]
        else:
            return False
    return True


def add_to_left_or_right(snailfish_number: List[Any], number: int, index: List[int], orient=0):
    other_orient = 0 if orient == 1 else 1
    going_in = [x for x in range(len(index)) if index[x] == other_orient]
    if going_in:
        going_in = going_in[-1]
        tmp = get_snailfish_by_index(snailfish_number, index[:going_in])
        if isinstance(tmp[orient], list):
            insert_in_rec_list(tmp[orient], number, other_orient)
        elif isinstance(tmp[orient], int):
            tmp[orient] += number


def insert_in_rec_list(snailfish_number: List[Any], number: int, index: int):
    if isinstance(snailfish_number[index], list):
        insert_in_rec_list(snailfish_number[index], number, index)
    else:
        snailfish_number[index] += number

def puzzle1(numbers: List[Any]) -> int:
    current = numbers[0]
    for i in tqdm(range(1, len(numbers))):
        current = [current, (numbers[i])]
        reduce(current)
    return calculate_magnitude(current)


def puzzle2(numbers: List[Any]):
    highest_magnitude = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            to_eval_1 = [deepcopy(numbers[i]), deepcopy(numbers[j])]
            to_eval_2 = [deepcopy(numbers[j]), deepcopy(numbers[i])]
            reduce(to_eval_1)
            reduce(to_eval_2)
            magn_1 = calculate_magnitude(to_eval_1)
            magn_2 = calculate_magnitude(to_eval_2)
            if magn_1 > highest_magnitude:
                highest_magnitude = magn_1
            if magn_2 > highest_magnitude:
                highest_magnitude = magn_2
    return highest_magnitude


def read_input(path: str) -> (str, dict):
    with open(path, "r") as f:
        lines = f.readlines()
        return [json.loads(x.strip()) for x in lines]


if __name__ == "__main__":
    snailfish_numbers = read_input("./input.txt")
    answer1 = puzzle1(snailfish_numbers)
    snailfish_numbers = read_input("./input.txt")
    answer2 = puzzle2(snailfish_numbers)
    print(f"The answer to day 18 puzzle 1: {answer1}")
    print(f"The answer to day 18 puzzle 2: {answer2}")
