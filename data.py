import sys
import time
from cat import Cat
from user import User
from figure import show


def my_print(text): # Print style: print letter one by one
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)
        print()
        time.sleep(0.1)


def greeting():
    global user, cat
    my_print('Hello! This is a game of raising an electronic cat.')
    time.sleep(0.3)
    my_print('Please enter your details first!')
    print()
    time.sleep(0.3)
    user_name = input('Please enter your name: ')
    user = User(user_name)
    print()
    time.sleep(0.3)
    my_print(f'Hello, {user_name}!')
    time.sleep(0.3)
    my_print('You have $100 and 5 credit points at the start:')
    print(user)
    print()
    time.sleep(0.3)
    my_print('Now, we have assigned you a cat, but it doesn\'t belong to you currently.')
    my_print('You can take actions such as feed it or play with it to increase your credit.')
    my_print('When your credit reaches 10, you officially own this cat.')
    print()
    cat_name = input('Please give your cat a name: ')
    cat = Cat(cat_name)
    my_print(f'Following is the initial status of {cat_name}:')
    print(cat)
    my_print('The maximum for each criteria is 5. If Health drops to 0, the cat will die.')
    print()
    time.sleep(0.5)
    while True:
        call = input(f'Try to call it by typing \"Hi, {cat_name}\": ')
        if call == f'Hi, {cat_name}':
            show('cat')
            break
    time.sleep(1)
    my_print('Now, start your game!')
    return user, cat


def update(category: str, action: str, quantity: int):
    global user, cat
    if category == 'feed':
        if action == 'increase':
            if cat.energy < 5:
                cat.energy += quantity
                user.amount -= 10
                show('feed') # 'Yammy' figure 
                print(f' 🍗 + {quantity}', ' 💰 - $10', sep = '\n') 
            elif cat.energy == 5:
                if cat.health == 5:
                    print(f' {cat.name} is full!')
                elif cat.health < 5:
                    cat.health += 1
                    print(f' {cat.name} is full! 🟢+ 1')
            
        elif action == 'decrease':
            if cat.energy - quantity < 0:
                cat.energy = 0
            else:
                cat.energy -= quantity
            print(f' 🍗 - {quantity}')

    elif category == 'health':
        if action == 'increase':
            if cat.health == 5:
                pass
            elif cat.health < 5:
                cat.health += quantity
            print(f' 🟢 + {quantity}')
        elif action == 'decrease':
            if cat.health - quantity < 0:
                cat.health = 0
            else:
                cat.health -= quantity
            print()
            print(f' Energy is 0!\n 🟢 - {quantity}')


    elif category == 'mood':
        if action == 'increase':
            if cat.mood < 5:
                cat.mood += quantity
                print(f' 🧡 + {quantity}')
            elif cat.mood == 5 and cat.energy != 0 and cat.health > 2:
                user.credit += 1
                print(f' Full 🧡! ⭐️+ 1')
                
        elif action == 'decrease':
            if cat.mood - quantity < 0:
                cat.mood = 0
            else:
                cat.mood -= quantity
            print(f' 🧡 - {quantity}')

    elif category == 'treat':
        cat.energy = 3
        cat.health = 3
        cat.mood = 0
        user.amount -= 40
        print(' 💰 - $40')
        print(cat)
        print(f'{cat.name} recovered, but is in a bad mood!')
    

    elif category == 'find':
        user.amount -= 30
        print(' 💰 - $30')
        print(f' {cat.name} is back!')
