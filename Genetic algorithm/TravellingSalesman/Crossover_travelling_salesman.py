from Common_components.Crossover import Crossover
from Common_components.Individual import Individual
from TravellingSalesman.Phenotype_travelling_salesman import PhenotypeTSP
import random


class CrossoverTSP(Crossover):

    def crossover(self, father, mother):
        """
        father and mother are two indvidual objects
        :returns descendant
        """
        return self.order_one_crossover_method(father=father.phenotype.route, mother=mother.phenotype.route)[0]

    def crossover_from_paper(self, father, mother):
        tracko1 = father.copy()
        tracko2 = mother.copy()
        o1 = father.copy()
        o2 = mother.copy()
        c1 = []
        c2 = []
        n = len(o1)

        # step 2
        # this is find the first available element in o2 step
        i = self.get_first_available_element(tracko2)
        c1.append(i)
        # tracko1[tracko1.index(i)] = None

        while tracko1[o1.index(i)] is not None:
            tracko1[i] = None
            i = o1.index(i)
            i = o2[i]
            i = o1.index(i)
            i = o2[i]
            c2.append(i)

            # step 4
            i = o1.index(i)
            i = o2[i]
            c1.append(i)
            tracko1[o1.index(i)] = None
            i = o2.index(i)
            i = o1[i]
            c2.append(i)
            tracko2[o2.index(i)] = None

        print(c1, c2)

    def get_first_available_element(self, track):
        for element in track:
            if element is not None:
                return element
        return None

    def order_one_crossover_method(self, father, mother):
        n = len(father)
        p1 = int(n / 3)
        p2 = int((n / 3) * 2)
        child1 = []
        child2 = []
        i = 0
        while i < (p2 - p1):
            child1.append(father[i + p1])
            child2.append(mother[i + p1])
            i += 1

        child1 = self.finish_crossover(child1, mother, p2)
        child2 = self.finish_crossover(child2, father, p2)
        return child1, child2

    def finish_crossover(self, child, parent, t):
        while len(child) < len(parent):
            if t >= len(parent):
                t = 0
            if not parent[t] in child:
                child.append(parent[t])
            t += 1

        return Individual(PhenotypeTSP(child))


if __name__ == "__main__":
    x = CrossoverTSP()
    # x.crossover_from_paper(father=[0,1,2,3,4,5,6,7], mother=[1, 6, 4, 7, 3, 0, 5, 4])
    # x.crossover_from_paper(father=[2, 3, 7, 1, 6, 0, 5, 4], mother=[3, 1, 4, 0, 5, 7, 2, 6])
    print(x.order_one_crossover_method(father=[2, 3, 7, 1, 6, 0, 5, 4], mother=[3, 1, 4, 0, 5, 7, 2, 6]))
