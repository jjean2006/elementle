from colorama import Fore
import random
import os

def clear():
    os.system('clear')

def checker():
    if listguess == list(word):
        print('Good job, you got it')
        with open('done.ini', 'a') as f:
            f.write(' ' + str(index))
        quit()
    for i in listguess:
        listindex = listguess.index(i)
        if i in word.lower():
            if listguess.index(i) == word.index(i):
                listguess[listindex] = Fore.GREEN + i
            elif listguess.index(i) != word.index(i):
                listguess[listindex] = Fore.YELLOW + i
        else:
            listguess[listindex] = Fore.BLUE + i


index = random.randint(0, 117)
full = ''
places = ['first', 'second', 'third', 'fourth', 'fifth']

with open('elements.ini', 'r') as f:
    elements = f.read().lower()
    elems = elements.split(' ')

with open('done.ini', 'w+') as f:
    done = f.read().split(' ')


while str(index) in done:
    index = random.randint(0, 117)


word = elems[index].lower()
am = index + 1


for i in places:
    guess = input(Fore.CYAN +  i + ' guess:\n').lower()
    while guess.lower() not in elems:
        print("That's not an element present in the periodic table")
        guess = input(Fore.CYAN + 'Try again:\n')
    clear()
    listguess = list(guess)
    checker()

    full = ''
    for i in listguess:
        full = full + i
    print(full)

print("You're out of tries! Better luck next time. The correct answer was " + word + ', ' + str(am))
with open('done.ini', 'a') as f:
    f.write(' ')
    f.write(str(index))
