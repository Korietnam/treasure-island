print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
fork1 = input("You stumble across a fork in the road. It leads left and right. Which path do you take?\n")
l_fork1 = fork1.lower()

if l_fork1 == "left":
  print("You decide to take the left path. You stumble across a river with a steady flow of water. (left or right)")
elif l_fork1 == "right":
  print("You take the right path and find that you are killed by bandits. GAME OVER")
else:
  print("You decide to say 'who cares about rules' and steered off the path. You get lost in the forest and are killed by the forest of the living trees. GAME OVER")

river1 = input("Next to a dock, do you fjord the river or wait for a boat to take you across? (swim or wait)\n")
l_river1 = river1.lower()

if l_river1 == "wait":
  print("You decide to wait for a passing boat... While waiting, you check out the dock.")
elif l_river1 == "swim" or l_river1 == "fjord":
  print("You decide to swim across the water. Your swimming stat is too low and you drown in a very slow moving river. Shame. GAME OVER")
else:
  print("You decide to... LOOK OUT A BEAR! oops, you're dead. GAMEOVER")

dock1 = input("The dock has 3 sheds. One with a red door, one with a blue door, and one with a yellow door. Which do you choose? (red, blue, or yellow)\n")
l_dock1 = dock1.lower()

if l_dock1 == "yellow":
  print("You decide to go through the yellow door and you find a bunch of bags full with treasure! YOU WIN")
elif l_dock1 == "blue":
  print("You decide to go through the blue door and you fall through a hole meant for an outhouse. Now you'll never get the treasure. GAME OVER")
elif l_dock1 == "red":
  print("You decide to go through the red door. Didn't anyone tell you to not go through the red doors? GAME OVER")
else:
  print("You decide to not go through a door and wait for a boat. While waiting, an ensuing storm blows you into the river and you drown because of your low swim stat. GAME OVER")