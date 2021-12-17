from typing import List, Tuple


def hits_target(current_pos: Tuple[int, int], velocity: Tuple[int, int], target: List[Tuple[int, int]]) -> bool:
    while True:
        if target[0][0] <= current_pos[0] <= target[0][1] and target[1][0] <= current_pos[1] <= target[1][1]:
            return True
        elif (current_pos[0] < target[0][0] and velocity[0] == 0) or \
                (current_pos[0] > target[0][1]) or \
                (current_pos[1] < target[1][0]):
            return False
        else:
            current_pos = (current_pos[0] + velocity[0], current_pos[1] + velocity[1])
            velocity = (max(0, velocity[0] - 1), velocity[1] - 1)


def puzzle1(target: List[Tuple[int, int]]) -> int:
    highest = 0
    for i in range(1000):
        if sum(range(i + 1)) < target[0][0]:
            continue
        if sum(range(i + 1)) > target[0][1]:
            break
        for j in range(500):
            if hits_target((0, 0), (i, j), target):
                height = sum(range(j + 1))
                highest = height if height > highest else highest
    return highest

def puzzle2(target: List[Tuple[int, int]]) -> int:
    targets_hit = 0
    for i in range(target[0][1] + 1):
        if sum(range(i + 1)) < target[0][0]:
            continue
        for j in range(target[1][0], 500):
            if hits_target((0, 0), (i, j), target):
                targets_hit += 1
    return targets_hit


if __name__ == "__main__":
    target_input = [(195, 238), (-93, -67)]
    answer1 = puzzle1(target_input)
    answer2 = puzzle2(target_input)
    print(f"The answer to day 17 puzzle 1: {answer1}")
    print(f"The answer to day 17 puzzle 2: {answer2}")
