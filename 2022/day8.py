from utils import get_input_file
import numpy as np

def parse_input():
    input_file = get_input_file(2022, 'day8_input.txt')
    trees = input_file.split("\n")[:-1]
    trees = [list(treeline) for treeline in trees]
    trees = [[int(t) for t in treeline] for treeline in trees]
    return trees


def find_hidden_trees(trees: list):
    from_left = trees
    from_right = [list(reversed(treeline)) for treeline in from_left]
    from_top = [[] for _ in trees[0]]
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            from_top[j].append(trees[i][j])
    from_bottom = [list(reversed(treeline)) for treeline in from_top]


def test_day8():
    trees = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]
    find_hidden_trees(trees)


if __name__ == "__main__":
    test_day8()
    #trees = get_input_file("day8_input.txt")
    #trees = [list(treeline) for treeline in trees]
    #trees = [[int(t) for t in treeline] for treeline in trees]
    #n_hidden_trees = find_hidden_trees(trees)
    #print(f"The number of hidden trees for tree houses is {n_hidden_trees}.")
    ##task 2