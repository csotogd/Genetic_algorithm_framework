import math
from math import sqrt
from math import cos
import numpy as np
import random


def calculate_distance_between_cities(gamma):
    return sqrt(2 - 2 * cos(math.radians(gamma)))


def fitness_function(path, distances):
    """

    :param path: list of nodes in sequence
    :param distances: n x n matrix of distance from city i to j
    :return: float of the total distance of the overall path (TSP solution)
    """
    total_distance = 0
    number_of_cities = len(path)
    for i in range(number_of_cities):
        if i < number_of_cities - 1:
            total_distance += distances[path[i], path[i + 1]]
        else:
            total_distance += distances[path[i], path[0]]
    return total_distance


def generate_random_population(number_of_cities, size_of_population):
    population = []
    for tmp in range(size_of_population):
        tmp_route = [int(x) for x in range(number_of_cities)]
        random.shuffle(tmp_route)
        population.append(tmp_route)

    return population


def mutate_individual(individual, rate):
    mutation = random.random()
    if mutation < rate:
        n = len(individual)
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        tmp = individual[i]
        individual[i] = individual[j]
        individual[j] = tmp
        return individual
    else:
        return individual



n = 5
degrees = []
route = [str(x) for x in range(n)]

for p in range(n):
    degrees.append(random.randint(0, 359))

dictionary = dict(zip(route, degrees))
best_route = sorted(dictionary, key=dictionary.get)

cities = np.zeros((5, 5))
x = 1
for i in range(n):
    for j in range(n):
        if i == j:
            pass
        else:
            cities[i, j] = calculate_distance_between_cities(degrees[i] - degrees[j])

print('best root is: ', best_route)
print('distance between cities matrix:')
print(cities)
distances = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
path = [0, 1, 2]
print(fitness_function(path, distances))
print(generate_random_population(number_of_cities=5, size_of_population=4))




