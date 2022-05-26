import os
import sys
import commands 

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
ss = s.split()
fs = ['varH', 'varHv5', 'pzz1e5VarH', 'pzzv51e5VarH']

def walkFile(file):
    ts = [[0 for i in range(12-5)] for i in range(len(ss))]
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
                            ts[j][h-5] = tm
    return ts
for d in fs:
    # print('logs/'+d)
    ts = walkFile('logs/'+d)
    for i in ts[-1]:
       print 1.0*i/1000, 
    print 

print
for d in fs:
    # print('logs/'+d)
    ts = walkFile('logs/'+d)
    for i in ts[-2]:
       print 1.0*i/1000, 
    print 