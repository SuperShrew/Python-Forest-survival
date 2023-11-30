import time
import os
from replit import db
from termcolor import colored
class colours():
  def __init__(self):
    self.GREEN = '\033[1;32;40m'
    self.RED = '\033[1;31;40m'
    self.YELLOW = '\033[1;33;40m'
    self.BLUE = '\033[1;34;40m'
    self.WHITE = '\033[0;37;40m'
    self.CYAN = '\033[1;36;40m'
    self.MAGENTA = '\033[1;35;40m'
    self.BLACK = '\033[1;30;40m'
    self.RESET = '\033[0;0m'
    self.BOLD = '\033[1m'
    self.UNDERLINE = '\033[4m'
    self.INVISIBLE = '\033[08m'

colour = colours()
def scroll(text, speed):
  for x in text:
    print(x, end='', flush=True)
    time.sleep(speed)
  print()

chosen = False
new = False
classes = ["Archer", "Mage", "Fighter", "Necromancer"]

print(colour.WHITE + "**********" + colour.GREEN + "Forest Survival" + colour.WHITE + "**********")
scroll(colour.WHITE + "Welcome to Forest Survival, a text-based incremental adventure game.", 0.1)
scroll(colour.WHITE + "Your goal is to survive as long as possible.", 0.1)
scroll(colour.WHITE + "Good luck and have fun!", 0.1)
scroll(colour.WHITE + "********************", 0.05)

scroll(colour.GREEN + "Press Enter to Continue", 0.1)
input(colour.WHITE + "> ")
os.system('clear')

user = input(colour.GREEN + "Username\n> ")
try:
  save = open(user + ".txt", "x")
  save.close()
  save = open(user + ".txt", "r+")
  new = True
except:
  save = open(user + ".txt", "r+")

os.system("clear")

while not(chosen):
  if new == True:
    scroll(colour.CYAN + "Choose your Class:", 0.1)
    scroll(colour.GREEN + "1. Archer," + colour.MAGENTA + " has accurate ranged attacks", 0.1)
    scroll(colour.GREEN + "2. Mage," + colour.MAGENTA + " has tactical spells and effects", 0.1)
    scroll(colour.GREEN + "3. Fighter," + colour.MAGENTA + " specialises in powerful melee attacks", 0.1)
    scroll(colour.GREEN + "4. Necromancer," + colour.MAGENTA + " has the ability to summon troops in combat and support with spells", 0.1)
    Class = input(colour.GREEN + "Choose Your Class (1, 2, 3, 4)\n> ")
    os.system("clear")
    if Class == "1" or Class == "2" or Class == "3" or Class == "4":
      scroll(colour.GREEN + "You have Chosen " + colour.CYAN + classes[int(Class)-1], 0.1)
      save.write(classes[int(Class)-1] + "\n")
      save.write("1" + "\n")
      save.write("1" + "\n")
      save.write("30" + "\n0")
      chosen = True
  else:
    print(save.read())
    chosen = True

time.sleep(1)
os.system("clear")
save.close()

while True:
  with open(user + ".txt", "r+") as save:
    data = save.readlines()
  data[0] #class
  data[1] #increaser
  data[2] #loot power/rarity
  data[3] #HP
  data[4] #inventory
  if data[0] == "Archer\n" and data[4] == "0":
    data[4] = "wooden_bow "
  elif data[0] == "Mage\n" and data[4] == "0":
    data[4] = "wooden_wand "
  elif data[0] == "Fighter\n" and data[4] == "0":
    data[4] = "wooden_sword "
  elif data[0] == "Necromancer\n" and data[4] == "0":
    data[4] = "necromancer_scroll "


  
  save.close()
  save = open(user + ".txt", "w")
  save.writelines(data)
  save.close()
  os.system("clear")
  
    