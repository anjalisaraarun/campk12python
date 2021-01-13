def f(name,age = 20):
    print(name,age)
f('Emma',25)






name = 'susan'
for letter in name:
    if letter=='b':
        break
    print('i found b')
print('bye')

for i in range(1,51):
    if i % 3 == 0:
        continue
    print(i)


s = input('Enter you name')
