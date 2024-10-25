import time
import os

#global variables declaration
pClass = ""
newpClass = False

def loading3secs():
    os.system('cls')# Clearing the Screen
    print ('''
                                    
                            
                            
    .::.                    
    'M .-;-.-
    (J ( ( ( ( 
    `P `-;-`-
    `::'                    
                            
                            
    ''')
    time.sleep(0.5)
    os.system('cls')# Clearing the Screen

    print ('''
                        
                            
                            
    .::.                    
    'M .-;-.-.-.-.-.-.-.
    (J ( ( ( ( ( ( ( ( ( 
    `P `-;-`-`-`-`-`-`-`
    `::'                    
                            
                            
    ''')
    time.sleep(0.5)
    os.system('cls')# Clearing the Screen

    print ('''
                                    ___
                            ( ((
                            ) ))
    .::.                    / /(
    'M .-;-.-.-.-.-.-.-.-.-/| ((:::::::::
    (J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====
    `P `-;-`-`-`-`-`-`-`-`-\| ((:::::::::
    `::'                    \ \(
                            ) ))
                            (_((
    ''')
    time.sleep(0.5)
    os.system('cls')# Clearing the Screen

    print ('''
                                    ___
                            ( ((
                            ) ))
    .::.                    / /(
    'M .-;-.-.-.-.-.-.-.-.-/| ((:::::::::::::::::::::
    (J ( ( ( ( ( ( ( ( ( ( ( |  ))   -================
    `P `-;-`-`-`-`-`-`-`-`-\| ((:::::::::::::::::::::
    `::'                    \ \(
                            ) ))
                            (_((
    ''')
    time.sleep(0.5)
    os.system('cls')# Clearing the Screen

    print ('''
                                    ___
                            ( ((
                            ) ))
    .::.                    / /(
    'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
    (J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
    `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
    `::'                    \ \(
                            ) ))
                            (_((
    ''')
    time.sleep(0.5)
    os.system('cls')# Clearing the Screen
def starting():
    print('''
                                    |>>>
                                    |
                        |>>>      _  _|_  _         |>>>
                        |        |;| |;| |;|        |
                    _  _|_  _    \\.    .  /    _  _|_  _
                |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
                \\..      /    ||;   . |    \\.    .  /
                    \\.  ,  /     ||:  .  |     \\:  .  /
                    ||:   |_   _ ||_ . _ | _   _||:   |
                    ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                    ||:   ||.    .     .      . ||:  .|
                    ||: . || .     . .   .  ,   ||:   |       \,/
                    ||:   ||:  ,  _______   .   ||: , |            
                    ||:   || .   /+++++++\    . ||:   |
                    ||:   ||.    |+++++++| .    ||: . |
                __ ||: . ||: ,  |+++++++|.  . _||_   |
        ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
    -~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~
        ''')


    print ("Welcome to your Dungeon Castle!")                                                                  # flavour 
    time.sleep(1)                                                                                              # text for
    print ("You will choose your own adventure.")                                                              # the beginning
    print ("Use the words to make your choices. Good Luck!")
    time.sleep(1)
    print("You dismount your horse, Septer, in the front of a gagtunan white marble castle.")
    time.sleep(1)
    print("Your horse seems spooked. Do you take your sword and Shield, your wand or your bow and arrows?") # checking what class
    global pClass
    global newpClass
    pClass = input("Type, S, W or B?").lower()
    newpClass = False

    while pClass != "s" and pClass != "w" and pClass != "b":
        newpClass = False
        pClass = input("Type, S, W or B?").lower()
    else:
        newpClass = True


    loading3secs() #loading between sections and clears the screen

    print('''
        
    -_-_-_-_-      -_-_-_-_-
        |_|_|_|        |_|_|_|
        ||_|_||        ||_|_||
        |_|_|_|________|_|_|_|
        ||_|_|_|_|_|_|__|_|_||
        |_|_|_|_|_|_|_|_|_|_||
        ||_|_|_|_|_|_|_|_|_|_|
        |_|_|_|_|_###_|_|_|_||
        ||_|_|_|#######|_|_|_|
        |_|_|_|_#######_|_|_||
        ||_|_|_|#######|_|_|_|
    ___|_|_|_|_#######_|_|_||___
    :::\|_|_|_|#######|_|_|_/:::
    ::::::::::::::::::::::::::::
    ::::__________________::::::
    :::/&&&&&&&&&&&&&&&&&&\___
    :::\&&&&&&&&&&&&&&&&&&&&&&):
    ::::\&&&&&&&&&&&&&&&&&&&&&|
    :::::|********************|
    ''')

    if pClass == "s":
        print("You take out your sword and shield of your horse. You walk forward, over the mote and to the 2 large wooden and brass doors.")
        newpClass = True
    elif pClass == "w":
        print("You take out your wand. You walk forward, over the mote and to the 2 large wooden and brass doors.")
        newpClass = True
    elif pClass == "b":
        print("You take out your bow and arrows. You walk forward, over the mote and to the 2 large wooden and brass doors.")
        newpClass = True


starting()

roomFirst = input("We made it.")
print(roomFirst)