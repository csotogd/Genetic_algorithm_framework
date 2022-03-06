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
        individual.fitness_score = self.calculate_distance_TSP(individual.phenotype.route)
        return individual.fitness_score

    @staticmethod
    def calculate_distance_TSP(path):
        """
            :param path: list of nodes in sequence
            :param distances: n x n matrix of distance from city i to j
            :return: float of the total distance of the overall path (TSP solution)
            """
        distances = PhenotypeTSP.distances
        total_distance = 0
        number_of_cities = len(path)
        for i in range(number_of_cities):
            if i < number_of_cities - 1:
                total_distance += distances[path[i], path[i + 1]]
            else:
                total_distance += distances[path[i], path[0]]

        return total_distance

    def test_solution_is_feasible(self, individual):
        """Returns true if the solution respects all the problems constraints, false otherwise"""
        for i in range(len(individual.phenotype.route)):
            if not i in individual.phenotype.route:
                return False

        return True
