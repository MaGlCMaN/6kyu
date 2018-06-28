def find_it(seq):
    my_dict = {}
    num = 0

    for i in seq:
        my_dict[i] = 0
    
    for i in seq:
        try:
            while seq[num] == i:
                my_dict[i] += 1
                if num <= len(seq)-1:
                    num += 1
                else:
                    break
        except IndexError:
            pass
        
    for i in my_dict:
        if my_dict[i] % 2 != 0:
            return i