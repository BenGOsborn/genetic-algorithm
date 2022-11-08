import math
import random
import string

# Calculate fitness for a given guess vs actual


def fitness(guess, actual):
    assert len(guess) == len(actual)

    diff = 0

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            diff += 1

    return math.inf if diff == 0 else math.log(1 / diff)


# Breed two parents to create a child with a chance of mutating
def breed(parent1, parent2, mutation_chance):
    assert len(parent1) == len(parent2)
    assert mutation_chance >= 0 and mutation_chance <= 1

    out = ["" for _ in parent1]

    # Create a random string from the crossover
    choices = [0, 1, 2]
    choice_distribution = [
        0.5 - mutation_chance / 2,
        0.5 - mutation_chance / 2,
        mutation_chance
    ]

    for i in range(len(parent1)):
        choice = random.choices(choices, choice_distribution)[0]

        if choice == 0:
            out[i] = parent1[i]
        elif choice == 1:
            out[i] = parent2[i]
        else:
            out[i] = random.choice(string.printable)

    return "".join(out)


# Calculate probabilities from scores relative to their performance
def softmax(scores):
    out = [math.exp(score) for score in scores]
    summed = sum(out)

    return [elem / summed for elem in out]


# Create a generation from an output of the given generation
def create_next_generation(candidates, population_size):
    # **** Take the candidates
    # **** Select 2 at a time probabilistically and breed them until the desired population size has been met

    pass


if __name__ == "__main__":
    p1 = "hello"
    p2 = "aeslp"
    mutation = 0.01

    print(fitness(p1, p2))

    print(breed(p1, p2, mutation))
