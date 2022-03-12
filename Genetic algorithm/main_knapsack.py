import time

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
import os

if __name__ == '__main__':
    mutation_rate = np.arange(0.0, 1.0, 0.1).tolist()
    iterations = [10, 100, 200]
    pop_size = [10, 100, 200]
    size_of_individuals_phenotype = [10, 100, 200]
    number_of_parameters_to_test = 20*3*3*3
    blah = 0
    number_of_samples_per_combinations_of_parameters = 5
    column_names = ['mutation_rate', 'iterations_number', 'population_size', ' number_of_cities',
                    'average_solution_distance']
    df = pd.DataFrame(columns=column_names)
    start = time.time()
    for rate in mutation_rate:
        for iteration in iterations:
            for pop in pop_size:
                for size in size_of_individuals_phenotype:
                    results = []
                    for i in range(number_of_samples_per_combinations_of_parameters):
                        crossover = Crossover_Knapsack()
                        fitness_obj = Fitness_calculator_knapsack(capacity=20)
                        factory = Ind_factort_knapsack()
                        parents_selector = Parents_selector()
                        mutator = Mutator_knapsack(rate=rate)
                        population = Population()
                        population.create_first_population(size_pop=pop, ind_factory=factory, n=size)
                        config_object = Configuration(population, crossover, mutator, fitness_obj, factory,
                                                      parents_selector)
                        evolution = Genetic_search(config_object, pop, population)
                        results.append(evolution.optimize(iteration))
                    tmp_df = pd.DataFrame(columns=column_names, data=[[rate, iteration, pop, size, np.mean(results)]])
                    df = pd.concat([df, tmp_df], ignore_index=True)
                blah = blah +1
                print('Completed number of parameters:', blah ,'/', number_of_parameters_to_test)
    end = time.time()
    print('time took: ', end-start)
    df.to_csv(r'Knapsack_results_calculate_fitness_linear_violated.csv', index=False, header=True)

