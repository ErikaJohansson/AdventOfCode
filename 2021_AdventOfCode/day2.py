import util


def run_a():
    directions = util.read_file("input/day2.txt")

    horizontal_position = 0
    depth_position = 0
    for direction in directions:
        command = direction.split(" ")[0]
        amount = int(direction.split(" ")[1])

        if command == "forward":
            horizontal_position += amount
        elif command == "down":
            depth_position += amount
        elif command == "up":
            depth_position -= amount

    print("Horizontal position: ", horizontal_position)
    print("Depth position: ", depth_position)
    print("Multiplied: ", horizontal_position * depth_position)


def run_b():
    directions = util.read_file("input/day2.txt")

    horizontal_position = 0
    depth_position = 0
    aim = 0

    for direction in directions:
        command = direction.split(" ")[0]
        amount = int(direction.split(" ")[1])

        if command == "forward":
            horizontal_position += amount
            depth_position += aim * amount
        elif command == "down":
            aim += amount
        elif command == "up":
            aim -= amount

    print("Horizontal position: ", horizontal_position)
    print("Depth position: ", depth_position)
    print("Multiplied: ", horizontal_position * depth_position)


if __name__ == "__main__":
    print("--- Day 2: Dive! ---")
    run_a()
    print("\n--- Part Two ---")
    run_b()
