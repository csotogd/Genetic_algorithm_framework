class Configuration():

    def __init__(self, population, prob_assinger, crossover, mutator, fitness_obj, individual_factory):
        self.prob_assigner = prob_assinger
        self.crossover_obj = crossover
        self.mutator = mutator
        self.fitness_obj = fitness_obj
        self.individual_factory = individual_factory

