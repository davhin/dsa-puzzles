from pathlib import Path

def get_input_file(name):
    filepath = Path(__file__).parent / "input" / name
    with open(filepath, 'r') as f:
        input_file = [line.rstrip('\n') for line in f]
        return input_file