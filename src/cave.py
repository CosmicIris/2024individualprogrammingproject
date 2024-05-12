import time
class Cave:
  def GoToCave(self):
    while True:
      time.sleep(1)
      print(
      "You travel to the cave. The cave is very dark, so you decide to\
 open your spell book to create light. Which spell do you choose?")
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
      time.sleep(1)
      light = input("Choose a spell: ")

      if light == "2":
        time.sleep(1)
        print("You perform the spell titled “Illuminus”, which creates a\
spark of light at the tip of your wand. You can now see much better\
    than before.")
        print("You pick them up, putting them in your satchel. As you do\
         this, a dragon that is sleeping in the cave wakes up and notices to\
         trying to steal the jewels, breathing fire in an attempt to kill\
         you. Luckily, you notice the dragon just before it burns you to a\
         crisp. You remember your task and try to think of a way to distract the\
         dragon in order to quickly grab three of its eggs. How do you\
         distract the dragon?")

      elif light == "1":
        time.sleep(1)
        print("You perform the spell titled “Flammae Raptura”, which\
creates a burst of flame at the tip of your wand instead of pure light. Incorrect\
       spell. Try again.")

      elif light == "3":
        time.sleep(1)
        print("You perform the spell titled “Aqua Fluctus”, which creates\
an overwhelming amount of water and nearly floods the forest. Incorrect\
        spell. Try again.")
      elif light == "4":
        time.sleep(1)
        print("You perform the spell titled “Terrae”, which creates\
many boulders, blocking your path. Incorrect spell. Try again.")
      elif light == "5":
        time.sleep(1)
        print("You perform the spell titled “Ventus Fortis”, which\
creates creates a gust of wind. Incorrect spell. Try again.")
      else:
        time.sleep(1)
      print("You must choose a spell. Please choose one from the list.")


