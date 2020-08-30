import re
file = open('regex_sum_863160.txt')
data = file.read()

number = re.findall('[0-9]+', data)
sum = 0
for i in number:
    sum = sum + int(i)

print(sum)
