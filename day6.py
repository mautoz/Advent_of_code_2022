def check_repetition(subtring: str) -> bool:
    return len(set(subtring)) == len(subtring)


def read_substring(signal: str, marker_distinct_len: int):
    signal_len = len(signal)
    start = 0
    while (start + marker_distinct_len) <= signal_len:
        if check_repetition(signal[start : start + marker_distinct_len]):
            # We found the marker!
            return start + marker_distinct_len
        start += 1

    return -1


def main():
    with open("day_6_input", "r") as f:
        signal = f.readline()
        print("Part 1 - First Marker after character:")
        print(read_substring(signal, 4))
        print("Part 2 - First Marker after character:")
        print(read_substring(signal, 14))


if __name__ == "__main__":
    main()
