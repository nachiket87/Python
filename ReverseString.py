test_empty =[]
test_one = ['A']

Test_string = ['A', 'B', 'C', 'D', 'E']



def reversal(list_of_chars):
    if len(list_of_chars) <= 1:
        return list_of_chars
    return list_of_chars[::-1]



print(reversal(Test_string))


#this is the wrong answer.