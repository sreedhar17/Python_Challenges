
import re


def findSeatAndType(lst_seats):
    seat_type=['WS', 'MS', 'AS', 'AS','MS','WS']
    dict_t={}
    k=0
    total_seats=108
    tot_pairs=total_seats//2
    tot_cab_seats=12
    min_seat_in_row=1
    max_seat_in_row=tot_cab_seats
    row_addition=1
    for i in range(0, tot_pairs):
        t=tuple((min_seat_in_row, max_seat_in_row))
        dict_t[seat_type[k] + str(min_seat_in_row) +"-"+ str(max_seat_in_row)]=t
        min_seat_in_row=min_seat_in_row + 1
        max_seat_in_row=max_seat_in_row - 1
        k=k + 1
        if k >= 6:
            k=0
            row_addition=row_addition+1
            min_seat_in_row=min_seat_in_row+6
            max_seat_in_row=tot_cab_seats*row_addition
    print(dict_t)
    for x in range(len(lst_seats)):
        seat=lst_seats[x]

        reObj=re.compile(str(seat))
        for key, value in dict_t.items():
            if reObj.search(key):
                if int(value[0]) == int(seat):
                    opp_seat=value[1]
                else:
                    opp_seat=value[0]
                print(opp_seat,  key[0:2])
                break

T=int(input())
lst_seat=[]
for i in range(T):
    seat_no=input()
    lst_seat.append(seat_no)

findSeatAndType(lst_seat)

