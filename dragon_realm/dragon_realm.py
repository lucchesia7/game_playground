import random
import time

def display_intro():
    print('''
          You are in large catacomb, the roof broken to pieces, allowing natural light to seep into the otherwise dark area. 
          In front of you, you see pathways. Each of these paths lead to a cave with a dragon sleeping inside it. In one of the caves,
          the dragon is friendly and will share his hoard with you. In the other cave, the Dragon is greedy and hungry. 
          He will choose to eat you on sight.
          \n''')
    
def choose_cave():
    cave = ''
    while cave != '1' and cave !='2':
        print("Which cave will you go into? (1 or 2)")
        cave = input()
        
    return cave

def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('''
          It is dark and musty. You feel along the rough, 
          damp walls as you fumble your way through the darkness, you finally approach the light of the dragon\'s cave.
          As you step into the mouth of the cave, the dragon stirs and...
          ''')
    # Delays print speed and holds terminal output for x seconds.
    time.sleep(2)

    friendly_cave = random.randint(1,2)

    if chosen_cave == str(friendly_cave):
        print('The dragon is friendly and shares his hoard with you!')
    else:
        print('The dragon snaps the jaws of his maw around you so fast and tight, you can\'t react. Game Over.')
play_again = 'yes'
while play_again in ['yes', 'y']:
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)
    print('Do you want to play again? (yes or no)')
    play_again = input()