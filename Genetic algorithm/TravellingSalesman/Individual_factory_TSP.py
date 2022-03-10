from Common_components.Individual import Individual
from Common_components.Individual_factory import Individual_factory
from TravellingSalesman.Phenotype_travelling_salesman import PhenotypeTSP
import random


class Individual_factory_TSP(Individual_factory):

    def create_random_individual(self, n=0):
        PhenotypeTSP.initialize_common_info(n)
        route =[int(x) for x in range(n)]
        random.shuffle(route)
        return Individual(PhenotypeTSP(route))