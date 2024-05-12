import time
from wizardfight import wizardFight
from cave import Cave
c2 = Cave()

class Map:

  def map_choice(self):
    while True:
      time.sleep(1)
      print(
          "Before you leave, the scribe tells you that you need to find ten items\
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
      time.sleep(1)
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
            print(
                "You open your spell book and take out your wand, flipping to\
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
  spark of light at the tip of your wand. You can now see much better than before."
                    )
              time.sleep(1)
              wings = input("As you are walking through the forest, you find\
  four eagle’s wings lying on the floor. Do you pick them up? Type 'y' to pick\
 them up:")
              if wings == "y":
                time.sleep(1)
                items = 4
                print("You pick them up, putting them in your satchel for safe\
  keeping. You continue walking though the forest until you reach the end. Where do you\
  travel to next?")
              break
            elif spell == "1":
              time.sleep(1)
              print("You perform the spell titled “Flammae Raptura”, which\
 creates a burst of flame at the tip of your wand instead of pure light. Incorrect\
 spell.Try again.")
            elif spell == "3":
              time.sleep(1)
              print(
                  "You perform the spell titled “Aqua Fluctus”, which creates\
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
              print(
                  "You must choose a spell. Please choose one from the list.")

      elif map_choice == "2":
       c2.GoToCave()
      elif map_choice == "3":
        while True:
          time.sleep(1)
          print('You travel to the small hut. Upon arriving, you politely\
  knock on the door of the hut. An old wizard answers. “What can I do for you?” he\
  asks. You explain to him that you were tasked with breaking the curse that has\
  been placed on the kingdom’s crops and were told he has a unicorn horn, which is\
needed to break it. “Ah. I see. If you wish to acquire the unicorn horn, you\
  must fight me first.”')
          wizard_fight = input("Do you fight the wizard? Type 'y' to fight\
 the wizard: ")
          if wizard_fight == "y": 
              time.sleep(1)
              print(
                'You decide to fight the wizard. Instructions: The objective of\
  this fight will be to decrease the wizard’s health to 15. The wizard’s health\
  will start at 70. The wizard will start the fight by casting a certain spell. You\
 will then choose a spell from the available options in response. Certain spells\
 will deteriorate the wizard’s health by a certain amount. However, some spells may\
 not be as effective and the wizard could end up damaging your health more than you\
 damage his. If your health reaches 0, the fight will be over and you will have to\
 restart the fight. That is all for the instructions. Good luck.')
          time.sleep(1)
          w1 = wizardFight()
          w1.fight()   
      

      elif map_choice == "4":
        time.sleep(1)
        print(
            "You cannot travel to Esmeralda’s castle until you collect all ten\
 items. Pick a different location.")
      else:
        time.sleep(1)
        print("Invalid choice. Please choose a valid location.")
        continue
