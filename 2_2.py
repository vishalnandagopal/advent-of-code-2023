# https://adventofcode.com/2023/day/

from os.path import dirname

with open(dirname(__file__) + "./input.txt", "r") as f:
    test_cases = [line.strip() for line in f.readlines() if line]


def game(test_case: str) -> (int, bool):
    """
    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

    Sample format of a line - Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    """

    game_num, _ = test_case.split(":")

    rounds = _.split(";")
    mini = dict()
    for r in rounds:
        for pick in r.split(","):
            num, color = pick.strip().split(" ")
            mini[color] = max(mini[color], int(num)) if color in mini else int(num)

    ans = 1
    for val in mini.values():
        ans *= val

    return ans


print(sum(map(game, test_cases)))
