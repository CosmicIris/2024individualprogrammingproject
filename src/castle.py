import time
import random

class Castle:
  def __init__(self):
    self.enchanterhealth = 80
    self.attacks = ["attacks", "dodges the spell", "cannot attack"]
    self.playerhealth = 100
    
  def GoToCastle(self):
    while self.enchanterhealth > 15:
      if self.playerhealth <= 15:
        print("Your health is too low. Restarting the fight...")
        self.playerhealth = 100  
        self.enchanterhealth = 80
        continue

      time.sleep(3)
      print("Choose a spell from the available options:")
      time.sleep(1)
      print("1) Fireball: Creates a ball of fire that flies towards the target, dealing\
  fire damage on impact and draining the opponent’s health by 9 points")
      time.sleep(1)
      print("2) Shadow Bolt: Unleashes a bolt of dark energy at the target, dealing\
  necrotic damage and draining the opponent’s health by 13 points")
      time.sleep(1)
      print("3) Ice Shards: Summons a sharp shard of ice to hurl at the\
  target, causing cold damage and draining the opponent’s health by 15 points and\
  slowing the opponent's movements")
      time.sleep(1)
      print("4) Earthquake: Shakes the ground beneath the opponent, knocking them off\
  their feet and draining the opponent's health by 8 points")
      time.sleep(1)
      print("5) Energy Drain: drains the energy of the opponent as well as their\
  health by 10 points")
      time.sleep(1)

      attack_spell_choice = input("Spell Choice: ")

      if attack_spell_choice == "1":
                print("You cast a fireball at Esmeralda.")
                attack_name = random.choice(self.attacks)
                print(f"Esmeralda {attack_name}.")

                if attack_name == "attacks":
                  self.playerhealth -= 10
                  self.enchanterhealth -= 9
                  time.sleep(1)
                  print("Esmeralda casts a tsunami spell, which reduces your health\
      by 10 points.")
                  time.sleep(1)
                  print("Your health is now", self.playerhealth)
                  time.sleep(1)
                  print("Esmeralda's health is now", self.enchanterhealth)
                  continue

                elif attack_name == "dodges the spell":
                  self.playerhealth -= 11
                  time.sleep(1)
                  print("Esmeralda dodges the attack and casts a tsunami spell towards\
  you, reducing your health by 11 points.")
                  time.sleep(1)
                  print("Your health is now", self.playerhealth)
                  time.sleep(1)
                  print("Esmeralda's health is now", self.enchanterhealth)
                  continue

                elif attack_name == "cannot attack":
                  time.sleep(1)
                  self.enchanterhealth -= 9
                print("Your attack is so powerful that Esmeralda temporarily cannot\
  cast a spell.")
                time.sleep(1)
                print("Your health is now", self.playerhealth)
                time.sleep(1)
                print("Esmeralda's health is now", self.enchanterhealth)
                continue

      elif attack_spell_choice == "2":
                print("You cast a shadow bolt at Esmeralda.")
                attack_name = random.choice(self.attacks)
                time.sleep(1)
                print(f"Esmeralda {attack_name}.")

                if attack_name == "attacks":
                  self.playerhealth -= 11
                  self.enchanterhealth -= 13
                  time.sleep(1)
                  print("Esmeralda attacks with a shadow wind spell, reducing your\
  health by 11 points.")
                  time.sleep(1)
                  print("Your health is now", self.playerhealth)
                  time.sleep(1)
                  print("Esmeralda's health is now", self.enchanterhealth)
                  continue

                elif attack_name == "dodges the spell":
                  self.playerhealth -= 10
                  time.sleep(1)
                  print("Esmeralda dodges the attack and casts a shadow wind spell\
  towards you, reducing your health by 10 points.")
                  time.sleep(1)
                  print("Your health is now", self.playerhealth)
                  time.sleep(1)
                  print("Esmeralda's health is now", self.enchanterhealth)
                  continue

                elif attack_name == "cannot attack":
                 time.sleep(1)
                 self.enchanterhealth -= 13
                 print("Your attack is so powerful that Esmeralda temporarily cannot\
  cast a spell.")
                 time.sleep(1)
                 print("Your health is now", self.playerhealth)
                 time.sleep(1)
                 print("Esmeralda's health is now", self.enchanterhealth)
                 continue

      elif attack_spell_choice == "3":
                    print("You cast ice shards at Esmeralda.")
                    attack_name = random.choice(self.attacks)
                    time.sleep(1)
                    print(f"Esmeralda {attack_name}.")

                    if attack_name == "attacks":
                      self.playerhealth -= 15
                      self.enchanterhealth -= 15
                      time.sleep(1)
                      print("Esmeralda attacks with a reflection spell, which reflects\
  the ice shards back to you and reduces your health\
  by 15 points.")
                      time.sleep(1)
                      print("Your health is now", self.playerhealth)
                      time.sleep(1)
                      print("Esmeralda's health is now", self.enchanterhealth)
                      continue

                    elif attack_name == "dodges the spell":
                      self.playerhealth -= 16
                      time.sleep(1)
                      print("Esmeralda dodges the attack and casts a frost nova spell\
  towards you, reducing your health by 16 points.")
                      time.sleep(1)
                      print("Your health is now", self.playerhealth)
                      time.sleep(1)
                      print("Esmeralda's health is now", self.enchanterhealth)
                      continue

                    elif attack_name == "cannot attack":
                     time.sleep(1)
                     self.enchanterhealth -= 15
                     print("Your attack is so powerful that Esmeralda temporarily\
  cannot cast a spell.")
                     time.sleep(1)
                     print("Your health is now", self.playerhealth)
                     time.sleep(1)
                     print("Esmeralda's health is now", self.enchanterhealth)
                    continue

      elif attack_spell_choice == "4":
                    print("You cast an earthquake spell at Esmeralda.")
                    attack_name = random.choice(self.attacks)
                    time.sleep(1)
                    print(f"Esmeralda {attack_name}.")

                    if attack_name == "attacks":
                      self.playerhealth -= 6
                      self.enchanterhealth -= 8
                      time.sleep(1)
                      print("Esmeralda attacks with a rock blast spell, reducing your\
  health by 6 points.")
                      time.sleep(1)
                      print("Your health is now", self.playerhealth)
                      time.sleep(1)
                      print("Esmeralda's health is now", self.enchanterhealth)
                      continue

                    elif attack_name == "dodges the spell":
                      self.playerhealth -= 7
                      time.sleep(1)
                      print("Esmeralda dodges the attack and casts a rock blast spell\
  towards you, reducing your health by 7 points.")
                      time.sleep(1)
                      print("Your health is now", self.playerhealth)
                      time.sleep(1)
                      print("Esmeralda's health is now", self.enchanterhealth)
                      continue

                    elif attack_name == "cannot attack":
                     time.sleep(1)
                     self.enchanterhealth -= 8
                     print("Your attack is so powerful that Esmeralda temporarily\
  cannot cast a spell.")
                     time.sleep(1)
                     print("Your health is now", self.playerhealth)
                     time.sleep(1)
                     print("Esmeralda's health is now", self.enchanterhealth)
                    continue

      elif attack_spell_choice == "5":
                    print("You cast a soul drain spell at Esmeralda.")
                    attack_name = random.choice(self.attacks)
                    time.sleep(1)
                    print(f"Esmeralda {attack_name}.")

                    if attack_name == "attacks":
                      self.playerhealth -= 6
                      self.enchanterhealth -= 10
                      time.sleep(1)
                      print("Esmeralda attacks with a blinding light spell, reducing\
  your health by 6 points.")
                      time.sleep(1)
                      print("Your health is now", self.playerhealth)
                      time.sleep(1)
                      print("Esmeralda's health is now", self.enchanterhealth)
                      continue

                    elif attack_name == "dodges the spell":
                      self.playerhealth -= 7
                      time.sleep(1)
                      print("Esmeralda dodges the attack and casts a blinding light\
  spell towards you,reducing your health by 7 points.")
                      time.sleep(1)
                      print("Your health is now", self.playerhealth)
                      time.sleep(1)
                      print("Esmeralda's health is now", self.enchanterhealth)
                      continue

                    elif attack_name == "cannot attack":
                     time.sleep(1)
                     self.enchanterhealth -= 10
                     print("Your attack is so powerful that Esmeralda temporarily\
  cannot cast a spell.")
                     time.sleep(1)
                     print("Your health is now", self.playerhealth)

                     time.sleep(1)
                     print("Esmeralda's health is now", self.enchanterhealth)
                    continue

     
    else:
     print("You defeat Esmeralda and gives you the instructions for breaking\
  the spell using the 10 items you created. With that, you save the kingdom from\
 peril. Congratulations!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
      return
    elif play_again != "no":
      print("Understandable. The initial question for starting the adventure will\
still be here if you change your mind. Thank you for playing!")
      return
    

    
    

     
