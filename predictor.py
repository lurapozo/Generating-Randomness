import numpy as np


def show_console(minimum, flag):
    l=""

    while minimum > 0:
        if flag:
            print(f"Current data length is {len(l)}, {minimum} symbols left")
        print('Print a random string containing 0 or 1:')
        print('')
        a = input('>')
        if a == 'enough':
            print('Game over!', end='')
            return l, False
        c = 0
        for i in a:
            if i == "0" or i == "1":
                l = l+i
                c += 1
        minimum = minimum - c

    return l, True


def analysis(l):
    numb = ['000', '001', '010', '011', '100', '101', '110', '111']
    numbers = {key: [0, 0] for key in numb}


    for i in range(0, len(l)-3):
        triad = l[i] + l[i + 1] + l[i + 2]
        if l[i + 3] == '1':
            numbers[triad][1] += 1
        else:
            numbers[triad][0] += 1

    return numbers
def prediction(l2, numbers):
    data = str(np.random.randint(0, 2, size=3))
    predicted_list = data[1] + data[3] + data[5]
    for i in range(0, len(l2)-3):
        triad = l2[i] + l2[i + 1] + l2[i + 2]
        if numbers[triad][0] >= numbers[triad][1]:
            predicted_list = predicted_list + '0'
        else:
            predicted_list = predicted_list + '1'
    return predicted_list

def comparison(l2, predicted_list):
    c = 0
    for i in range(3, len(l2)):
        if l2[i]==predicted_list[i]:
            c = c+1
    print(f'Computer guessed right {c} out of {len(l2)-3} symbols ({100*(c/(len(l2)-3)):.2f} %)')
    return c, (len(l2)-3)




if __name__ == "__main__":
    #AI learning
    print('Please give AI some data to learn...')
    l1, _ = show_console(100, True)
    numbers = analysis(l1)
    print('')
    print('Final data string:')
    print(l1)
    #Start of game
    print('')
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print(f'Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
    credit = 1000
    #loop
    while credit > 0:
        l2, flag = show_console(4, False)
        if flag == False:
            break
        print('prediction:')
        predicted_list = prediction(l2, numbers)
        print(predicted_list)
        print('')
        guessed, missed = comparison(l2, predicted_list)
        credit = credit - guessed + missed - guessed
        print(f'Your balance is now ${credit}')
        print('')


