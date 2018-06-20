def bingo(ticket,win):
    wins = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                wins += 1
    
    if wins >= win:
        return 'Winner!'
    else:
        return 'Loser!'