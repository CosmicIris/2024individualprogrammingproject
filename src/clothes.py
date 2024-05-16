import time

class Clothes:
  def clothes_choice(self):
    while True:
      time.sleep(1)
      print("You also decide to change your clothes.")
      time.sleep(1)
      print("What do you choose to change into?")
      time.sleep(1)
      print("1) light clothes with a wool cloak")
      time.sleep(1)
      print("2) an itchy, heavy sweater with jeans")
      time.sleep(1)
      print("3) a cotton t-shirt with shorts")
      time.sleep(1)
      clothes = input("Clothing Choice: ")
      
      if clothes == "1":
                  time.sleep(1)
                  print('You choose to change into light clothes that are\
 comfortable and warm, as well as a wool cloak to shield yourself from rain.')
                  break
      elif clothes == "2":
                  time.sleep(1)
                  print('After stepping out of your home, you realize that the sweater\
 is very uncomfortable and start furiously scratching yourself until\
 you bleed. Try again.')  
      elif clothes == "3":
                  time.sleep(1)
                  print('After stepping out of your home, you realize that choosing these\
 clothes was a terrible mistake, as it is pouring heavily and you quickly catch\
 hypothermia due to the rain. You die within an hour. Try again. ')
      else:
                time.sleep(1)
                print("You must pick a clothing choice. Please choose a valid option.")
      continue 
      
