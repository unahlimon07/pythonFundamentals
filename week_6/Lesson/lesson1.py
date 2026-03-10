

num_list = [10,20,30,40,50,60,70,80,90,100]

# Understanding for loops
print('\n\n')
print('-----------------[ [1] looping through list using for-in loop]------------------')

for num in num_list:
    print(num, end=' ')

print('\n\n')


print('\n\n')
print('-----------------[ [2] looping through range of num]------------------')
for x in range(0, 10):
    print(x, end=' ')

print('\n\n')


print('\n\n')
print('-----------------[ [3] with steps]------------------')
for x in range(0, 10, 3):
    print(x, end=' ')

print('\n\n')




num_list2 = [21,22,23,24,25,26,27,28,29,30]
print('\n\n')
print('-----------------[ [4] looping through list using for-in loop and range]------------------')
for x in num_list2:
    print(x, end=' ')

print('\n\n')

for x in range(0, len(num_list2)):
    print(num_list2[x], end=' ')

print('\n\n')






print('-----------------[ [5] looping through list of list  using for-in loop and range]------------------')
data = [
    ['Fish','Food', 120, 400, 425],
    ['beef','Food', 400, 250, 300],
    ['egg', 'Food', 10, 4125, 4500],
    ['pen','Non-Food', 20, 312, 401],
    ['eraser','Non-Food', 5, 252, 201],
    ['sharpener','Non-Food', 10, 372, 297]
]
for row in data: #
    print(row[2][0])

print('\n\n')

for x in range(0, len(data)): # index
    print(data[x][0])





print('-----------------[ [6] PRINTING ONLY NAME - looping through list of list  using for-in loop and range]------------------')
data = [
    ['Fish','Food', 120, 400, 425],
    ['beef','Food', 400, 250, 300],
    ['egg', 'Food', 10, 4125, 4500],
    ['pen','Non-Food', 20, 312, 401],
    ['eraser','Non-Food', 5, 252, 201],
    ['sharpener','Non-Food', 10, 372, 297]
]



for row in data:
    print(row[0])


print('\n\n')


for x in range(0, len(data)):
    print(data[x][0])


