# https://adventofcode.com/2023/day/1

from os.path import dirname

with open(dirname(__file__) + "./input.txt", "r") as f:
    test_cases = [line.strip() for line in f.readlines() if line]


words_to_num = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

count = 0

for _, test_case in enumerate(test_cases):
    i = 0
    while i < len(test_case):
        j = i + 3
        while j < len(test_case) + 1:
            if test_case[i:j] in words_to_num:
                # print(test_case)
                test_case = (
                    test_case[:i]
                    + str(words_to_num.index(test_case[i:j]))
                    + test_case[j:]
                )
                # print(test_case)
                break
            j += 1
        i += 1
    test_cases[_] = test_case

print(test_cases[-30:])


def a(test_case):
    _ = int(list(filter(lambda x: x.isnumeric(), list(test_case)))[0]) * 10 + int(
        list(filter(lambda x: x.isnumeric(), list(test_case)))[-1]
    )
    print(_)
    return _


# print(
#     sum(
#         map(
#             lambda test_case: a(test_case),
#             test_cases,
#         )
#     )
# )

# Alternate multi-line, readable solution

sumi = 0

for test_case in test_cases:
    _ = ""
    # _ is a string containing all the integers in one specific test test_case
    
    for x in test_case:
        if x.isnumeric():
            _ += x
    
    # This steps add the (first integer in the test test_case * 10 + last integer in the test test_case) to the overall sum, if _ is not empty. It can use first and last elements of _ directly since _ consists of just numbers of x and is in the same order
    sumi += int(_[0]) * 10 + int(_[-1]) if _ else 0
    print(f"{sumi} - {test_case}")

print(sumi)

