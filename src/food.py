import time

class Food:
  def food_choice(self):
      while True:
        time.sleep(1)
        print("Before leaving on your journey, you decide to head home to\
 eat something for energy.")
        time.sleep(1)
        print("What do you eat?")
        time.sleep(1)
        print("1) Moldy cheese") 
        print("""

                _ _”” - _
         _ _ ””           ""  - _
     _””                  _ _ _ _ _”” - 
  _‘’_ _- - ‘’- - - - - “”   .-.       |
  |           . -.         ‘--- ‘    - |
  |          ‘ __‘      .- -.       : _ 
  |_ _ _ _  _ _ _ _ _ _ ' _ _’ _ _ _  _|

                     
                     
                     
                     """)
        time.sleep(1)
        print("2) An apple dipped in a clear potion")
        print("""   
               ____  /  ___
              /  #         \\
              
             |              |
             
              \            /
               \ ___..___ /
             
                         """)
        time.sleep(1)
        print("3) Blue edamame")
        print("""
              ______
            |         |
           -"   ##      "-
          |                |
          |_                |__
            |                  |
             –                 ‘‘|
               |_                 |
                 |_              _ |
                    |_ _ _ _ _ _ | 
                           
                      """)
        time.sleep(1)
        food = input("Food Choice: ")

        if food == "1":
            time.sleep(1)
            print('The cheese is so moldy that you vomit until you die. Try again.')
        elif food == "2":
            time.sleep(1)
            print('You choose the apple, which increases your energy level by 20%.')
            break  
        elif food == "3":
            time.sleep(1)
            print('After eating the edamame, you feel a burning sensation throughout\
  your body. Turns out, the edamame is burning your insides. You die within\
  5 minutes. Try again.')
        else:
          time.sleep(1)
          print("You will become very weak if you do not eat\
 something. You must pick a food. Please choose a valid option.")

