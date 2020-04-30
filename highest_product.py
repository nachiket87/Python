'''Find the highest product you can get from three of the integers.'''

list_of_inputs = [-10, -10, 1, 3, 2]

highest_product = 0

def find_highest_product(list_of_inputs):
    if len(list_of_inputs)<3:
        return ValueError('Less than 3 items')

    highest_product_of_2 = list_of_inputs[0] * list_of_inputs[1]
    lowest_product_of_2 = list_of_inputs[0] * list_of_inputs[1]
    highest = max(list_of_inputs[0], list_of_inputs[1])
    lowest = min(list_of_inputs[0], list_of_inputs[1])
    highest_product_of_3 = highest_product_of_2 * list_of_inputs[2] 

    for i in range(2, len(list_of_inputs)):
        current = list_of_inputs[i]
        highest_product_of_3 = max(highest_product_of_3, highest_product_of_2 * highest, highest_product_of_2 * lowest)
        highest_product_of_2 = max(highest_product_of_2, current * highest, current * lowest)
        lowest_product_of_2 = min(lowest_product_of_2, lowest * current, current * highest)
        highest = max(highest, current)
        lowest= min(lowest, current)

    return highest_product_of_3

print(find_highest_product(list_of_inputs))