import copy
import uuid


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
        self.id = uuid.uuid4()

    def clone(self):
        clone = copy.copy(self)
        clone.id = uuid.uuid4()
        return clone

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

    def __unicode__(self):
        return "Inidvidual %s" % self.id

    def __str__(self):
        return "Inidvidual %s" % self.id

    def __repr__(self):
        return "Inidvidual %s" % self.id
