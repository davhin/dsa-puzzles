def main(sections: list):
    ## task 1
    sections_clean = [pair.split(',') for pair in sections]
    sections_clean = [[pair[0].split('-'), pair[1].split('-')] for pair in sections_clean]
    overlap_all = [[int(pair[1][0]) - int(pair[0][0]), int(pair[1][1]) - int(pair[0][1])] for pair in sections_clean]
    overlap_all = [True if diff[0]*diff[1] <= 0 else False for diff in overlap_all]
    print(f"The number of elf pairs with entirely overlapping sections is: {sum(overlap_all)}")


    ## task 2
    overlap_any = [False if int(pair[1][0]) > int(pair[0][1]) or int(pair[0][0]) > int(pair[1][1]) else True for pair in sections_clean]
    print(f"The number of elf pairs with any overlapping sections is: {sum(overlap_any)}")

def test_main():
    sections_test = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
        ]
    main(sections_test)


if __name__ == "__main__":
    with open('/Users/david/projects/adventofcode/2022/day4_input.txt', 'r') as f:
        sections = f.read().split("\n")[:-1]
    main(sections)