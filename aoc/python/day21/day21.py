from collections import Counter
from itertools import cycle, combinations


def puzzle2(pos1: int, pos2: int) -> int:
    all_outcomes = dict(Counter([sum(x) for x in set(combinations([1, 2, 3, 1, 2, 3, 1, 2, 3], 3))]))
    all_pos_scores = {f"{pos1},0,{pos2},0": 1}
    finished = {}
    player = 0
    while True:
        new_scenario = {}
        for scenario, count in all_pos_scores.items():
            scenario = [int(x) for x in scenario.split(",")]
            for outcome, count_2 in all_outcomes.items():
                scenario_copy = scenario.copy()
                pos = (scenario_copy[player] + outcome) % 10
                pos = 10 if pos == 0 else pos
                scenario_copy[player] = pos
                scenario_copy[player + 1] += pos
                if scenario_copy[player + 1] >= 21:
                    scenario_copy = ",".join([str(x) for x in scenario_copy])
                    finished[scenario_copy] = finished.get(scenario_copy, 0) + count * count_2
                else:
                    scenario_copy = ",".join([str(x) for x in scenario_copy])
                    new_scenario[scenario_copy] = new_scenario.get(scenario_copy, 0) + count * count_2
        player = 0 if player == 2 else 2
        if not new_scenario:
            break
        else:
            all_pos_scores = new_scenario.copy()
    player1_won = 0
    player2_won = 0
    for key, value in finished.items():
        scenario = [int(x) for x in key.split(",")]
        if scenario[1] >= 21:
            player1_won += value
        else:
            player2_won += value
    return player1_won if player1_won > player2_won else player2_won


def puzzle1(pos1: int, pos2: int) -> int:
    dice = cycle(range(1, 101))
    done = False
    turn = 0
    player = 1
    pos_scores = {1: {"pos": pos1, "score": 0}, 2: {"pos": pos2, "score": 0}}
    while not done:
        pos = (pos_scores[player]["pos"] + next(dice) + next(dice) + next(dice)) % 10
        pos = 10 if pos == 0 else pos
        pos_scores[player]["pos"] = pos
        pos_scores[player]["score"] += pos
        if pos_scores[player]["score"] >= 1000:
            done = True
        player = 1 if player == 2 else 2
        turn += 1
    return (turn * 3) * pos_scores[player]["score"]


if __name__ == "__main__":
    player1_start = 3
    player2_start = 4
    answer1 = puzzle1(player1_start, player2_start)
    answer2 = puzzle2(player1_start, player2_start)
    print(f"The answer to day 21 puzzle 1: {answer1}")
    print(f"The answer to day 21 puzzle 2: {answer2}")
