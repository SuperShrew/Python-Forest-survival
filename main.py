import time
import os
from replit import db
from termcolor import colored
import random

loot = {
  "Archer": 
  {
    "_1": ["Arrow"]*10
  },
  "Mage": 
  {
    "_1": ["spell"]*10
  },
  "Fighter":
  {
    "_1": ["Sword"]*10
  },
  "Necromancer":
  {
    "_1": ["Crystal"]*10
  },
}
enemies = {
  "_1":
  {
    "enemy1":
    {
      "name": "Zombie",
      "attack" : 5,
      "HP": 10
    },
    "enemy2":
    {
      "name": "Skeleton",
      "attack": 7,
      "HP": 8
    }
  }
}
print(enemies['_1'][random.choice(list(enemies['_1']))])
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
blanks = ["tree", "rock", "pond"]
def ran(increaser, prof, looting): # this code is prone to bug 3, debug with ai if possible
  a = random.randint(1, 3)
  if a == 1:
    looting = "_" + looting
    rando = random.randint(0, 9)
    return loot[(prof).replace("\n", "")][looting.replace("\n", "")][rando]
  elif a == 2:
    increaser = "_" + increaser
    return enemies[increaser.replace("\n", "")][random.choice(list(enemies[increaser.replace("\n", "")]))]
  elif a == 3:
    return random.choice(blanks)

def scroll(text, speed):
  for x in text:
    print(x, end='', flush=True)
    time.sleep(speed)
  print()

def generate_area(profession, increaser, loot_level):
  return [ran(increaser, profession, loot_level), ran(increaser, profession, loot_level), ran(increaser, profession, loot_level), ran(increaser, profession, loot_level)]
  #WIP and DO TESTING TO CONFIRM THIS WORKS ^^^ PRE ALPHA STUFF
chosen = False
new = False
classes = ["Archer", "Mage", "Fighter", "Necromancer"]

#print(colour.WHITE + "**********" + colour.GREEN + "Forest Survival" + colour.WHITE + "**********")
#scroll(colour.WHITE + "Welcome to Forest Survival, a text-based incremental adventure game.", 0.1)
#scroll(colour.WHITE + "Your goal is to survive as long as possible.", 0.1)
#scroll(colour.WHITE + "Good luck and have fun!", 0.1)
#scroll(colour.WHITE + "********************", 0.05)
# commented out for speed when debugging
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
    scroll(colour.CYAN + "Choose your Class:", 0.05)
    scroll(colour.GREEN + "1. Archer," + colour.MAGENTA + " has accurate ranged attacks", 0.05)
    scroll(colour.GREEN + "2. Mage," + colour.MAGENTA + " has tactical spells and effects", 0.05)
    scroll(colour.GREEN + "3. Fighter," + colour.MAGENTA + " specialises in powerful melee attacks", 0.05)
    scroll(colour.GREEN + "4. Necromancer," + colour.MAGENTA + " has the ability to summon troops in combat and support with spells", 0.05)
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
  current_area = generate_area(data[0], data[1], data[2])
  scroll(colour.WHITE + "You enter a new area, the features of this area are:", 0.1)
  for x in range(len(current_area)):
    if isinstance(current_area[x], dict):
      scroll(colour.GREEN + current_area[x]["name"], 0.1)
    else:
      scroll(colour.GREEN + str(current_area[x]), 0.1)
  print()
  scroll("Press Enter to Continue", 0.1)
  input("> ")
  save.close()
  save = open(user + ".txt", "w")
  save.writelines(data)
  save.close()
  os.system("clear")