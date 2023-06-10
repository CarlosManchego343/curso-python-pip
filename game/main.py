import random

def chooseOptions():
  options = ("piedra", "papel", "tijera")
  userOption = input("piedra, papel o tijera => ")
  userOption = userOption.lower()

  if not userOption in options:
    print("Esa opcion es invalida")
    # continue
    return None, None

  computerOption = random.choice(options)

  print("User option => ", userOption)
  print("Computer option => ",           
  computerOption)
  return userOption, computerOption

def checkRules(userOption, computerOption, userWins, computerWins):
  if userOption == computerOption:
    print("Empate")

  if userOption == "piedra":
    if computerOption == "tijera":
      print("Gana el usuario")
      userWins += 1
    elif computerOption == "papel":
      print("Gana el computador")
      computerWins += 1
  if userOption == "tijera":
    if computerOption == "papel":
      print("Gana el usuario")
      userWins += 1
    elif computerOption == "piedra":
      print("Gana el computador")
      computerWins += 1

  if userOption == "papel":
    if computerOption == "piedra":
      print("Gana el usuario")
      userWins += 1
    elif computerOption == "tijera":
      print("Gana el computador")
      computerWins += 1
  return userWins, computerWins

def absoluteWinner(userWins, computerWins):
  print("user wins => ", userWins)
  print("computer wins => ", computerWins)
  if computerWins == 2:
      print("El ganador final es la computadora")
      #break
      exit()

  if userWins == 2:
      print("El ganador final es el usuario")
      #break
      exit()
    


def runGame():
  computerWins = 0
  userWins = 0
  rounds = 1
  
  while True:
    print("*" * 50)
    print("ROUND", rounds)
    print("*" * 50)
    rounds += 1
    
    userOption, computerOption = chooseOptions()
    userWins, computerWins = checkRules(userOption, computerOption, userWins, computerWins)
    absoluteWinner(userWins, computerWins)
  
    
runGame()