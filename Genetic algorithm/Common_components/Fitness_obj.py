from abc import ABC, abstractmethod



class Fitness_calculator(ABC):

    @abstractmethod
    def calculate_fitness_population(self, population):
        """Calculates the fitness funtion of every individual in the population"""
        #population.values().apply(lambda x: self.calculate_fitness_individual(x))
        return None



