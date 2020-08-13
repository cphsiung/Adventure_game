# Get who sent the most emails and how many times
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

words = []
# Get a list of emails
for line in handle:
    if line.startswith('From ') == True:
        words.append(line.split()[1])

# Create histgram of emails
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

# Get the most frequent email
bigemail = None
bigcount = None
for key, value in counts.items():
    if bigemail is None or value > bigcount:
        bigemail = key
        bigcount = value
print(bigemail, bigcount)
