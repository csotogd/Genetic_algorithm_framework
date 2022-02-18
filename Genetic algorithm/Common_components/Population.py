class Population():
    generation_nr=0
    def __init__(self):
        self.fitness_score= None #population is a class
        self.individuals = {} #keys are ids and values are individual objects
        self.generation_nr = Population.generation_nr
        Population.generation_nr+=1


    def create_first_population(self, size_pop , ind_factory, n):
        """Generates a ppopulation randomly that corresponds to this object"""
        for i in range(size_pop):
            ind = ind_factory.create_random_individual(n=n)
            self.individuals[ind.id]=ind

    def get_size(self):
        return len(self.individuals)

    def add_individual(self, individual):
        self.individuals[individual.id]= individual

    def get_population_fitness(self, feasible= True):
        """returns the sum of the fitness score of all individuals in the population
        :feasible: whether the individual has to represent a feadible solution or not.
        """
        pop_score =sum([individual.fitness_score for individual in self.individuals.values()])
        return pop_score

    def get_most_fitted_individual(self, fitness_obj,feasible = True):
        max_f=-9999999
        max_ind= None

        for id, individual in self.individuals.items():
            if individual.fitness_score> max_f and fitness_obj.test_solution_is_feasible(individual):
                max_f = individual.fitness_score
                max_ind = individual

