take_out_orders = [1,4,5]

dine_in_orders = [2,3,6]

served_orders = [1,2,3,4,5,6]



'''def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    if len(served_orders) == 0:
        return True
    
    if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
        return is_first_come_first_served(take_out_orders[1:], dine_in_order, served_orders[1:])

    elif len(dine_in_order) and dine_in_order[0] == served_orders[0]:
        return is_first_come_first_served(take_out_orders, dine_in_order[1:], served_orders[1:])

    else:
        return False'''


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_order_index = 0
    max_take_out_orders_index = len(take_out_orders) - 1

    dine_in_orders_index = 0
    max_dine_in_orders_index = len(dine_in_orders) -1

    for item in served_orders:

        if take_out_order_index <= max_take_out_orders_index and item == take_out_orders[take_out_order_index]:
            take_out_order_index += 1
        
        elif max_dine_in_orders_index <= max_dine_in_orders_index and item == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1
        
        else:
            return False
    if dine_in_orders_index != len(dine_in_orders) or take_out_order_index != len(take_out_orders):
        return False
    
    return True
        

    
print(is_first_come_first_served(take_out_orders, dine_in_orders, served_orders))
