fruit = ['stawberry','banana','mango','blueberry','banana','banana']
print(fruit[-1])
fruit[1]='apple'
print(fruit)
fruit.insert(2,'watetmelon')
print(fruit)
fruit.append('lichi')
print(fruit)
fruit.remove('banana')
print(fruit)
fruit.pop(2)
print(fruit)
for i in fruit :
    print(i)
s = fruit.copy()
print(s)
a = [78+90+32+654+230]
b = [48,99,64,54,20]
t = (a+b)
print(t)