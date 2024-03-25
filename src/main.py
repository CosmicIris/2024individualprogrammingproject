from food import Food
import time 

f1 = Food()

print("Welcome to Enchanter's Curse! This is a text-based adventure game. To choose\
 certain choices throughout the game, type the number of the choice you want to\
 make. That is all for the instructions. Have fun!")
time.sleep(1.5)
print("You live in Saiviel Kingdom. You are at your home tending to your crops, when\
 you notice a small group of them are starting to wither. At first, you do not\
 think much of it, however, you notice that your neighbor’s crops are failing as well.\
 Suddenly, you hear a trumpet blow in the village square. You, along with many others,\
 arrive at the village square and discover thata scribe has appeared and is standing in\
 the center. The scribe informings you personally that a curse has been placed\
 upon all of the crops in the kingdom by an enchanter named Esmeralda, and that, as\
 a master sorcerer, it is your duty to lift the curse before she takes over\
 and rules the kingdom.")
while True:
  time.sleep(2)
  key = input('Do you accept the challenge? Type "y" to accept.')
  if key == "y":
    f1.food_choice()
   
