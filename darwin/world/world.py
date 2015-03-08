


class World(object):
    """World is the envoirment where individuals will go
    though natural selection. To a world, an Adam (first
    specimen) is provided that will evolve and reproduce"""

    def __init__(self, adam):
        super(World, self).__init__()
        self.adam = adam

    def mutate(self):
        pass

    def mate(self):
        pass

    def run(self, generations=100):
        pass
