from typing import Tuple


def check_value_in(value: str, extreme: list) -> bool:
    return (
        True
        if ((int(value) >= int(extreme[0])) and (int(value) <= int(extreme[1])))
        else False
    )


def get_extremes(interval_left: str, interval_right: str) -> Tuple[list, list]:
    return interval_left.split("-"), interval_right.split("-")


def check_fully_contain(extreme_left: list, extreme_right: list) -> bool:
    r_in_l = check_value_in(extreme_right[0], extreme_left) and check_value_in(
        extreme_right[1], extreme_left
    )
    l_in_r = check_value_in(extreme_left[0], extreme_right) and check_value_in(
        extreme_left[1], extreme_right
    )

    return r_in_l or l_in_r


def main_part_1():
    with open("day_4_input", "r") as f:
        total_fully_contained = 0
        for line in f:
            interval = line.strip().split(",")
            extremes_left, extremes_right = get_extremes(interval[0], interval[1])
            if check_fully_contain(extremes_left, extremes_right):
                total_fully_contained += 1

        print("Day 4 - Part 1:")
        print(total_fully_contained)


def check_contain(extreme_left: list, extreme_right: list) -> bool:
    r_in_l = check_value_in(extreme_right[0], extreme_left) or check_value_in(
        extreme_right[1], extreme_left
    )
    l_in_r = check_value_in(extreme_left[0], extreme_right) or check_value_in(
        extreme_left[1], extreme_right
    )

    return r_in_l or l_in_r


def main_part_2():
    with open("day_4_input", "r") as f:
        total_fully_contained = 0
        for line in f:
            interval = line.strip().split(",")
            extremes_left, extremes_right = get_extremes(interval[0], interval[1])
            if check_contain(extremes_left, extremes_right):
                total_fully_contained += 1

        print("Day 4 - Part 2:")
        print(total_fully_contained)


if __name__ == "__main__":
    main_part_1()
    main_part_2()
