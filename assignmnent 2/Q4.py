a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

if(a>b & a>c):
    print("a is greater than both b and c")

elif(b>a and b>c):
    print("b is greater than both a and c")

else:
    print("c is greater than both a and b")
