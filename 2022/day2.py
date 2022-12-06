def main():
    games_points = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }
    with open('/Users/david/projects/adventofcode/2022/day2_input.txt', 'r') as f:
        strategy_guide = f.read()
        strategy_guide = strategy_guide.split("\n")
        strategy_guide = [game for game in strategy_guide if len(game) == 3]
        points = [games_points[game] for game in strategy_guide]
    print(f"The total points for the first rock paper scissors round are: {sum(points)}")


    game_response = {
        'A': {
            'X': 'Z',
            'Y': 'X',
            'Z': 'Y',
            },
        'B': {
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
            },
        'C': {
            'X': 'Y',
            'Y': 'Z',
            'Z': 'X',
            }
    }
    with open('/Users/david/projects/adventofcode/2022/day2_input2.txt', 'r') as f:
        strategy_guide = f.read()
        strategy_guide = strategy_guide.split("\n")
        strategy_guide = [game for game in strategy_guide if len(game) == 3]
        strategy_guide = [game.split(' ') for game in strategy_guide]
        strategy_guide = [game[0]+' '+game_response[game[0]][game[1]] for game in strategy_guide]
        points = [games_points[game] for game in strategy_guide]
    print(f"The total points for the second rock paper scissors round are: {sum(points)}")

if __name__ == "__main__":    
    main()