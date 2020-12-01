x = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12] 


def quicksort(array): 
    if len(array) < 2:
        return array 
        
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater) 
        

print (quicksort(x))
