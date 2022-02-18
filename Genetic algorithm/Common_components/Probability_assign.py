from abc import ABC, abstractmethod

class Prob_assigner(ABC):

    @abstractmethod
    def assign_probs(self, popultation):
        pass