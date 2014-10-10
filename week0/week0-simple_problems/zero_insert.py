from number_to_list import number_to_list


def zero_insert(n):
    num_list = number_to_list(n)
    x = 0
    while(x < (len(num_list)-1)):
        if num_list[x] == num_list[x+1]:
            
        x = x + 1
