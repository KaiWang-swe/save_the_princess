from tools import print_pause
import characters
import random


def play_home(hero):
    print_pause(
        "You are sitting at home, reading an ancient book about"
        " a princess guarded by a dragon."
    )
    print_pause(
        "A memory of your grandfather's tales about a mighty sword"
        " hidden in the north mountains comes to mind."
    )
    print_pause(
        "You think about embarking on an adventure to find this sword"
        " and save the princess."
    )
    print_pause(
        "1. Go straight to the dungeon.\n"
        "2. Detour to the mountain.\n"
        "3. Sit at home and chill."
    )
    while True:
        choice = input("Choose an option (1-3): ")
        try:
            if int(choice) == 1:
                return play_dungeon(hero)
            elif int(choice) == 2:
                return play_mountain(hero)
            elif int(choice) == 3:
                print_pause("You lose. Perhaps the title was a clue.")
                return replay()
        except ValueError:
            print_pause("Please enter a number.")


def play_mountain(hero):
    yeti = characters.Yeti(random.randint(2, 4))
    print_pause(
        "You find a yeti at the entrance of a cave on the mountain."
    )
    print_pause(
        "1. Help the yeti.\n"
        "2. Sneak attack the yeti.\n"
        "3. Leave the mountain."
    )

    while True:
        choice = input("Choose an option (1-3): ")
        try:
            if int(choice) == 1:
                print_pause(
                    "The Yeti thanks you and gives you a sword from the cave."
                )
                hero.equip_sword = True
                print_pause("With the new sword, you head to the dungeon.")
                return play_dungeon(hero)
            elif int(choice) == 2:
                print_pause("You win but find nothing. \
                            You head to the dungeon.")
                return play_dungeon(hero)
            elif int(choice) == 3:
                print_pause("You leave with nothing.")
                return play_dungeon(hero)
        except ValueError:
            print_pause("Please enter a number.")


def play_dungeon(hero):
    dragon = characters.Dragon(random.randint(7, 9))
    print_pause(
        "You face the dragon in the dungeon, trembling as it breathes fire."
    )
    print_pause(
        "1. Fight the dragon.\n"
        "2. Flee."
    )

    while True:
        choice = input("Choose an option (1-2): ")
        try:
            if int(choice) == 1:
                battle_result = random.choices(
                    ["win", "lose"],
                    weights=[hero.strength, dragon.strength], k=1
                )[0] if not hero.equip_sword else "win"
                if battle_result == "win":
                    print_pause("You've saved the princess and become a hero.")
                    return replay()
                else:
                    print_pause("Unfortunately, you've lost.")
                    return replay()
            elif int(choice) == 2:
                print_pause("You lose. The title of the game was a hint.")
                return replay()
        except ValueError:
            print_pause("Please enter a number.")


def replay():
    user_input = input("Play again? y/n: ").lower()
    if user_input == "y":
        return play()
    elif user_input == 'n':
        print_pause("Goodbye.")
    else:
        print_pause("Please enter 'y' or 'n'.")
        return replay()


def play():
    hero = characters.Hero(random.randint(4, 6), equip_sword=False)
    play_home(hero)


if __name__ == "__main__":
    play()