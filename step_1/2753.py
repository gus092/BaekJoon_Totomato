#윤년 = 연도가 4의 배수이면서 100의 배수가 아닐 때 
#       또는 400의 배수일 때(이때는 4와 100의 배수임)

year = int(input())

if( year%4 == 0 ):
    if ( year% 100 != 0 ):
        print(1)
    elif(year % 400 == 0 ):
        print(1)
    else :
        print(0)
else:
    print(0)
