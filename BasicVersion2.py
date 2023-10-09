import random

red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
green = 0
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)

def roll():
    spin = random.randint(0,36)
    print('Landed on: ',spin)
    print('-=-=-=-=-=-=-=-=-=-=-')

    if (spin) == red:
        print('You won $.45')
    elif (spin) == black:
        print('You won $.45')
    elif (spin) == green:
        print('You won $5.00')
    elif (spin) == even:
        print('You won $.45')
    elif (spin) == odd:
        print('You won $.45')
    else:
        print('You lost')


def main():
    print(' Red = 1','\n Black = 2','\n Green = 3', '\n Even = 4','\n Odd = 5')

    print('-=-=-=-=-=-=-=-=-=-=-')
    player = int(input('Place your bet, 1-5: '))
    print('-=-=-=-=-=-=-=-=-=-=-')

    roll()

main()