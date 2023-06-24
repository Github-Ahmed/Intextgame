# Imports
import random
import time
import sys
import os

# Colors
WHITE = "\033[0;37m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
ORANGE = "\033[0;33m"
PINK = "\033[1;31m"
BLUE = "\033[0;34m"
PURPLE = '\033[95m'
DARKCYAN = '\033[36m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLACK = "\033[0;30m"
MAGENTA = "\033[0;35m"
BRIGHT_BLACK = "\033[0;90m"
BRIGHT_RED = "\033[0;91m"
BRIGHT_GREEN = "\033[0;92m"
BRIGHT_YELLOW = "\033[0;93m"
BRIGHT_BLUE = "\033[0;94m"
BRIGHT_MAGENTA = "\033[0;95m"
BRIGHT_CYAN = "\033[0;96m"
BRIGHT_WHITE = "\033[0;97m"

# bg = Background colors
bg_black = '\x1b[40m'
bg_red = '\x1b[41m'
bg_green = '\x1b[42m'
bg_yellow = '\x1b[43m'
bg_blue = '\x1b[44m'
bg_magenta = '\x1b[45m'
bg_cyan = '\x1b[46m'
bg_white = '\x1b[47m'
bg_grey = '\x1b[100m'
bg_bright_red = '\x1b[101m'
bg_bright_green = '\x1b[102m'
bg_bright_yellow = '\x1b[103m'
bg_bright_blue = '\x1b[104m'
bg_bright_magenta = '\x1b[105m'
bg_bright_cyan = '\x1b[106m'
bg_bright_white = '\x1b[107m'

# Extras
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# Sleep function
sleep = time.sleep
# sleep(2)     Sleep 2 seconds


def typewriter(message):
  for i in message:
    sys.stdout.write(i)
    sys.stdout.flush()
    if((i != "\n") and (i != ":")):
        time.sleep(0.05)
    else:
	    time.sleep(0.05)

#typewriter(text)

# Fast Typewriter


def typewriter1(message):
  for i in message:
    sys.stdout.write(i)
    sys.stdout.flush()
    if ((i != "\n") and (i != ":")):
        time.sleep(0.0001)
    else:
	    time.sleep(0.0001)

# Medium Typewriter


