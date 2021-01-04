

text = input('enter the text\n')
if('make a lot of money' in text):
    spam=True
elif('buy now'in text):
    spam=True
elif('click this'in text):
    spam=True
elif('subscribe this'in text):
    spam=True
else:
    spam=False
if(spam):
    print('this comment is spam')
else:
    print('this comment is not spam')
# # 5:04:50 / 11:52:23
