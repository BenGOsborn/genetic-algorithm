import math


def fitness(guess, actual):
    diff = 0

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            diff += 1

    return math.inf if diff == 0 else math.log(1 / diff)


if __name__ == "__main__":
    print(fitness("hello", "hellp"))
