

class Configuration(ABC):

    def __init__(self, population, prob_assinger, crossover, mutator, fitness_obj):
        self.prob_assigner = prob_assinger
        self.crossover_obj = crossover
        self.mutator = mutator
        self.fitness_obj = fitness_obj

