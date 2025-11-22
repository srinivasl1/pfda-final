class Creature():
    def __init__(self, name, size, type, rarity):
        self.name = name
        self.size = size #tiny, small, medium, large, giant
        self.type = type #winged, burrower, quick-footed, strong 
        self.rarity = rarity