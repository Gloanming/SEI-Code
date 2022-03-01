user_input = (input().split(' '))
user_input = [int(x) for x in user_input]
#print(user_input)
difference = []
count = 0
for i in range(0,len(user_input)):
    for j in range(i + 1,len(user_input)):
        difference.append(user_input[j] - user_input[i])
difference.sort()
print(difference[len(difference) - 1],end='')



