class Configuration():

    def __init__(self, population, crossover, mutator, fitness_obj, individual_factory, parents_selector):
        self.crossover_obj = crossover
        self.mutator = mutator
        self.fitness_obj = fitness_obj
        self.individual_factory = individual_factory
        self.parents_selector = parents_selector

