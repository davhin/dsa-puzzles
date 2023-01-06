import string


alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priorities = {}
for i in range(len(alphabet)):
    priorities[alphabet[i]] = i+1


def main(bag_contents: list):
    ## task 1
    bag_compartments = [[items[:int(len(items)/2)], items[int(len(items)/2):]] for items in bag_contents]
    shared_contents = [list(set(items[0]).intersection(set(items[1])))[0] for items in bag_compartments]
    shared_contents_prios = [priorities[item] for item in shared_contents]
    print(f"The sum of the shared items priorities is: {sum(shared_contents_prios)}")

    ##task 2
    bag_groups = [bag_contents[i:i+3] for i in range(0, len(bag_contents), 3)]
    shared_contents = [list(set(items[0]).intersection(set(items[1]).intersection(set(items[2]))))[0] for items in bag_groups]
    shared_contents_prios = [priorities[item] for item in shared_contents]
    print(f"The sum of the shared items priorities for the three-bag-groups is: {sum(shared_contents_prios)}")


def test_main():
    bag_contents_test = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]
    main(bag_contents_test)


if __name__ == "__main__":
    with open('/Users/david/projects/adventofcode/2022/day3_input.txt', 'r') as f:
        bag_contents = f.read().split("\n")[:-1]
    #test_main()
    main(bag_contents)