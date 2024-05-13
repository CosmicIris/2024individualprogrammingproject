import time
from wizardfight import wizardFight
w1 = wizardFight()
class Hut:
  def GoToHut(self):
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
      w1.wizardFight()   
