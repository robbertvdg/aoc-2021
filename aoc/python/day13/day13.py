from typing import List

import numpy as np


def do_fold(paper: np.ndarray, line: int, left=True):
    if left:
        to_fold = paper[line + 1:, :]
        flipped = np.flipud(to_fold)
        cut_paper = paper[:line, :]
        cut_paper += flipped
        return cut_paper
    else:
        to_fold = paper[:, line + 1:]
        flipped = np.fliplr(to_fold)
        cut_paper = paper[:, :line]
        cut_paper += flipped
        return cut_paper


def puzzle1(paper: np.ndarray, folds: List[List[str]]) -> int:
    fold = folds[0]
    if fold[0] == 'x':
        paper = do_fold(paper, int(fold[1]), True)
    else:
        paper = do_fold(paper, int(fold[1]), False)
    return np.count_nonzero(paper)


def puzzle2(paper: np.ndarray, folds: List[List[str]]):
    for fold in folds:
        if fold[0] == 'x':
            paper = do_fold(paper, int(fold[1]), True)
        else:
            paper = do_fold(paper, int(fold[1]), False)
    paper = np.flipud(np.rot90(np.clip(paper, 0, 1), axes=(0, 1)))
    for i in range(len(paper)):
        x = ''.join([str(int(y)) for y in list(paper[i])])
        print(x.replace('0', '.').replace('1', '#'))


def create_paper(dots: List[List[int]]) -> np.ndarray:
    paper_size_x = max([x[0] for x in dots]) + 1
    paper_size_y = max([x[1] for x in dots]) + 1
    paper = np.zeros((paper_size_x, paper_size_y))
    for dot in dots:
        paper[dot[0], dot[1]] = 1
    return paper


def read_input(path: str) -> (List[List[str]], List[dict]):
    with open(path, "r") as f:
        inputs = f.readlines()
        folds = []
        paper_dots = []
        for line in inputs:
            if ',' in line:
                paper_dots.append([int(x.strip()) for x in line.split(',')])
            elif '=' in line:
                folds.append(line.split('fold along ')[1].strip().split('='))
        return paper_dots, folds


if __name__ == "__main__":
    dots_list, fold_instructions = read_input("./input.txt")
    init_paper = create_paper(dots_list)

    answer1 = puzzle1(init_paper, fold_instructions)
    print(f"The answer to day 13 puzzle 1: {answer1}")
    init_paper = create_paper(dots_list)
    puzzle2(init_paper, fold_instructions)
