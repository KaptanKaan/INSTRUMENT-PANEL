import random
f = open("input.txt", "w")

for i in range(0,20):
    x=random.randint(0, 320)
    f.write(str(x))
    f.write("\n")

f.close()