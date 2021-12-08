def puzzle1(outputs: list) -> int:
    filtered = list(filter(lambda x: len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7, outputs))
    return len(filtered)


def puzzle2(patterns: list, outputs: list) -> int:
    result = []
    for i, pattern in enumerate(patterns):
        number_dict = deduct_signals(pattern)
        output_results = ""
        for output in outputs[i]:
            to_compare = set(list(output))
            for key, value in number_dict.items():
                if value == to_compare:
                    output_results += str(key)
        result.append(int(output_results))
    return sum(result)


def deduct_signals(pattern: list) -> dict:
    """
    lengths:
    2 -> (1)
    3 -> (7)
    4 -> (4)
    5 -> (2, 3, 5)
         -> 3 has similarity 3 with number 7 (rest 2)
         -> 5 has similarity 3 with number 4 (rest 2)
         -> 2 otherwise
    6 -> (0, 6, 9)
         -> 9 has similarity 4 with number 4
         -> 6 has similarity 5 with number 5
         -> 0 otherwise
    7 -> (8)
    :param pattern:
    :return:
    """
    numbers_dict = {x: [] for x in range(10)}
    for number in pattern:
        if len(number) == 2:
            numbers_dict[1] = set(list(number))
        elif len(number) == 3:
            numbers_dict[7] = set(list(number))
        elif len(number) == 4:
            numbers_dict[4] = set(list(number))
        elif len(number) == 7:
            numbers_dict[8] = set(list(number))
    for number in pattern:
        if len(number) == 5:
            split_set = set(list(number))
            if len((split_set & numbers_dict[7])) == 3:
                numbers_dict[3] = split_set
            elif len((split_set & numbers_dict[4])) == 3:
                numbers_dict[5] = split_set
            else:
                numbers_dict[2] = split_set
    for number in pattern:
        if len(number) == 6:
            split_set = set(list(number))
            if len((split_set & numbers_dict[4])) == 4:
                numbers_dict[9] = split_set
            elif len((split_set & numbers_dict[5])) == 5:
                numbers_dict[6] = split_set
            else:
                numbers_dict[0] = split_set
    return numbers_dict


def read_input(path: str) -> (list, list):
    with open(path, "r") as f:
        inputs = f.readlines()
        patterns = [list(map(lambda y: y.strip(), x.split("|")[0].split(" ")[:-1])) for x in inputs]
        outputs = [list(map(lambda y: y.strip(), x.split("|")[1].split(" ")[1:])) for x in inputs]

        return patterns, outputs


if __name__ == "__main__":
    all_patterns, all_outputs = read_input("./input.txt")
    flat_outputs = [x for line in all_patterns for x in line]
    answer1 = puzzle1(flat_outputs)
    answer2 = puzzle2(all_patterns, all_outputs)
    print(f"The answer to day 8 puzzle 1: {answer1}")
    print(f"The answer to day 8 puzzle 2: {answer2}")
