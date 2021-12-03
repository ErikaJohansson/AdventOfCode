import util


def run_a(day: str):
    data = util.read_file("input/" + day + ".txt")

    gamma_rate = ""
    epsilon_rate = ""
    zeroes = [0] * (len(data[0])-1)
    ones = [0] * (len(data[0])-1)
    for nb in data:
        for i in range(len(nb)):
            if nb[i] == "0":
                zeroes[i] += 1
            if nb[i] == "1":
                ones[i] += 1

    for i in range(len(zeroes)):
        if zeroes[i] > ones[i]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    print("Gamma Rate: ", gamma_rate)
    print("Epsilon Rate: ", epsilon_rate)
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print("Power Consumption: ", power_consumption)


def run_b(day: str):
    data = util.read_file("input/" + day + ".txt")
    


if __name__ == "__main__":
    today = "day3"
    print("--- Day 3: Binary Diagnostic ---")
    run_a(today)
    print("--- Part Two ---")
    run_b(today)
