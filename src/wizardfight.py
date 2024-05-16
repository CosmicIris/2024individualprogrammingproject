import time
import random

class wizardFight:
  
  def __init__(self):
      self.wizardhealth = 70
      self.attacks = ["earthquake", "frost nova", "shadow strike"]
      self.playerhealth = 100

   
  def wizardFight(self):
    while self.wizardhealth > 15:
      if self.playerhealth <= 15:
        print("Your health is too low. Restarting the fight...")
        self.playerhealth = 100  
        self.enchanterhealth = 70
        continue
        
      print("Choose a spell to attack the wizard with from the list below:")
      time.sleep(1)
      print("1) Fireball: Creates a ball of fire that flies towards the target, dealing\
 fire damage on impact and draining the opponent’s health by 7 points")
      time.sleep(1)
      print("2) Shadow Bolt: Unleashes a bolt of dark energy at the target, dealing\
 necrotic damage and draining the opponent’s health by 15 points")
      time.sleep(1)
      print("3) Ice Shards: Summons a sharp shard of ice to hurl at the target, causing\
 cold damage and draining the opponent’s health by 10 points and slowing the\
 opponent's movements")
      time.sleep(1)
     
      attack_spell_choice = input("Spell Choice: ")
      
      if attack_spell_choice == "1":
        print("You cast a fireball at the wizard, dealing 7 damage to him.")
        self.wizardhealth -= 7
        print("The wizard's health is now", self.wizardhealth)
        attack_name = random.choice(self.attacks)
        print(f"The wizard casts {attack_name}.")
        
        if attack_name == "earthquake":
          self.playerhealth -= 5
          print("The wizard's earthquake attack deals 5 damage to you.")
          print("Your health is now", self.playerhealth)
          continue
        
        elif attack_name == "frost nova":
          self.playerhealth -= 7
          print("The wizard's frost nova attack deals 7 damage to you.")
          print("Your health is now", self.playerhealth)
          continue
          
        elif attack_name == "shadow strike":
          self.playerhealth -= 10
        print("The wizard's frost nova attack deals 10 damage to you.")
        print("Your health is now", self.playerhealth)
        continue


      
      elif attack_spell_choice == "2":
        print("You cast a shadow bolt at the wizard, dealing 15 damage to him.")
        self.wizardhealth -= 15
        print("The wizard's health is now", self.wizardhealth)
        attack_name = random.choice(self.attacks)
        print(f"The wizard casts {attack_name}.")

        if attack_name == "earthquake":
          self.playerhealth -= 5
          print("The wizard's earthquake attack deals 5 damage to you.")
          print("Your health is now", self.playerhealth)
          continue

        elif attack_name == "frost nova":
          self.playerhealth -= 7
          print("The wizard's frost nova attack deals 7 damage to you.")
          print("Your health is now", self.playerhealth)
          continue

        elif attack_name == "shadow strike":
          self.playerhealth -= 10
          print("The wizard's frost nova attack deals 10 damage to you.")
          print("Your health is now", self.playerhealth)
          continue


      elif attack_spell_choice == "3":
        print("You cast ice shards at the wizard, dealing 10 damage to him.")
        self.wizardhealth -= 10
        print("The wizard's health is now", self.wizardhealth)
        attack_name = random.choice(self.attacks)
        print(f"The wizard casts {attack_name}.")

        if attack_name == "earthquake":
          self.playerhealth -= 5
          print("The wizard's earthquake attack deals 5 damage to you.")
          print("Your health is now", self.playerhealth)
          continue

        elif attack_name == "frost nova":
          self.playerhealth -= 7
          print("The wizard's frost nova attack deals 7 damage to you.")
          print("Your health is now", self.playerhealth)
          continue

        elif attack_name == "shadow strike":
          self.playerhealth -= 10
        print("The wizard's shadow strike deals 10 damage to you.")
        print("Your health is now", self.playerhealth)
       
      if self.playerhealth == 0:
          print("You have been defeated. Try again.")
          continue
        
    else:
      print("You defeat the wizard. As promised, he gives you the unicorn\
  horn. The final place you must travel to is Esmeralda’s castle.")
    time.sleep(1)
    print("You finally reach Esmeralda's castle. Upon entering, Esmeralda tells\
you that she's been expecting you. She tells you that she was aware you were chosen\
  to save the kindgdom from the curse.'The final step in breaking my curse is\
  to cast a spell using all the items you've collected. However, I will not give you\
  the instructions for casting this spell freely. You must fight me for it, and if you\
  win, I will give you the spell. If you lose, the curse will take over completely and\
  I will become the new ruler.'")
    time.sleep(1)
    print("Instructions: Similarly to the fight with the wizard, the object of this\
  fight will be to decrease Esmeralda's health to 15. The fight\
will begin with you choosing a spell from the available options. Certain spells will\
  deteriorate Esmeralda's health by a certain amount. However, Esmeralda's attacks\
  could damage your health more than it damages her's. If your health reaches 15, the\
  fight will be over and you will have to restart the fight. That is all for the\
  instructions. Good luck. (P.S: If you thought that this would be similar to\
  the wizard's fight and that it would be easy to defeat the enchanter, you are\
  wrong. The enchanter is much more powerful than the wizard. Choose your spells\
 wisely.)")
      
    
       
          






