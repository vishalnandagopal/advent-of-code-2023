# https://adventofcode.com/2023/day/

from os.path import dirname

with open(dirname(__file__) + "./input.txt", "r") as f:
    test_cases = [line.strip() for line in f.readlines() if line]


def f(test_case: str) -> str | int:
    
    ...

print(sum(map(f, test_cases)))
