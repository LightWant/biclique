import os
import sys
import commands 
import time
# import numpy as np

# s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
# s = "dblp"
# s = "nips flickr"
# ss = s.split()
algLogs = ["bclist/all/", "logs/eppq/", "logs/v2SpecificPQ/", "logs/v5SpecificPQ/", 
        "logs/bcpath/", "logs/bcpathv5/", "logs/onlysparseEPpq", "logs/onlysparseEPpq"]
datas = ["git", "dblp"]
# ans = np.ones((len(algLogs), len(datas), 10, 10))*-1
ans = [[[[-1 for i in range(10)] for i in range(10)] for i in range(len(datas))] for i in range(len(algLogs))]

def bcall(file, dataset, i, j):
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

            p = int(f[a  + 1: b])
            q = int(f[b + 1 : c])

            if p >= 10 or q >= 10:
                continue

            with open(totalF, 'r') as f:
                lines = f.readlines()
                # print lines
                for line in lines:
                    if line.startswith("Computing biclique: using") or line.startswith("Count butterflies"):
                        h = 0
                        while line[h].isdigit() == False:
                            h += 1
                        
                        t = h + 1
                        while line[t].isdigit() or line[t]=='.':
                            t += 1                       

                        if line.startswith("Count butterflies"):
                            ti = float(line[h : t])
                            print ti
                            ans[i][j][p][q] = ti*1000
                        else:
                            ti = int(line[h : t])
                            ans[i][j][p][q] = ti

                        # if p == 2 and q == 2:
                        #     print ti
                        # print ti
                        # if ti > 0:
                        #     print ss[j],p,q,ti

# walkFile2("bclist/all/")

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
                    if line.startswith("time"):
                        h = 0
                        while line[h].isdigit() == False:
                            h += 1
                        
                        t = h + 1
                        while line[t].isdigit():
                            t += 1
                        
                        ti = int(line[h : t])

                        # print ti
                        # if ti > 0:
                        #     print p,q,ti
                        ans[i][j][p][q] = ti
                        # print i,j,p,q,ans[i][j][p][q]

def onlySparse(file, file2, dataset, i, j):
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
                    if line.startswith("time"):
                        h = 0
                        while line[h].isdigit() == False:
                            h += 1
                        
                        t = h + 1
                        while line[t].isdigit() or line[t] == '.':
                            t += 1
                        
                        ti = float(line[h : t])
                        # print line[h: t], ti

                        # print ti
                        # if ti > 0:
                        #     print p,q,ti
                        ans[i][j][p][q] = ti
    
    for root, dirs, files in os.walk(file2):
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
                    if line.startswith("appro done"):
                        h = 0
                        while line[h].isdigit() == False:
                            h += 1
                        
                        t = h + 1
                        while line[t].isdigit() or line[t] == '.':
                            t += 1
                        
                        ti = float(line[h : t])
                        # print line[h: t], ti

                        # print ti
                        # if ti > 0:
                        #     print p,q,ti
                        if ans[i][j][p][q] == -1:
                            print "error"
                        ans[i][j][p][q] += ti*1000

i = 0
for j in range(len(datas)):
    bcall(algLogs[i], datas[j], i, j)
    # print i, j, algLogs[i], datas[j]
    # for p in range(10):
    #     for q in range(10):
    #         if ans[i][j][p][q] != -1:
    #             print i,j,p,q,ans[i][j][p][q]

for i in range(len(algLogs)-2):
    for j in range(len(datas)):
        eppq(algLogs[i], datas[j], i, j)
        # print i, j, algLogs[i], datas[j]
        # for p in range(10):
        #     for q in range(10):
        #         if ans[i][j][p][q] != -1:
        #             print i,j,p,q,ans[i][j][p][q]

i = len(algLogs)-2
for j in range(len(datas)):
    onlySparse(algLogs[i], "logs/bcpath/", datas[j], i, j)
    print i, j, algLogs[i], "logs/bcpath/", datas[j]
    # for p in range(10):
    #     for q in range(10):
    #         if ans[i][j][p][q] != -1:
    #             print i,j,p,q,ans[i][j][p][q]
i = len(algLogs)-1
for j in range(len(datas)):
    onlySparse(algLogs[i], "logs/bcpathv5/", datas[j], i, j)
    print i, j, algLogs[i], "logs/bcpathv5/", datas[j]

    # for p in range(10):
    #     for q in range(10):
    #         if ans[i][j][p][q] != -1:
    #             print i,j,p,q,ans[i][j][p][q]


PQs = [(2,3), (2,8), (3,4), (3,5), (3,9), (4, 5), 
    (4, 8), (5,3),(5,6),(5,9), (6,4),(6,7), (7,4),(7,7), (8,4),(8,8),(9,4),(9,9)]
# for p in range(2, 10):
#     for q in range(2, 10):
for p,q in PQs:
    print "({},{})".format(p, q),

    minV = [10000000000 for i in range(len(datas))]
    minJ = [0 for i in range(len(datas))]
    for i in range(len(algLogs)):
        for j in range(len(datas)):
            if ans[i][j][p][q] < minV[j]:
                minJ[j] = i
                minV[j] = ans[i][j][p][q]

    for i in range(len(algLogs)):
        for j in range(len(datas)):
            if minJ[j] == i:
                print '&',"\\textbf{","{:.2f}".format(1.0*ans[i][j][p][q]/1000),"}",
            else:
                print '&',"{:.2f}".format(1.0*ans[i][j][p][q]/1000),
    print "\\\\"


