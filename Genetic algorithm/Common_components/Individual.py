from abc import ABC, abstractmethod

class Individual(ABC):
    id=0


    def __init__(self, phenotype, random=False):
        self.fitness_score = None
        self.assigned_prob = None  # population is a class
        self.phenotype = phenotype
        self.id=Individual.id
        Individual.id+=1

        if random:
            self.phenotype= self.generate_random_phenotype()


    def get_phenotype(self):
        return self.phenotype



