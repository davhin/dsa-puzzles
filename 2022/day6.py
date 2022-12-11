

def parse_msg_input():
    with open('/Users/david/projects/adventofcode/2022/day6_input.txt', 'r') as f:
        msg = f.read().split("\n")[0]
    return msg


def find_marker_pos(msg: str, chars: int):
    """Takes a message msg and returns the last position of the marker given the number of unique chars that denote a marker"""
    marker_pos = 0
    for i in range(chars, len(msg), 1):
        if len(set(msg[i-chars:i])) == chars:
            marker_pos = i
            break
    return marker_pos


def test_find_packet_marker_pos():
    assert find_marker_pos("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert find_marker_pos("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert find_marker_pos("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert find_marker_pos("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11


if __name__ == "__main__":
    ##task 1
    msg = parse_msg_input()
    test_find_packet_marker_pos()
    print(f"The end bit of the first start of packet marker is at position {find_marker_pos(msg, 4)}.")
    ##task 2
    print(f"The end bit of the first start of message marker ist at position {find_marker_pos(msg, 14)}")