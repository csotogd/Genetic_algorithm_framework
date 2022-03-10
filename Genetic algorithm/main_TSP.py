from Common_components.Configuration import Configuration
from Common_components.Evolution import Genetic_search
from Common_components.Population import Population
from Common_components.parents_selector.Parents_selector import Parents_selector
from TravellingSalesman.Crossover_travelling_salesman import CrossoverTSP
from TravellingSalesman.Fitness_obj_travelling_salesman import FitnessTSP
from TravellingSalesman.Individual_factory_TSP import Individual_factory_TSP
from TravellingSalesman.Mutator_travelling_salesman import Mutator_TSP
import numpy as np

if __name__ == '__main__':
    mutation_rate = np.arange(0.0, 1.0, 0.05).tolist()
    iterations = [10, 100, 1000]
    pop_size = [10, 100, 1000]
    size_of_individuals_phenotype = [10, 100, 1000]

    mutation_rate = 0.05
    nr_iterations = 1000
    pop_size = 1000
    size_of_individuals_phenotype = 1000


    for rate in mutation_rate:
        for iteration in iterations:
            for pop in pop_size:
                for size in size_of_individuals_phenotype:
                    crossover = CrossoverTSP()
                    fitness_obj = FitnessTSP()
                    factory = Individual_factory_TSP()
                    parents_selector = Parents_selector()
                    mutator = Mutator_TSP(rate=mutation_rate)
                    population = Population()
                    population.create_first_population(size_pop=pop_size, ind_factory=factory, n=size_of_individuals_phenotype)
                    config_object = Configuration(population, crossover, mutator, fitness_obj, factory, parents_selector)
                    evolution = Genetic_search(config_object, pop_size, population)
                    print(evolution.optimize(nr_iterations))
