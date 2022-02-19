import random
class Phenotype_kanpsack:
    packages={} #this info is common to all phenotypes so we make it static
    def __init__(self, included):
        self.included = included #list of eithet 0 and ones, where 0 at index i represents that package with index i is not included
        self.value, self.weight = self.calculate_total_value_weight()
        #list of ids included

    def calculate_total_value_weight(self):
        value=0
        weight= 0
        for i in range(len(self.included)):
            if self.included[i]==1:
                value+= Phenotype_kanpsack.packages[i].value
                weight+=Phenotype_kanpsack.packages[i].weight
        return value, weight

    def to_string(self):
        return str(self.included) + "  with value: " + str(self.value) + "   and weight: " + str(self.weight)

    @staticmethod
    def  initialize_common_info(n):
        """we initialize the inmutable info that is common to all genotype
        TODO: JD, for you, you would be initializing here, the set of stations
        in your world, the distance matrix, etc....at least that is what makes sense to me"""
        for value in range(n):
            weight = random.random()*10
            package = Package(weight, value )
            Phenotype_kanpsack.packages[value]= package




class Package:
    def __init__(self, weight, value):
        self.id=value
        self.value= value
        self.weight= weight
