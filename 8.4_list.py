fname = input("Enter file name: ") #romeo.txt
fh = open(fname)
lst = list()
for line in fh:
	words = line.rstrip().split()
	for word in words:
		if word not in lst:
			lst.append(word)

lst.sort()
print(lst)
