from Common_components.Crossover import Crossover
import copy
import random

from Common_components.Individual import Individual
from Knapsack.Phenotype_kanpsack import Phenotype_kanpsack


class Crossover_Knapsack(Crossover):


    def crossover(self, father, mother):
        """
        :returns descendant
        """
        return self.crossover_random_point(father, mother)

    def crossover_random_point(self, father, mother):
        """"
        LEts say we have two indivuals
        in1= 0011011011
        in2= 0001001110

        then a random splitting point is chosen with equal probability.
        Say the splitting point is 3, then we have two possible descendants
        000   1011011

        and
        001   1001110

        then we choose one of them both randomly

        :returns a descendant object
        """

        splitting_point = random.randint(0, len(father.phenotype.included))
        offspring_1 = father.phenotype.included[:splitting_point] + mother.phenotype.included[splitting_point:]
        offspring_2 = mother.phenotype.included[:splitting_point] + father.phenotype.included[splitting_point:]
        idx = random.randint(0,1)

        included = [offspring_1, offspring_2][idx]
        descendant =self.create_new_individual(included, father)
        return descendant

    def create_new_individual(self, included, father):
        """

        :param included: a list of 1s and 0 indicating whether a gene is contained or not
        :param father: an individual user that will be used to clone
        :return: a descendant containing included in its phenotype
        """

        descendant = copy.deepcopy(father)
        descendant.id = Individual.id
        Individual.id+=1
        phenotype = Phenotype_kanpsack(included)
        descendant.phenotype =phenotype
        return descendant
    #TODO try out different crossover techniques