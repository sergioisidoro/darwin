from pyspark import SparkConf, SparkContext

conf = (SparkConf()
        .setMaster("local")
        .setAppName("Darwin")
        .set("spark.executor.memory", "1g"))


class World(object):
    """World is the envoirment where individuals will go
    though natural selection. To a world, an Adam (first
    specimen) is provided that will evolve and reproduce"""

    population = []

    def __init__(self, adam):
        super(World, self).__init__()
        self.adam = adam

        # Initialize Spark Library
        sc = SparkContext(conf=conf)
        sc.addPyFile('../individual/Individual.py')

        # POPULATE
        self.population = sc.parallelize(adam)

    def epoch(self):
        pass

    # Visitor pattern to visit every individual
    def evaluate(self, individual):
        return individual.evaluate()

    def mate(self):
        pass

    def evolve(self, generations=100):
        pass
