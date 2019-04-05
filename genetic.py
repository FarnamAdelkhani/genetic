# ---------------------------------------- March, 16 2018 -- Farnam Adelkhani
# -------------- Genetic Algorithms --- Reinforcement learning --------------
# ---------- Evolving Generative Design ---------- Evolve a String ----------
# Creating a random population - (popSize = user defined)
#
# Assess the fitness of different items (strings) -
#                                  chars are in correct position
# Crossover/Breed - Create a mating pool likely to lead to propagation
# Mutation - User defined in (if mrate < 0.01:)
#
# - Goal: Clone items with features that are desirable from parents -
#
import random

from evolve import evolve, target
from helpers import summarize

# User defined population size as an int
popSize = int(input("Population size? "))
# Create empty population array
population = []
bestScore = 0
generation = 1

# Iterate from popSize times
for i in range(popSize):
    # Define new phrase object
    population.append(evolve())

# Run until the max of the target
while bestScore < len(target):

    # Find out everyone's ability
    for i in range(popSize):
        # *Remember getFitness creates a new property within the object
        population[i].getFitness()

        # If it's better than anything previously seen
        if population[i].fitness > bestScore:
            bestScore = population[i].fitness
            # Current gen, what string?, best score it's seen thus far
            summarize(generation, population[i].getContents(), bestScore)

    matingPool = []
    # Copy contents over
    parents = population[:]
    # Reset population
    population = []

    for i in range(popSize):
        for j in range(parents[i].fitness):
            # Add every single item to the mating pool once
            matingPool.append(parents[i])

    # Randomly pair people together
    for i in range(popSize):
        # Randomly pick 1 item from the mating pool - once for each parent
        x = random.choice(range(len(matingPool)))
        y = random.choice(range(len(matingPool)))

        # Get child object after merger
        child = matingPool[x].crossover(matingPool[y])
        # First product of generation 2
        child.mutate(generation)
        # First prodigy of next Gen
        population.append(child)

# We're finished now so increase generation by 1
    generation += 1
