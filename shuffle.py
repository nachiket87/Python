#in-place shuffle of array

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling+1)

def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list
    
    last_index = len(the_list) - 1

    for index_to_be_chosen in range(0, len(the_list)-1):
        random_index = get_random(index_to_be_chosen, last_index)

        
        if random_index != index_to_be_chosen:
            the_list[index_to_be_chosen], the_list[random_index] = the_list[random_index], the_list[index_to_be_chosen]
    return the_list

print(shuffle([1,2,3,4,5]))