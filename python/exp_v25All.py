import os
import sys
import commands 
import time

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
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

for i in range(len(ss)):
    st = time.time()
    # outF = "logs/samplev51e6/"+ss[i]+".txt"
    outF = "logs/H10/"+ss[i]+".txt"
    run = "run -f " + dataSets[i] + " -H 11 -cp -t 100000 " + " > " + outF
    print(commands.getstatusoutput(run))
    # print run
    ed = time.time()
    # print "dataSets ", ss[i], ed - st 
    # logger.write("dataSets "+ ss[i] + ' ' + str(ed - st) +"\n")
# 6068

# for i in range(len(ss)):
#     st = time.time()
#     # outF = "logs/samplev51e6/"+ss[i]+".txt"
#     outF = "logs/H10_v5/"+ss[i]+".txt"
#     run = "run -f " + dataSets[i] + " -H 11 -v5 -cp -t 100000 " + "> " + outF
#     print(commands.getstatusoutput(run))
#     # print run
#     ed = time.time()
#     # print "dataSets ", ss[i], ed - st 
#     # logger.write("dataSets "+ ss[i] + ' ' + str(ed - st) +"\n")
# # 5884