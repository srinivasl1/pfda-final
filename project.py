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
    
    global meadow, glade, cave

    meadow, glade, cave = setup()
    
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
    global meadow, glade, cave
    regions_dict = {"Meadow":meadow, "Glade":glade, "Cave":cave}

    cutscene_status = {"five_creatures":False, "found_scarf":False, "found_prison":False}

    ans = ""
    while ans != "EXIT":
        if (len(bestiary) >= 5 and cutscene_status["five_creatures"] == False):
            five_creatures_cutscene()
            cutscene_status["five_creatures"] = True
            continue

        if (glade.areas[2].puzzles[0].is_solved == True and cutscene_status["found_scarf"] == False):
            found_scarf_cutscene()
            cutscene_status["found_scarf"] = True
            continue

        if (cave.areas[1].puzzles[0].is_solved == True and cutscene_status["found_prison"] == False and current_area.name != "Stone Prison"):
            found_prison_cutscene()
            cutscene_status["found_prison"] = True
            continue
        
        
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
                    print(f"\n{puzz.description}")
                else:
                    print(f"\n{puzz.solved}")


        ans = input(" >>> ").strip().upper()

        new_region = ""
        new_area = ""

        if ans in ["N", "E", "S", "W"]:
            if ans not in valid_dir_initials:
                print("You cannot go that way.")
            else:
                currently_bordering = current_area.borders 
                match ans:
                    case "N":
                        new_region = regions_dict[currently_bordering[0][0]]
                        for i in new_region.areas:
                            if i.name == currently_bordering[0][1]:
                                new_area = i
                    case "E":
                        new_region = regions_dict[currently_bordering[1][0]]
                        for i in new_region.areas:
                            if i.name == currently_bordering[1][1]:
                                new_area = i
                    case "S":
                        new_region = regions_dict[currently_bordering[2][0]]
                        for i in new_region.areas:
                            if i.name == currently_bordering[2][1]:
                                new_area = i
                    case "W":
                        new_region = regions_dict[currently_bordering[3][0]]
                        for i in new_region.areas:
                            if i.name == currently_bordering[3][1]:
                                new_area = i
                
                if new_area.name == "Mossy Slope" and current_area.name == "Sunlit Clearing":
                    print(f"\n{new_area.description}")

                    fall_text = ["\nIngram: \"What is this, growing on the rocks?\"",
                     "Weld: \"It's moss! Isn't it lovely?\"",
                     "Weld: \"But it's quite a fall from here, so watch your step, or - AAH!\"",
                     "Weld: \"Oh no! I dropped my pen!\"",
                     "Weld: \"It's just down there... maybe if I just... reaaachh.......\"",
                     "Weld: \"AAAAH!!\"",
                     "Ingram: \"Weld?! WELD! Where did you go?!\"",
                     "Ingram: \"...Don't leave me up here!\"",
                     "Ingram: \".....Weld?\"",
                     "...."]
                    
                    
                    for line in fall_text:
                        print(line)
                        if delay:
                            time.sleep(2.0)

                    print(f"\nYou are now entering THE CAVE.")

                    current_region = cave
                    current_area = cave.areas[3]
                    continue

                if new_area.name == "Bramble Patch" and glade.areas[3].puzzles[0].is_solved == True and glade.areas[4].puzzles[0].is_solved == False:
                    glade.areas[4].puzzles[0].is_solved = True
                    print(glade.areas[4].puzzles[0].solving)

                if new_area.name == "Stone Prison" and meadow.areas[1].puzzles[0].is_solved == True and cave.areas[1].puzzles[0].is_solved == False:
                    cave.areas[1].puzzles[0].is_solved = True
                    print(cave.areas[1].puzzles[0].solving)


                if new_region != current_region:
                    print(f"\nYou are now entering THE {new_region.name.upper()}")
                current_region = new_region
                current_area = new_area

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


        if found not in bestiary:
            bestiary.append(found)
            print(f"[{found.name} added to the Bestiary!]")
        else:
            print(f"[{found.name} is already in the Bestiary!]")

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

                    if (current_area.puzzles[0].is_solved == True):
                         toprint.append(f"Ingram: \"It says we've already received all the help it can give in this area.\"")

                    elif (current_area.puzzles[0].answer_type == bestiary[page].type):
                        toprint.append(f"Ingram: \"It says it can!\"")
                        toprint.append(current_area.puzzles[0].solving)
                        current_area.puzzles[0].is_solved = True
                        
                    else:
                        toprint.append(f"Ingram:\"Aww, it says it wouldn't be of much use here. It's a {bestiary[page].type} creature, after all.\"")
                    
                else:
                    toprint.append(f"Weld: \"What's a creature supposed to help us with here, silly?\"")

                for line in toprint:
                        print(line)
                        if delay:
                            time.sleep(2.0)

                toggle == "X"
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

    meadow.areas[1].puzzles = [Puzzle("dens", meadow, meadow.areas[1], "Weld: \"Do you think anything could be hiding in those burrows? Ooh, what if there's treasure?\"", "The creature begins to dig itself a new burrow, loose dirt flying through the air as it slips into the earth. In a moment, it returns with a key in its mouth. It deposits the slimey key in Ingram's hand.", "A fresh pile of loosed earth is the only sign of the creature you summoned.", "burrower")]

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
    glade_areas.append(Area("Woodsman's Hut", "Glade", "Almost hidden amidst the trees is a small wooden shack. A flat stump nearby bears the aged marks of an axe's blade, pile of firewood leans against one of the walls. Wherever the woodsman's axe is, though, it's not here.", "S",
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

    glade.areas[2].puzzles = [Puzzle("tree", glade, glade.areas[2], "Something flutters from a tree branch overhead, but it's too far up to see what it is, much less to reach.", "The creature flits up into the foliage and out of sight. A moment, then two, and it returns with the item in the trees - a long silk scarf of fabric, in mourning black.\nIngram: \"...This is my mother's.\"\n", "The queen's black scarf was stuck in the trees - she must have been here at some point.", "winged")]
    glade.areas[3].puzzles = [Puzzle("shed", glade, glade.areas[3], "Ingram: \"This door won't budge. It's all warped in the doorframe. Could we break it open somehow?\"", "The creature takes a few steps back, then barrels right at the shed door. With a loud SLAM, it breaks through the old wood! The creature shakes its head clear of the splinters, then trots off into the trees. Inside the shed, on a narrow workbench, is the woodsman's axe. Weld hefts it in both hands with a grin.", "The door to the little shed is now smashed open. Weld has already taken the axe.", "strong")]
    glade.areas[4].puzzles = [Puzzle("log", glade, glade.areas[4], "Amidst the brambles is a tall, splintered stump with a gnarled crack in the center. It seems hollow inside, but the crack is too small to fit your hand through.", "Weld hoists her axe, staggering backward briefly under the weight. Then she heaves it over her head, and with a splintering CRACK, the hollow stump splits open. Inside is a gold ring with a black stone. Weld gasps, dropping the axe to grab the ring.", "The stump Weld broke open is now splintered and empty.", "none")]

    cave_animals = []

    #CAVE
    #common
    cave_animals.append(Creature("Bat", "small", "winged", "common", "cave"))
    cave_animals.append(Creature("Cricket", "tiny", "quick-footed", "common", "cave"))

    #uncommon
    cave_animals.append(Creature("Mole", "small", "burrower", "uncommon", "cave"))
    cave_animals.append(Creature("Salamander", "medium", "quick-footed", "uncommon", "cave"))

    #rare
    cave_animals.append(Creature("Bear", "medium", "strong", "rare", "cave"))


    cave_areas = []
    
    cave_areas.append(Area("Underground Pool", "Cave", "A wide cavern opens up ahead, scattered light dancing across every surface. A pool glitters in the center of the cave, gleaming in a few stray beams of sunlight from overhead. Narrow passages delve further into the cave to the north, east, and west.", "C",
                            [("Cave", "Stone Prison"),
                             ("Cave", "Bear Den"),
                             ("Cave", "Cave Mouth"),
                             ("Cave", "Mushroom Cavern")]))
    cave_areas.append(Area("Stone Prison", "Cave", "The shadowy passage north is lined with hairline cracks through the stone. Large iron bars are set into the wall of rock ahead of you - creating a prison cell of the cavern. \nIngram: \"What is this place...?\"\n", "N",
                            ["X",
                             "X",
                             ("Cave", "Underground Pool"),
                             "X"]))
    cave_areas.append(Area("Bear Den", "Cave", "The air here is musky with the smell of fur. The passage quickly darkens, until the cavern ahead is almost pitch black. In the near silence... a sound like snoring comes from ahead. Best to tread quietly.", "E",
                            ["X",
                             "X",
                             "X",
                             ("Cave", "Underground Pool")],
                            has_creatures=True))
    cave_areas.append(Area("Cave Mouth", "Cave", "The maw of a forest cave opens up ahead, its rocky surface blanketed in slick moss and tall ferns. Daylight ripples across its stone walls, reflected from some pool of water ahead.", "S",
                            [("Cave", "Underground Pool"),
                             "X",
                             ("Glade", "Mossy Slope"),
                             "X"]))
    cave_areas.append(Area("Mushroom Cavern", "Cave", "This cavern is full of daylight and smells richly of damp earth and growing things. Fungi of strange shapes and colors grow on rocky outcroppings, creating the image of a small forest.", "W",
                            ["X",
                             ("Cave", "Underground Pool"),
                             "X",
                             "X"],
                            has_creatures=True))


    cave = Region("Cave", cave_animals, .4, cave_areas) 

    cave.areas[1].puzzles = [Puzzle("tree", cave, cave.areas[1], "The cell is fastened shut by a massive iron lock. It's too dark to see much further into the cell...", "Ingram: \"I have this key from the dens in the field. I think it will fit.\"\nWeld: \"Are you sure we should...? I don't like this place...\"\n.....\nThe key fits the lock, and the cell door groans as it swings open.", "The cell is empty, but the stone walls are scored with deep gouge marks from massive claws. They're layered atop one another, as if something had been trapped here a long time.", "none")]

    return meadow, glade, cave # understory, cave, 

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



    ans = ""
    while ans != "C":
        ans = input("[[ To search for a creature in the area, enter (C). ]] > ").strip().upper()

    found = meadow.random_creature()
    bestiary.append(found)



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
    


def five_creatures_cutscene():
    dialogue = ["\nWeld: \"Five whole entries in the bestiary!\"",
                "Weld: \"I can't wait to show Scribe Fedwren... he'll love these drawings!\"",
                "Weld: \"I guess we should head back now, though...\"",
                "Ingram: \"No!\"",
                "Ingram: \"...I want to keep exploring.\"",
                "Weld: \"The queen might worry. But you've hardly been coughing all morning!\"",
                "Weld: \"What is it you're sick with, anyways?\"",
                "Ingram: \"...I'm not sick.\"",
                "Weld: \"Come onnnn, you can tell.\"",
                "Weld: \"Is it flu? Pox? Oh, I hated the pox.\"",
                "Ingram: \"I'm in poor health. I'm fragile. I'm sensitive to the sun, and to cold winds.\"",
                "Ingram: \"...I've always been this way.\"",
                "Weld: \"But look at you! You're in the sun and wind right now!\"",
                "Weld: \"I didn't like the look of you in the castle. You were all hollow and sickly looking.\"",
                "Weld: \"But out here you look strong! Like a boy who climbs trees and catches hares!\"",
                "Ingram: \"...I do?\""]
    
    for line in dialogue:
        print(line)
        if delay:
            time.sleep(2.0)


def found_scarf_cutscene():
    dialogue = ["\nWeld: \"...Do you really think that black scarf is the queen's?\"",
                "Ingram: \"It must be.\"",
                "Ingram: \"She's the only one who still dresses in black.\"",
                "Weld: \"What was she doing out here?\"",
                "Ingram: \"I don't know. She always says these woods are too dangerous to wander alone.\"",
                "Ingram: \"I hope she wasn't alone.\""]

    for line in dialogue:
        print(line)
        if delay:
            time.sleep(2.0)

def found_prison_cutscene():
    dialogue = ["\nWeld: \"That prison was really creepy.\"",
                "Weld: \"Did you see those claw marks in the walls? What could've made them?\"",
                "Weld: \"Do you think it's a huge creature?!\"",
                "Weld: \"Maybe we can add it to the bestiary!\"",
                "Ingram: \"....\"",
                "Ingram: \"I don't like the idea that my mother was here.\"",
                "Ingram: \"What if that creature in the prison chased her? Or hurt her?\"",
                "Weld: \"But we just saw the queen when we were the castle this morning, right?\"",
                "Weld: \"She seemed fine to me.\"",
                "Ingram: \"She's good at seeming fine.\"",
                "Ingram: \"She hides things.\""]
    
    for line in dialogue:
        print(line)
        if delay:
            time.sleep(2.0)

main()