from creature import Creature
from region import Region
from area import Area
from puzzle import Puzzle

import time

global current_region
global current_area

def main():

    global bestiary
    bestiary = []
    
    global meadow, glade

    meadow, glade = setup()
    
    global current_region
    current_region = meadow
    global current_area
    current_area = meadow.areas[0]

    global delay
    delay = None

    while (delay == None):
        ans = input("Would you like to play with text delays between lines? (Recommended) (Y/N) > ").strip().upper()
        if ans == "Y":
            delay = True
        elif ans == "N":
            delay = False
        else:
            print("Invalid input! Please try again.")
            

    intro()

    game()


def game():
    global current_region
    global current_area
    global meadow, glade
    regions_dict = {"Meadow":meadow, "Glade":glade}

    ans = ""
    while ans != "EXIT":
        print(f"\n{current_area.description}")

        borders = current_area.borders

        valid_directions = []

        for ix in range(len(borders)):
            if borders[ix] != "X":
                match ix:
                    case 0:
                        valid_directions.append("north")
                    case 1:
                        valid_directions.append("east")
                    case 2:
                        valid_directions.append("south")
                    case 3:
                        valid_directions.append("west")

        valid_dir_initials = [i[0].upper() for i in valid_directions]
        
        print(f"You may go {", ".join(valid_directions)}. ({" / ".join(valid_dir_initials)})")


        if len(current_area.puzzles) != 0: 
            for puzz in current_area.puzzles:
                if puzz.is_solved == False:
                    print(puzz.description)
                else:
                    print(puzz.solved)


        ans = input(" >>> ").strip().upper()

        if ans in ["N", "E", "S", "W"]:
            if ans not in valid_dir_initials:
                print("You cannot go that way.")
            else:
                currently_bordering = current_area.borders 
                match ans:
                    case "N":
                        current_region = regions_dict[currently_bordering[0][0]]
                        for i in current_region.areas:
                            if i.name == currently_bordering[0][1]:
                                current_area = i
                    case "E":
                        current_region = regions_dict[currently_bordering[1][0]]
                        for i in current_region.areas:
                            if i.name == currently_bordering[1][1]:
                                current_area = i
                    case "S":
                        current_region = regions_dict[currently_bordering[2][0]]
                        for i in current_region.areas:
                            if i.name == currently_bordering[2][1]:
                                current_area = i
                    case "W":
                        current_region = regions_dict[currently_bordering[3][0]]
                        for i in current_region.areas:
                            if i.name == currently_bordering[3][1]:
                                current_area = i
        elif ans == "C":
            if current_area.creatures == False:
                print("This doesn't seem like a good place to search for creatures.")
            else:
                attempt_find_creature()

        elif ans == "B":
            navigate_bestiary()

        elif ans == "H" or ans == "HELP":
            print("HELP MENU\n--==*==--\n" \
            "Navigate the world using the N / E / S / W keys.\n" \
            "To attempt to search for creatures in an area, use (C). Its easier to find creatures in some areas than others.\n" \
            "All the creatures you find will be added to Weld's bestiary. Use (B) to open the bestiary.\n" \
            "You can ask the creatures in Weld's bestiary for help with an area of interest. Just open the bestiary and use (H) to summon the creature on the current page.\n" \
            "This help menu can be accessed with (H) or (HELP).\n" \
            "At any time, enter (EXIT) to quit the game. Your progress will not be saved!\n")
            inp = ""
            while inp != "X":
                inp = input("Press (X) to continue >>> ").upper().strip()
        
        else:
            print("Invalid input!")
        



