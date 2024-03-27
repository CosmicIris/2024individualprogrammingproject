import time

class Map:
    def map_choice(self):
        while True:
            time.sleep(1)
            print("Before you leave, the scribe tells you that you need to find ten items\
  to break the spell: five eagle’s wings, three dragon eggs, one unicorn horn, and snake\
  venom. He also hands you a map with four locations on it: the forest, a cave, a small\
hut, and Esmeralda’s castle. Where do you travel to first?")
            time.sleep(1)
            print("1) the dark forest")
            time.sleep(1)
            print("2) the cave")
            time.sleep(1)
            print("3) the small hut")
            time.sleep(1)
            print("4) Esmeralda’s castle")
            map_choice = input("Choose a location: ")

            if map_choice == "1":
                time.sleep(1)
                print("You travel to the dark forest. By the time you reach the\
  forest, the sun has set and everything is covered in darkness. You can’t see a thing\
  but realized that you took your spell book, which might have a spell on creating\
  light.")
                book = input("Do you use the spell book? Type 'y' to use the spell\
 book: ")
                if book == "y":
                    time.sleep(1)
                    print("You open the spellbook.")
                    break

            elif map_choice == "4":
                time.sleep(1)
                print("You cannot travel to Esmeralda’s castle until you collect all ten\
  items. Pick a different location.")

            else:
                time.sleep(1)
                print("Invalid choice. Please choose a valid location.")
                continue
