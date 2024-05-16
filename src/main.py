
from food import Food
from clothes import Clothes
from cave import Cave
from castle import Castle
from forest import Forest
from map import Map
from hut import Hut
from wizardfight import wizardFight
import time 

f1 = Food()
f2 = Forest()
c1 = Clothes()
m1 = Map()
c2 = Cave()
w1 = wizardFight()
h1 = Hut()
c3 = Castle()


print("Welcome to Enchanter's Curse! This is a text-based adventure game. To choose\
 certain choices throughout the game, type the number of the choice you want to\
 make. Do not type anything extra, or else the game will take you back to the choice\
 you previously made. Type 'start' to start the game. That is all for the\
 instructions. Have fun!")

time.sleep(1)
start = input("Type 'start' to start the game: ")
if start == "start":
  time.sleep(1)
  print("You live in Saiviel Kingdom. You are at your home tending to your crops, when\
 you notice a small group of them are starting to wither. At first, you do not\
 think much of it, however, you notice that your neighbor’s crops are failing as well.\
 Suddenly, you hear a trumpet blow in the village square. You, along with many others,\
 arrive at the village square and discover that a scribe has appeared and is standing\
 in the center. The scribe informs you personally that a curse has been placed\
 upon all of the crops in the kingdom by an enchanter named Esmeralda, and that, as\
 a master sorcerer, it is your duty to lift the curse before she takes over\
 and rules the kingdom.")
while True:
  time.sleep(1)
  key = input('Do you accept the challenge? Type "y" to accept: ')
  if key == "y":
    f1.food_choice()
    c1.clothes_choice()
    m1.map_choice()
    f2.GoToForest()
    c2.GoToCave()
    h1.GoToHut()
    w1.wizardFight() 
    c3.GoToCastle()
  else:
    time.sleep(2)
    print("A month after you refused to accept the challenge, all of the crops in the\
  kingdom died. With no way of reviving them or planting more, Esmeralda takes over\
 as the new ruler. Great job. You failed to protect the kingdom and you are a\
 dissappointment to everyone.")

 
   
