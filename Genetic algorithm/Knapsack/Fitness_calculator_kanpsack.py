from Common_components.Fitness_obj import Fitness_calculator
from Knapsack.Phenotype_kanpsack import Phenotype_kanpsack



class Fitness_calculator_knapsack(Fitness_calculator):
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fitness_individual(self, individual):
        """
        Assigns a fitness score to each individual
        :param individual:
        :return: the fitness score
        """
        individual.fitness_score= self.calculate_fitness_linear_violated(individual)
        return individual.fitness_score

    def calculate_fitness_square_violated(self, individual):
        """"
        The score is the value minus the amount of capacity violation squared in case.
        This is done to penalize violation
        """""

        return 'to be implemented'

    def calculate_fitness_linear_violated(self, individual):
        """"
        The score is the value minus the amount of capacity violation.
        """""

        violation = individual.phenotype.weight - self.capacity
        violation = max (0, violation)
        fitness = individual.phenotype.value - violation

        return fitness

    def test_solution_is_feasible(self, individual):
        violation = individual.phenotype.weight - self.capacity
        if violation>0:
            return False
        else:
            return  True


    #TODO: try out different fitness functions

