from creature import Creature
from region import Region

import time

def main():

    global bestiary
    bestiary = []
    
    global meadow, glade

    global delay
    delay = None

    meadow, glade = setup()

    while (delay == None):
        ans = input("Would you like to play with text delays between lines? (Recommended) (Y/N) > ").strip().upper()
        if ans == "Y":
            delay = True
        elif ans == "N":
            delay = False
        else:
            print("Invalid input! Please try again.")
            

    intro()

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

    """

    choice = input("Open bestiary? Y/N > ").strip().upper()
    if choice == "Y":
        navigate_bestiary(bestiary)
    elif choice == "N":
        print("ok then")
    else:
        print("Invalid input!")

    """

def navigate_bestiary():
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
    meadow_animals.append(Creature("Mouse", "tiny", "burrowers", "common", "meadow"))
    meadow_animals.append(Creature("Hare", "small", "quick-footed", "common", "meadow"))

    #uncommon
    meadow_animals.append(Creature("Snake", "small", "burrowers", "uncommon", "meadow"))
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
    

    print("MEADOW\n--==*==--\n")
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
                  "Weld: \"Ingram, we HAVE to go down to the forest!\""]
    
    for line in exit_convo:
        print(line)
        if delay:
            time.sleep(2.0)
    

main()