

from Common_components.Crossover import Crossover
from Common_components.Mutator import Mutator
from Common_components.Population import Population
from tqdm import tqdm


class Genetic_search():

    def __init__(self, configuration, population_size, first_pop):

        self.population= first_pop
        self.crossover_obj = configuration.crossover_obj
        self.mutator = configuration.mutator
        self.fitness_obj = configuration.fitness_obj
        self.ind_factory = configuration.individual_factory
        self.parents_selector = configuration.parents_selector
        self.population_size = population_size


    def optimize(self, nr_iterations):
        most_fitted = None
        for i in range(nr_iterations):
            self.fitness_obj.calculate_fitness_population(self.population)
            tmp = self.population.get_most_fitted_individual(self.fitness_obj, feasible=True)
            most_fitted = self.fittest(most_fit_so_far=most_fitted, tmp=tmp)
            self.produce_next_gen()

        self.fitness_obj.calculate_fitness_population(self.population)
        tmp = self.population.get_most_fitted_individual(self.fitness_obj, feasible = True )
        most_fitted = self.fittest(most_fit_so_far=most_fitted, tmp=tmp)
        if most_fitted is None:
            return 0.0
        else:
            return most_fitted.fitness_score

    def fittest(self, most_fit_so_far, tmp):
        if tmp is None:
            return most_fit_so_far
        elif most_fit_so_far is None:
            return tmp
        elif most_fit_so_far.fitness_score < tmp.fitness_score:
            return tmp
        else:
            return most_fit_so_far







    def produce_next_gen(self, rate= 0.1):
        """

        :param selected_indi: iterable of individuals that are to be reproduce
        :return: a population object containing the new population
        """

        new_population = Population()
        self.parents_selector.assigned_probs=None
        for i in range(self.population.get_size()): #new population will have same length as old one
            father, mother =self.parents_selector.select_parents(self.population)
            descendant = self.crossover_obj.crossover(father, mother)
            self.mutator.mutate(descendant)
            new_population.add_individual(descendant)

        self.population = new_population



    def select_pair(self, individals):
        """
        Selects two individuals to be reproduced together either using a certain probability or using the same probability
        for all of them
        :return:
        """
        #return father, mother
        return None



    def select_using_probs(self, nr_individuals):
        """"
        Using the assigned probability that each indiviaual in the population has, it selects a set a number of them
        for reproduction.


        :return: an iterable with the selected individuals
        """
        return 0


if __name__ == '__main__':
        #process= Genetic_process()
        #process.optimize()
    print('done')