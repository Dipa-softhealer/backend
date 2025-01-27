# List People Aged 30 and Above
inp = [("Alice", 25), ("Bob", 35), ("Charlie", 30)]
def task2(inp):
    adult_list = []
    for i in inp :
        i = list(i)
        if(i[1] >= 30):
            adult_list.append(i[0])
    return adult_list

res = task2(inp)
print(f"output: {res}")  