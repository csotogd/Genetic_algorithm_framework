from abc import ABC, abstractmethod

from Common_components.Crossover import Crossover
from Common_components.Mutator import Mutator
from Common_components.Population import Population


class Genetic_process(ABC):

    def __init__(self, configuration):
        self.population= None
        self.prob_assigner = configuration.prob_assigner
        self.crossover_obj = configuration.crossover_obj
        self.mutator = configuration.mutator
        self.fitness_obj = configuration.fitness_obj




    def produce_next_gen(self):
        self.fitness_obj.calculate_fitness_population(self.population)
        selected_indi = self.select_individuals_for_reproduction()
        new_population = self.reproduce(selected_indi)
        self.population= new_population

    def select_individuals_for_reproduction(self):
        """
        Selects the individuals that will reproduce
        :return:
        """
        self.prob_assigner.assign_probs_for_reproduction()
        selected_individuals = self.select_using_probs()
        return selected_individuals


    def reproduce(self, selected_indi, rate= 0.1):
        """

        :param selected_indi: iterable of individuals that are to be reproduce
        :return: a population object containing the new population
        """

        new_population = Population()

        for i in range(self.population.get_size()): #new population will have same length as old one
            father, mother =self.select_pair(selected_indi)
            descendant = self.crossover_obj.crossover(father, mother)
            descendant = self.mutator.mutate(descendant, rate)
            new_population.add_individual(descendant)

        return new_population



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

