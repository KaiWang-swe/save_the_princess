from tools import print_pause
import characters
import random


def play_home(hero):
    print_pause(
        "You are sitting in the quiet comfort of your home, engrossed in the pages of an ancient book.\n"
        "The weathered text tells a tale from long ago: a beautiful princess, imprisoned within the dark recesses of a foreboding dungeon, guarded by a fearsome dragon.\n"
        "Legend holds that only the bravest of knights could ever hope to defeat the dragon and rescue the princess."         
                )
    print_pause(
        "As you ponder the story, a memory surfaces—a tale once whispered by your grandfather during a chilly evening by the fire.\n"
        "He spoke of the highest mountain in the north, a daunting peak shrouded in perpetual mists, where the most formidable sword was hidden away by ancient forces.\n"
        "This sword, imbued with untold powers, was said to be capable of conquering any foe, no matter how mighty."         
                )
    print_pause(
        "Now, with the legend of the princess echoing in your mind, you find yourself contemplating a daring adventure.\n"
        "Could the fabled sword be the key to saving the princess?\n"
        "Could you, perhaps, be the knight foretold by legend?"         
                )
    print_pause(
        "1. Go straight to the dungeon.\n"
        "2. Detour to the mountain.\n"
        "3. Sitting at home and chill. "         
                )
    while True:
        choice = input("Please enter a valid option(enter a number): ")
        try:
            if int(choice) == 1:
                return play_dungeon(hero)
            elif int(choice) == 2:
                return play_mountain(hero)
            elif int(choice) == 3:
                print_pause("You lose. Perhaps the title of the game was a clue after all.")
                return replay()
        except ValueError:
            print_pause("Not a number, please try again.")


def play_mountain(hero):
    yeti = characters.Yeti(random.randint(2,4))
    print_pause(
        "You head to the mountain and find a yeti stuck at the entrance of a cave.\n"
        "What would you do?"    
                )
    print_pause(
        "1. Offer to help the yeti.\n"
        "2. sneak attack the yeti.\n"
        "3. Turn your back and leave. "         
                )     
       
    while True:
        choice = input("Please enter a valid option(enter a number): ")
        try:
            if int(choice) == 1:
                print_pause("Grateful, the Yeti thanks you and offers you a sword he found in the cave.")
                hero.equip_sword = True
                print_pause("Equipped with the new sword, you head to the dungeon with confidence.")
            elif int(choice) == 2:
                print_pause("The Yeti cannot fight back. You win but find nothing in the cave.")
                print_pause("You head to the dungeon with bare hands.")
            elif int(choice) == 3:
                print_pause("You leave the mountain with empty hands.")                    
            return play_dungeon(hero)
        except ValueError:
            print_pause("Not a number, please try again.")


def play_dungeon(hero):
    dragon = characters.Dragon(random.randint(7,9))
    print_pause(
        "After a long journey, you finally enter the dungeon and come face-to-face with the dragon.\n"
        "The dragon breathes fire.\n"
        "You shake uncontrollably."
                )
    print_pause(
        "1. Fight the dragon.\n"
        "2. Flee the scene."        
                )     
       
    while True:
        choice = input("Please enter a valid option(enter a number): ")
        try:
            if int(choice) == 1:
                battle_result = random.choices(["win","lose"], weights=[hero.strength, dragon.strength], k = 1)[0] if not hero.equip_sword else "win"
                if battle_result == "win":
                    print_pause("Congratulations, you've won!")
                    print_pause("You've saved the princess and become a hero.")
                    return replay()
                else:
                    print_pause("Unfortunately, you've lost.")
                    return replay()
            elif int(choice) == 2:
                print_pause("You lose. Perhaps the title of the game was a clue after all.")
                return replay()             
        except ValueError:
            print_pause("Not a number, please try again.")



def replay():
    user_input = input("Play again? y/n: ").lower()
    if user_input == "y":
        return play()
    elif user_input == 'n':
        print_pause("Goodbye.")
        return 
    else:
        print_pause("Please enter 'y' or 'n'.")
        return replay()

def play():
    hero = characters.Hero(random.randint(4,6),equip_sword=False)
    play_home(hero)


if __name__ == "__main__":
    play()