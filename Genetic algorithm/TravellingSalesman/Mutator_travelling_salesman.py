import random
from Common_components.Individual import Individual
from TravellingSalesman.Phenotype_travelling_salesman import PhenotypeTSP


class Mutator_TSP:

    def __init__(self, rate):
        self.rate=rate

    def mutate(self, individual):
        """mutates the individual with probability rate.
        mutation is just flipping one random bit from 0 to 1 or vice versa

        individual is an individual object
        """
        individual= individual.phenotype.route
        mutation = random.random()
        if mutation < self.rate:
            n = len(individual)
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            tmp = individual[i]
            individual[i] = individual[j]
            individual[j] = tmp
            return Individual(PhenotypeTSP(individual))
        else:
            return Individual(PhenotypeTSP(individual))