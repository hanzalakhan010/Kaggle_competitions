c = []
with open('./data.txt','r') as d:
    for line in d.readlines():
        lin = line.split(' ')
        if lin[0] == 'd':
            c.append(lin[2].replace('\n',''))
print(c)
