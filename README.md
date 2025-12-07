# THE BESTIARY

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: https://github.com/srinivasl1/pfda-final/

## Description
*The Bestiary* is a text-based open-world adventure/puzzle game, set in a fantastical medieval world. The story follows two children who sneak out of the royal castle for a day to explore the surrounding woods, discovering creatures to add to their personal bestiary. Along the way, they find clues to a greater mystery surrounding the castle, the queen, and the prince's mysterious illness.

This version is a demo, but the foundations for a full game are there. 

```project.py``` holds the main gameplay logic and written scenes. 

```region.py``` defines the Region class. Regions contain a set of unique areas and creatures, with an ascending difficulty for finding creatures the deeper into the map the player ventures.

```area.py``` defines the Area class. Areas contain navigational logic (tracking which other Areas they border), a list of all Puzzles in the Area, and descriptions of the Area.

```puzzle.py``` defines the Puzzle class. Puzzles contain descriptions for their three states: unsolved, solving, and solved. They also contain references to the Area they're in, and an easy reference to their is_solved state.

```creature.py``` defines the Creature class, allowing for easy storage of Creature names, types, regions, and rarity for display in the bestiary.

Designing a navigation system that felt robust was challenging, as was deciding how and where different Regions should border one another. For ease of putting together a demo, I decided on Regions that were split into 5 Areas - Center, North, East, South, and West. Regions would border one another only on their external Areas. However, fitting together a grid of different Regions would be very simple with the shape created by this approach.

With the existing framework it would be simple to add more Regions with more unique Creatures, more Puzzles that interconnect, and build on top of the story with more cutscene triggers. For now, I achieved my goal of demonstrating a few key features - open world navigation, an interactable beastiary menu, puzzles, cutscenes, and an appealing way to interact with the world within the game.