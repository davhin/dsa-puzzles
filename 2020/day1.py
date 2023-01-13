from utils import get_input_file


def sum_two_mul(expenses: list):
    for exp_a in expenses:
        for exp_b in expenses:
            if (exp_a + exp_b) == 2020:
                return exp_a * exp_b


def sum_three_mul(expenses: list):
    for exp_a in expenses:
        for exp_b in expenses:
            if (exp_a + exp_b) >= 2020:
                continue
            else:
                for exp_c in expenses:
                    if (exp_a + exp_b + exp_c) == 2020: #check that expenses are not equal here if that is not allowed
                        return exp_a * exp_b * exp_c


def test_day1():
    test_expenses = [
        1721,
        979,
        366,
        299,
        675,
        1456,
        ]
    assert sum_two_mul(test_expenses) == 514579
    assert sum_three_mul(test_expenses) == 241861950


if __name__ == "__main__":
    test_day1()
    expenses = get_input_file('day1_input.txt')
    expenses = [int(n) for n in expenses]
    print(f"The multiplication of the two expenses that sum to 2020 is {sum_two_mul(expenses)}")
    print(f"The multiplication of the three expenses that sum to 2020 is {sum_three_mul(expenses)}")