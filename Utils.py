import math
import random
import string


# Calculate fitness for a given guess vs actual
def fitness(guess, target):
    assert len(guess) == len(target)

    diff = 0

    for i in range(len(target)):
        if guess[i] != target[i]:
            diff += 1

    return 2 if diff == 0 else math.log(1) - math.log(diff)


# Breed two parents to create a child with a chance of mutating
def breed(parent1, parent2, mutation_chance):
    assert len(parent1) == len(parent2)
    assert mutation_chance >= 0 and mutation_chance <= 1

    out = [""] * len(parent1)

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


# Initialize the first generation of candidates
def initialize_candidates(target, population_size):
    candidates = [
        "".join(random.choice(string.printable) for _ in range(len(target))) for _ in range(population_size)
    ]

    return candidates


# Create a generation from an output of the given generation
def create_next_generation(candidates, target, population_size, mutation_chance):
    assert len(candidates) >= 2

    # Generate probabilities for each candidate based on their fitness
    scores = [fitness(candidate, target) for candidate in candidates]
    probs = softmax(scores)
    probs_index = list(range(len(probs)))

    # Breed current population to create next generation
    out = [""] * population_size

    for i in range(population_size):
        parent1 = None
        parent2 = None

        while parent1 == parent2:
            parent1 = random.choices(probs_index, probs)[0]
            parent2 = random.choices(probs_index, probs)[0]

        out[i] = breed(candidates[parent1],
                       candidates[parent2], mutation_chance)

    return out


if __name__ == "__main__":
    target = "hello"
    mutation_chance = 0.01
    population_size = 50

    max_iterations = 5000

    population = initialize_candidates(target, population_size)

    i = 0
    while i < max_iterations:
        population = create_next_generation(
            population, target, population_size, mutation_chance
        )

        avg_fitness = sum(fitness(candidate, target)
                          for candidate in population) / len(population)

        print(f"Population {i + 1} | Fitness {avg_fitness}")

        i += 1

    print(population)
