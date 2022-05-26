import os
import sys
import commands 

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
ss = s.split()
fs = ['varT', 'varTv5', 'pzzvarT', 'pzzv5varT']

def walkFile(file):
    ts = [[0 for i in range(10)] for i in range(len(ss))]
    for root, dirs, files in os.walk(file):
        i = 0
        for f in files:
            if f.endswith(".txt") and f.startswith("total") == False and f[0].isdigit():

                totalF = os.path.join(root, f)
                
                j = 0
                while(j < len(ss) and totalF.count(ss[j]) == 0):
                    j += 1
                if j == len(ss):
                    continue

                # print(f)
                h = int(f[0])
                if f[1].isdigit():
                    h = int(f[0:2])
                # fileNames[j] = totalF

                with open(totalF, 'r') as f:
                    lines = f.readlines()

                    for line in lines:
                        if line.startswith("time:"):
                            # print("there")
                            i = line.index(':')
                            jj = line.index('ms')

                            tm = int(line[i + 1:jj])
                            ts[j][h-1] = tm
    return ts

outData = ['ama', 'dblp']

for s in outData:
    print s
    j = 0
    while(ss[j] != s):
        j += 1
    for d in fs:
        # print('logs/'+d)
        ts = walkFile('logs/'+d)
        for i in ts[j]:
            print 1.0*i/1000, 
        print

    print