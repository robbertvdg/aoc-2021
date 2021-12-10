from typing import List


def get_closing_character_scores(characters: List[str]) -> int:
    score_dict = {'(': 1,
                  '[': 2,
                  '{': 3,
                  '<': 4}
    total_score = 0
    characters.reverse()
    for char in characters:
        total_score *= 5
        total_score += score_dict.get(char)
    return total_score


def get_character_score(character: str) -> int:
    score_dict = {')': 3,
                  ']': 57,
                  '}': 1197,
                  '>': 25137}

    return score_dict.get(character)


def is_opening_char(character: str) -> bool:
    return get_character_score(character) is None


def matches_closing_char(opening: str, closing: str) -> bool:
    return (opening == '(' and closing == ')') or \
           (opening == '[' and closing == ']') or \
           (opening == '{' and closing == '}') or \
           (opening == '<' and closing == '>')


def puzzle1(inputs: List[str]) -> int:
    total_score = 0
    for input_str in inputs:
        opening_chars = []
        for char in input_str:
            if is_opening_char(char):
                opening_chars.append(char)
            else:
                if matches_closing_char(opening_chars[-1], char):
                    opening_chars.pop()
                else:
                    total_score += get_character_score(char)
                    break
    return total_score


def puzzle2(inputs: List[str]) -> int:
    total_scores = []
    for input_str in inputs:
        faulty = False
        opening_chars = []
        for char in input_str:
            if is_opening_char(char):
                opening_chars.append(char)
            else:
                if matches_closing_char(opening_chars[-1], char):
                    opening_chars.pop()
                else:
                    faulty = True
                    break
        if not faulty:
            total_scores.append(get_closing_character_scores(opening_chars))
    total_scores = list(sorted(total_scores))
    return total_scores[round((len(total_scores) - 1) / 2)]


def read_input(path: str) -> List[str]:
    with open(path, "r") as f:
        inputs = f.readlines()
        return [x.strip() for x in inputs]


if __name__ == "__main__":
    navigation_system = read_input("./input.txt")
    answer1 = puzzle1(navigation_system)
    answer2 = puzzle2(navigation_system)
    print(f"The answer to day 10 puzzle 1: {answer1}")
    print(f"The answer to day 10 puzzle 2: {answer2}")
