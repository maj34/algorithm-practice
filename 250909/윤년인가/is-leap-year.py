Y = int(input())

if Y%100==0 and Y%400!=0:
    print("false")
elif Y%4==0:
    print("true")
else:
    print("false")