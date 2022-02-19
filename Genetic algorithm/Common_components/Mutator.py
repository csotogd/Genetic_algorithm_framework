from abc import ABC, abstractmethod


class Mutator(ABC):
    def __init__(self, rate):
        self.rate=rate

    @abstractmethod
    def mutate(self, individual):
        """

        :param individual:
        :param rate:
        :return: mutated_individual
        """
        pass
