from abc import ABC, abstractmethod

class Prob_assigner(ABC):

    @abstractmethod
    def assign_probs_for_reproduction(self, population):
        """"
        Assigns each individual in the population a probability of being picked.
        It internally changes the population object of the class
        
        :population: is a population object
        
        returns: the same population object with probabilities assigned to each of the individuals
        """""
        pass
