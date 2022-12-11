import re


class CrateStacker:
    def __init__(self, stacks_input: list, moves_input: list):
        self.stacks = stacks_input
        self.moves  = moves_input

    def apply_moves_to_stacks(self):
        for move in self.moves:
            for _ in range(move[0]):
                crate = self.stacks[move[1]-1].pop(0)
                self.stacks[move[2]-1].insert(0, crate)

    def apply_moves_to_stacks_9001(self):
        for move in self.moves:
            crates = self.stacks[move[1]-1][:move[0]]
            self.stacks[move[1]-1] = self.stacks[move[1]-1][move[0]:]
            self.stacks[move[2]-1] = crates + self.stacks[move[2]-1]


def parse_moves_input():
    with open('/Users/david/projects/adventofcode/2022/day5_input_moves.txt', 'r') as f:
        moves = f.read().split("\n")[:-1]
        moves = [re.findall(r'\b\d+\b', move) for move in moves]
        moves = [[int(l[0]), int(l[1]), int(l[2])] for l in moves]
    return moves

def get_stacks_input():
    """the formatting is super weird so I'm not wasting time on parsing"""
    stacks_input = [
        ['V','Q','W','M','B','N','Z','C'],
        ['B','C','W','R','Z','H'],
        ['J','R','Q','F'],
        ['T','M','N','F','H','W','S','Z'],
        ['P','Q','N','L','W','F','G'],
        ['W','P','L'],
        ['J','Q','C','G','R','D','B','V'],
        ['W','B','N','Q','Z'],
        ['J','T','G','C','F','L','H']
    ]
    return stacks_input

def test_CrateStacker():
    test_stacks_input = [
        ['N', 'Z'],
        ['D', 'C', 'M'],
        ['P']
    ]
    test_moves_input = [
        [1,2,1],
        [3,1,3],
        [2,2,1],
        [1,1,2],
    ]
    CS = CrateStacker(test_stacks_input, test_moves_input)
    CS.apply_moves_to_stacks()
    assert CS.stacks == [['C'], ['M'], ['Z', 'N', 'D', 'P']]


def test_CrateStacker_9001():
    test_stacks_input = [
        ['N', 'Z'],
        ['D', 'C', 'M'],
        ['P']
    ]
    test_moves_input = [
        [1,2,1],
        [3,1,3],
        [2,2,1],
        [1,1,2],
    ]
    CS = CrateStacker(test_stacks_input, test_moves_input)
    CS.apply_moves_to_stacks_9001()
    assert CS.stacks == [['M'], ['C'], ['D', 'N', 'Z', 'P']]



if __name__ == "__main__":
    ##task 1
    stacks = get_stacks_input()
    moves = parse_moves_input()
    CS = CrateStacker(stacks, moves)
    CS.apply_moves_to_stacks()
    stack_tops = [stack[0] for stack in CS.stacks]
    result = "".join([crate for crate in stack_tops])
    print(f"The tops of the final stacks sequence for CrateMover 9000 is {result}")

    ##task 2
    stacks = get_stacks_input()
    moves = parse_moves_input()
    CS = CrateStacker(stacks, moves)
    CS.apply_moves_to_stacks_9001()
    stack_tops = [stack[0] for stack in CS.stacks]
    result = "".join([crate for crate in stack_tops])
    print(f"The tops of the final stacks sequence for CrateMover 9001 is {result}")