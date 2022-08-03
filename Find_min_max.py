def find_min(my_list, min = None):

    if len(my_list) == 0:

        return min

    if min == None or my_list[0] < min:

        min = my_list[0]

    return find_min(my_list[1:], min)

def find_max(my_list, max = None):

    if len(my_list) == 0:

        return max

    if max == None or my_list[0] > max:

        max = my_list[0]

    return find_max(my_list[1:], max)
