from utils import get_input_file
from collections import defaultdict


def get_sizes(lines: list):
    # We can safely strip ls commands from the input
    lines = [entry for entry in lines if not entry == "$ ls"]
    filepath = []
    sizes = defaultdict(int)

    for entry in lines:
        if entry.startswith("$ cd"):
            match entry:
                case "$ cd /":
                    filepath.clear()
                    filepath.append("/")
                case "$ cd ..":
                    filepath.pop()
                case _:
                    dir = entry.split()[-1]
                    filepath.append(dir)
        else:
            # We have a listing of a file. Add the size to the current dir and all of its parent dirs.
            filesize = entry.split()[0]
            if filesize.isdigit():
                filesize = int(filesize)
                # Iterate through every dir in the full path to the file
                for i in range(len(filepath)):
                    dir = '/'.join(filepath[:i+1]).replace("//", "/")
                    sizes[dir] += filesize
    return sizes


def test_day7():
    test_lines = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k"
        ]
    test_sizes = get_sizes(test_lines)
    test_dirs_below_threshold = {directory: size for (directory, size) in test_sizes.items() if size <= 100000}
    assert sum(test_dirs_below_threshold.values()) == 95437

if __name__ == '__main__':
    test_day7()
    lines = get_input_file("day7_input.txt")
    sizes = get_sizes(lines)

    # Part one
    dirs_below_threshold = {directory: size for (directory, size) in sizes.items() if size <= 100000}
    print(sum(dirs_below_threshold.values()))

    # Part two
    total_disk_space = 70000000
    needed_disk_space = 30000000
    space_to_free = sizes["/"] + needed_disk_space - total_disk_space
    dirs_above_threshold = {directory: size for (directory, size) in sizes.items() if size >= space_to_free}
    print(min(dirs_above_threshold.values()))