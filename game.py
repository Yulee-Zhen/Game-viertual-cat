import random
from cat import Cat
from user import User
from figure import show
from data import *


def alive(user, cat):
    if cat.health == 0:
        print()
        print(f'\033[1;31m ⚠ {cat.name} is sick, need $40 for the treatment.\033[0m')
        print()
        treat = input('[Yes | No]:').lower()
        if treat == 'yes':
            print()
            update('treat', '', 0)
            return True
        elif treat == 'no':
            print()
            print(f'\033[1;31m 💀 Unfortunately, {cat.name} is dead. 💀\033[0m')
            return False
    elif 0 < cat.health < 3:
        print()
        print(f'\033[1;31m ⚠ {cat.name} is of low health!\033[0m')
        return True
    elif cat.health >= 3:
        return True


def game():
    user, cat = greeting()
    while True:
        if not alive(user, cat):
            return         
        elif user.credit >= 10:
            exit(f'Congratulations! Your credit reaches 10, you are a good owner! {cat.name} is yours!')
        elif user.credit == 0:
            exit(f'Your credit is 0, you lose qualification to keep {cat.name}!')
        elif user.amount <= 0:
            exit(f'You are bankrupt, you lose qualification to keep {cat.name}!')

        print()
        command = input('What to do [Feed | Play]: ').lower()
        if command in ('feed', 'play'):
            if 0 < cat.energy < 3:
                print()
                print(f'\033[1;31m ⚠ Warning: {cat.name} is of low energy!\033[0m')
                print()
            elif cat.energy <= 0:
                print()
                print('\033[1;31m ⚠ Warning: Energy is 0!\033[0m')
                print()
                          
            if command == 'feed':
                update('feed', 'increase', 1) 
                            
            elif command == 'play':
                place = input('[Outdoor | Cancel]: ').lower()
                if place == 'outdoor':
                    
                    if cat.energy == 0:
                        update('health', 'decrease', 3)
                        update('mood', 'decrease', 1)
                    else:
                        update('feed', 'decrease', 1)
                        update('mood', 'increase', 1)
                    show('outdoor')
                    print(' Fantastic! I love outdoor games!')

                    if random.randint(1, 10) == random.randint(1, 10): # 10% probability of lost
                        print()
                        print(f'\033[1;31m ⚠ Accident: OMG! {cat.name} is lost!\033[0m')
                        print()
                        find = input('Post a lost notice ($30) to find it back (yes/no): ').lower()
                        if find == 'yes':
                            update('find', '', 0)
                        elif find == 'no':
                            print()
                            exit('Unfortunately! You lost your cat!')
                elif place == 'cancel':
                    continue

        elif command == 'my status':
            print(user)
        elif command == 'cat status':
            print(cat)
        else:
            show('confuse')
            print(f'{cat.name} seems confused, please enter valid command!')
        


def main():
    game()






if __name__ == '__main__':
    main()