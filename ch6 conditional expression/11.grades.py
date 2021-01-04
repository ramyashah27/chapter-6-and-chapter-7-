marks=int(input("enter ur marks\n"))

# if marks<90:
#     print('congo u got A++ GRADE')
if marks>90:
    grade="A++"
elif marks>80:
    grade="A"
elif marks>70:
    grade="b"  
elif marks>60:
    grade="c"
elif marks>50:
    grade="D"  
elif marks<40:
    grade="FAIL" 
print("ur grade are: ",grade)
