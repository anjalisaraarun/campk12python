import random

print ('Rock paper scissors , pick any one and beat the unbeatable robot ! Have fun.')
you_winning = 0
computer_winning = 0

def user_choice():
    user_choice = input ('Pick rock paper or scissors..')
    if user_choice in['rock','ROCK','Rock','rOCK','RoCk','r','R','ROck','roCK','RocK','rOCk'] :
        user_choice = 'rock'
    elif user_choice in ['paper','PAPER','Paper','pAPER','PAper','paPer','pAPEr','PapeR','paPer','pAper','p']:
        user_choice = 'paper'
    elif user_choice in['scissors','SCISSORS','SCISsors','scisSORS','sCISSORs','Scissors','scissSrs','S','s']:
        user_choice = 'scissors'
    else: 
        print('Please type ssomething more meaningful !')
        user_choice()
    return user_choice()

def comp_choice():
    comp_choice = random