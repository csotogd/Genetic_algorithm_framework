import random

class Parents_selector:

    def __init__(self):
        self.assigned_probs=None
        #dictionary, key will be id of individual and key will be its assigned probability


    def select_parents(self, population):
        """"
        population: a population with already assigned probabilities
        """
        self.assign_probs_for_reproduction(population)
        father, mother = self.probability_based_selection(population)
        #father, mother = self.tournament_based_selection(population)
        return father, mother

    def check_assigned_probs(self):
        """returns True if individuals already have a probability
        assigned to them and False if they do not have it yet"""
        if self.assigned_probs is None:
            return False
        return True

    def assign_probs_for_reproduction(self, population):
        if self.check_assigned_probs():
            return #already assigned
        else:
            #self.roulette_wheel_boltzmann_probs(population)
            self.roulette_wheel_probs(population)

    def roulette_wheel_probs(self, population):
        self.assigned_probs= {}
        pop_f = population.get_population_fitness()
        for ind in population.individuals.keys():
            self.assigned_probs[ind] = ind/pop_f
        return 0

    def roulette_wheel_boltzmann_probs(self,population):
        return 'to be implemented'

    def probability_based_selection(self, population):
        """"
        returns the ids of two parents that will be reproduced
        """

        father= -1
        mother = -1
        while mother ==-1:
            for id, prob in self.assigned_probs.items():
                if prob> random.random():
                    if father== -1:
                        father = id
                    else:
                        mother = id
                        return father, mother





