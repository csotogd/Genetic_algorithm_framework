from Common_components.Configuration import Configuration
from Common_components.Evolution import Genetic_search
from Common_components.Population import Population
from Common_components.parents_selector.Parents_selector import Parents_selector
from TravellingSalesman.Crossover_travelling_salesman import CrossoverTSP
from TravellingSalesman.Fitness_obj_travelling_salesman import FitnessTSP
from TravellingSalesman.Individual_factory_TSP import Individual_factory_TSP
from TravellingSalesman.Mutator_travelling_salesman import Mutator_TSP

if __name__ == '__main__':
    mutation_rate = 0.4
    nr_iterations = 100000  # 1000,100-16.39821734955649 10000,100-
    pop_size = 10

    crossover = CrossoverTSP()
    fitness_obj = FitnessTSP()
    factory = Individual_factory_TSP()
    parents_selector = Parents_selector()
    mutator = Mutator_TSP(rate=mutation_rate)

    population = Population()
    population.create_first_population(size_pop=pop_size, ind_factory=factory, n=10)

    config_object = Configuration(population, crossover, mutator, fitness_obj, factory, parents_selector)

    evolution = Genetic_search(config_object, pop_size, population)
    evolution.optimize(nr_iterations)
