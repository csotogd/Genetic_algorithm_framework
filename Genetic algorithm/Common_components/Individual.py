

class Individual():
    id=0


    def __init__(self, phenotype):
        self.fitness_score = None
        self.phenotype = phenotype
        self.id=Individual.id
        Individual.id+=1


    def get_phenotype(self):
        return self.phenotype



