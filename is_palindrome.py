## Nachiket's first solution:

'''def has_palindrome_permutation(the_string):

    list_of_each_char_in_string = []
    
    for each_letter in the_string:
        list_of_each_char_in_string.append(each_letter)
    
    list_of_each_char_in_string = set(list_of_each_char_in_string)
    
    
    return ((len(the_string)-1) * 0.5) + 1 >= len(list_of_each_char_in_string) 


print(has_palindrome_permutation(''))'''


#Official Solution

def has_palindrome_permutation(the_string):

    unpaired_chars = set()

    for char in the_string:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return len(unpaired_chars) <= 1

print(has_palindrome_permutation('civic'))