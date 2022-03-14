from Common_components.Configuration import Configuration
from Common_components.Evolution import Genetic_search
from Common_components.Population import Population
from Common_components.parents_selector.Parents_selector import Parents_selector
from TravellingSalesman.Crossover_travelling_salesman import CrossoverTSP
from TravellingSalesman.Fitness_obj_travelling_salesman import FitnessTSP
from TravellingSalesman.Individual_factory_TSP import Individual_factory_TSP
from TravellingSalesman.Mutator_travelling_salesman import Mutator_TSP
import numpy as np
import pandas as pd
import time
if __name__ == '__main__':
    mutation_rate = np.arange(0.0, 1.0, 0.1).tolist()
    iterations = [10, 100, 200]
    pop_size = [10, 100, 200]
    size_of_individuals_phenotype = [10, 100, 200]
    number_of_samples_per_combinations_of_parameters = 5

    # mutation_rate = 0.05
    # iterations = 10
    # pop_size = 10
    # size_of_individuals_phenotype = 1000

    column_names = ['mutation_rate', 'iterations_number', 'population_size', ' number_of_cities', 'average_solution_distance']
    df = pd.DataFrame(columns=column_names)
    start = time.time()

    for rate in mutation_rate:
        for iteration in iterations:
            for pop in pop_size:
                for size in size_of_individuals_phenotype:
                    results = []
                    for i in range(number_of_samples_per_combinations_of_parameters):
                        crossover = CrossoverTSP()
                        fitness_obj = FitnessTSP()
                        factory = Individual_factory_TSP()
                        parents_selector = Parents_selector()
                        mutator = Mutator_TSP(rate=rate)
                        population = Population()
                        population.create_first_population(size_pop=pop, ind_factory=factory, n=size)
                        config_object = Configuration(population, crossover, mutator, fitness_obj, factory, parents_selector)
                        evolution = Genetic_search(config_object, pop, population)
                        results.append(evolution.optimize(iteration))
                    tmp_df = pd.DataFrame(columns=column_names, data=[[rate, iteration, pop, size, np.mean(results)]])
                    df = pd.concat([df,tmp_df], ignore_index=True)
        print('Done with mutation rate: ', rate)
    end = time.time()
    print('time took: ', end - start)
    df.to_csv(r'TSP_results_order_one_crossover_method.csv', index=False, header=True)
