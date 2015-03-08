from darwin.individual import Individual
from darwin.world import World


class IndividualExample(Individual):

    def survival_test():
        pass

    def mutate():
        pass


adam = IndividualExample([1, 2, 3, 4, 5, 6])

brave_new_world = World(adam)
brave_new_world.evolve()
