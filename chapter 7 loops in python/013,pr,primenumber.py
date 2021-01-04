# num = int(input('enter the number: '))
# prime=True

# for i in range(2,num):
     
#     if(num%i == 0):
#      prime = False
#     break 
# if prime:
#         print('this is a prime')
# else:
#         print('this is not a prime')



num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")