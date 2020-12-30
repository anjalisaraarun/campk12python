abc = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"year": 2020
}
print(abc)
print(len(abc))
x = abc.keys()
print(x)
abc["year"] = 1964
print(abc)
abc.update({"color": "red"})
print(abc)