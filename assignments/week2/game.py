import timeit
from colorama import init, Fore, Style
import time
import sys
import random

knowledge = 0
stress = 0
social = 0
day = 1
init(autoreset=True)

def story_text(text, delay=0.05, color=Fore.BLUE,):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
print("Welcome to: ")
print(" ░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░▒▓████████▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░                                                                                                                                        ")
print("░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ")
print("░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ")
print(" ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░   ")
print("       ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ")
print("       ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ")
print("░▒▓███████▓▒░   ░▒▓█▓▒░    ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░ ")

print("\n A choose-your-own-adventure game")

print("________________________________________________________________________________________________________________________________________________")

story_text("\n You are a student studying Digital Media at Leuphana Univerity.", delay=0.05)
story_text("\n In a week, theres gonna be a big test. How will you spend your time in a week in the life of a student?", delay=0.05)
story_text("\n MONDAY MORNING. You wake up. No lectures today. It is nice and calm outside. Birds are singing their songs, \n you feel like nothing in the world can stop you today", delay=0.05)


def handle_choice(choice, options):
    action = options.get(choice)
    if action:
        action()
    else:
        print("Wrong input. Try writing the numbers of the choices given")
        return False
    return True
def stats():
    global knowledge, stress, social, day
    story_text(f"knowledge=^ {knowledge} stress = {stress} social = {social}", delay=0.05)
def start():
    story_text("\n But how are you going to spend your day? \n 1) Study for the test \n 2) Do something social instead", delay=0.05)
    options = {
        "1": study_test,
        "2": social_1,
    }
    while not handle_choice(input("> "), options):
        pass

def study_test():
    global knowledge, stress, social, day
    if day <= 2:
        story_text("You decided to study. Good choice. After all, you want to get a degree. ", delay=0.05)
        knowledge += 1
        stress += 1
        if random.random() < 0.33:
            social -= 1
        stats()
        studying()
    if day == 3:
        story_text("You decided to study. Good choice. After all, you want to get a degree. ", delay=0.05)
        story_text("But what can you study on the last day?", delay=0.05)
        if knowledge < 2:
            story_text("You procrastinated a LOT during the last week and there is still much catching up to be done", delay=0.05)
            story_text("Should you do an all-nighter? 1) yes 2) no", delay=0.05)
            options = {
                "1": all_nighter,
                "2": no_nighter,
            }
            while not handle_choice(input("> "), options):
                pass
        else:
            story_text("As you have already studied a lot, you can just take one last look at everything and then call it a day", delay=0.05)
            knowledge += 1
            end()

def social_1():
        story_text("Studying is for losers. Lets do something fun instead. But what?", delay=0.05)
        story_text("Will you 1) go to a party or 2) do sports?", delay=0.05)
        options = {
            "1": party,
            "2": sports,
        }
        while not handle_choice(input("> "), options):
            pass
def sports():
    global knowledge, stress, social, day
    story_text("Which sport are you going to try?", delay=0.05)
    type_sport = input()
    story_text(f"You try {type_sport}.", delay=0.05)
    if random.random() < 0.40:
        story_text(f"You are amazing at {type_sport}!", delay=0.05)
        story_text(f"Everybody cheers for you and the coach asks you if you want to be on the university team!", delay=0.05)
        story_text("Will you 1) join  or 2) not", delay=0.05)
        options = {
            "1": join_team,
            "2": dont_team,
        }
        while not handle_choice(input("> "), options):
            pass
    else:
        story_text(f"Disaster! Everybody laughs at you. You forgot you were a Digital Media student.",
                   delay=0.05)
        story_text(f"You are not got at sports!", delay=0.05)
        social -= 1
        next_day()
def join_team():
    global knowledge, stress, social, day
    story_text(f"You join the sports team. This is gonna take up a lot of your spare time, but you're GOOD.",
               delay=0.05)
    social += 2
    stress += 1
    stats()
    next_day()

def dont_team():
    global knowledge, stress, social, day
    story_text(f"You dont join the team but the question itself was good enough to boost your ego and social standing.", delay=0.05)
    social += 1
    stats()
    next_day()