def typewriter2(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") and (i != ":")):
            time.sleep(0.051)
        else:
            time.sleep(0.033)


# Clear screen function
def clear(): return os.system('clear')
# clear()

# Loading function


def loading():
  print("Loading:")

  animation = ["10%", "20%", "30%", "40%",
               "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
               "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

  for i in range(len(animation)):
      time.sleep(0.6)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  typewriter("\n")


# Owner of Repl
owner = os.environ['REPL_OWNER']
# print(owner)

# Global variables...
stars = 0
wallet = 0
health = 100
inventory = []

# Gameover
gameover = BLUE + BOLD + """

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""" + END

# GTA
gta = ORANGE + BOLD + """

──────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████──────────██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██──────────██░░░░░░░░░░██─
─██░░██████████─██████░░██████─██░░██████░░██──────────██░░██████████─
─██░░██─────────────██░░██─────██░░██──██░░██──────────██░░██─────────
─██░░██─────────────██░░██─────██░░██████░░██──────────██░░██████████─
─██░░██──██████─────██░░██─────██░░░░░░░░░░██──────────██░░░░░░░░░░██─
─██░░██──██░░██─────██░░██─────██░░██████░░██──────────██████████░░██─
─██░░██──██░░██─────██░░██─────██░░██──██░░██──────────────────██░░██─
─██░░██████░░██─────██░░██─────██░░██──██░░██──────────██████████░░██─
─██░░░░░░░░░░██─────██░░██─────██░░██──██░░██──────────██░░░░░░░░░░██─
─██████████████─────██████─────██████──██████──────────██████████████─
──────────────────────────────────────────────────────────────────────
""" + END


inventory.append('default weapon')

# Printing Hi
typewriter(ORANGE + BOLD + "Hey " + owner + "\n\n" + END)

# Using loading
loading()
clear()

typewriter1(gta)
sleep(0.6)

# Asking for game works...


def ask():
  ask = input("\n\nDo you want see how this game works? (y/n)\n: ")
  ask = ask.lower()

  if ask == 'y' or ask == 'yes':
    typewriter2(bg_black + BOLD +
                """
    \n1. Choose from the map.
    \n2. Every wrong input may lead back to map.
    \n3. Every move that you take will decrease 5 health.
    \n4. More information about the places will be given after you choose the place.
    \n5. Make a smart choice when you are under an arrest.
    \n6. You can check your money, health, inventory from Profile Check.
    """ + END)
    sleep(0.5)
    typewriter(YELLOW + BOLD + "\n\nLet's go to map now!\n" + END)
    sleep(0.5)
    clear()

  elif ask == 'n' or ask == 'no':
    typewriter(GREEN + BOLD + '\nOk, Just continue on!\n' + END)
    sleep(0.2)
    clear()


# Def for bribing and stars
def bribe():
  global wallet
  global stars
  global health

  if stars == 1:
    ask = input(BRIGHT_BLACK + BOLD + "\nSince you were cassed with 1 star, here are the few things you can do now:-\n1. Bribe with 100 dollars.\n2. Leave him there.\n: " + END)
    ask = ask.lower()

    if ask == '1' or ask == 'bribe':
      wallet -= 100

      typewriter(YELLOW + BOLD +
                 "\nYou bribed him making your stars go back to zero\n" + END)
      stars -= 1

      # Random money
      random_money = random.randint(0, 70)
      typewriter(
          YELLOW + BOLD + "\nThe guy who you killed was having $" + str(random_money) + END)
      press = input("\nPress 'e' to add that to your wallet.\n")

      if press == 'e':
        wallet += random_money
        typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                   ' has been successfully added to your wallet\n' + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + "You left the money out there.\n" + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

    elif ask == '2' or ask == 'leave':
      typewriter(RED + BOLD + "\nThe cop killed you." + END)

  elif stars == 2:
    ask = input(BRIGHT_BLACK + BOLD + "\nSince you were cassed with 2 stars, here are the few things you can do now:-\n1. Bribe with 150 dollars.\n2. Leave him there.\n: " + END)
    ask = ask.lower()

    if ask == '1' or ask == 'bribe':
      wallet -= 150
      typewriter(YELLOW + BOLD +
                 "\nYou bribed him making your stars go back to zero\n" + END)
      stars -= 2

      # Random money
      random_money = random.randint(0, 70)
      typewriter(
          YELLOW + BOLD + "\nThe guy who you killed was having $" + str(random_money) + END)
      press = input("\nPress 'e' to add that to your wallet.\n")

      if press == 'e':
        wallet += random_money
        typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                   ' has been successfully added to your wallet\n' + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + "You left the money out there.\n" + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

    elif ask == '2' or ask == 'leave':
      typewriter(RED + BOLD + "\nThe cop killed you" + END)

  elif stars == 3:
    ask = input(BRIGHT_BLACK + BOLD + "\nSince you were cassed with 3 stars, here are the few things you can do now:-\n1. Bribe with 200 dollars.\n2. Leave him there.\n: " + END)
    ask = ask.lower()

    if ask == '1' or ask == 'bribe':
      wallet -= 200
      typewriter(YELLOW + BOLD +
                 "\nYou bribed him making your stars go back to zero\n" + END)
      stars -= 3

      # Random money
      random_money = random.randint(0, 70)
      typewriter(
          YELLOW + BOLD + "\nThe guy who you killed was having $" + str(random_money) + END)
      press = input("\nPress 'e' to add that to your wallet.\n")

      if press == 'e':
        wallet += random_money
        typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                   ' has been successfully added to your wallet\n' + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + "You left the money out there.\n" + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

    elif ask == '2' or ask == 'leave':
      typewriter(RED + BOLD + "\nThe cop killed you" + END)

  elif stars == 4:
    ask = input(BRIGHT_BLACK + BOLD + "\nSince you were cassed with 4 stars, here are the few things you can do now:-\n1. Bribe with 250 dollars.\n2. Leave him there.\n: " + END)
    ask = ask.lower()

    if ask == '1' or ask == 'bribe':
      wallet -= 250
      typewriter(YELLOW + BOLD +
                 "\nYou bribed him making your stars go back to zero\n" + END)
      stars -= 4

      # Random money
      random_money = random.randint(0, 70)
      typewriter(
          YELLOW + BOLD + "\nThe guy who you killed was having $" + str(random_money) + END)
      press = input("\nPress 'e' to add that to your wallet.\n")

      if press == 'e':
        wallet += random_money
        typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                   ' has been successfully added to your wallet\n' + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + "You left the money out there.\n" + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

    elif ask == '2' or ask == 'leave':
      typewriter(RED + BOLD + "\nThe cop killed you" + END)

  elif stars == 5:
    ask = input(BRIGHT_BLACK + BOLD + "Since you were cassed with 5 stars, here are the few things you can do now:-\n1. Bribe with 300 dollars.\n2. Leave him there.\n: " + END)
    ask = ask.lower()

    if ask == '1' or ask == 'bribe':
      wallet -= 300
      typewriter(YELLOW + BOLD +
                 "\nYou bribed him making your stars go back to zero\n" + END)
      stars -= 5

      # Random money
      random_money = random.randint(0, 70)
      typewriter(
          YELLOW + BOLD + "\nThe guy who you killed was having $" + str(random_money) + END)
      press = input("\nPress 'e' to add that to your wallet.\n")

      if press == 'e':
        wallet += random_money
        typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                   ' has been successfully added to your wallet\n' + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + "You left the money out there.\n" + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

    elif ask == '2' or ask == 'leave':
      typewriter(RED + BOLD + "\nThe cop killed you" + END)

  else:
    typewriter(GREEN + BOLD +
               "\nYou are safe since you don't have any stars!\n" + END)
    health -= 5

    typewriter(BLUE + BOLD + '\nBack to map...' + END)
    all()

# All


def all():
  def map():
    global place
    place = input(WHITE + "Where do you wanna go from these 4 places:- \n1. Bank\n2. Weapon store\n3. Hospital\n4. Stunt Jump\n5. Check your profile\n6. Exit\n")
    place = place.lower()

  # Bank
  def bank():
    global place
    global wallet
    global inventory
    global stars
    global health

    # In Bank
    if place == '1' or place == 'bank':
      what_to_do = input(
          "Things you can do here:-\n1. Withdraw\n2. Rob the bank\n3. Kill a person\n ")
      what_to_do = what_to_do.lower()

      # Withdraw
      if what_to_do == '1' or what_to_do == 'withdraw':
        typewriter(
            PINK + BOLD + "You are in a right spot. You can only withdraw $100 at once. How much do you wanna withdraw?" + END)
        withdraw = int(input("\n: "))

        if withdraw <= 100:
          typewriter(GREEN + BOLD + "\nYou withdrawed " + str(withdraw) +
                     " dollars and it has been added to your wallet.\n" + END)
          wallet += withdraw
          typewriter(BLUE + BOLD + '\nBack to map...' + END)

          sleep(0.2)
          clear()
          all()

        else:
          typewriter(
              RED + BOLD + "You can't withdraw that much amount at once or Invalid input!\n" + END)
          health -= 5

          typewriter(BLUE + BOLD + '\nBack to map...' + END)

          sleep(0.2)
          clear()
          all()

      # rob
      elif what_to_do == '2' or what_to_do == 'rob the bank' or what_to_do == 'rob':

          # To check if you have a weapon in your inventory
          def check():
            global wallet
            global health
            if 'powerful weapon' in inventory:
              random_money = random.randint(0, 5000)

              typewriter(PINK + BOLD + "Since you have powerful weapon in your inventory, you killed 5 cops. You found the hidden treasure of $" +
                         str(random_money) + " in the bank\n" + END)
              press = input("Press 'e' to add this to to your wallet.\n")
              press = press.lower()

              # Adding the wallet from robbery
              if press == 'e':
                wallet += random_money

                typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                           ' has been successfully added to your wallet\n' + END)
                health -= 5

                typewriter(BLUE + BOLD + '\nBack to map...' + END)

                sleep(0.2)
                clear()
                all()

              else:
                typewriter(
                    RED + BOLD + "You left the money out there.\n" + END)
                health -= 5

                typewriter(BLUE + BOLD + '\nBack to map...' + END)

                sleep(0.2)
                clear()
                all()

            else:
              typewriter(
                  RED + BOLD + "You can't rob with your actual default weapon. Go to weapon store to  buy for yourself one...\n" + END)
              health -= 5
              typewriter(BLUE + BOLD + '\nBack to map...' + END)

              sleep(0.2)
              clear()
              all()

          check()

      elif what_to_do == '3' or what_to_do == 'kill a person':

        def check():
          global stars
          global health
          if 'default weapon' in inventory:

            luck = ["you weren't in front of a cop, So you are safe",
                    "you were in front of a cop, So you were cassed with 1 star."]
            random_sel = random.choice(luck)
            typewriter(ORANGE + BOLD +
                       "You killed 1 person, while " + random_sel + END)

            if random_sel == 'you were in front of a cop, So you were cassed with 1 star.':
              stars += 1
              bribe()

            elif random_sel == "you weren't in front of a cop, So you are safe":
              typewriter(ORANGE + BOLD +
                         " and you got nothing from the body\n" + END)
              health -= 5

              typewriter(BLUE + BOLD + '\nBack to map...' + END)

              sleep(0.2)
              clear()
              all()

        check()

      else:
        typewriter(RED + BOLD + '\nInvalid input!\n' + END)
        health -= 5
        typewriter(BLUE + BOLD + "Back to map..." + END)
        sleep(0.2)
        clear()
        all()

  # Weapon store

  def wstore():
    global place
    global wallet
    global inventory
    global health

    if place == '2' or place == 'weapon store':
      what_to_do = input(
          "You are here to buy weapons for yourself.\nHere is the list:-\n1. Powerful weapon\n2. Medium weapon\n3. Default weapon\n")
      what_to_do = what_to_do.lower()

      # Powerful weapon
      if what_to_do == '1' or what_to_do == 'powerful weapon':
        typewriter(CYAN + BOLD + "\nThis weapon helps you to easily destroy 5 people at a time. For this weapon you need 650 dollars in your wallet.\n" + END)

        # To check if you already have this item.
        def check_already():
          global inventory
          global health

          if 'powerful weapon' in inventory:
            typewriter(
                YELLOW + BOLD + "You already have this weapon in your inventory. You can use it now.\n" + END)
            health -= 5
            typewriter(BLUE + BOLD + "\nBack to map..." + END)
            sleep(0.2)
            clear()
            all()

          else:
            check()

        # To check if you have that much of money
        def check():
          global wallet
          global health
          if wallet >= 650:
            inventory.append('powerful weapon')
            typewriter(
                GREEN + BOLD + "\nYou successfully bought this weapon and it has been added to your inventory\n" + END)
            wallet -= 650
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)

            sleep(0.2)
            clear()
            all()

          else:
            typewriter(
                RED + BOLD + "\nWe are sorry, you don't have that much amount to buy this weapon.\n" + END)
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)

            sleep(0.2)
            clear()
            all()

        check_already()

      # Medium weapon
      elif what_to_do == '2' or what_to_do == 'medium weapon':
        typewriter(CYAN + BOLD + 'This weapon helps you to easily destroy 2-3 people at a same time. For this weapon you need 300 dollars in your wallet.\n' + END)

        # To check if you already have this item.
        def check_already():
          global inventory
          global health

          if 'medium weapon' in inventory:
            typewriter(
                YELLOW + BOLD + "You already have this weapon in your inventory. You can use it now.\n" + END)
            health -= 5
            typewriter(BLUE + BOLD + "\nBack to map..." + END)
            sleep(0.2)
            clear()
            all()

          else:
            check()

        # To check if you have that much of money
        def check():
          global wallet
          global health
          if wallet >= 300:
            inventory.append('medium weapon')

            typewriter(
                GREEN + BOLD + '\nYou successfully bought this weapon and it has been added to your inventory\n' + END)
            wallet -= 300
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)

            sleep(0.2)
            clear()
            all()

          else:
            typewriter(
                RED + BOLD + "\nWe are sorry, you don't have that much amount to buy this weapon\n" + END)
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)

            sleep(0.2)
            clear()
            all()

        check_already()

      # Default weapon
      elif what_to_do == '3' or what_to_do == 'default weapon':

        # Printing a sentence
        typewriter(CYAN + BOLD + "This weapon can be used to destroy only one person at a time and also this weapon has been already available in your inventory as your default.\n" + END)
        health -= 5

        typewriter(BLUE + BOLD + '\nBack to map...' + END)

        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + '\nInvalid input!\n' + END)
        health -= 5
        typewriter(BLUE + BOLD + "Back to map...")
        sleep(0.2)
        clear()
        all()

  # Hospital

  def hospital():
    global place
    global wallet
    global inventory
    global health
    global stars

    if place == '3' or place == 'hospital':
      what_to_do = input(
          "Things you can do here:-\n1. Increase your health.\n2. Buy a bed\n3. Kill a person\n4. Wander around to find some thing\n5. Rent your bed\n")
      what_to_do = what_to_do.lower()

      if what_to_do == '1' or what_to_do == 'increase your health':
        typewriter(GREEN + BOLD + "You boosted your health to 100%\n" + END)
        less = 100 - health
        health += less

        typewriter(BLUE + BOLD + '\nBack to map...' + END)
        sleep(0.2)
        clear()
        all()

      elif what_to_do == '2' or what_to_do == 'buy a bed':

        # To check if you already have this item.
        def check_already():
          global inventory
          global health

          if 'bed' in inventory:
            typewriter(
                YELLOW + BOLD + "You already have this weapon in your inventory. You can use it now.\n" + END)
            health -= 5
            typewriter(BLUE + BOLD + "\nBack to map..." + END)
            sleep(0.2)
            clear()
            all()

          else:
            check()

        # To check correct amount of money
        def check():
          global wallet
          global inventory
          global health

          typewriter(
              PINK + BOLD + "You need at least 2000 dollars in your wallet to buy a bed in this hospital. You can use this bed to rent it.\n" + END)

          if wallet >= 2000:

            inventory.append('bed')
            wallet -= 2000
            typewriter(
                GREEN + BOLD + "\nYou successfully bought this bed for 2000 dollars and it has been added to your inventory\n" + END)
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)
            sleep(0.2)
            clear()
            all()

          else:
            typewriter(
                RED + BOLD + "\nWe are sorry, you don't have that much amount to buy this bed.\n" + END)
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)
            sleep(0.2)
            clear()
            all()

        check_already()

      elif what_to_do == '3' or what_to_do == 'kill a person':
        def check():
          global stars
          global health
          if 'default weapon' in inventory:

            luck = ["you weren't in front of a cop, So you are safe",
                    "you were in front of a cop, So you were cassed with 1 star."]
            random_sel = random.choice(luck)
            typewriter(ORANGE + BOLD +
                       "You killed 1 person, while " + random_sel + END)

            if random_sel == 'you were in front of a cop, So you were cassed with 1 star.':
              stars += 1
              bribe()

            elif random_sel == "you weren't in front of a cop, So you are safe":
              typewriter(ORANGE + BOLD +
                         " and you got nothing from the body\n" + END)
              health -= 5

              typewriter(BLUE + BOLD + '\nBack to map...' + END)

              sleep(0.2)
              clear()
              all()

        check()

      elif what_to_do == '4' or what_to_do == 'wander around':

        typewriter(
            PINK + BOLD + "You planned to just wander around the hospital property without any reason\n" + END)

        luck = ['\nYou got under a caught of a cop and',
                '\nYou successfully wandered over the place and']
        random_sel = random.choice(luck)
        if random_sel == luck[0]:
          typewriter(BRIGHT_BLACK + BOLD +
                     luck[0] + " you were cassed with 2 stars.\n" + END)
          stars += 2
          bribe()

        elif random_sel == luck[1]:
          typewriter(PURPLE + BOLD + luck[1] + " You found something!!" + END)
          random_money = random.randint(0, 500)
          typewriter(PURPLE + BOLD + "\nIt's $" + str(random_money) + END)

          press = input("\nPress 'e' to add that to your wallet: ")
          if press == 'e':
            wallet += random_money
            typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                       ' has been successfully added to your wallet\n' + END)
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)
            sleep(0.2)
            clear()
            all()

          else:
            typewriter(RED + BOLD + "You left the money out there\n" + END)
            health -= 5

            typewriter(BLUE + BOLD + '\nBack to map...' + END)
            sleep(0.2)
            clear()
            all()

      elif what_to_do == '5' or what_to_do == 'rent your bed':

        # To check if you have bed in your inventory
        def check():
          global inventory
          global health

          if 'bed' in inventory:
            random_sel = random.randint(100, 500)
            typewriter(PURPLE + BOLD + "\nYou rented your bed at " +
                       str(random_sel) + END)
            press = input("\nPress 'e' to add that to your wallet.\n")

            if press == 'e':
              typewriter(GREEN + BOLD + "\n$" + str(random_sel) +
                         " has been successfully added to your wallet.\n" + END)
              health -= 5
              typewriter(BLUE + BOLD + '\nBack to map...' + END)
              sleep(0.2)
              clear()
              all()

            else:
              typewriter(RED + BOLD + "\nYou left the money out there." + END)
              health -= 5
              typewriter(BLUE + BOLD + '\nBack to map...' + END)
              sleep(0.2)
              clear()
              all()

          else:
            typewriter(
                RED + BOLD + "\nWe are sorry that you don't have bed in your inventory, proceed to choice 2 to buy yourself one...\n" + END)
            health -= 5
            typewriter(BLUE + BOLD + '\nBack to map...' + END)
            sleep(0.2)
            clear()
            all()

        check()

      else:
        typewriter(RED + BOLD + '\nInvalid input!\n' + END)
        health -= 5
        typewriter(BLUE + BOLD + "Back to map...")
        sleep(0.2)
        clear()
        all()

  # Stunt Jump

  def stunt_jump():
    global health
    global inventory
    global wallet

    if place == '4' or place == 'stunt jump':
      what_to_do = input(
          "Things you can do here:- \n1. Jump\n2. Ignore the jump\n3. Get up and down\n")
      what_to_do = what_to_do.lower()

      if what_to_do == '1' or what_to_do == 'jump':
        luck = ['you are safe', 'you fell down out of the jump']
        random_sel = random.choice(luck)

        if random_sel == luck[0]:
          typewriter(
              GREEN + BOLD + "\nYou successfully jumped over, Your health is now as before.\n" + END)
          health -= 5
          typewriter(BLUE + BOLD + "\nBack to map..." + END)
          sleep(0.2)
          clear()
          all()

        elif random_sel == luck[1]:
          typewriter(
              PURPLE + BOLD + "\nIt seems like you fell off the jump making your health drop by 50\n" + END)
          health -= 50
          typewriter(BLUE + BOLD + "Back to map...")
          sleep(0.2)
          clear()
          all()

      elif what_to_do == '2' or what_to_do == 'ignore' or what_to_do == 'ignore the jump':
        typewriter(YELLOW + BOLD + "\nYou ignored the jump!!\n" + END)
        health -= 5
        sleep(0.2)
        clear()
        all()

      elif what_to_do == '3' or what_to_do == 'get up and down':
        typewriter(
            PURPLE + BOLD + "\nYou got at the summit of the jump and got down and " + END)

        random_money = random.randint(50, 70)
        typewriter(PURPLE + BOLD + "You found something\nIt's $" +
                   str(random_money) + END)
        press = input("\nPress 'e' to add that to your wallet: ")

        if press == 'e':
          typewriter(GREEN + BOLD + '\n$' + str(random_money) +
                     ' has been successfully added to your wallet\n' + END)
          wallet += random_money
          health -= 5
          typewriter(BLUE + BOLD + "\nBack to map..." + END)
          sleep(0.2)
          clear()
          all()

        else:
          typewriter(RED + BOLD + "You left the money out there!\n" + END)
          health -= 5
          typewriter("\nBack to map...")
          sleep(0.2)
          clear()
          all()

      else:
        typewriter(RED + BOLD + "\nInvalid input!\n" + END)
        health -= 5
        typewriter("\nBack to map...")
        sleep(0.2)
        clear()
        all()

  # Check your profile

  def check_profile():
    global wallet
    global health
    global inventory
    if place == '5' or place == 'check your profile':
      what_to_do = input(
          "Things you can do here:-\n1. Check your wallet\n2. Check your health\n3. Check your inventory\n4. Check all\n")
      what_to_do = what_to_do.lower()

      if what_to_do == '1' or what_to_do == 'check your wallet' or what_to_do == 'wallet':
        typewriter(DARKCYAN + "\nYour current wallet amount is:- " +
                   BOLD + str(wallet) + ' dollars\n' + END)
        health -= 5
        typewriter(BLUE + BOLD + '\nBack to map...' + END)
        sleep(0.2)
        clear()
        all()

      elif what_to_do == '2' or what_to_do == 'check your health' or what_to_do == 'health':
        typewriter(DARKCYAN + "\nYour current health is:- " +
                   BOLD + str(health) + END)
        health -= 5
        typewriter(BLUE + BOLD + "\n\nBack to map..." + END)
        sleep(0.2)
        clear()
        all()

      elif what_to_do == '3' or what_to_do == 'check your inventory' or what_to_do == 'inventory':
        typewriter(DARKCYAN + '\nYour current inventory looks like this:-\n' +
                   BOLD + str(inventory) + END)
        health -= 5
        typewriter(BLUE + BOLD + '\n\nBack to map...' + END)
        sleep(0.2)
        clear()
        all()

      elif what_to_do == '4' or what_to_do == 'check all' or what_to_do == 'all':
        typewriter(DARKCYAN + "\nYour current wallet amount is:- " + BOLD + str(wallet) + ' dollars.' + END + DARKCYAN + '\nYour current health is:- ' +
                   BOLD + str(health) + END + DARKCYAN + "\nYour current inventory looks like this:- \n" + BOLD + str(inventory) + END)
        health -= 5
        typewriter(BLUE + BOLD + '\n\nBack to map...' + END)
        sleep(0.2)
        clear()
        all()

      else:
        typewriter(RED + BOLD + '\nInvalid input!\n' + END)
        health -= 5
        typewriter(BLUE + BOLD + '\nBack to map...' + END)
        sleep(0.2)
        clear()
        all()

    # Exit
    if place == '6' or place == 'exit':
      typewriter1(GREEN + BOLD + "\nExit successful!\n")

  # Accessing all of the functions
  map()
  bank()
  wstore()
  hospital()
  stunt_jump()
  check_profile()


# All()
ask()
all()

typewriter1(gameover)
