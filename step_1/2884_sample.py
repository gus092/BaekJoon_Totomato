h,m=map(int,input().split())
print(10-3*(m<45))
print((h-(m<45))%24,(m-45)%60)