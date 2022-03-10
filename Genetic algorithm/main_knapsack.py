from Common_components.Configuration import Configuration
from Common_components.Evolution import Genetic_search
from Common_components.Population import Population
from Common_components.parents_selector.Parents_selector import Parents_selector
from Knapsack.Crossover_knapscack import Crossover_Knapsack
from Knapsack.Fitness_calculator_kanpsack import Fitness_calculator_knapsack
from Knapsack.Ind_factory_knapsack import Ind_factort_knapsack
from Knapsack.Mutator_knapsack import Mutator_knapsack
import numpy as np
import pandas as pd

if __name__ == '__main__':
    mutation_rate = np.arange(0.0, 1.0, 0.05).tolist()
    iterations = [10, 100, 1000]
    pop_size = [10, 100, 1000]
    size_of_individuals_phenotype = [10, 100, 1000]
    number_of_samples_per_combinations_of_parameters = 100

    rate= 0.1
    iteration= 100
    pop =100
    size = 10

    crossover = Crossover_Knapsack()
    fitness_obj = Fitness_calculator_knapsack( capacity = 20 )
    factory = Ind_factort_knapsack()
    parents_selector = Parents_selector()
    mutator = Mutator_knapsack(rate= rate)
    population = Population()
    population.create_first_population(size_pop=pop, ind_factory=factory, n = size)
    config_object = Configuration(population, crossover, mutator, fitness_obj, factory, parents_selector)
    evolution = Genetic_search(config_object, pop, population)
    evolution.optimize(iteration)



