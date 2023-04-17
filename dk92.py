







if __name__ == '__main__':
    date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    arriveAlice = "03-05"
    leaveAlice = "07-14"
    arriveBob = "04-14"
    leaveBob = "09-21"
    lt = [[arriveAlice, leaveAlice], [arriveBob, leaveBob]]
    lt.sort(key=lambda x: x[0])
    start_a = lt[0][0]
    end_a = lt[0][1]
    start_b = lt[1][0]
    end_b = lt[1][1]
    if end_a < start_b:
        print(0)
    else:
        min_end = min(lt[0][1], lt[1][1])
        start = lt[1][0]
        s_month = int(start.split('-')[0])
        s_day = int(start.split('-')[1])
        e_month = int(min_end.split('-')[0])
        e_day = int(min_end.split('-')[1])
        daydiff = (date[s_month] - s_day) - (date[e_month] - e_day)
        monthdiff = 0
        tmp = e_month
        while s_month < tmp:
            monthdiff += date[tmp]
            tmp -= 1
        print(daydiff + monthdiff + 1)