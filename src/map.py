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
            time.sleep(1)

            if map_choice == "1":
              while True:
                time.sleep(1)
                print("You travel to the dark forest. By the time you reach the\
 forest, the sun has set and everything is covered in darkness. You can’t see a thing\
  but you realize that you took your spell book and wand, which might have a spell on\
 creating light.")
                time.sleep(1)
                book = input("Do you use the spell book? Type 'y' to use the spell\
 book: ")
      
                if book == "y":
                    time.sleep(1)
                    print("You open your spell book and take out your wand, flipping to\
 the elements and light section. Which spell do you choose?")
                    time.sleep(1)
                    print("1) Flammae Raptura")
                    time.sleep(1)
                    print("2) Illuminus")
                    time.sleep(1)
                    print("3) Aqua Fluctus")
                    time.sleep(1)
                    print("4) Terrae")
                    time.sleep(1)
                    print("5) Ventus Fortis")
                    spell = input("Choose a spell: ")
                   
                    if spell == "2":
                      time.sleep(1)
                      print("You perform the spell titled “Illuminus”, which creates a\
  spark of light at the tip of your wand. You can now see much better than before.")
                      break
                    elif spell == "1":
                      time.sleep(1)
                      print("You perform the spell titled “Flammae Raptura”, which\
 creates a burst of flame at the tip of your wand instead of pure light. Incorrect\
 spell.Try again.")
                    elif spell == "3":
                      time.sleep(1)
                      print("You perform the spell titled “Aqua Fluctus”, which creates\
  an overwhelming amount of water and nearly floods the forest. Incorrect\
  spell. Try again.")
                    elif spell == "4":
                      time.sleep(1)
                      print("You perform the spell titled “Terrae”, which creates\
 many boulders, blocking your path. Incorrect spell. Try again.")
                    elif spell == "5":
                      time.sleep(1)
                      print("You perform the spell titled “Ventus Fortis”, which\
 creates creates a gust of wind. Incorrect spell. Try again.")
            
                    else:
                      time.sleep(1)
                      print("You must choose a spell. Please choose one from the list.")

          
            elif map_choice == "4":
                time.sleep(1)
                print("You cannot travel to Esmeralda’s castle until you collect all ten\
  items. Pick a different location.")

            else:
                time.sleep(1)
                print("Invalid choice. Please choose a valid location.")
                continue
