#fibonacci
b=int(input("enter no of terms"))
c,d=1,0
print(d)
for i in range(1,b):
    s=c+d
    c=d
    d=s
    print(s)