from Common_components.Individual import Individual
from Common_components.Individual_factory import Individual_factory
from Knapsack.Phenotype_kanpsack import Phenotype_kanpsack
import random


class Ind_factort_knapsack(Individual_factory):

    def create_random_individual(self, n=0):
        Phenotype_kanpsack.initialize_common_info(n)
        #Phenotype_kanpsack.initialize_common_info_deterministic_1(n)
        #Phenotype_kanpsack.initialize_common_info_deterministic_2(n)
        included = self.__select_packages_ids_for_individual(n)
        phenotype = Phenotype_kanpsack( included)
        return Individual(phenotype)


    def __select_packages_ids_for_individual(self, n):
        selected =[]
        for i in range(n):
            if random.random()>0.5:
                selected.append(0)
            else:
                selected.append(1)
        return selected




