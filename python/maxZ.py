import os
import sys
import commands 
import time

s = "dbpe you book	git	cite stackoverflow	mu	imdb actor2	ama	dblp"
ts = [100000, 100000, 100000, 20000000, 100000, 1000000, 10000000, 1000000, 5000000, 10000000, 100000]
# s = "git dblp"
# s = "ama"
# s = "dblp"
ss = s.split()

dataSets = ['' for i in range(len(ss))]
def walkFile2(file):
    global ans
    for root, dirs, files in os.walk(file):
        i = 0

        for f in files:
            if f.endswith(".txt") == False:
                continue
            
            j = 0
            while(j < len(ss) and f.count(ss[j]) == 0):
                j += 1
            if j == len(ss):
                continue

            totalF = os.path.join(root, f)
            dataSets[j] = totalF

walkFile2("data/")


for data, t, f in zip(dataSets, ts, ss):
    print data, t
    run = "run -cp -f " + data +" -t "+ str(t) + " > logs/maxZ/v2/"+f+".txt" 
    print run
    commands.getstatusoutput(run)
    run = "run -cp -v5 -f " + data +" -t "+ str(t) + " > logs/maxZ/v5/"+f+".txt" 
    commands.getstatusoutput(run)
    run = "run -pp -f " + data +" -t "+ str(t) + " > logs/maxZ/pzzv2/"+f+".txt" 
    commands.getstatusoutput(run)
    run = "run -pp -v5  -f " + data +" -t "+ str(t) + " > logs/maxZ/pzzv5/"+f+".txt" 
    commands.getstatusoutput(run)



#  15424