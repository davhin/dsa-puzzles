def main():
    with open('/Users/david/projects/adventofcode/2022/day1_input.txt', 'r') as f:
        calories = f.read()
        calories = calories[:-1].split("\n\n")
        calories = [[int(n) for n in cals_elf.split("\n")] for cals_elf in calories]
    max_cals = max([sum(cals) for cals in calories])
    top_three = sum(sorted([sum(cals) for cals in calories])[-3:])
    print(max_cals, top_three)


if __name__ == "__main__":    
    main()