def attempt_find_creature():
    global current_area
    global current_region
    global meadow, glade

    success = current_region.find_creature()
    if success:
        found = current_region.random_creature()
        foundtext = ["Weld: \"There! I see one!\"",
                     "....",
                     f"Weld: \"It's a {found.name}!\""]

        for line in foundtext:
            print(line)
            if delay:
                time.sleep(2.0)

        bestiary.append(found)

        print(f"[{found.name} added to the Bestiary!]")
    else:
        foundtext = ["Weld: \"There! I think I see one!\"",
                     "....",
                     f"Weld: \"Aww.. it ran away.\""]
        
        for line in foundtext:
            print(line)
            if delay:
                time.sleep(2.0)
        
        print(f"[You didn't find anything.]")



            
def navigate_bestiary():
        global current_area
        global current_region
        page = 0
        toggle = ""
        while toggle != "X":
            bestiary[page].page_display()

            print(f"Viewing page {page + 1} of {len(bestiary)}")

            toggle = input("View next page (D), view previous page (A), or close bestiary (X). If you would like this animal's help, enter (H) to summon it > ").strip().upper()

            if toggle == "A" and page == 0:
                print("You are already on the first page!")
            elif toggle == "A":
                page -= 1
            elif toggle == "D" and page == len(bestiary) - 1:
                print("You are already on the last page!")
            elif toggle == "D":
                page += 1
            elif toggle == "H":
                toprint = [f"Ingram: \"I wish we had a {bestiary[page].name} here now to help us.\""]
                if len(current_area.puzzles) > 0:
                    toprint.append(f"Weld: \"...No way. Ingram, look!\"")
                    toprint.append(f"Weld: \"It's a {bestiary[page].name}, right there!\"")
                    toprint.append(f"Ingram: \"{bestiary[page].name}, could you do us a favor?\"")
                    toprint.append("...")
                    if (current_area.puzzles[0].answer_type == bestiary[page].type):
                        toprint.append(f"Ingram: \"It says it can!\"")
                        toprint.append(current_area.puzzles[0].solving)
                        
                    else:
                        toprint.append(f"Ingram:\"Aww, it says it wouldn't be of much use here. It's a {bestiary[page].type} creature, after all.\"")
                    
                else:
                    toprint.append(f"Weld: \"What's a creature supposed to help us with here, silly?\"")

                for line in toprint:
                        print(line)
                        if delay:
                            time.sleep(2.0)

                continue

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

    meadow_areas = []
    meadow_areas.append(Area("Grassy Knoll", "Meadow", "Tall grass glimmers with sunlight, swaying in the pleasant, warm breeze. The crest of the hill smooths into a valley towards the east. The royal palace rises up on the high cliffside to the west.", "C", 
                             [("Meadow","Abandoned Dens"),
                              ("Meadow","Orchard Valley"),
                              ("Meadow","Flower Field"),
                              ("Meadow","Castle Gates")]))
    meadow_areas.append(Area("Abandoned Dens", "Meadow", "The grass here is patchy and the earth is pocketed with small burrows. This may be a good place to search for creatures.", "N", 
                             ["X",
                              "X",
                              ("Meadow","Grassy Knoll"),
                              "X"],
                              has_creatures=True))
    meadow_areas.append(Area("Orchard Valley", "Meadow", "The grass slopes gently down towards the edge of the woods to the east. The valley is dotted with rows of apple trees, just beginning to flower.", "E", 
                             ["X",
                              ("Glade", "Bramble Patch"),
                              "X",
                              ("Meadow", "Grassy Knoll")]))
    meadow_areas.append(Area("Flower Field", "Meadow", "An expanse of colorful wildflowers stretches as far as the eye can see. The crest of the grassy meadow lays to the north.", "S",
                             [("Meadow", "Grassy Knoll"),
                              "X",
                              "X",
                              "X"]))
    meadow_areas.append(Area("Castle Gates", "Meadow", "The gates of the castle walls are 20 feet of cold, unforgiving steel and stone. \nIngram does not want to go back home.", "W",
                             ["X",
                              ("Meadow", "Grassy Knoll"),
                              "X",
                              "X"]))

    # meadow_areas = ["Grassy Knoll", "Abandoned Dens", "Orchard Valley", "Flower Field", "Castle Gates"]

    meadow = Region("Meadow", meadow_animals, .8, meadow_areas) 

    meadow.areas[1].puzzles = [Puzzle("dens", meadow, meadow.areas[1], "Weld:\"Do you think anything could be hiding in those burrows? Ooh, what if there's treasure?\"", "The creature begins to dig itself a new burrow, loose dirt flying through the air as it slips into the earth. In a moment, it returns with a key in its mouth. It deposits the slimey key in Ingram's hand.", "A fresh pile of loosed earth is the only sign of the creature you summoned.", "burrower")]

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

    glade_areas = []
    #glade_areas = ["Sunlit Clearing", "Mossy Slope", "Forest Creek", "Woodsman's Hut", "Bramble Patch"]
    glade_areas.append(Area("Sunlit Clearing", "Glade", "There's a gap in the forest canopy here, the clearing full of mid-morning sun. A thicket of brambles lays to the west, and the sounds of running water trickle from the east. You may have better luck finding creatures in more wooded areas.", "C",
                            [("Glade", "Mossy Slope"),
                             ("Glade", "Forest Creek"),
                             ("Glade", "Woodsman's Hut"),
                             ("Glade", "Bramble Patch")]))
    glade_areas.append(Area("Mossy Slope", "Glade", "A slope of boulders covered in slippery moss. Watch your footing here...", "N",
                            ["X",
                             "X",
                             ("Glade", "Sunlit Clearing"),
                             "X"]))
    glade_areas.append(Area("Forest Creek", "Glade", "A creek trickles through a rocky bed, filling the air with the rich smell of mud. Songbirds sing back and forth to one another overhead.", "E",
                            ["X",
                             "X",
                             "X",
                             ("Glade", "Sunlit Clearing")],
                            has_creatures=True))
    glade_areas.append(Area("Woodsman's Hut", "Glade", "Almost hidden in the trees is a small wooden shack. An axe is still wedged in a wide tree stump nearby, and a pile of firewood leans against one of the walls.", "S",
                            [("Glade", "Sunlit Clearing"),
                             "X",
                             "X",
                             "X"]))
    glade_areas.append(Area("Bramble Patch", "Glade", "At the edge of the woods, a thicket of blackberry brambles grows wild - bound to scratch up anyone who enters the woods, but also likely hiding critters under the brambles. The hills of the meadow rise up to the west.", "W",
                            ["X",
                             ("Glade", "Sunlit Clearing"),
                             "X",
                             ("Meadow","Orchard Valley")],
                            has_creatures=True))


    glade = Region("Glade", glade_animals, .6, glade_areas) 


    return meadow, glade # understory, cave, 

