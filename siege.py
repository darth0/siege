
import math
import random

name = ""
userInput = ""
wave = 1
castleHealth = 100 * wave
men = wave * 10 + 10
arrowDamage = men * 1
menDamage = men * 2
catapultDamage = 50 * wave
count = 0

def whatwillyoudo(wave, castleHealth, men, arrowDamage, catapultDamage):
  
    castleHealth = 100 * wave
    men = wave * 10 + 10
    count = 0
    

    while (castleHealth > 0 and men > 0):
        decisionInput = input("Type 1 to shoot arrows, Type 2 to send a certain amount of men to make a rush towards the castle, and Type 3 to fire the catapult")

        if decisionInput == "1":
            menkilled = random.randint(0, wave * 2)
            men = men - menkilled
            arrowdamagedone = 13 
            131
            131
            1311
            1311
            
            
            
            
            '* men * wave
            castleHealth = castleHealth - arrowdamagedone
            print("The castle now has " + str(castleHealth) + " health.")
            print("You have lost " + str(menkilled) + " men from return fire. You now have " + str(men) + ".")

        if decisionInput == "2":
            rushinput = int(input("How many men would you like to make a rush at the castle?"))
            if int(rushinput) > men:
                print('Please enter a valid input. You have ' + str(men) + ' men left.')
            if int(rushinput) <= men:
                menkilled = random.randint(0, int(rushinput))
                men = men - menkilled
                mendamagedone = rushinput * 3
                castleHealth = castleHealth - mendamagedone
                print("The castle now has " + str(castleHealth) + " health.")
                print("You have lost " + str(menkilled) + " men from rushing. You now have " + str(men) + "."
                )
        
        if decisionInput == "3":
            count = count + 1
            if count >= 2:
                print("You have already used the catapult once!")
                
            elif count == 1: 
              catapultChance = random.randint(0 , 2)
              menkilled = random.randint(0, wave * 3)
              men = men - menkilled
              if catapultChance == 2:
                  print("The catapult missed! The castle now has " + str(castleHealth) + " health.")
                  print("You have lost " + str(menkilled) + " men from return fire. You now have " + str(men) + ".")
              else:
                  castleHealth = castleHealth - catapultDamage
                  count = count + 1
                  print("The catapult struck! The castle now has " + str(castleHealth) + " health")
                  print("You have lost " + str(menkilled) + " men from return fire. You now have " + str(men) + ".")
    
    if castleHealth <= 0:
        print("Castle " + str(wave) + " sieged!")
        print("Starting next wave. . .")
        startGame(wave + 1, castleHealth, men, arrowDamage, catapultDamage) #problem with next wave
    
    if men <= 0:
        print("All of your men died! GAME OVER!")
        exit


def startGame(wave, castleHealth, men, arrowDamage, catapultDamage):
  castleHealth = 100 * wave
  men = wave * 10 + 10
  print("CASTLE " + str(wave))
  print("Men = " + str(men))
  print("Castle Health = " + str(castleHealth))

  whatwillyoudo(wave, castleHealth, men, arrowDamage, catapultDamage)



userInput = input('Welcome to S.I.E.G.E alpha v1.5. Press 1 to continue')
if userInput == "1":
    name = input("What shall your leader's name be?")

    userInput = input(name + "! A magnificent choice indeed..." "\n"
                             "Press 1 for directions or 2 to start the game")
    if userInput == "1":
        input('You are raiding the castles of a neighboring kingdom...' "\n"
              'There are 10 castles. In order to win a round, you must bring the health of the castle to 0.' "\n"
              'Press 1 to make your men shoot arrows at the castle (hint: this has a low risk of your men dying but medium damage).' "\n"
              'Press 2 to send a certain amount of your men to make a rush towards the castle (hint: this has a high risk of your men dying but high damage).' "\n"
              'Or Press 3 to fire the catapult (hint: the catapult has 1 use per round and high a 1/3 chance of causing high damage).' "\n"
              'Your men count changes every round but if all of your men die in one round, you lose'  "\n"
              'Each level will get increasingly difficult. Good luck! (Press 1 to start)')
        if userInput == "1":
            print('Starting. . .')
            startGame(1, castleHealth * wave, men, arrowDamage, catapultDamage)
        else:
            print('Invalid Input.')
    elif userInput == "2":
        print('Starting. . .')
        startGame(1, castleHealth * wave, men, arrowDamage, catapultDamage)


else:
    print("Invalid Input. Try Again.")


