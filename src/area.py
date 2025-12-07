class Area():
    def __init__(self, name, region, description, direction, borders, has_creatures=False, puzzles=[]):
        self.name = name
        self.region = region
        self.description = description
        self.direction = direction #C, N, E, S, W - center of region map or cardinal direction 
        self.borders = borders #[N, E, S, W] #(str:Region, str:Area)
        self.creatures = has_creatures
        self.puzzles = puzzles
        

