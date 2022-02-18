from abc import ABC, abstractmethod



class Fitness_calculator(ABC):

    def calculate_fitness_population(self, population):
        """Calculates the fitness funtion of every individual in the population"""
        population.values().apply(lambda x: self.calculate_fitness_individual(x))
        return None

    @abstractmethod
    def calculate_fitness_individual(self, individual):
        """given an individual, calculates its fitness score and
        assigns the probability to its internal fitness_score parameter"""

