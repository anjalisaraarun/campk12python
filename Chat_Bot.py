import random

# lists

happy = ['Stay happy','Have a nice and cheerful day','Have an even better day','Have an amazing day','Keep smilling','Stay happy always','Have a swell day','Happiness']

sad = ['Hope i made you fell better','Do not be sad','Hope you will be cheerful again','Cheer up','Be happy','Do not be sad','All is well']

angry = ['please do not be angry','what made you angry cheer up','hope you cheer up soon','cool down','do not hurt yourself','you will be happpoer soon',]

while True:
    print('How are you feeling ?')
    mood = ('Press 1 if you are Happy , 2 if you are Sad and three if you are Angry ')
    if mood == '1' :
        print(random.choice(happy))
    elif mood =='2':
        print(random.choice(sad))
    elif mood == '3':
        print(random.choice(angry))
