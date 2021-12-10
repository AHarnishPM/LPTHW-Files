from sys import exit


def gold_chest():
    print "\"You survived, now take your gold before I do.\" says a mysterious voice"
    print "You take the gold and are never seen again."
    exit(0)

def dead(why):
    print why, "Nice try."
    exit(0)

def repeat_question():
    retry = 0
    while retry < 10:
        raw_input("> ")
        print "Wrong answer. Try again."
        retry += 1
    dead("There was no right answer.")


def start():
    print "You are sitting under a tree.\n Suddenly three paths appear.\n Pick one."
    choice = raw_input("> ")

    if choice == "1":
        path_one()

    elif choice == "2":
        path_two()

    elif choice == "3":
        path_three()

    else:
        dead("You can't choose a path, so you die a lonely death.")

def path_one():
    print "You start walking on the path, and meet a stranger."
    print "He offers you a choice between a parachute (1) and a scuba tank (2)."
    print "Which do you choose?"

    choice = raw_input("1 or 2? > ")

    if choice == "1":
        print "Good choice, parachutes come in handy."
        item = choice

    elif choice == "2":
        print "That's a weird one, when would you use a scuba tank on a path?"
        item = choice

    else:
        dead("You choose nothing and the stranger eats you.")

    print "You continue your journey on the path when suddenly it splits."
    print "The path to the left goes up, and the right path goes down."
    print "Where do you go?"

    choice = raw_input("> ")

    if choice == "left":
        print "You keep walking up the path until you reach a cliff."
        print "Suddenly, a bear starts roaring behind you."
        print "Your only option is to jump!"

        if item == "1":
            print "Luckily, you have a parachute."
            print "You slowly glide down and see a treasure chest when you land."
            gold_chest()

        elif item == "2":
            dead("You plummet to your death with your fancy scuba tank.")

        else:
            dead("You die mysteriously, im not sure how you got this far.")

    elif choice == "right":
        print "You walk down the path until suddenly the dirt falls under your foot."
        print "You fall in to deep water, but see something shiny far away."

        if item == "2":
            print "You put on your handy dandy scuba tank and swim to the chest."
            gold_chest()

        elif item == "1":
            dead("You drown while getting untangled from your parachute.")

        else:
            dead("You are very special, but drown anyways.")


def path_two():
    print "You start walking down the path"
    print "Suddenly you see an extremely obese bear in the path"
    print "How do you get past it?"

    choice = raw_input("> ")

    if "run" in choice:
        dead("You start to run, but the bear eats you.")

    elif "kill" in choice:
        dead("You try to kill the bear but it eats you.")

    elif "sing" in choice:
        print "You sing to the bear and it happily moves out of the way."
        print "You quickly run past it before it changes it's mind."
        print "It was sitting in front of a chest of gold."
        gold_chest()

    else:
        dead("Bad plan. You get mauled to death.")


def path_three():
    print "You start walking but are stopped by an elderly man"
    print "He says \"Guess the secret word to pass\""
    print "\"Or a terrible death you shall have\""

    repeat_question()


start()
