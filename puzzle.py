class Puzzle():
    def __init__(self, id, region, area, description, solving, solved, answer_type):
        self.id = id
        self.region = region
        self.area = area
        self.is_solved = False
        self.description = description
        self.solving = solving
        self.solved = solved
        self.answer_type = answer_type

