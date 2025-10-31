"""
Skip numbers divisible by 3, from (0,100)
Interview question
# """
for i in range(1, 30):
    if i % 3 == 0:
        continue
    else:
     print(i)