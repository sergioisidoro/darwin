
from darwin import settings
from darwin.models.strategy import SelectionStrategy, NormalProbabilitySelection
import uuid
import logging


logger = logging.getLogger(__name__)


class World(object):
    """World is the envoirment where individuals will go
    though natural selection. To a world, an Adam (first
    specimen) is provided that will evolve and reproduce"""

    population = []
    world_size = settings.DEFAULT_WORLD_SIZE
    mutation_probability = settings.DEFAULT_MUTATION_PROBABILITY
    harshness = settings.DEFAULT_HARSHNESS

    # Using strategy pattern for selection strategy modularity
    selection_strategy = None
    mating_strategy = None

    def __init__(self, adam, size=None,
                 selection_strategy=None,
                 mating_strategy=None):

        self.id = uuid.uuid4()
        self.adam = adam

        if size:
            self.world_size = size

        for n in range(1, self.world_size):
            adam_clone = self.adam.clone()
            adam_clone.mutate()
            self.population.append(adam_clone)

        if selection_strategy:
            self.selection_strategy = selection_strategy
        else:
            # set default strategy
            self.selection_strategy = NormalProbabilitySelection()

        if mating_strategy:
            self.mating_strategy = mating_strategy
        else:
            # set default strategy
            self.mating_strategy = NormalProbabilitySelection()

        super(World, self).__init__()

    def epoch(self):
        # Evaluates the population
        self.population = map(self.evaluate, self.population)
        self.select()
        # Mate

    # Visitor pattern to visit every individual
    # Evauluates each one and updates the individual fitness
    def evaluate(self, individual):
        return individual.evaluate()

    # Interface for the selection strategy, which is a filter
    def select(self):
        # Select
        self.selection_strategy.update_population(self.population)
        select_filter = lambda x: self.selection_strategy.select(x)
        self.selected = filter(select_filter, self.population)

    # Method for competing selection strategies
    def fight(self):
        raise NotImplemented("This is staged for future development")

    def mate(self, selected_individuals):
        pass
        # Randomizes the selected

    def evolve(self, generations=100):
        for gen in range(0, generations):
            logger.info("World %s at generation %d" % (self.id, gen))
            self.epoch()
