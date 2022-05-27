import os
import sys
import commands 
import time

s = "dbpe you book	git	cite stackoverflow	mu	imdb  actor2	ama	dblp"
# s = "dblp"
# s = "nips flickr"
ss = s.split()

dataSets = ['' for i in range(len(ss))]
def walkFile2(file):
    # global ans
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


ans = ['' for i in range(len(ss))]
def walkFile3(file):
    for root, dirs, files in os.walk(file):
        i = 0
        for f in files:
            if f.startswith("pivot_") and f.count('exam') == 0:

                totalF = os.path.join(root, f)
                
                j = 0
                while(j < len(ss) and totalF.count(ss[j]) == 0):
                    j += 1
                if j == len(ss):
                    continue
                
                ans[j] = totalF
walkFile3("logs/")

# logger = open("logs/bcpathAll.txt", "a")


def solve(g, outLog, dataSet, ans, i):
    ps = []
    qs = []
    vs = []

    with open(ans, 'r') as f:
        lines = f.readlines()
        # print lines
        for line in lines:
            if line.count('-') > 0 and line.count(':') > 0:
                p1 = line.index('-')
                p2 = line.index(':')

                p = int(line[:p1])
                q = int(line[p1 + 1 : p2])

                if p == 1 or q == 1 or p >= 100 or q >= 100:
                    continue

                v = int(line[p2 + 1:-1])

                ps.append(p)
                qs.append(q)
                vs.append(v)
    
    for p, q, v in zip(ps, qs, vs):
        # print p, q,
        st = time.time()
        outF = ss[i]+'_'+str(p)+'_'+str(q)+'.txt'
        run = "run -f " + dataSet +" -p "+str(p)+" -q "+str(q)+" -v "+str(v)+g+"  > "+outLog + outF
        # print run
        print commands.getstatusoutput(run), 

        ed = time.time()
        # print "dataSets ", ss[i], p, q, ed - st 
        # logger.write("dataSets " + ss[i] + ' ' + str(p) + ' ' + str(q) + ' '+ str(ed - st)+"\n" )


for i in range(0, len(ss)):
    # st = time.time()
    solve(" -v5 -bcpath ", "logs/bcpathv5/", dataSets[i], ans[i], i)
    solve(" -bcpath ", "logs/bcpath/", dataSets[i], ans[i], i)
    # ed = time.time()
    # print "dataSets ", ss[i], ed - st ,dataSets[i], ans[i]
    # logger.write("dataSets "+ ss[i] + ' ' + str(ed - st) +"\n")

#  76244