from sys import exit
import time

# hub world:
def far_land():
    print "\nYou travel to a land far away."
    time.sleep(3)
    print "On your way, you are given four paths to follow."
    time.sleep(3)
    print "There is either the path of the raiders of the lost ark. To go down this road, type \'ark\'."
    time.sleep(3)
    print "Or you want to join the last crusade. Type \'crusade\' then."
    time.sleep(3)
    print "If you like a hearty meal before your exploration, visit the temple of doom and type \'doom\'."
    time.sleep(3)
    print "For a more mature experience, you might want to see the kingdom of the crytal skull. Therefore type \'skull\'."

    choice = raw_input("X ")

    if choice == "ark":
        raiders_path()
    elif choice == "crusade":
        crusade_path()
    elif choice == "doom":
        doom_path()
    elif choice == "skull":
        skull_path()
    else:
        dead("You could not even land the plane right. You crashed. End of game. I am sorry!")
        exit(0)

# raiders of the lost ark level:
def raiders_path():
    print "You are climbing into a dark cave.\nAt the end of it you find a golden figure on a rock. You curiously take it.\nA loud quiver can be heard. A huge stone ball comes crashing down..."
    time.sleep(5)
    print "What do you do? Do you run \'back\' or \'forth\'?"

    choice = raw_input("X ")

    if choice == "back":
        covenant()
    elif choice == "forth":
        dead("The ball catches up with you and crushes you...")
    else:
        dead("Standing does not help you at all. You are immediately smashed!")

def covenant():
    print "After an exhausting run and many many detours you find yourself in the middle of a weird hunt for the lost ark of the covenant.\nSomehow you end up with it, but are surrounded by your Nazi enemies..."
    time.sleep(5)
    print "You can either \'surrender\' and hand the ark over to the Nazis or \'open it\' yourself."

    choice = raw_input("X ")

    if choice == "surrender":
        happy_end("The Nazis creedily open the ark and are destroyed by the overwhelming force. You however get to live.")
    elif choice == "open it":
        dead("You bumbling fool have unleashed higher powers you cannot control. Everyone is killed!")
    else:
        dead("The Nazis shoot you for stalling.")

# the last crusade level:
def crusade_path():
    print "You fly to Europe in order to save another archaeologist, who has been captured (again by Nazis).\nYou find out he is your own father..."
    time.sleep(5)

    while True:
        print "Your father is annoying. Do you save him anyway?"

        choice = raw_input("X ")

        if choice == "yes":
            grail()
        elif choice == "no":
            dead("You continue living, but trouble yourself with horrible regrets because you did not save him. After a long remorseful life you finally die all alone.")
        else:
            error ()

def grail():
    print "Your father and you go for a vacation together but end up with the Nazis in a room full of goblets.\nThe knight guarding the place presents you with 3 goblets..."
    time.sleep(5)

    while True:
        print "Pick either 1, 2 or 3. Know that only one gives, the other two take life!"

        choice = raw_input("X ")

        if choice == "1":
            dead("Not all that shines is made of gold! The poison ends your existence!")
        elif choice == "2":
            dead("Nice try! This one might have looked good, but is filled with pure death!")
        elif choice == "3":
            happy_end("You are not blinded by the outside as you picked the cup of a carpenter. The rejuvenating energy of the grail pervades you.")
        else:
            error ()

# the temple of doom level:
def doom_path():
    print "India is a wonderful country to feast in, but also for dark savage cults.\nAfter dining with the locals, you want to see their catacombs..."
    time.sleep(5)
    print "What is the best way to be lead down to their place of worship? \'Ask politely\' or \'supply yourself as a human sacrifice\'?"

    choice = raw_input("X ")

    if "ask" in choice:
        dead("The villagers eat you alive.")
    elif "supply" or "human sacrifice" in choice:
        temple()
    else:
        start("You decide that you are not that curious and return home.")

def temple():
    print "You are led into a gigantic underground dome. Indigenous people tie you to a statue and strip off your shirt.\nA creepy looking priest is babbeling \"kalima\" and touches your chest..."
    time.sleep(5)
    print "What is the last thing you would like to do before you are sacraficed? \'Insult and scream\' at those creeps or \'pray\' to God?"

    choice = raw_input("X ")

    if choice in ["insult","scream"]:
        dead("The priest laughs at you and rips your heart out!")
    elif "pray" in choice:
        happy_end("Just before the hand of the priest grabs your heart, your sidekick arrives and saves the day!")
    else:
        dead("You wasted your last chance! The inevitable happens...")

# the kingdom of the crytsal skull level:
def skull_path():
    print "You are older and way more pissed than when you started your journey.\nYou find yourself in a deserted little village in the middle of nowhere and have no clue why you are here.\nA loud alarm goes off..."
    time.sleep(5)
    print "You realize that this is a testing area for nuclear weapons. Do you \'run away\' before the bomb detonates or \'hide in a fridge\'?"

    choice = raw_input("X ")

    if "run" in choice:
         dead("You cannot escape the blast of a nuclear bomb, idiot!")
    elif "hide" or "fridge" in choice:
         pyramid()
    else:
         dead("Ignoring it, will not make it go away. You are dematerialized by the explosion!")

def pyramid():
    print "The fridge is nuked high into the sky and lands a couple of miles away. Naturally you survive this!\nAfter reuniting with your past love and your son, fighting with the Russians, being betrayed twice by your friend and follwing mad conspiracy theories, you made it to the center hall of the pyramid..."
    time.sleep(5)
    print "Now you either \'abuse the power of the skull\' you stole from the Russians (or they stole from you) or you \'give it back to the aliens\' living in the pyramid."

    choice = raw_input("X ")

    if choice in ["abuse","power"]:
        dead("The aliens will not let you do that and abduct you to conduct all kinds of cruel experiments on you.")
    elif "give" in choice:
        happy_end_v2("As the skull is returned the aliens thank you and leave planet earth in their pyramid UFO.")
    else:
        dead("The Russians get there first and use the skull's power to convert everybody to socialism. You have failed the American people!")

# possible outcomes:
def happy_end(why):
    print why, "\nWise choice! You safely return home with the artifact in your hands. You are a true adventurer!\n"
    exit(0)

def happy_end_v2(why):
    print why, "\nWise choice! You return home without any artifact, but all well and alive.\nYou decide to retire, because you are too old for this shit!\n"
    exit(0)

def dead(why):
    print why, "\nGame over!\n"
    exit(0)

def error():
    print "\nYou have to make a choice!\n"

# welcome screen:
def welcome():
    print "\nWelcome to THE ADVENTURES OF INDIANA JONES\n"
    time.sleep(3)
    print "In this mini game you will become your favorite archaeologist and explore the mysteries of history."
    time.sleep(3)
    print "So buckle up and get ready for the experience of a lifetime!"
    time.sleep(3)
    start("")

# entering the game:
def start(why):

    while True:
       print why, "\nType \'start\' to begin a new journey and \'quit\' to abort!"

       choice = raw_input("X ")

       if choice == "start":
          far_land()
       elif choice == "quit":
           print "I am sorry for you missing out!\n"
           exit(0)
       else:
          start("Try again!\n")

welcome()
