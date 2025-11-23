class Creature():
    def __init__(self, name, size, type, rarity, region):
        self.name = name
        self.size = size #tiny, small, medium, large, giant
        self.type = type #winged, burrower, quick-footed, strong 
        self.rarity = rarity #common, uncommon, rare
        self.region = region

    def page_display(self):
        print(rf"""

                    __________________   __________________
                .-/|                  \ /                  |\-.
                ||||{self.name.center(19)}|{(self.size + ", " + self.type).center(19)}||||
                ||||     --==*==--     |{"creature".center(19)}||||
                ||||{"Found in the".center(19)}|{"~~*~~".center(19)}||||
                ||||{self.region.upper().center(19)}|                   ||||
                ||||                   |                   ||||
                ||||                   |{self.rarity.upper().center(19)}||||
                ||||                   |{"--==*==--".center(19)}||||
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||__________________ | __________________||||
                ||/===================\|/===================\||
                `--------------------~___~-------------------''

        """)