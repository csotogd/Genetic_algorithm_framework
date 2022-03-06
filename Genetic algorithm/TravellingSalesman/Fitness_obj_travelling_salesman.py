from abc import ABC
from TravellingSalesman.Phenotype_travelling_salesman import PhenotypeTSP
from Common_components.Fitness_obj import Fitness_calculator


class FitnessTSP(Fitness_calculator, ABC):

    def calculate_fitness_individual(self, individual):
        """
        Assigns a fitness score to each individual
        :param individual:
        :return: the fitness score
        """
        individual.fitness_score = PhenotypeTSP.calculate_distance_of_best_route(individual.phenotype.route)
        return individual.fitness_score

    def test_solution_is_feasible(self, individual):
        """Returns true if the solution respects all the problems constraints, false otherwise"""
        for i in range(len(individual.phenotype.route)):
            if not i in individual.phenotype.route:
                return False

        return True
