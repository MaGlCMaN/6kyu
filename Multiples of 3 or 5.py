def solution(number):
    the_list = []
    mult_list = []
    the_set = set()
    
    for i in range(1, number):
        the_list.append(i)
    
    for i in the_list:
        if i % 3 == 0:
            mult_list.append(i)
        
    for i in the_list:
        if i % 5 == 0:
            mult_list.append(i)
    
    the_set = set(mult_list)   
    the_set = sum(the_set)
    return the_set