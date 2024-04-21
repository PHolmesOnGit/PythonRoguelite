# ALPHA #

from weapons import Weapons
from round_knight import RoundKnight
from four_armed_samurai import FourArmedSamurai
from virtuous_monk import VirtuousMonk
from the_dark_bandit import TheDarkBandit
rknight = RoundKnight()
fasam = FourArmedSamurai()
vmonk = VirtuousMonk()
dbandit = TheDarkBandit()

intro = True


def startgame_amara():
    print("Starting new game as Amara")
    return ""


def startgame_acrius():
    print("Starting new game as Acrius")
    return ""


def startgame_akuma():
    print("Starting new game as Akuma")
    return ""


def startgame_alphis():
    print("Starting new game as Alphis")
    return ""


story = "4000 years ago, the world was threatened with destruction by a evil creature known as the Demon King. " \
        "An ancient warrior, Pantheon, wielded the power of the gods and defeated the demon, the ferocity of their" \
        " fight forever altered the world, separating the land into four main bodies. Pantheon is said to have" \
        "died in the aftermath of the fight."


while intro:
    character_choice = input(
        "\nSelect your character, you can also type <name>_lore to read a character's backstory and learn about their passive: \n\n"
        "Amara \nAcrius \nAkuma \nAlphis \n\nWho would you like to play as? : ").lower()

    if character_choice == "amara_lore":
        print(fasam.lore)
        print("\n ---PASSIVE--- \n")
        print(fasam.passive_lore)
    elif character_choice == "acrius_lore":
        print(rknight.lore)
        print("\n ---PASSIVE--- \n")
        print(rknight.passive_lore)
    elif character_choice == "akuma_lore":
        print(vmonk.lore)
        print("\n ---PASSIVE--- \n")
        print(vmonk.passive_lore)
    elif character_choice == "alphis_lore":
        print(dbandit.lore)
        print("\n ---PASSIVE--- \n")
        print(dbandit.passive_lore)
    elif character_choice == "amara":
        intro = False
        startgame_amara()
    elif character_choice == "acrius":
        intro = False
        startgame_acrius()
    elif character_choice == "akuma":
        intro = False
        startgame_akuma()
    elif character_choice == "alphis":
        intro = False
        startgame_alphis()
    else:
        print("That entry is not listed, check your spelling")

