from creature import Creature
from region import Region

def main():
    bestiary = []
    meadow, glade = setup()

    success = meadow.find_creature()
    if success:
        found = meadow.random_creature()
        print(found.name)
        bestiary.append(found)
    else:
        print("You didn't find anything!")

    success = meadow.find_creature()
    if success:
        found = meadow.random_creature()
        print(found.name)
        bestiary.append(found)
    else:
        print("You didn't find anything!")

    choice = input("Open bestiary? Y/N > ").strip().upper()
    if choice == "Y":
        navigate_bestiary(bestiary)
    elif choice == "N":
        print("ok then")
    else:
        print("Invalid input!")



def navigate_bestiary(bestiary):
        page = 0
        toggle = ""
        while toggle != "X":
            bestiary[page].page_display()

            print(f"Viewing page {page + 1} of {len(bestiary)}")

            toggle = input("View next page (D), view previous page (A), or close bestiary (X) > ").strip().upper()

            if toggle == "A" and page == 0:
                print("You are already on the first page!")
            elif toggle == "A":
                page -= 1
            elif toggle == "D" and page == len(bestiary) - 1:
                print("You are already on the last page!")
            elif toggle == "D":
                page += 1
            elif toggle == "X":
                continue
            else:
                print("Invalid input!")

    

def setup():
    meadow_animals = []

    #MEADOW
    #common
    meadow_animals.append(Creature("Mouse", "tiny", "burrower", "common", "meadow"))
    meadow_animals.append(Creature("Hare", "small", "quick-footed", "common", "meadow"))

    #uncommon
    meadow_animals.append(Creature("Snake", "small", "burrower", "uncommon", "meadow"))
    meadow_animals.append(Creature("Grasshopper", "tiny", "winged", "uncommon", "meadow"))

    #rare
    meadow_animals.append(Creature("Hawk", "medium", "winged", "rare", "meadow"))

    meadow = Region("Meadow", meadow_animals, .8) 


    glade_animals = []
    
    #GLADE
    #common
    glade_animals.append(Creature("Songbird", "small", "winged", "common", "glade"))
    glade_animals.append(Creature("Squirrel", "small", "quick-footed", "common", "glade"))

    #uncommon
    glade_animals.append(Creature("Fox", "small", "quick-footed", "uncommon", "glade"))
    glade_animals.append(Creature("Faun", "medium", "quick-footed", "uncommon", "glade"))

    #rare
    glade_animals.append(Creature("Stag", "medium", "strong", "rare", "glade"))

    glade = Region("Glade", glade_animals, .6) 

    return meadow, glade # understory, cave, 

main()