import os

with open(os.path.dirname(__file__) + "./input.txt", "r") as f:
    test_cases = [line.strip() for line in f.readlines()]


print(
    sum(
        map(
            lambda case: int(list(filter(lambda x: x.isnumeric(), list(case)))[0]) * 10
            + int(list(filter(lambda x: x.isnumeric(), list(case)))[-1]),
            test_cases,
        )
    )
)
