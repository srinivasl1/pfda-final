import random
import numpy as np

class Region():
    def __init__(self, name, creatures, difficulty, areas):
        self.name = name
        self.creatures = creatures #list of potential creatures that can be found in this region, always 2 common, 2 uncommon, 1 rare
        self.difficulty = difficulty
        self.areas = areas #in order - center, north, east, south, west

    #def attempted to find creature
    def find_creature(self):
        return np.random.choice([1, 0], p=[self.difficulty, 1-self.difficulty])
        

    def random_creature(self):
        probs = [.3, .3, .15, .15, .1] #2 common, 2 uncommon, 1 rare
        return np.random.choice(self.creatures, p=probs)

