# https://adventofcode.com/2023/day/

from os.path import dirname

with open(dirname(__file__) + "./input.txt", "r") as f:
    test_cases = [line.strip() for line in f.readlines() if line]


def checker(r: str, allowed: dict[str, int]):
    # 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    _ = dict()
    for pick in r.split(","):
        num, color = pick.strip().split(" ")
        _[color] = int(num)

    for color in allowed:
        if color in _ and _[color] > allowed[color]:
            return False
    return True


def game(test_case: str) -> (int, bool):
    """
    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

    Sample format of a line - Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    """

    game_num, _ = test_case.split(":")

    rounds = _.split(";")
    for r in rounds:
        if not checker(r.strip(), {"blue": 14, "green": 13, "red": 12}):
            # Even if one round fails, can go to the next game
            return (int(game_num[5:].strip()), False)
            
    return (int(game_num[5:].strip()), True)


print(sum(g[0] for g in filter(lambda x: x[1], map(game, test_cases))))
