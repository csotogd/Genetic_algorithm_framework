from Common_components.Configuration import Configuration
from Common_components.Evolution import Genetic_search
from Common_components.Population import Population
from Common_components.parents_selector.Parents_selector import Parents_selector
from Knapsack.Crossover_knapscack import Crossover_Knapsack
from Knapsack.Fitness_calculator_kanpsack import Fitness_calculator_knapsack
from Knapsack.Ind_factory_knapsack import Ind_factort_knapsack
from Knapsack.Mutator_knapsack import Mutator_knapsack

if __name__ == '__main__':
    mutation_rate= 0.1
    nr_iterations= 100
    pop_size =100


    crossover = Crossover_Knapsack()
    fitness_obj = Fitness_calculator_knapsack( capacity = 20 )
    factory = Ind_factort_knapsack()
    parents_selector = Parents_selector()
    mutator = Mutator_knapsack(rate= mutation_rate)

    population = Population()
    population.create_first_population(size_pop=pop_size, ind_factory=factory, n = 10)

    config_object = Configuration(population, crossover, mutator, fitness_obj, factory, parents_selector)


    evolution = Genetic_search(config_object, pop_size, population)
    evolution.optimize(nr_iterations)



