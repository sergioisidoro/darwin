

class Individual(object):
    """Individual is an specimen of a species
    An idividual has a genetic code that is a list of genes
    that will be a key factor for the individual's survival"""

    # The genetic code is a list of generic objecs (genes)
    genetic_code = []
    fitness = 0

    def __init__(self, genetic_code):
        self.genetic_code = genetic_code
        super(Individual, self).__init__()

    def test(self):
        return 1 - 1

    def evaluate(self):
        self.fitness = self.survival_test()
        return self

    def survival_test(self):
        raise NotImplementedError(
            "survival_test should be implemented, "
            "expressing a rating of how well individual is fit to the world."
        )

    def mutate(self):
        raise NotImplementedError(
            "mutate should be implemented, "
            "randomly changing a gene from the idividual, with random value"
        )
