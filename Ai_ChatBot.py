import time
a = input('Hi i am AI bot ! What is your name ? ')
time.sleep(1)
print('Hi',a)
s = input('How old are you ? ')
time.sleep(1)
print ('I am 22 years old and you are',s)
d = input('What is your e-mail address ? ')
time.sleep(1)
print('All your data is saved ')
time.sleep(1)
print('I will assist you on your studies and career')
f = str(input('Are you interested to get my guidance ? '))
if f == 'yes' or 'Yes' :
    print('Ok good choice let us continue ')
else :
    print('Ok then good luck with your studies',a )
    time.sleep(0.5)
    print('Bye!')
    