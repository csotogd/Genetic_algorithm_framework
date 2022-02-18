import random
class Phenotype_kanpsack:
    packages={} #this info is common to all phenotypes so we make it static
    def __init__(self, included, n):
        self.included = included #list of eithet 0 and ones, where 0 at index i represents that package with index i is not included
        self.value, self.weight = self.calculate_total_value_weight()
        #list of ids included

    def calculate_total_value_weight(self):
        value=0
        weight= 0
        for pckg_id in self.included:
            value+= Phenotype_kanpsack.packages[pckg_id].value #this is the same as the id
            weight+=Phenotype_kanpsack.packages[pckg_id].weight
        return value, weight

    def to_string(self):
        return str(self.included) + "  with value: " + str(self.value) + "   and weight: " + str(self.weight)

    @staticmethod
    def  initialize_common_info(n):
        """we initialize the inmutable info that is common to all genotype
        TODO: JD, for you, you would be initializing here, the set of stations
        in your world, the distance matrix, etc....at least that is what makes sense to me"""
        for i in range(n):
            weight = random.random()*10
            package = Package(weight)
            Phenotype_kanpsack.packages[i]= package

class Package:
    id=1
    def __init__(self, weight):
        self.id=Package.id
        self.value= self.id
        Package.id+=1
        self.weight= weight
