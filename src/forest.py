import time

class Forest:
  def GoToForest(self):
    while True:
      time.sleep(1)
      print("You travel to the dark forest. By the time you reach the\
 forest, the sun has set and everything is covered in darkness. You can’t see a\
 thing but you realize that you took your spell book and wand, which might have a\
 spell on creating light.")
      print("""
         /|
        .'|_________
       |            |
       |  Spells    |
       |            |
       |            |
       |            |
       |____________|
               """)
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
 spark of light at the tip of your wand. You can now see much better than before.")
          time.sleep(1)
          print("As you are walking through the forest, you find\
 four eagle’s wings lying on the floor.")
          print("""
              ( ‘ /\\
              ’=  \\/\\
               ’=  \\/\\
                  ’=\\/
                     \\
                    """)
          wings = input("Do you pick them up? Type 'y' to pick\
 them up: ")
          if wings == "y":
            time.sleep(1)
            print("You pick them up, putting them in your satchel for safe\
 keeping. You continue walking though the forest until you reach the end. The next\
 location you must travel to is the cave.")
            break
          elif wings == "n":
            time.sleep(1)
            second_guess = input("Are you sure? You might need them later.")
            if second_guess == "n":
             time.sleep(1)
             print("You pick them up, putting them in your satchel for safe\
              keeping. You continue walking though the forest until you reach the\
  end. The next location you must travel to is the cave.")
            
            elif second_guess == "y":
              time.sleep(1)
              print("Incorrect choice. As a reminder, you actually need them to break\
  the curse placed upon the kingdom. Try again.")
        
        elif spell == "1":
          time.sleep(1)
          print("You perform the spell titled “Flammae Raptura”, which creates fire\
 instead of pure light. Incorrect spell.Try again.")
        elif spell == "3":
          time.sleep(1)
          print("You perform the spell titled “Aqua Fluctus”, which creates\
 an overwhelming amount of water and nearly floods the forest. Incorrect spell. Try\
 again.")
        elif spell == "4":
          time.sleep(1)
          print("You perform the spell titled “Terrae”, which creates many boulders, \
 blocking your path. Incorrect spell. Try again.")
        elif spell == "5":
          time.sleep(1)
          print("You perform the spell titled “Ventus Fortis”, which creates a gust of\
  wind. Incorrect spell. Try again.")
        else:
          time.sleep(1)
          print("You must choose a valid spell.")
      elif book == "n":
        time.sleep(1)
        print("You decide to not use the spell book. You continue walking. Because you\
  do not have any source of light, you fail to notice that a bear is about to attack\
  you. The bear kills you instantly. Incorrect\
  choice. Try again.")
