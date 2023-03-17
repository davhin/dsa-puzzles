from utils import get_input_file


def increasing_depths(depths: list):
    n_increasing_depths = 0
    for i in range(len(depths)-1):
        if depths[i+1] > depths[i]:
            n_increasing_depths += 1
    return n_increasing_depths


def smooth_depths(depths: list):
    smooth_depths = []
    for i in range(len(depths)-2):
        smooth_depths.append(depths[i] + depths[i+1] + depths[i+2])
    return smooth_depths


def test_day1():
    test_depths = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
        ]
    assert increasing_depths(test_depths) == 7
    assert(increasing_depths(smooth_depths(test_depths))) == 5


if __name__ == "__main__":
    test_day1()
    depths = get_input_file("day1_input.txt")
    depths = [int(n) for n in depths]
    n_increasing_depths = increasing_depths(depths)
    print(f"The number of increasing depth measurements is {n_increasing_depths}")
    n_increasing_smooth_depths = increasing_depths(smooth_depths(depths))
    print(f"The number of increasing smothed depth measurements is {n_increasing_smooth_depths}")