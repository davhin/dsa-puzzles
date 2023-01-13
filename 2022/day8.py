from utils import get_input_file
import numpy as np

def parse_input():
    input_file = get_input_file(2022, 'day8_input.txt')
    trees = input_file.split("\n")[:-1]
    trees = [list(treeline) for treeline in trees]
    trees = [[int(t) for t in treeline] for treeline in trees]
    return trees


def transpose_grid(trees: list):
    transposed = [[] for _ in trees[0]]
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            transposed[j].append(trees[i][j])
    return transposed


def reverse_grid(trees: list):
    return [list(reversed(treeline)) for treeline in trees]


def hidden_trees_from_side(trees: list):
    hidden_trees = []
    for line in trees:
        hidden_trees_in_line = []
        tree_max = 0
        for tree in line:
            if tree <= tree_max:
                hidden_trees_in_line.append(1)
            else:
                hidden_trees_in_line.append(0)
                tree_max = tree
        hidden_trees.append(hidden_trees_in_line)
    return hidden_trees

def find_hidden_trees(trees: list):
    from_left = hidden_trees_from_side(trees)
    from_right = reverse_grid(hidden_trees_from_side(reverse_grid(trees)))
    from_top = transpose_grid(hidden_trees_from_side(transpose_grid(trees)))
    from_bottom = reverse_grid(transpose_grid(hidden_trees_from_side(transpose_grid(reverse_grid(trees)))))
    print(from_left)
    print(from_right)
    #print(from_top)
    #print(from_bottom)


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