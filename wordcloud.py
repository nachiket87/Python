import string
string2 = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."

string1 ="Add milk and eggs, then add flour and sugar."




string1 = string1.lower()

string2 = string2.lower()

string2 = string2.translate(str.maketrans('','', string.punctuation))


string1 = string1.translate(str.maketrans('','', string.punctuation))

l = string1.split(' ') + string2.split(' ')

cloud = {}


for i in set(l):
    cloud[i]=0

for i in l:
    cloud[i]+=1

print(cloud)