def intro():
    print(rf"""

                    __________________   __________________
                .-/|                  \ /                  |\-.
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||{"THE".center(19)}|{"A text".center(19)}||||
                ||||{"BESTIARY".center(19)}|{"adventure by".center(19)}||||
                ||||{"--==*==--".center(19)}|{"LAYA SRINIVAS".center(19)}||||
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||                   |                   ||||
                ||||__________________ | __________________||||
                ||/===================\|/===================\||
                `--------------------~___~-------------------''

        """)
    
    print("[Type (H) or (HELP) at any time for a list of commands.]")
    time.sleep(2.0)
    print("\n MEADOW\n--==*==--\n")
    time.sleep(2.0)

    """
    
    ingram_intro = ["Ingram: \"Weld.\"",
                      "...",
                      "Ingram: \"Weld!\"",
                      "Ingram: \"I don't like it here! I want to go back.\""]
    
    for line in ingram_intro:
        print(line)
        if delay:
            time.sleep(2.0)

    intro_convo = ["Weld: \"What? We've barely left the castle!\"",
                   "Ingram: \"I said, I don't like it. The grass is all... wet. It's making my shoes all muddy.\"",
                   "Weld: \"That's only the morning dew, silly. Anyways, a little mud might be good for you.\"",
                   "Weld: \"We haven't even seen a single animal yet!\"",
                   "Weld: \"Didn't you want to see them for yourself?\"",
                   "Ingram: \"I liked looking at the pictures. Inside the castle.\"",
                   "Weld: \"Scribe Fedwren says it isn't right for a boy your age to stay indoors all the time.\"",
                   "Weld: \"He says some fresh air would be leagues better off for your health than to be shut inside like an invalid.\"",
                   "Weld: \"...He also said not to repeat his words to anyone.\"",
                   "...",
                   "Weld: \"What's that, in the grass there? Did you hear that?\"",
                   "Weld: \"I hear something rustling! Come on, follow me, quietly!\""]
    
    for line in intro_convo:
        print(line)
        if delay:
            time.sleep(2.0)

    """

    ans = ""
    while ans != "C":
        ans = input("[[ To search for a creature in the area, enter (C). ]] > ").strip().upper()

    found = meadow.random_creature()
    bestiary.append(found)

    """

    for c in ['.','.','.','.','.']:
        print(c)
        time.sleep(0.5)

    catch_convo = ["Ingram: \"...What is that?!\"",
                   f"Weld: \"It's only a {found.name}! Look!\"",
                   "Ingram: \"AAGH! Stop, don't bring it any closer!\"",
                   f"Weld: \"Come here, little {found.name}, give Ingram a niiiice big kiss!\"",
                   "Ingram: \"AAAAAGH!\""]
    
    if found.rarity == "uncommon":
        catch_convo[1] == "Weld: \"Wow, we found a {found.name}! Look!\""
    elif found.rarity == "rare":
        catch_convo[1] == "Weld: \"Woaaah, no way! It's a {found.name}! Look!\""

    for line in catch_convo:
        print(line)
        if delay:
            time.sleep(2.0)

    bestiary_convo = ["...",
                      "Weld: \"Aww, he ran away.\"",
                      f"Weld: \"It's okay, little {found.name}. Hold still just a second...\"",
                      "Weld: \"There! I knew it was a good idea to bring my book and pen!\"",
                      "Weld: \"I want to start my own bestiary, just like Scribe Fedwren's.\"",
                      "Weld: \"But it'll be even better, because the two of us will work on it together!\"",
                      "Ingram: \"Isn't it odd that a scribe's apprentice can't write?\"",
                      "Weld: \"I CAN! I can write! I just don't like to very much.\"",
                      "Weld: \"So I'll draw the pictures, and you write the entries!\"",
                      "...",
                      "[[ TUTORIAL ]]",
                      "Weld: \"...Alright, done with my drawing!\"",
                      f"Weld: \"Now take this, and write {found.name} right at the top.\"",
                      f"Weld: \"Scribe Fedwren will also write a description of the animal in his bestiary.\"",
                      f"Weld: \"This one is {found.size}, and they tend to be {found.type}.\"",
                      f"Weld: \"They're also pretty {found.rarity} around here! Let's write that down too.\"",
                      "Weld: \"...Okay, I think that's everything.\"",
                      "Weld: \"Wow, look! Our first bestiary entry!\""]
    
    for line in bestiary_convo:
        print(line)
        if delay:
            time.sleep(2.0)

    ans = ""
    while ans != "B":
        ans = input("[[ To open the Bestiary and view entries, enter 'B' ]] > ").strip().upper()
    
    navigate_bestiary()

    

    exit_convo = ["Ingram: \"...\"",
                  "Ingram: \"I want to see more creatures like that.\"",
                  "Weld: \"Come on, I bet we'll find more around here!\"",
                  "Weld: \"We might even see some bigger ones down in the forest...\"",
                  "Weld: \"*GASP*... We might even see a baby deer!\"",
                  "Weld: \"Ingram, we HAVE to go down to the forest!\"",
                  "Weld: \"Let's go! Lead the way!\""]
    
    for line in exit_convo:
        print(line)
        if delay:
            time.sleep(2.0)
    
    """

main()