import numpy as np

def parse_input():
    with open('/Users/david/projects/adventofcode/2022/day8_input.txt', 'r') as f:
        trees = f.read().split("\n")[:-1]
        trees = [list(treeline) for treeline in trees]
        trees = [[int(t) for t in treeline] for treeline in trees]
    return trees


def find_hidden_trees(trees: list):
    trees = np.array(trees)
    from_left = trees
    from_right = [list(reversed(treeline)) for treeline in trees]
    from_top = []


def test_find_hidden_trees():
    trees = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]
    assert find_hidden_trees(trees) == 21


if __name__ == "__main__":
    ##setup
    test_find_hidden_trees()
    trees = parse_input()
    ##task 1
    hidden_trees = find_hidden_trees(trees)
    print(f"The number of hidden trees for tree houses is {hidden_trees}.")
    ##task 2