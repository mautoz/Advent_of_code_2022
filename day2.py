# A = Rock, B = Paper and C = Scissor
jokenpo_win = {"A": "Y", "B": "Z", "C": "X"}
jokenpo_equal = {"A": "X", "B": "Y", "C": "Z"}

point = {"X": 1, "Y": 2, "Z": 3}

# Your choose: [win, draw, loss]
jokenpo_strategy = {"A": ["B", "A", "C"], "B": ["C", "B", "A"], "C": ["A", "C", "B"]}
point_2 = {"A": 1, "B": 2, "C": 3}


def sum_point(you: str, opponent: str):
    if jokenpo_equal[opponent] == you:
        return point[you] + 3

    if jokenpo_win[opponent] == you:
        return point[you] + 6

    return point[you]


def main_part_1():
    with open("day_2_input", "r") as f:
        matches_points = []
        for line in f:
            match = line.strip().split()
            opponent = match[0]
            you = match[1]
            matches_points.append(sum_point(you, opponent))

    print("Day 2 - Part 1:")
    print(sum(matches_points))


def sum_points_part_2(you: str, opponent: str):
    if you == "X":
        return point_2[jokenpo_strategy[opponent][2]]
    if you == "Y":
        return point_2[jokenpo_strategy[opponent][1]] + 3

    return point_2[jokenpo_strategy[opponent][0]] + 6


def main_part_2():
    with open("day_2_input", "r") as f:
        matches_points = []
        for line in f:
            match = line.strip().split()
            opponent = match[0]
            you = match[1]
            matches_points.append(sum_points_part_2(you, opponent))

    print("Day 2 - Part 2:")
    print(sum(matches_points))


if __name__ == "__main__":
    main_part_1()
    main_part_2()
