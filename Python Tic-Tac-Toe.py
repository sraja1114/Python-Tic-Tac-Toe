# Name: 	    Sohaib Raja
# Project Name:	Python Tic-Tac-Toe

restart = True
while restart == True: #used to restart program in the menu
    ### Menu of Game ###
    print("\nWelcome to Python Tic-Tac-Toe. The rules of are the same as the basic rules of any Tic-Tac-Toe game.")
    start = input("The goal is to get the same character in a row horizonally, vertically, or diagonally.\nTo begin playing enter 'start' or enter 'stop' to end the program: ")
    if start == 'stop' or start == 'Stop':
        break
    dim = input("\nEnter the number for the dimensions of the board:\n1: 3x3\n2: 5x5\nYou can also enter 'back' to go back in menu: ") #used to set dimensions for game
    if dim == 'back' or dim == 'Back': #stop code if players wish
        continue
    dim = int(dim) #changes dim to integer
    if dim == 1: #sets board based on input
        row1 = [chr(9633),chr(9633),chr(9633)]
        row2 = [chr(9633),chr(9633),chr(9633)]
        row3 = [chr(9633),chr(9633),chr(9633)]
    elif dim == 2:
        row1 = [chr(9633),chr(9633),chr(9633),chr(9633),chr(9633)]
        row2 = [chr(9633),chr(9633),chr(9633),chr(9633),chr(9633)]
        row3 = [chr(9633),chr(9633),chr(9633),chr(9633),chr(9633)]
        row4 = [chr(9633),chr(9633),chr(9633),chr(9633),chr(9633)]
        row5 = [chr(9633),chr(9633),chr(9633),chr(9633),chr(9633)]

    print("\nList of characters: (Enter 'back' to go back in menu)")
    for i in range(1,8): #outputs characters for players to select
        print('{i}: {char}'.format(i = i, char = chr(i+9634)))
    char1 = input('Player 1, please enter the number of the character you want: ') #takes input for P1
    if char1 == 'back' or char1 == 'Back':
        continue
    char1 = int(char1)
    print('\nList of characters:')
    for i in range(1,8): #outputs characters again
        print('{i}: {char}'.format(i = i, char = chr(i+9634)))
    char2 = int(input('Player 2, please enter a different number for the character you want. ')) #takes input for P2

    while char1 == char2: #Asks user to reenter if the character are the same, code same as before
        print('\nPlease select different characters from one another. List of characters: ')
        for i in range(1, 8):
            print('{i}: {char}'.format(i=i, char=chr(i + 9634)))
        char1 = int(input('Player 1, please enter the number of the character you want: '))
        print('\nList of characters:')
        for i in range(1, 8):
            print('{i}: {char}'.format(i=i, char=chr(i + 9634)))
        char2 = int(input('Player 2, please enter a different number for the character you want. '))

    char1 = chr(char1+9634) #sets input equal to correct character
    char2 = chr(char2+9634)
    counter = 0 #used to determine if there is a tie
    ### Start of code for actual game ###
    print('\nTo select a place to place your character enter its row and column separated by a space') #instructions for input
    print("For example, enter '2 1' to place something in row 2 column 1") #Explains exact syntax before starting loop
    print("You may, at any time, enter 'stop' to end the game.")

    while start == 'start' or 'Start': #start loop for the game
        if dim == 1: #prints board based on dimensions
            print(''.join(row1))
            print(''.join(row2))
            print(''.join(row3))
        elif dim == 2:
            print(''.join(row1))
            print(''.join(row2))
            print(''.join(row3))
            print(''.join(row4))
            print(''.join(row5))
        if dim == 1: #for 3x3
            loc = input('Player 1, please enter where you want to place your character: ').split() #divides the location into a list
            if loc[0] == 'stop': #ends code if user enters stop
                break

            if loc[0] == '1': #finds location to place character based on list loc, this if is for the row
                if loc[1] == '1' and row1[0] == chr(9633): #the second set of if statements are for the columns

                    row1[0] = char1
                elif loc[1] == '2' and row1[1] == chr(9633):

                    row1[1] = char1
                elif loc[1] == '3' and row1[2] == chr(9633):

                    row1[2] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue
            elif loc[0] == '2':  # finds location to place character
                if loc[1] == '1' and row2[0] == chr(9633):

                    row2[0] = char1
                elif loc[1] == '2' and row2[1] == chr(9633):

                    row2[1] = char1
                elif loc[1] == '3' and row2[2] == chr(9633):

                    row2[2] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue
            elif loc[0] == '3':  # finds location to place character
                if loc[1] == '1' and row3[0] == chr(9633):

                    row3[0] = char1
                elif loc[1] == '2' and row3[1] == chr(9633):

                    row3[1] = char1
                elif loc[1] == '3' and row3[2] == chr(9633):

                    row3[2] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue

            counter += 1
            if dim == 1:  # checks for winner of 3x3
                if ''.join(row1) == '{c}{c}{c}'.format(c=char1):  # checks vertically
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row1) == '{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[0] and char1 == row3[0]:  # checks horizontally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[0] and char2 == row3[0]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[1] and char1 == row2[1] and char1 == row3[1]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[1] and char2 == row2[1] and char2 == row3[1]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[2] and char1 == row2[2] and char1 == row3[2]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[2] and char2 == row2[2] and char2 == row3[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[1] and char1 == row3[2]:  # checks diagonally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[1] and char2 == row3[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row3[0] and char1 == row2[1] and char1 == row1[2]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row3[0] and char2 == row2[1] and char2 == row1[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif counter == 9: #checks for tie
                    print('\nThe Game is a Tie!')
                    break
            pl2loop = True
            while pl2loop == True: #this loop allows the loop to restart if the location is already taken
                if dim == 1:  # prints the game
                    print(''.join(row1))
                    print(''.join(row2))
                    print(''.join(row3))
                elif dim == 2:
                    print(''.join(row1))
                    print(''.join(row2))
                    print(''.join(row3))
                    print(''.join(row4))
                    print(''.join(row5))
                loc1 = input('Player 2, please enter where you want to place your character: ').split() #asks player 2 for where they want to place their character
                if loc1[0] == 'stop': # stops if user asks
                    print('Please enter stop one more time to exit game.')
                    break



                if loc1[0] == '1':  # finds location to place character, based on first element of list or the row
                    if loc1[1] == '1' and row1[0] == chr(9633): #next it finds the column of the place

                        row1[0] = char2

                    elif loc1[1] == '2' and row1[1] == chr(9633):

                        row1[1] = char2
                    elif loc1[1] == '3' and row1[2] == chr(9633):

                        row1[2] = char2
                    else: #makes it so player 2 is able to reenter the invalid spot
                        print('Please reenter the spot.')
                        continue
                elif loc1[0] == '2':  # finds location to place character
                    if loc1[1] == '1' and row2[0] == chr(9633):

                        row2[0] = char2
                    elif loc1[1] == '2' and row2[1] == chr(9633):

                        row2[1] = char2
                    elif loc1[1] == '3' and row2[2] == chr(9633):

                        row2[2] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                elif loc1[0] == '3':  # finds location to place character
                    if loc1[1] == '1' and row3[0] == chr(9633):

                        row3[0] = char2
                    elif loc1[1] == '2' and row3[1] == chr(9633):

                        row3[1] = char2
                    elif loc1[1] == '3' and row3[2] == chr(9633):

                        row3[2] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                counter +=1
                break
            if dim == 1:  # checks for winner of 3x3
                if ''.join(row1) == '{c}{c}{c}'.format(c=char1):  # checks vertically
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row1) == '{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[0] and char1 == row3[0]:  # checks horizontally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[0] and char2 == row3[0]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[1] and char1 == row2[1] and char1 == row3[1]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[1] and char2 == row2[1] and char2 == row3[1]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[2] and char1 == row2[2] and char1 == row3[2]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[2] and char2 == row2[2] and char2 == row3[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[1] and char1 == row3[2]:  # checks diagonally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[1] and char2 == row3[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row3[0] and char1 == row2[1] and char1 == row1[2]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row3[0] and char2 == row2[1] and char2 == row1[2]:
                    print('\nPlayer 2 Wins!')
                    break
        elif dim == 2:
            loc = input('Player 1, please enter where you want to place your character: ').split()

            if loc[0] == 'stop': #stops if user asks
                break
            if loc[0] == '1':  # finds location to place character
                if loc[1] == '1' and row1[0] == chr(9633):

                    row1[0] = char1
                elif loc[1] == '2' and row1[1] == chr(9633):

                    row1[1] = char1
                elif loc[1] == '3' and row1[2] == chr(9633):

                    row1[2] = char1
                elif loc[1] == '4' and row1[3] == chr(9633):

                    row1[3] = char1
                elif loc[1] == '5' and row1[4] == chr(9633):

                    row1[4] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue
            elif loc[0] == '2':  # finds location to place character
                if loc[1] == '1' and row2[0] == chr(9633):

                    row2[0] = char1
                elif loc[1] == '2' and row2[1] == chr(9633):

                    row2[1] = char1
                elif loc[1] == '3' and row2[2] == chr(9633):

                    row2[2] = char1
                elif loc[1] == '4' and row2[3] == chr(9633):

                    row2[3] = char1
                elif loc[1] == '5' and row2[4] == chr(9633):

                    row2[4] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue
            elif loc[0] == '3':  # finds location to place character
                if loc[1] == '1' and row3[0] == chr(9633):

                    row3[0] = char1
                elif loc[1] == '2' and row3[1] == chr(9633):

                    row3[1] = char1
                elif loc[1] == '3' and row3[2] == chr(9633):

                    row3[2] = char1
                elif loc[1] == '4' and row3[3] == chr(9633):

                    row3[3] = char1
                elif loc[1] == '5' and row3[4] == chr(9633):

                    row3[4] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue
            elif loc[0] == '4':  # finds location to place character
                if loc[1] == '1' and row4[0] == chr(9633):

                    row4[0] = char1
                elif loc[1] == '2' and row4[1] == chr(9633):

                    row4[1] = char1
                elif loc[1] == '3' and row4[2] == chr(9633):

                    row4[2] = char1
                elif loc[1] == '4' and row4[3] == chr(9633):

                    row4[3] = char1
                elif loc[1] == '5' and row4[4] == chr(9633):

                    row4[4] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue
            elif loc[0] == '5':  # finds location to place character
                if loc[1] == '1' and row5[0] == chr(9633):

                    row5[0] = char1
                elif loc[1] == '2' and row5[1] == chr(9633):

                    row5[1] = char1
                elif loc[1] == '3' and row5[2] == chr(9633):

                    row5[2] = char1
                elif loc[1] == '4' and row5[3] == chr(9633):

                    row5[3] = char1
                elif loc[1] == '5' and row5[4] == chr(9633):

                    row5[4] = char1
                else: #restarts loop to ask for input if the spot is taken
                    print('Please reenter the spot.')
                    continue

            counter += 1
            if dim == 2:  # checks for 5x5 winner
                if ''.join(row1) == '{c}{c}{c}{c}{c}'.format(c=char1):  # checks vertically
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row1) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row4) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row4) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row5) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row5) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[0] and char1 == row3[0] and char1 == row4[0] and char1 == row5[
                    0]:  # checks horizontally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[0] and char2 == row3[0] and char2 == row4[0] and char2 == row5[0]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[1] and char1 == row2[1] and char1 == row3[1] and char1 == row4[1] and char1 == row5[1]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[1] and char2 == row2[1] and char2 == row3[1] and char2 == row4[1] and char2 == row5[1]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[2] and char1 == row2[2] and char1 == row3[2] and char1 == row4[2] and char1 == row5[2]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[2] and char2 == row2[2] and char2 == row3[2] and char2 == row4[2] and char2 == row5[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[3] and char1 == row2[3] and char1 == row3[3] and char1 == row4[3] and char1 == row5[3]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[3] and char2 == row2[3] and char2 == row3[3] and char2 == row4[3] and char2 == row5[3]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[4] and char1 == row2[4] and char1 == row3[4] and char1 == row4[4] and char1 == row5[4]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[4] and char2 == row2[4] and char2 == row3[4] and char2 == row4[4] and char2 == row5[4]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[1] and char1 == row3[2] and char1 == row4[3] and char1 == row5[
                    4]:  # checks diagonally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[1] and char2 == row3[2] and char2 == row4[3] and char2 == row5[
                    4]:  # checks diagonally
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[4] and char1 == row2[3] and char1 == row3[2] and char1 == row4[1] and char1 == row5[0]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[4] and char2 == row2[3] and char2 == row3[2] and char2 == row4[1] and char2 == row5[0]:
                    print('\nPlayer 2 Wins!')
                    break
                elif counter == 25:
                    print('\nThe Game is a Tie!')
                    break
            pl2loop1 = True
            while pl2loop1 == True: #allows player 2 to reenter invalid location (if it is already taken)
                if dim == 1: #reprints the board
                    print(''.join(row1))
                    print(''.join(row2))
                    print(''.join(row3))
                elif dim == 2:
                    print(''.join(row1))
                    print(''.join(row2))
                    print(''.join(row3))
                    print(''.join(row4))
                    print(''.join(row5))
                loc1 = input('Player 2, please enter where you want to place your character: ').split()
                if loc1[0] == 'stop':
                    print('Please enter stop one more time to exit game.')
                    break

                if loc1[0] == '1':  # finds location to place character
                    if loc1[1] == '1' and row1[0] == chr(9633):

                        row1[0] = char2
                    elif loc1[1] == '2' and row1[1] == chr(9633):

                        row1[1] = char2
                    elif loc1[1] == '3' and row1[2] == chr(9633):

                        row1[2] = char2
                    elif loc1[1] == '4' and row1[3] == chr(9633):

                        row1[3] = char2
                    elif loc1[1] == '5' and row1[4] == chr(9633):

                        row1[4] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                elif loc1[0] == '2':  # finds location to place character
                    if loc1[1] == '1' and row2[0] == chr(9633):

                        row2[0] = char2
                    elif loc1[1] == '2' and row2[1] == chr(9633):

                        row2[1] = char2
                    elif loc1[1] == '3' and row2[2] == chr(9633):

                        row2[2] = char2
                    elif loc1[1] == '4' and row2[3] == chr(9633):

                        row2[3] = char2
                    elif loc1[1] == '5' and row2[4] == chr(9633):

                        row2[4] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                elif loc1[0] == '3':  # finds location to place character
                    if loc1[1] == '1' and row3[0] == chr(9633):

                        row3[0] = char2
                    elif loc1[1] == '2' and row3[1] == chr(9633):

                        row3[1] = char2
                    elif loc1[1] == '3' and row3[2] == chr(9633):

                        row3[2] = char2
                    elif loc1[1] == '4' and row3[3] == chr(9633):

                        row3[3] = char2
                    elif loc1[1] == '5' and row3[4] == chr(9633):

                        row3[4] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                elif loc1[0] == '4':  # finds location to place character
                    if loc1[1] == '1' and row4[0] == chr(9633):

                        row4[0] = char2
                    elif loc1[1] == '2' and row4[1] == chr(9633):

                        row4[1] = char2
                    elif loc1[1] == '3' and row4[2] == chr(9633):

                        row4[2] = char2
                    elif loc1[1] == '4' and row4[3] == chr(9633):

                        row4[3] = char2
                    elif loc1[1] == '5' and row4[4] == chr(9633):

                        row4[4] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                elif loc1[0] == '5':  # finds location to place character
                    if loc1[1] == '1' and row5[0] == chr(9633):

                        row5[0] = char2
                    elif loc1[1] == '2' and row5[1] == chr(9633):

                        row5[1] = char2
                    elif loc1[1] == '3' and row5[2] == chr(9633):

                        row5[2] = char2
                    elif loc1[1] == '4' and row5[3] == chr(9633):

                        row5[3] = char2
                    elif loc1[1] == '5' and row5[4] == chr(9633):

                        row5[4] = char2
                    else:
                        print('Please reenter the spot.')
                        continue
                counter +=1
                break
            if dim == 2:  # checks for 5x5 winner
                if ''.join(row1) == '{c}{c}{c}{c}{c}'.format(c=char1):  # checks vertically
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row1) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row2) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row3) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row4) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row4) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif ''.join(row5) == '{c}{c}{c}{c}{c}'.format(c=char1):
                    print('\nPlayer 1 Wins!')
                    break
                elif ''.join(row5) == '{c}{c}{c}{c}{c}'.format(c=char2):
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[0] and char1 == row3[0] and char1 == row4[0] and char1 == row5[
                    0]:  # checks horizontally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[0] and char2 == row3[0] and char2 == row4[0] and char2 == row5[0]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[1] and char1 == row2[1] and char1 == row3[1] and char1 == row4[1] and char1 == row5[1]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[1] and char2 == row2[1] and char2 == row3[1] and char2 == row4[1] and char2 == row5[1]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[2] and char1 == row2[2] and char1 == row3[2] and char1 == row4[2] and char1 == row5[2]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[2] and char2 == row2[2] and char2 == row3[2] and char2 == row4[2] and char2 == row5[2]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[3] and char1 == row2[3] and char1 == row3[3] and char1 == row4[3] and char1 == row5[3]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[3] and char2 == row2[3] and char2 == row3[3] and char2 == row4[3] and char2 == row5[3]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[4] and char1 == row2[4] and char1 == row3[4] and char1 == row4[4] and char1 == row5[4]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[4] and char2 == row2[4] and char2 == row3[4] and char2 == row4[4] and char2 == row5[4]:
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[0] and char1 == row2[1] and char1 == row3[2] and char1 == row4[3] and char1 == row5[
                    4]:  # checks diagonally
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[0] and char2 == row2[1] and char2 == row3[2] and char2 == row4[3] and char2 == row5[
                    4]:  # checks diagonally
                    print('\nPlayer 2 Wins!')
                    break
                elif char1 == row1[4] and char1 == row2[3] and char1 == row3[2] and char1 == row4[1] and char1 == row5[0]:
                    print('\nPlayer 1 Wins!')
                    break
                elif char2 == row1[4] and char2 == row2[3] and char2 == row3[2] and char2 == row4[1] and char2 == row5[0]:
                    print('\nPlayer 2 Wins!')
                    break

    if dim == 1:#prints board after winner is announced
        print(''.join(row1))
        print(''.join(row2))
        print(''.join(row3))
    elif dim == 2:
        print(''.join(row1))
        print(''.join(row2))
        print(''.join(row3))
        print(''.join(row4))
        print(''.join(row5))