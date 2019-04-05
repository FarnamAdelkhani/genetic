# Reminder: An object/Python is similar to a structure/C or an object/JS
# Credits: Doug Lloyd @ Harvard
import random

# Get user string
target = input("What target do you want to match? ")

# Create a new class
class evolve:
    # First parameter is always self
    def __init__(self):
        # Create an array of characters
        self.characters = []
        # Every phrase should have same number of char as target itself
        for i in range(len(target)):
            # Take a number and turn it into a char
            # + Randomly select some characters from valid ascii characters
            character = chr(random.choice(range(32, 127)))
            # Attach that char to the end of list
            self.characters.append(character)

    # Define new method - Build a string 1 char at a time to join everything
    def getContents(self):
        # Return as string
        return ''.join(self.characters)

    # Method to gather fitness properties
    def getFitness(self):
        # New field
        self.fitness = 0
        # Compare every char in new string to target
        for i in range(len(self.characters)):
            if self.characters[i] == target[i]:
                self.fitness += 1

    # Create a new child object
    def crossover(self, partner):
        # New Child object
        child = evolve()
        # Get random num from 0-1
        for i in range(len(self.characters)):
            if random.random() < 0.5:
                # 50% of time take from mother
                child.characters[i] = self.characters[i]
            else:
                # Otherwise from other parent
                child.characters[i] = partner.characters[i]

        # Object that we have created
        return child

    def mutate(self, generation):
        # Iterate over all the characters
        for i in range(len(self.characters)):
            if generation > 100:
                mrate = random.random()
                mrate *= (generation / 100)
                # The mutation rate - May want to increase as approaching final
                # 1% of the time change into something random
                if mrate < 0.01:
                    self.characters[i] = chr(random.choice(range(32, 127)))
