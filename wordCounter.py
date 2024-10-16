'Programme to count the words in each project'

'Make function that counts the words in each lab'
previousProjectsSingle = []
with open("/Users/sadiqkhawaja/Desktop/KCL/7BBM113/previousProjects.txt") as file:
    for line in file:
        words = line.split()
        for word in words:
            previousProjectsSingle.append(word.lower())
        
counts = {}
for item in previousProjectsSingle:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
counts


'Make function that counts the words in each lab'
previousProjectsSingle = []
with open("/Users/sadiqkhawaja/Desktop/KCL/7BBM113/previousProjects.txt") as file:
    for line in file:
        words = line.split()
        for word in words:
            previousProjectsSingle.append(word.lower())
        
counts = {}
for item in previousProjectsSingle:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
counts

counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

print(counts)
