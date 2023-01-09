s1=int(input("Enter the length of side 1 : "))
s2=int(input("Enter the length of side 2 : "))
s3=int(input("Enter the length of side 3 : "))

if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
    print("The triangle can be formed")

else:
    print("The triangle cannot be formed")