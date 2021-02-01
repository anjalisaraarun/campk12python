import random
print('Rock paper scissors , pick any one and beat the unbeatable robot ! Have fun.')

# VARIABLES

you_win = 0
AI_win = 0
tie = 0
Rcount = 0
Pcount = 0
Scount = 0
Rtime = 0
Ptime = 0
Stime = 0         

CC = ['rock','paper','scissors']

play1 = random.choice (CC)
play2 = random.choice (CC)
play3 = random.choice (CC)
play4 = random.choice (CC)
play5 = random.choice (CC)

player_pic = input('Pick rock , paper , scissors or quit. ')
while player_pic !='quit' :
    if player_pic == 'rock' :
        Rtime = Rtime + 1
    elif player_pic == 'paper' :
        Ptime = Ptime + 1
    elif player_pic == 'scissors' :
        Stime = Stime + 1
    CRtime = 0
    CPtime = 0
    CStime = 0
    play1 = play2
    play2 = play3
    play3 = play4
    play4 = play5
    play5 = player_pic

    CC = ['rock','paper','scissors']

    if play1 == 'rock':
        CRtime = CRtime + 1
    elif play1 == 'paper':
        CPtime = CPtime + 1
    elif play1 == 'scissors':
        CStime = CStime + 1

    if play2 == 'rock':
        CRtime = CRtime + 1
    elif play2 == 'paper':
        CPtime = CPtime + 1
    elif play2 == 'scissors':
        CStime = CStime + 1

    if play3 == 'rock':
        CRtime = CRtime + 1
    elif play3 == 'paper':
        CPtime = CPtime + 1
    if play3 == 'scissors':
        CStime = CStime + 1

    if play4 == 'rock':
        CRtime = CRtime + 1
    elif play4 == 'paper':
        CPtime = CPtime + 1
    elif play4 == 'scissors':
        CStime = CStime + 1

    if play5 == 'rock':
        CRtime = CRtime + 1
    elif play5 == 'paper':
        CPtime = CPtime + 1
    elif play5 == 'scissors':
        CStime = CStime + 1
    else :
        print('Sorry.There is an error. Check your spelling and capitalization')   
    if CRtime > CPtime & CRtime > CStime:
        CC = 'paper'
    elif CPtime > CStime & CPtime > CRtime:
        CC = 'scissors'
    elif CStime > CRtime & CStime > CPtime:
        CC = 'rock'
    else:
        CC = random.choice(CC)
    
    if player_pic == "rock":
        if CC == 'paper':
            print(CC)
            print('You lost and AI wiins')
            AI_win = AI_win + 1
        elif CC == 'rock':
            print(CC)
            print('Tie game')
            tie = tie + 1
        elif CC == 'scissors':
            print(CC)
            print('AI lost and you win.')
            you_win = you_win + 1



    elif player_pic == "paper":
        if CC == 'scissors':
            print(CC)
            print('You lost and AI wiins')
            AI_win = AI_win + 1
        elif CC == 'paper':
            print(CC)
            print('Tie game')
            tie = tie + 1
        elif CC == 'rock':
            print(CC)
            print('Bot lost and you won')
            you_win = you_win + 1




    elif player_pic == "scissors":
        if CC == 'rock':
            print(CC)
            print('You lost and AI wiins')
            AI_win = AI_win + 1
        elif CC == 'scissors':
            print(CC)
            print('Tie game')
            tie = tie + 1
        elif CC == 'paper':
            print(CC)
            print('Bot lost and you won')
            you_win = you_win + 1


    player_pic = input('Pick rock , paper , scissors or quit.')
print ('The final score is  ' + str (AI_win) +  ' to' + str (you_win) )
print ('You tied ' + str (tie) + ' times')
if AI_win > you_win:
    print('AI won the game')
elif you_win == AI_win :
    print('Tie game')
else:
    print ('You win')
print('Rock = ', Rtime )
print('Paper = ', Ptime  )
print('Scissors = ', Stime  )