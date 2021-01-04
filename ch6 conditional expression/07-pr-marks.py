english=int(input("enter your marks for english\n"))
maths=int(input("enter your marks for maths\n"))
science=int(input("enter ur marks for science\n"))

if(maths<33 or english<33 or science<33):
    print("u are failed because u are stupid " )

elif(english+science+science)/3 <40:
    print("u are failed")
else:
    print("congo u are passed")
# else:
#     print("Congatulations! You passed the exam")
# sub1 = int(input("Enter first subject marks\n"))
# sub2 = int(input("Enter second subject marks\n"))
# sub3 = int(input("Enter third subject marks\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You are fail because you have less than 33% in one of the subjects")
# elif(sub1+sub2+sub3)/3 < 40:
#     print("You are fail due to total percentage less than 40")
