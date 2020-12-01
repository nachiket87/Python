
x = [True] * 600

for i in range(2, len(x), 2):
    x[i] = False


for i in range(3, len(x), 2):
    if x[i] == True:
        for j in range(i*i, len(x), i ):
            x[j] = False

x[0] = x[1] = False

for k in range(len(x)-1, 1, -1):
    if x[k] == True:
        print(k)
        break
    
