import math
import random
from math import sqrt, cos

import numpy as np


def calculate_distance_between_cities(gamma):
    return sqrt(2.0 - 2.0 * cos(math.radians(gamma)))


class PhenotypeTSP():
    distances = []

    def to_string(self):
        return 'Route:' + str(self.route) + ' with distance: ' + str(PhenotypeTSP.calculate_distance_of_best_route(self.route, PhenotypeTSP.distances))

    def __init__(self, route):
        self.route = route

    @staticmethod
    def initialize_common_info(n):
        degrees = []
        route = [str(x) for x in range(n)]
        for p in range(n):
            degrees.append(p*(360.0/n))


        cities = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i == j:
                    pass
                else:
                    cities[i, j] = calculate_distance_between_cities(degrees[i] - degrees[j])
        PhenotypeTSP.distances = cities

    @staticmethod
    def calculate_distance_of_best_route(path, distances=None):
        """
            :param path: list of nodes in sequence
            :param distances: n x n matrix of distance from city i to j
            :return: float of the total distance of the overall path (TSP solution)
            """
        if(distances is None):
            distances = PhenotypeTSP.distances

        path = [int(i) for i in path]
        total_distance = 0
        number_of_cities = len(path)
        for i in range(number_of_cities):
            if i < number_of_cities - 1:
                total_distance += distances[path[i], path[i + 1]]
            else:
                total_distance += distances[path[i], path[0]]

        return total_distance

if __name__ =="__main__":
    print(calculate_distance_between_cities(180))