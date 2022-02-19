import random

class Mutator_knapsack:

    def __init__(self, rate):
        self.rate=rate

    def mutate(self, individual):
        """mutates the individual with probability rate.
        mutation is just flipping one random bit from 0 to 1 or viceversa

        individual is an individual object
        """

        if random.random()<self.rate:
            idx = random.randint(0, len(individual.phenotype.included)-1)
            if individual.phenotype.included[idx]== 0:
                individual.phenotype.included[idx]=1
            else:
                individual.phenotype.included[idx] = 0
