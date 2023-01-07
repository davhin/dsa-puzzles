from utils import get_input_file

def main():
    calories = get_input_file('day1_input.txt')
    calories = calories[:-1].split("\n\n")
    calories = [[int(n) for n in cals_elf.split("\n")] for cals_elf in calories]
    max_cals = max([sum(cals) for cals in calories])
    top_three = sum(sorted([sum(cals) for cals in calories])[-3:])
    print(max_cals, top_three)


def test_task1():
    assert 1 == 1






if __name__ == "__main__":    
    main()