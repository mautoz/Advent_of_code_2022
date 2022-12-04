# Calculate the value by the ASCII code
def get_item_priority(item: str):
    if item.isupper():
        return ord(item) - 38

    return ord(item) - 96


def get_rucksack_content(content: str):
    compartment_1 = content[: int(len(content) / 2)]
    compartment_2 = content[int(len(content) / 2) :]
    result = list(set(compartment_1).intersection(compartment_2))
    return get_item_priority(result[0])


def main_part_1():
    with open("day_3_input", "r") as f:
        priority_sum = 0
        for line in f:
            priority_sum += get_rucksack_content(line.strip())

        print("Day 3 - Part 1:")
        print(priority_sum)


def get_common_item(buffers):
    intersection_list = set(set(buffers[0]).intersection(buffers[1]))
    common_item = list(intersection_list.intersection(buffers[2]))
    return get_item_priority(common_item[0])


def main_part_2():
    with open("day_3_input", "r") as f:
        priority_sum = 0
        buffers = []
        for i, line in enumerate(f):
            buffers.append(line.strip())
            if (i + 1) % 3 == 0:
                priority_sum += get_common_item(buffers)
                buffers.clear()

        print("Day 3 - Part 2:")
        print(priority_sum)


if __name__ == "__main__":
    main_part_1()
    main_part_2()
