stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}


def read_crates_start_positions(line: list):
    print(len(line))
    stack = 1
    position = 0
    while position < len(line):
        if line[position] == "":
            position += 4
        else:
            crate = str(line[position]).replace("[", "").replace("]", "")
            stacks[stack].append(crate)
            position += 1
        stack += 1


def read_instructions(line: str):
    import re

    # Convert instruction line to list. Example:
    # move X from Y to Z => [X, Y, Z]
    return re.findall(r"\d+", line)


def invert_stacks_list():
    for key, value in stacks.items():
        stacks[key] = list(reversed(value))


def move_crane(move: list):
    num_crates = int(move[0])
    while num_crates > 0:
        stacks[int(move[2])].append(stacks[int(move[1])].pop())
        num_crates -= 1


def move_crane_9001(move: list):
    num_crates = int(move[0])

    stacks[int(move[2])] += stacks[int(move[1])][-num_crates:]
    del stacks[int(move[1])][-num_crates:]


def get_top_stacks():
    top_stacks = []
    for _, value in stacks.items():
        top_stacks.append(value.pop())
    print("".join(top_stacks))


def clear_stacks():
    for _, value in stacks.items():
        value.clear()


def main_part_1():
    with open("day_5_input", "r") as f:
        for i, line in enumerate(f):
            if any(letter.isdigit() for letter in line):
                invert_stacks_list()
                break
            read_crates_start_positions(line.strip().split(" "))

        import pprint as pp

        print(">>> Stacks - Part 1 - Start")
        pp.pprint(stacks)

        for line in f:
            if line == "\n":
                continue
            move_crane(read_instructions(line.strip()))

        print(">>> Stacks - Part 1 - End")
        pp.pprint(stacks)

        print("Top Stacks - Part 1:")
        get_top_stacks()


def main_part_2():
    with open("day_5_input", "r") as f:
        for i, line in enumerate(f):
            if any(letter.isdigit() for letter in line):
                invert_stacks_list()
                break
            read_crates_start_positions(line.strip().split(" "))

        import pprint as pp

        print(">>> Stacks - Part 2 - Start")
        pp.pprint(stacks)

        for line in f:
            if line == "\n":
                continue
            move_crane_9001(read_instructions(line.strip()))

        print(">>> Stacks - Part 2 - End")
        pp.pprint(stacks)

        print("Top Stacks - Part 2:")
        get_top_stacks()


if __name__ == "__main__":
    main_part_1()
    clear_stacks()
    main_part_2()
