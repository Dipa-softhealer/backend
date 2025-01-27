# Remove Even Numbers Using List Comprehension

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list comprehension
inp = [el for el in inp if el%2 != 0]
print("output : ",inp)