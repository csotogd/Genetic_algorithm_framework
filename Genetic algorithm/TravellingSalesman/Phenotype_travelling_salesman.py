import random
from math import sqrt, cos, radians

import numpy as np


def calculate_distance_between_cities(gamma):
    return sqrt(2 - 2 * cos(radians(gamma)))


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
            degrees.append(random.randint(0, 359))

        dictionary = dict(zip(route, degrees))
        best_route = sorted(dictionary, key=dictionary.get)

        cities = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i == j:
                    pass
                else:
                    cities[i, j] = calculate_distance_between_cities(degrees[i] - degrees[j])

        best_route = ['2', '8', '1', '4', '3', '5', '0', '6', '7', '9']
        cities = np.array([[0.0, 1.9780317267238336, 0.7492131868318245, 1.696096192312852, 1.992389396183491, 1.2036300463040965, 0.08723877473067185, 0.38161799075308955, 0.9079809994790938, 0.5847434094454735], [1.9780317267238336, 0.0, 1.7232583208830514, 1.2988960966603673, 0.4668907277118107, 1.7576342253239308, 1.963254366895328, 1.8852829821843569, 1.6282310367126385, 1.8051705686997213], [0.7492131868318245, 1.7232583208830514, 0.0, 1.969615506024416, 1.9126095119260709, 1.7143346014042247, 0.6676137184675424, 0.38161799075308983, 0.17431148549531658, 0.17431148549531658], [1.696096192312852, 1.2988960966603673, 1.969615506024416, 0.0, 0.9079809994790935, 0.7167358990906005, 1.7407113918797994, 1.8671608529944035, 1.992389396183491, 1.9318516525781366], [1.992389396183491, 0.4668907277118107, 1.9126095119260709, 0.9079809994790935, 0.0, 1.4862896509547885, 1.9980964431637156, 1.9890437907365468, 1.8543677091335748, 1.9562952014676112], [1.2036300463040965, 1.7576342253239308, 1.7143346014042247, 0.7167358990906005, 1.4862896509547885, 0.0, 1.272156440555528, 1.4862896509547885, 1.7975880925983339, 1.618033988749895], [0.08723877473067185, 1.963254366895328, 0.6676137184675424, 1.7407113918797994, 1.9980964431637156, 1.272156440555528, 0.0, 0.29561882225922137, 0.8293864853124784, 0.500760008108883], [0.38161799075308955, 1.8852829821843569, 0.38161799075308983, 1.8671608529944035, 1.9890437907365468, 1.4862896509547885, 0.29561882225922137, 0.0, 0.5512747116339985, 0.2090569265353067], [0.9079809994790938, 1.6282310367126385, 0.17431148549531658, 1.992389396183491, 1.8543677091335748, 1.7975880925983339, 0.8293864853124784, 0.5512747116339985, 0.0, 0.34729635533386055], [0.5847434094454735, 1.8051705686997213, 0.17431148549531658, 1.9318516525781366, 1.9562952014676112, 1.618033988749895, 0.500760008108883, 0.2090569265353067, 0.34729635533386055, 0.0]])

        PhenotypeTSP.distances = cities
        print('best root is: ', best_route)
        print('distance between of the best route is: ', PhenotypeTSP.calculate_distance_of_best_route(best_route, cities))

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