# figure out distribution of hours email sent
# print out the counts, sorted by hour as shown below.
# file name: mbox-short.txt
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

words = []
# Get a list of hours
# e.g. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
for line in handle:
    if line.startswith('From ') == True:
        words.append(line.split()[5][0:2])

# Create histgram of hours
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

# sorted by hours from small to large number
lst = list()
for hour, count in counts.items():
    tup = (hour, count)
    lst.append(tup)
lst = sorted(lst)
# print out hour count
for x, y in lst:
    print(x, y)
