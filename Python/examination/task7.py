# Invert a Dictionary

# i.e. dict[value] = key
inp = {'a': 1, 'b': 2, 'c': 3}
out = {}
for i in inp.items():
    out.update({i[1]:i[0]})
print(out)