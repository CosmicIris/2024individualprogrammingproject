import time
from cave import Cave
from forest import Forest
from hut import Hut

c2 = Cave()
f2 = Forest()
h1 = Hut()

class Map:
  def map_choice(self):
    while True:
      time.sleep(1)
      print("Before you leave, the scribe tells you that you need to find ten items\
 to break the spell: five eagle’s wings, three dragon eggs, one unicorn horn, and\
 snake venom. He also hands you a map with four locations on it: the forest, a cave, a\
 small hut, and Esmeralda’s castle, telling you that you must travel to each location\
 in a specific order. The first place you must travel to is the dark forest.")
      break
