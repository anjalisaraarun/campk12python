print ('This is voter eligiblity test')
age = int (input( 'What is your age'))
if  age >= 18 and age < 120:
    print('You are eligibil to vote')
elif age < 18 and age > 0:
    print ('you are not  eligibil to vote')
    num_of_years = 18 - age
    print('You have to wait for ', num_of_years)
elif (age <= 0):
    print('Please check your age')
elif age > 120 :
    print ('You can not be so old')