def party():
    global knowledge, stress, social, day
    social += 1
    story_text("Yeah! Lets go to a party.", delay=0.05)
    stats()
    if random.random() < 0.35:
        story_text("The party is really fun.", delay=0.05)
        story_text("But what is especially fun is looking at the very attractive person in the corner", delay=0.05)
        story_text("Will you 1) approach them or 2) leave it be", delay=0.05)
        options = {
            "1": flirt,
            "2": afraid,
        }
        while not handle_choice(input("> "), options):
            pass
    else:
        story_text("The party is kind of lame. You go home early. At least you went to a party", delay=0.05)
        stress -= 1
        stats()
        next_day()

def flirt():
    global knowledge, stress, social, day
    story_text("What are you going to say to them", delay=0.05)
    line = input()
    story_text(f"You approach the attractive person: 'Hi'. They answer: 'Hi'. '{line}'", delay=0.05)
    if random.random() < 0.30:
        story_text("They laugh. 'You seem nice. You wanna have my number?'", delay=0.05)
        story_text("You just  got a LOVE INTEREST! As a Digital Media student! You Win!", delay=0.05)
        story_end()
    else:
        story_text("-'What? Get out of my face! You are disgusting!'", delay=0.05)
        story_text("They walk away. You dont know what you have done wrong.", delay=0.05)
        story_text("This evening it gets hard to sleep as your stomague aches and feel bad about the outcome of the party", delay=0.05)
        social -= 1
        stress += 1
        stats()
        next_day()

def afraid():
    global knowledge, stress, social, day
    story_text("You spend the rest of the evening awkwardly standing a few meters away from the attractive person", delay=0.05)
    story_text("On the way back home you are very angry at yourself for not managing to approach them", delay=0.05)
    stress += 1
    stats()
    next_day()
def studying():
    global knowledge, stress, social, day
    story_text("What topic are you going to study for? ", delay=0.05)
    topic = input()
    story_text(f"Great! You are going to study {topic} for the test.", delay=0.05)
    story_text(f"You spend your whole evening studying {topic}.", delay=0.05)
    if random.random() < 0.70:
        knowledge += 1

        story_text(
            "At first, everything seems stupid and wrong. But after a while, you start to get your head around the topic. ",
            delay=0.05)
    else:
        story_text("Hours pass and you look out of the window. Its getting dark.", delay=0.05)
        story_text("You realise that you didn't remember anything you just studied", delay=0.05)
    stats()
    if day == 1:
        next_day()
    elif day == 2:
        third_day()

def next_day():
    global knowledge, stress, social, day
    day += 1
    story_text("[...]", delay=0.05)
    story_text("WEDNESDAY LUNCH. You just had the most boring lecture of all time,", delay=0.05)
    story_text("But now, your lectures for today are finally over.", delay=0.05)
    story_text("In your head, you start planing the rest of your spare day", delay=0.05)
    story_text("How should you spend it? Should you 1) study some more or 2) do something else?", delay=0.05)
    options = {
        "1": study_test,
        "2": social_2,
    }
    while not handle_choice(input("> "), options):
        pass

def social_2():
    story_text("You find a handout advertising for the formation of a local band. Being in a band sounds cool,", delay=0.05)
    story_text("maybe YOU could do that.", delay=0.05)
    story_text("As you arrive at their practice room, the band is in a heated debate about their future band name.", delay=0.05)
    story_text("Before you can even introduce yourself, they ask you:'How would you call our band?'", delay=0.05)
    band_name = input()
    story_text(f"'{band_name}? Thats a cool name! Lets use that one. Youre in!'", delay=0.05)
    story_text("What kind of instrument do you play? 1) guitar 2) drums", delay=0.05)
    options = {
        "1": guitar,
        "2": drums,
    }
    while not handle_choice(input("> "), options):
        pass
def guitar():
    global knowledge, stress, social, day, band_name
    story_text("So you decided to play guitar. You look so cool!", delay=0.05)
    social += 1
    stats()
    if random.random() < 0.10:
        story_text(f"And this is the story of how {band_name} got formed.", delay=0.05)
        story_text("Soon enough they got very famous and lived happyly ever after while touring the world", delay=0.05)
        story_text("You WIN!", delay=0.05)
        story_end()
    else:
        third_day()
def drums():
    global knowledge, stress, social, day, band_name
    story_text("So you decided to play drums. Thats good for releasing stress!", delay=0.05)
    stress -= 1
    stats()
    if random.random() < 0.10:
        story_text(f"And this is the story of how {band_name} got formed.", delay=0.05)
        story_text("Soon enough they got very famous and lived happyly ever after while touring the world", delay=0.05)
        story_text("You WIN!", delay=0.05)
        story_end()
    else:
        third_day()
