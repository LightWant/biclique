import os
import sys
import commands 
import time

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
# s = "git dblp"
# s = "ama"
s = "dblp"
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

# pqs = [(9, 9, 74632958)]

# pqs = [[(9, 9, 74632958)], [(9, 9, 2651792304)]]
# pqs = [[(9,9,2620701899)]]

pqs = [[(9, 9, 2651792304)]]#dblp
# pqs = [[(9,5)]]#dblp
# ts = [1, 2, 5,7,10, 15,20,30,40,50,60,70,80,90,100]
# ts = [0.002, 0.004, 0.006, 0.008, 0.01]
ts = [0.0001*i for i in range(1,10)]
ts = [0.1]
ts = [0.0001,0.001,0.01,0.1,1]
# ts = [100,200,300,400,500,600,700,800,900,1000]

for i in range(len(dataSets)):
    for p,q,v in pqs[i]:
        for t in ts:
            T = t*100000
            # T = t
            
            dataPath = dataSets[i]
            data = ss[i]

            run = "./run -bcpath -bar 0 -f "+dataPath+" -p "+str(p)+ " -q "+str(q)+ " -v "+str(v)+\
                    " -t " + str(T) + " > logs/specificVarT/v2/"+data+"_"+str(p)+"_"+str(q)+"_"+str(t)+".txt"
            # print run
            commands.getstatusoutput(run)

            run = "./run -bcpath -bar 0 -v5 -f "+dataPath+" -p "+str(p)+ " -q "+str(q)+ " -v "+str(v)+\
                    " -t " + str(T) + " > logs/specificVarT/v5/"+data+"_"+str(p)+"_"+str(q)+"_"+str(t)+".txt"
            # print run
            commands.getstatusoutput(run)

            run = "./run -bcpath -bar 1000 -f "+dataPath+" -p "+str(p)+ " -q "+str(q)+ " -v "+str(v)+\
                    " -t " + str(T) + " > logs/specificVarT/bcv2/"+data+"_"+str(p)+"_"+str(q)+"_"+str(t)+".txt"
            # print run
            commands.getstatusoutput(run)

            run = "./run -bcpath -bar 1000 -v5 -f "+dataPath+" -p "+str(p)+ " -q "+str(q)+ " -v "+str(v)+\
                    " -t " + str(T) + " > logs/specificVarT/bcv5/"+data+"_"+str(p)+"_"+str(q)+"_"+str(t)+".txt"
            # print run
            commands.getstatusoutput(run)

# 11080