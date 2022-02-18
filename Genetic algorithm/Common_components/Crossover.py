from abc import ABC, abstractmethod


class Crossover(ABC):

    @abstractmethod
    def crossover(self, father, mother):
        """
        :returns descendant
        """
        pass
