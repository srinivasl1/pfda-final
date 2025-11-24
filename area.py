class Area():
    def __init__(self, name, region, description, direction, borders, puzzles=[]):
        self.name = name
        self.region = region
        self.description = description
        self.direction = direction #C, N, E, S, W - center of region map or cardinal direction 
        self.borders = borders #[N, E, S, W] #(str:Region, str:Area)
        self.puzzles = puzzles
        

