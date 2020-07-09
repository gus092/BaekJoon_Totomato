a = int(input())
b = int(input())

b100 = b//100
b10 = (b%100)//10
b1 = b%10

c3 = a*b1
c4 = a*b10
c5 = a*b100

print(c3)
print(c4)
print(c5)
print(c3+10*c4+100*c5)