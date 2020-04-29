unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGEST_POSSIBLE_SCORE = 100

#returns [91, 89, 65, 53, 41, 37]
''' this is quicksort

def sort_scores(scores):
    
    if len(scores) < 2:
        return scores 
        
    else:
        pivot = scores[0]
        less = [i for i in scores[1:] if i <= pivot]
        greater = [i for i in scores[1:] if i > pivot]

        return sort_scores(greater)  + [pivot] + sort_scores(less)
        

print(sort_scores(unsorted_scores))
'''

def sorted_scores(unsorted_scores, HIGEST_POSSIBLE_SCORE):
    score_counts = [0] * (HIGEST_POSSIBLE_SCORE + 1) # make a list of 100 0's like [0,0,0,0,0,0,0]

    for score in unsorted_scores: 
        score_counts[score] += 1 #if a score is in the unsorted scores list add it to the score counts - so change 0 to 1 if the number is there.
    
    
    sorted_scores = [] #just initialize an empty list of sorted scores.

    for score in range(len(score_counts)-1, -1, -1):
        
        count = score_counts[score] #reverse count as we want to find the largest first. 
        # the count variable contain the number of times a number is counted.
        # score variable keeps track of the number.
        for time in range(count): #if count is greater than 0 it will add that number to the final sorted list those many times.

            sorted_scores.append(score)
        
    return sorted_scores
    
print(sorted_scores(unsorted_scores, 100))