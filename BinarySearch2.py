#find pivot point.

#words = ['k', 'v', 't', 'y', 'c', 'd', 'e', 'g', 'i']

words = ['m','n','x','y','z', 'a', 'b', 'c']

first_word = words[0]
floor_index = 0
ceiling_index = len(words) - 1

#print(words[floor_index + ((ceiling_index - floor_index) // 2)])

while floor_index < ceiling_index:
    guess_index = floor_index + ((ceiling_index - floor_index) // 2)
    print(ceiling_index)
    print(guess_index)
    
    if words[guess_index] >= first_word:
        floor_index = guess_index
    
    else:
        ceiling_index = guess_index

    if floor_index + 1 == ceiling_index:
        
        print(words[ceiling_index])
        break



print('y'>= 'm')