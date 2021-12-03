import util


def run_a():
    measured_depths = util.read_file("day1/input_1_a.txt")
    increased_depths = 0
    for n in range(1, len(measured_depths)):
        if int(measured_depths[n - 1]) < int(measured_depths[n]):
            increased_depths += 1

    print("number of increased depths: ", increased_depths)


def run_b():
    measured_depths = util.read_file("day1/input_1_a.txt")
    increased_depths = 0
    for n in range(0, len(measured_depths) - 3):
        measurement_1 = int(measured_depths[n]) + int(measured_depths[n + 1]) + int(measured_depths[n + 2])
        measurement_2 = int(measured_depths[n + 1]) + int(measured_depths[n + 2]) + int(measured_depths[n + 3])
        if measurement_2 > measurement_1:
            increased_depths += 1

    print("number of increased depth windows: ", increased_depths)


if __name__ == "__main__":
    print("--- Day 1: Sonar Sweep ---")
    run_a()
    print("--- Part Two ---")
    run_b()