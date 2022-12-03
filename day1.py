def main():
    elves_calories = []
    with open("day_1_input", "r") as f:
        buffer = []
        for line in f:
            if line == "\n":
                elves_calories.append(sum(buffer))
                buffer.clear()
                continue
            buffer.append(int(line))
        print("Day 1 - Part 1:")
        print(max(elves_calories))

        sort_elves_calories = sorted(elves_calories)
        print("Day 1 - Part 2:")
        print(sum(sort_elves_calories[-3:]))


if __name__ == "__main__":
    main()
