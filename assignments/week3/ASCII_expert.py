import random
import time
import sys
from colorama import init, Fore, Style
#Definitions
def main_text(text, delay, color=Fore.YELLOW,):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
def art_text(text, color=Fore.BLUE,):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
def family_text(text, color=Fore.LIGHTBLUE_EX,):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()

names = [ "Bumbo", "Tilly", "Mondo", "Lula", "Thunderfoot", "Nala", "Jumbo", "Poppy",
          "Sable", "Tank", "Ellie", "Matari", "Toto", "Kibo", "Zara", "Brutus", "Willow",
          "Dundu", "Maji", "Pebble", "Paul"]
main_text("Look at this beautiful elephant!\n", delay=0.1)
art_text("    _    _\n")
art_text("   /=\\\"\"/= \\\n")
art_text("  (=(0_0 |=)__\n")
art_text("   \\_\\ _/_/   )\n")
art_text("     /_/   _  /\\\n")
art_text("    |/ |\\ || |\n")
art_text("       ~ ~  ~\n")
main_text("Its beautiful, but right now, its alone and sad. It needs a family!\n", delay=0.1)
main_text("Can you help create it? \n", delay=0.1)
while True:
    main_text("How many parents should there be?\n>", delay=0.1)
    parents = input()
    if parents.isdigit():
        number_parents = int(parents)
        if 1 <= number_parents:
            if number_parents >= 10:
                main_text("these are too many parents. They will always fight. \n", delay=0.1)
            else:
                break
        else:
            main_text("Stop making fun of a sad elephant! You monster! \n", delay=0.1)
    else:
        main_text("This is not a real number. Come on, the elephant is sad!\n", delay=0.1)
while True:
    main_text("How many brothers and sisters should there be?\n>", delay=0.1)
    children = input()
    if children.isdigit():
        number_children = int(children)
        if 1 <= number_children:
            if number_children >= 10:
                main_text("these are too many children. The parents wont have enough time for everybody. \n", delay=0.1)
            else:
                break
        else:
            main_text("The parents want to have some children. Fulfill their wish! \n", delay=0.1)
    else:
        main_text("This is not a real number. Come on, the elephant is sad!\n", delay=0.1)

for n in range(number_parents):
    art_text("                        ____\n")
    art_text("                   .---'-    \\ \n")
    art_text("      .-----------/           \\ \n")
    art_text("     /           (         ^  |   __\n")
    art_text("&   (             \\        0  /  / .'\n")
    art_text("'._/(              '-'  (.   (_.' /\n")
    art_text("     \\                    \\     ./\n")
    art_text("      |    |       |    |/ '._.'\n")
    art_text("       )   @).____\\|  @ |\n")
    art_text("   .  /    /       (    |    \n")
    art_text("  \\|, '_:::\\  . ..  '_:::\\ ..\\).\n")
for n in range(number_children):
    art_text("    _    _\n")
    art_text("   /=\\\"\"/= \\\n")
    art_text("  (=(^_^ |=)__\n")
    art_text("   \\_\\ _/_/   )\n")
    art_text("     /_/   _  /\\\n")
    art_text("    |/ |\\ || |\n")
    art_text("       ~ ~  ~\n")
main_text("the names of the parents are: \n", delay=0.1)
for n in range(number_parents):
    p = random.choice(names)
    main_text(p + ", ", delay=0.1)
    names.remove(p)
main_text("\nthe names of the children are: \n", delay=0.1)
for n in range(number_children):
    c = random.choice(names)
    main_text(c + ", ", delay=0.1)
    names.remove(c)
main_text("How should the family be called?\n>", delay=0.1)
family = input()
main_text("This is the\n", delay=0.5)
family_text(f"{family}-family",)