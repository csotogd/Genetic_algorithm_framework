import random

class Parents_selector:

    def __init__(self):
        self.assigned_probs=None
        #dictionary, key will be id of individual and key will be its assigned probability


    def select_parents(self, population):
        """"
        population: a population with already assigned probabilities
        returns two individual objects that will be reproduced
        """
        self.assign_probs_for_reproduction(population)
        father_id, mother_id = self.probability_based_selection_ids(population)
        #father, mother = self.tournament_based_selection(population)

        father = population.individuals[father_id]
        mother = population.individuals[mother_id]
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
            self.roulette_wheel_probs_all_positive(population)

    def roulette_wheel_probs(self, population):
        self.assigned_probs= {}
        pop_f = population.get_population_fitness()
        for ind in population.individuals.keys():
            self.assigned_probs[ind] = population.individuals[ind].fitness_score/pop_f
        return 0



    def roulette_wheel_probs_all_positive(self, population):
        """
        we first add to all fitness score a constant to make them all positive
        This is the minimum of all fitness scores
        :param population:
        :return:
        """

        #get minimum of all fitness scores
        minimum_f_score = 99999
        for ind in population.individuals.keys():
            if minimum_f_score>  population.individuals[ind].fitness_score:
                minimum_f_score = population.individuals[ind].fitness_score

        if minimum_f_score<0:
            #make all positive
            for ind in population.individuals.keys():
                population.individuals[ind].fitness_score += -1*minimum_f_score

        self.assigned_probs = {}
        pop_f = population.get_population_fitness()
        for ind in population.individuals.keys():
            self.assigned_probs[ind] = population.individuals[ind].fitness_score / pop_f
        return 0


    def roulette_wheel_boltzmann_probs(self,population):
        return 'to be implemented'

    def probability_based_selection_ids(self, population):
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





