from creature import Creature
from region import Region

def main():
    bestiary = []
    meadow, glade = setup()

    success = meadow.find_creature()
    if success:
        print(meadow.random_creature().name)
    else:
        print("You didn't find anything!")



def setup():
    meadow_animals = []

    #MEADOW
    #common
    meadow_animals.append(Creature("Mouse", "tiny", "burrower", "common"))
    meadow_animals.append(Creature("Hare", "small", "quick-footed", "common"))

    #uncommon
    meadow_animals.append(Creature("Snake", "small", "burrower", "uncommon"))
    meadow_animals.append(Creature("Grasshopper", "tiny", "winged", "uncommon"))

    #rare
    meadow_animals.append(Creature("Hawk", "medium", "winged", "rare"))

    meadow = Region("Meadow", meadow_animals, .8) 


    glade_animals = []
    #GLADE
    #common
    glade_animals.append(Creature("Songbird", "small", "winged", "common"))
    glade_animals.append(Creature("Squirrel", "small", "quick-footed", "common"))

    #uncommon
    glade_animals.append(Creature("Fox", "small", "quick-footed", "uncommon"))
    glade_animals.append(Creature("Faun", "medium", "quick-footed", "uncommon"))

    #rare
    glade_animals.append(Creature("Stag", "medium", "strong", "rare"))

    glade = Region("Glade", glade_animals, .6) 

    return meadow, glade # understory, cave, 

main()