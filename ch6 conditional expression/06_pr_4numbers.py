num1= (input('enter 1stnumber: '))
num2= (input('enter 2ndnumber: '))
num3= (input('enter 3rdnumber: '))
num4= (input('enter 4thnumber: '))

num1=int(num1)
num2=int(num2)
num3=int(num3)
num4=int(num4)

if(num1>num2):
    f1= num1
else:
    f1 = num2
if(num3>num4):
    f2= num3
else:
    f2 = num4
if(f1>f2):
    print(f1 ,'is the greatest number')
else:
    print(f2,'is the greatest number')