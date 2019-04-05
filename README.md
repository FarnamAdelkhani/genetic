## Goal: Clone items with features that are desirable from parents. ##

#### March, 16 2018 - Farnam Adelkhani ####
### Genetic Algorithms - Evolving Generative Design --- Not unlike reinforcement learning. ###

We use concepts from evolutionary Biology to find a global min to an optimization problem.
GAs can also be utilized while implementing machine learning applications for tasks such as optimal route determination.

**Selection - Crossover - Mutation**
- Creating a random population -- (popSize = user defined)
- Assess the fitness of different items (strings) - chars are in correct position 
- Crossover/Breed - Create a mating pool likely to lead to propagation
- Mutations - User defined in (if mrate < 0.01:)


**Start here:**
1. Run genetic.py
2. User input: **What target do you want to match?**
   - Tell the program what string to target
3. User input: **Population size?**
   - Define the default population size. Choosing a lower value causes greater delays as you progress.

**Output:**

![alt text](https://github.com/FarnamAdelkhani/geneticAlgorithms_GenerativeDesign/blob/master/genRuntime.png?raw=true "Hello, world! My name is, Farnam!")

... we get lucky in the first example, only 74 Generations till reaching the target @ 34 seconds.


**Below**, is a more complex example that I terminated since it was simply taking too much time.
This exposes two weak points of the program:
1. An inability to increase population size during later generations, this would help optimize runtime.
2. Pooly optimized algorithm - genetic algorithms are not known for their runtime but we could try and make improvements.


![alt text](https://github.com/FarnamAdelkhani/geneticAlgorithms_GenerativeDesign/blob/master/genRuntime_slow.png?raw=true "User Input: It is better to be feared than loved, if you cannot be both.")

Create a branch, then see if you can improve upon this program!

- Relevant read: Evolving Design by Danil Nagy
   - Link: https://medium.com/generative-design/evolving-design-b0941a17b759

- Relevant read: The Nature of Code by Daniel Shiffman
   - Link: https://natureofcode.com/book/chapter-9-the-evolution-of-code/

Credits: Doug Lloyd @ Harvard
