#fibonacci

l = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
x = 1
y = 1
z= 0
count = 0

while z <= 4000000:
    z = x + y
    x = y
    y = z
    if z % 2 == 0:
        b.append(z)
   

print(sum(b))