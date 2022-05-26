import os
import sys
import commands 
import time
# import numpy as np

# s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
s = "dblp"
# s = "nips flickr"
ss = s.split()
algLogs = ["logs/v2SpecificPQ/", "logs/v5SpecificPQ/", "logs/bcpath/", "logs/bcpathv5/"]
datas = ["git", "dblp"]
# ans = np.ones((len(algLogs), len(datas), 10, 10))*-1
ans = [[[[-1 for i in range(10)] for i in range(10)] for i in range(len(datas))] for i in range(len(algLogs))]


def eppq(file, dataset, i, j):
    # pqT = [[-1 for i in range(10)] for i in range(10)]
    global ans
    for root, dirs, files in os.walk(file):
        for f in files:
            if f.count(dataset) == 0:
                continue

            totalF = os.path.join(root, f)
            
            a = f.index('_')
            b = a + 1
            while f[b] != '_':
                b += 1
            c = f.index('.')

            p = int(f[a + 1: b])
            q = int(f[b + 1 : c])

            if p >= 10 or q >= 10:
                continue

            with open(totalF, 'r') as f:
                lines = f.readlines()
                # print lines
                for line in lines:
                    if line.startswith("error"):
                        h = 0
                        while line[h].isdigit() == False:
                            h += 1
                        
                        t = h + 1
                        while line[t].isdigit() or line[t] == '.':
                            t += 1
                        
                        ti = float(line[h : t])

                        # print ti
                        # if ti > 0:
                        #     print p,q,ti
                        ans[i][j][p][q] = ti
                        # print i,j,p,q,ans[i][j][p][q]





for i in range(len(algLogs)):
    for j in range(len(datas)):
        eppq(algLogs[i], datas[j], i, j)
        # print i, j, algLogs[i], datas[j]
        # for p in range(10):
        #     for q in range(10):
        #         if ans[i][j][p][q] != -1:
        #             print i,j,p,q,ans[i][j][p][q]


for p in range(2, 10):
    for q in range(2, 10):
        print "({},{})".format(p, q),
        for i in range(len(algLogs)):
            for j in range(len(datas)):
                print '&',"{:.2f}".format(ans[i][j][p][q]*100),
        print "\\\\"


