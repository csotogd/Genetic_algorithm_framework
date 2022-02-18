from abc import ABC, abstractmethod

from Common_components.Individual import Individual


class Population(ABC):
    generation_nr=0
    def __init__(self):
        self.fitness_score= None #population is a class
        self.individuals = {} #keys are ids and values are individual objects
        self.generation_nr = Population.generation_nr
        Population.generation_nr+=1

    @abstractmethod
    def fitness_function(self):
        pass

    def get_size(self):
        return len(self.individuals)

    def add_individual(self, individual):
        self.individuals[individual.id]= individual

    def get_population_fitness(self):
        pop_score =sum([individual.fitness_score for individual in self.individuals.values()])
        return pop_score

    def generate_first_population(self, size):
        for i in range(size):
            ind = Individual(phenotype= None, random=True)
            self.individuals[ind.id]=ind
