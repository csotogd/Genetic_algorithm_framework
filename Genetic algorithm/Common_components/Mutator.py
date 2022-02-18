from abc import ABC, abstractmethod


class Mutator(ABC):

    @abstractmethod
    def mutate(self, individual, rate):
        """

        :param individual:
        :param rate:
        :return: mutated_individual
        """
        pass
