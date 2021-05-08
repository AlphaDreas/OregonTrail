import random

miles = 2000
health = 5
days = 282
food = 500
game = True
hunted = 0
travelled = 0
moved = 0

def commands():
  print("Travel")
  print("Rest")
  print("Hunt")
  print("Status")
  print("Help")
  print("quit")


name = input("What is your name Pioneer? ")

print("-----------------")
print("You have " + str(food) + "lbs of food.")
print("-----------------")
print("What would you like to do " + name + "?")
print("")
menu = commands()
print("")

#Win/Loss

while game == True:
  if food <= 0:
    print("You died! Next make sure to rest!")
    break
  elif travelled == "2000":
    print("You win! You've reached Oregon!")
    break
  elif days == 0:
    if miles >= 2000:
      print("YOU WON! YOU'VE REACHED OREGON")
      break
    elif miles < 0:
      print("You didn't make it to Oregon. You Lose.")
      break
  elif health <= 0:
    print("You lost all your health!")
    break
    
# Game Commands

  cmd = input("")
  if cmd == "quit":
    print("Quitting game.....")
    print("Game Ended")
    break
  elif cmd == "help":
    print("")
    print("Commands")
    print("-----------------")
    menu = commands()
    print("-----------------")
  elif cmd == "hunt":
    hunted = random.randint(2,5)
    days = days - hunted
    hunted = str(hunted)
    food = food + 100
    health_loss = random.randint(1,2)
    if health_loss == 1:
      health = health - 1
    print("You hunted for " + hunted + " days and gathered 100lbs of food.")
    a = (int(hunted)*5)
    food = food - a
  elif cmd == "status":
    print("You have " + str(food) + "lbs of food.")
    print("You have " + str(health) + " health.")
    print("You have travelled " + str(travelled) + " miles.")
    print("You have " + str(days) + " days to go.")
  elif cmd == "rest":
    health_loss = random.randint(1,2)
    if health_loss == 1:
      health = health - 1
    if health == 5:
      rested = random.randint(2,5)
      print("You rested for " + str(rested) + " days!")
      days = days - rested
      a = (rested*5)
      food = food - a
    elif health < 5:
      rested = random.randint(2,5)
      health = health + 1
      days = days - rested
      a = (rested*5)
      print("You rested for " + str(a) + " days!")
      food = food - a
  elif cmd == "travel":
    move = random.randint(30,60)
    travelled = travelled + move
    miles = miles - move
    day = random.randint(3,7)
    days = days - day
    b = day*5
    food = food - b
    health_loss = random.randint(1,2)
    if health_loss == 1:
      health = health - 1
    print("You travelled " + str(move) + " miles in " + str(day) + " days!")