def third_day():
    global knowledge, stress, social, day
    day += 1
    story_text("[...]", delay=0.05)
    story_text("SUNDAY MORNING. Today is the LAST DAY before the test.", delay=0.05)
    story_text(
        "The weather perfectly reflects your mood as you hear the drumming sound of the raindrops against your window",
        delay=0.05)
    story_text("Do you have the mental capacity to 1) study on this day or should you 2) distract your mind?", delay=0.05)
    options = {
        "1": study_test,
        "2": social_3,
    }
    while not handle_choice(input("> "), options):
        pass
def social_3():
    global knowledge, stress, social, day
    if knowledge < 2:
        stress += 1
    story_text("You decide to eat out to disctract your mind", delay=0.05)
    story_text("A student has finite spending capabilities ", delay=0.05)
    story_text("How much money do you want to spend (In €)?", delay=0.05)
    budget = int(input())
    if budget <= 0:
        story_text("Thats not how money works. Try a positive number.", delay=0.05)
        social_3()
    elif budget <= 6:
        story_text("You eat at the Leuphana mensa. its nothing special but its fun to meet other people", delay=0.05)
        social += 1
        end()
    elif 6<= budget >=10:
        story_text("You eat at a fast food restaurant. Its unhealthy but really tasty!", delay=0.05)
        social += 1
        stress -= 1
        end()
    elif 10<= budget >=20:
        story_text("You eat at a real restaurant.", delay=0.05)
        story_text(
            "Its nice to do that once in a while but youre anxious about your budget for the rest of the month",
            delay=0.05)
        social += 1
        stress += 1
        end()
    elif budget <=20:
        story_text("Do you want to eat at a michelin restaurant? You dont have that kind of money!", delay=0.05)
        story_text("Try again with something more reasonable.", delay=0.05)
        social_3()
def all_nighter():
    global knowledge, stress, social, day
    story_text("The hours pass and pass and pass and you work and work and work.", delay=0.05)
    story_text("As the dawn breaks, you swear to yourself that you will never do this again",delay=0.05)
    stress += 2
    knowledge += 2
    stats()
    end()
def no_nighter():
    global knowledge, stress, social, day
    story_text("Trying to learn everything in one night just stresses you out and achieves nothing.", delay=0.05)
    story_text("You will just take a short look at everything and hope for the best.", delay=0.05)
    knowledge += 1
    stats()
    end()
def end():
    global knowledge, stress, social, day
    story_text("Now the day of the test as come. Will you pass?", delay=0.05)
    story_text("[...]", delay=0.2)
    if knowledge == 5:
        story_text("You passed!", delay=0.05)
    elif knowledge  <=4:
        if random.random() < 0.70:
            story_text("You passed!", delay=0.05)
        else:
            story_text("You failed!", delay=0.05)
    elif knowledge <= 2:
        if random.random() < 0.40:
            story_text("You passed!", delay=0.05)
        else:
            story_text("You failed!", delay=0.05)
    elif knowledge <= 1:
        if random.random() < 0.20:
            story_text("You passed!", delay=0.05)
        else:
            story_text("You failed!", delay=0.05)
    if stress >= 3:
        story_text("But at what cost? You lived a very stressful life. You cant keep it up like that or youre gonna get a burnout", delay=0.05)
        story_text("You most certainly didnt win", delay=0.05)
    if social <= 1:
        story_text(
            "Nobody knows you at the university. While other will already have formed families and friends/ buisness partners for a lifetime",
            delay=0.05)
        story_text(
            "You will just be a lonely person with a degree.", delay=0.05)
        story_text("You most certainly didnt win", delay=0.05)
    elif social >= 3:
        story_text("But who cares? You're the coolest person on campus 😎", delay=0.05)
    stats()
    story_end()
def story_end():
    story_text("⭐️Do you want to try again?⭐️ (yes/no)", delay=0.05)
    choice = input("> ").strip().lower()
    if choice == "yes":
        new_state = GameState()
        start(new_state)
    else:
        story_text("Thanks for playing!", delay=0.05)
        sys.exit()
        ##implement social and stress level to affect score
start()

