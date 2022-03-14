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
        # res= self.order_one_crossover_method(father=father.phenotype.route, mother=mother.phenotype.route)[0]
        # res = Individual(PhenotypeTSP(self.cxOrdered(ind1=father.phenotype.route, ind2=mother.phenotype.route)[0]))
        # res = Individual(PhenotypeTSP(self.cxPartialyMatched(ind1=father.phenotype.route, ind2=mother.phenotype.route)[0]))
        res = Individual(PhenotypeTSP(self.order_one_crossover_method(father.phenotype.route, mother.phenotype.route)[0]))
        return res

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

        return child

    """
        Source: https://github.com/DEAP/deap/blob/master/deap/tools/crossover.py
    """

    def cxOrdered(self, ind1, ind2):
        """Executes an ordered crossover (OX) on the input
        individuals. The two individuals are modified in place. This crossover
        expects :term:`sequence` individuals of indices, the result for any other
        type of individuals is unpredictable.
        :param ind1: The first individual participating in the crossover.
        :param ind2: The second individual participating in the crossover.
        :returns: A tuple of two individuals.
        Moreover, this crossover generates holes in the input
        individuals. A hole is created when an attribute of an individual is
        between the two crossover points of the other individual. Then it rotates
        the element so that all holes are between the crossover points and fills
        them with the removed elements in order. For more details see
        [Goldberg1989]_.
        This function uses the :func:`~random.sample` function from the python base
        :mod:`random` module.
        .. [Goldberg1989] Goldberg. Genetic algorithms in search,
           optimization and machine learning. Addison Wesley, 1989
        """
        size = min(len(ind1), len(ind2))
        a, b = random.sample(range(size), 2)
        if a > b:
            a, b = b, a

        holes1, holes2 = [True] * size, [True] * size
        for i in range(size):
            if i < a or i > b:
                holes1[ind2[i]] = False
                holes2[ind1[i]] = False

        # We must keep the original values somewhere before scrambling everything
        temp1, temp2 = ind1, ind2
        k1, k2 = b + 1, b + 1
        for i in range(size):
            if not holes1[temp1[(i + b + 1) % size]]:
                ind1[k1 % size] = temp1[(i + b + 1) % size]
                k1 += 1

            if not holes2[temp2[(i + b + 1) % size]]:
                ind2[k2 % size] = temp2[(i + b + 1) % size]
                k2 += 1

        # Swap the content between a and b (included)
        for i in range(a, b + 1):
            ind1[i], ind2[i] = ind2[i], ind1[i]

        return ind1, ind2

    """
        Source: https://github.com/DEAP/deap/blob/master/deap/tools/crossover.py
    """

    def cxPartialyMatched(self, ind1, ind2):
        """Executes a partially matched crossover (PMX) on the input individuals.
        The two individuals are modified in place. This crossover expects
        :term:`sequence` individuals of indices, the result for any other type of
        individuals is unpredictable.
        :param ind1: The first individual participating in the crossover.
        :param ind2: The second individual participating in the crossover.
        :returns: A tuple of two individuals.
        Moreover, this crossover generates two children by matching
        pairs of values in a certain range of the two parents and swapping the values
        of those indexes. For more details see [Goldberg1985]_.
        This function uses the :func:`~random.randint` function from the python base
        :mod:`random` module.
        .. [Goldberg1985] Goldberg and Lingel, "Alleles, loci, and the traveling
           salesman problem", 1985.
        """
        size = min(len(ind1), len(ind2))
        p1, p2 = [0] * size, [0] * size

        # Initialize the position of each indices in the individuals
        for i in range(size):
            p1[ind1[i]] = i
            p2[ind2[i]] = i
        # Choose crossover points
        cxpoint1 = random.randint(0, size)
        cxpoint2 = random.randint(0, size - 1)
        if cxpoint2 >= cxpoint1:
            cxpoint2 += 1
        else:  # Swap the two cx points
            cxpoint1, cxpoint2 = cxpoint2, cxpoint1

        # Apply crossover between cx points
        for i in range(cxpoint1, cxpoint2):
            # Keep track of the selected values
            temp1 = ind1[i]
            temp2 = ind2[i]
            # Swap the matched value
            ind1[i], ind1[p1[temp2]] = temp2, temp1
            ind2[i], ind2[p2[temp1]] = temp1, temp2
            # Position bookkeeping
            p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
            p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

        return ind1, ind2

    """
    Adapted from: https://codereview.stackexchange.com/questions/226179/easiest-way-to-implement-cycle-crossover
    """
    def cycle_crossover(self, parent_one, parent_two):
        chrom_length = len(parent_one)
        p1_copy = parent_one.copy()
        p2_copy = parent_two.copy()
        child_one = [-1] * chrom_length
        child_two = [-1] * chrom_length
        swap = True
        count = 0
        pos = 0

        while True:
            if count > chrom_length:
                break
            for i in range(chrom_length):
                if child_one[i] == -1:
                    pos = i
                    break

            if swap:
                while True:
                    child_one[pos] = parent_one[pos]
                    count += 1
                    pos = parent_two.index(parent_one[pos])
                    if p1_copy[pos] == -1:
                        swap = False
                        break
                    p1_copy[pos] = -1
            else:
                while True:
                    child_one[pos] = parent_two[pos]
                    count += 1
                    pos = parent_one.index(parent_two[pos])
                    if p2_copy[pos] == -1:
                        swap = True
                        break
                    p2_copy[pos] = -1

        for i in range(chrom_length):  # for the second child
            if child_one[i] == parent_one[i]:
                child_two[i] = parent_two[i]
            else:
                child_two[i] = parent_one[i]

        for i in range(chrom_length):  # Special mode
            if child_one[i] == -1:
                if p1_copy[i] == -1:  # it means that the ith gene from p1 has been already transfered
                    child_one[i] = parent_two[i]
                else:
                    child_one[i] = parent_one[i]

        return child_one, child_two


if __name__ == "__main__":
    x = CrossoverTSP()
    print(x.crossover_from_paper(father=[0, 1, 2, 3, 4, 5, 6, 7], mother=[1, 6, 4, 7, 3, 0, 5, 4]))
    print(x.crossover_from_paper(father=[2, 3, 7, 1, 6, 0, 5, 4], mother=[3, 1, 4, 0, 5, 7, 2, 6]))
