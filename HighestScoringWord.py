import string

def high(x):
    score_card = {}
    my_dict = {}
    my_list = []
    word_list = x.split()
    
    for number, letter in enumerate(string.ascii_lowercase):
      score_card[letter] = number+1
      
    for i in x.split():
        score = 0
        for j in i:
            score += score_card.get(j)
        my_list.append(score)
    
    indx = my_list.index((max(my_list)))

    return word_list[indx]