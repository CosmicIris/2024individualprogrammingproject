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
      if light == "1":
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
     
      elif light == "2":
        time.sleep(1)
        print("You perform the spell titled “Illuminus”, which creates a\
spark of light at the tip of your wand. You can now see much better\
    than before.")
        print("As you are walking through the cave, you notice that the floor of the\
        cave is covered in shiny red jewels. Do you pick them up?")
        time.sleep(1)
        jewels = input("Type 'y' to pick them up or 'n' to not pick them up:")
        if jewels == 'y':
          print("You pick them up, putting them in your satchel. As you do\
         this, a dragon that is sleeping in the cave wakes up and notices to\
         trying to steal the jewels, breathing fire in an attempt to kill\
         you. Luckily, you notice the dragon just before it burns you to a\
         crisp. You remember your task and try to think of a way to distract the\
         dragon in order to quickly grab three of its eggs. How do you\
         distract the dragon?")
        time.sleep(1)
        print("1) perform a spell that creates colorful fireworks")
        time.sleep(1)
        print("2)lure the dragon away from its eggs and attempt to sing it to sleep")
        time.sleep(1)
        print("3)create an illusion of yourself stealing the jewels and running away\
        while you making your actual body invisible")
        time.sleep(1)
      
        distraction = input("Choose a distraction:")

        if distraction == "1":
          time.sleep(1)
          print("You perform the spell, which distracts the dragon…for about five\
          seconds. Before you reach for the eggs, the firework show has ended and the\
          dragon returns its attention to you, slashing you and letting you slowly\
          bleed out until you die. Try again.")

        elif distraction == "2":
          time.sleep(1)
          print("You try to sing the dragon to sleep but fail horribly, as you have\
          a scratchy singing voice. Worse, the dragon hates your voice so much that it\
          decides to kill you by ripping out your heart. Try again.")
        elif distraction == "3":
          time.sleep(1)
          print("Fortunately, the illusion distracts the dragon long enough for you to\
      take three of its eggs and carefully put it into your satchel. With the eggs\
          secured, you quickly head out of the cave. The next place you must travel to\
  is the small hut. ")
          break
 


     
