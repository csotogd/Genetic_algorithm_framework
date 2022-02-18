from Common_components.Crossover import Crossover
import copy
import random

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
        """

        descendant = copy.deepcopy(father)
        #TODO check that this is also copying all inner objects

        splitting_point = random.randint(0, len(father.phenotype.included))
        offspring_1 = father.phenotype.included[:splitting_point] + mother.phenotype.included[splitting_point:]
        offspring_2 = mother.phenotype.included[:splitting_point] + father.phenotype.included[splitting_point:]
        idx = random.randint(0,1)

        return [offspring_1, offspring_2][idx]

    #TODO try out different crossover techniques