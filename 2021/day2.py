from utils import get_input_file


def first_navigation(commands: list):
    pos = [0, 0]
    for command in commands:
        if command[0] == 'forward':
            pos[0] += int(command[1])
        elif command[0] == 'down':
            pos[1] += int(command[1])
        elif command[0] == 'up':
            pos[1] -= int(command[1])
    return pos[0]*pos[1]


def second_navigation(commands: list):
    pos = [0, 0]
    aim = 0
    for command in commands:
        if command[0] == 'forward':
            pos[0] += int(command[1])
            pos[1] += aim*int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
    return pos[0]*pos[1]


def test_day2():
    test_commands = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
        ]
    test_commands = [line.split(" ") for line in test_commands]
    assert first_navigation(test_commands) == 150
    assert second_navigation(test_commands) == 900


if __name__ == "__main__":
    test_day2()
    commands = get_input_file("day2_input.txt")
    commands = [line.split(" ") for line in commands]
    print(f"The result of the first navigation procedure is: {first_navigation(commands)}")
    print(f"The result of the first navigation procedure is: {second_navigation(commands)}")