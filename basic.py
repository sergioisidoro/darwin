from darwin.models import Individual
from darwin.models import World


class IndividualExample(Individual):

    def survival_test(self):
        pass

    def mutate(self):
        pass


adam = IndividualExample([1, 2, 3, 4, 5, 6])

brave_new_world = World(adam)

brave_new_world.evolve()
