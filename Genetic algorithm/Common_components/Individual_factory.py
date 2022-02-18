from abc import ABC, abstractmethod
class Individual_factory:
    @abstractmethod
    def create_random_individual(self, n=0):
        """

        :param n:
        :return: an indivual with its respective phenotype
        """
