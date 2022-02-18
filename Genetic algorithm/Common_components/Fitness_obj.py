from abc import ABC, abstractmethod



class Fitness_calculator(ABC):


    def calculate_fitness_population(self, population):
        """Calculates the fitness funtion of every individual in the population"""
        return sum([self.calculate_fitness_individual(ind) for ind in population.individuals.values()])

    @abstractmethod
    def calculate_fitness_individual(self, individual):
        pass

    @abstractmethod
    def test_solution_is_feasible(self):
        """Returns true if the solution respects all the problems constraints, false otherwise"""
        pass
