import os
import sys
import commands 
import time

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
# s = "dblp"
# s = "nips flickr"
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

# logger = open("logs/bcAll.txt", "a")

realV = [[[0  for j in range(10)] for i in range(10)] for i in range(len(ss))]
sumWv2 = [[0 for i in range(10)] for i in range(len(ss))]
sumWv5 = [[0 for i in range(10)] for i in range(len(ss))]
sumWpzzv2 = [[0 for i in range(10)] for i in range(len(ss))]
sumWpzzv5 = [[0 for i in range(10)] for i in range(len(ss))]

def solve(dataSet, ans, si):
    with open(ans, 'r') as f:
        lines = f.readlines()
        # print lines
        for line in lines:
            if line.count('-') > 0 and line.count(':') > 0:
                p1 = line.index('-')
                p2 = line.index(':')

                p = int(line[:p1])
                q = int(line[p1 + 1 : p2])

                if p == 1 or q == 1 or p >= 10 or q >= 10:
                    continue

                v = int(line[p2 + 1:-1])

                realV[si][p][q] = v
    
    
    with open("logs/varT/10" + ss[si] + ".txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith('sumW:'):
                h = 2
                for i in range(len(line)):
                    if line[i] == ':':
                        j = i + 1
                        while j < len(line) and line[j].isdigit() == True:
                            j += 1
                        sumWv2[si][h] = int(line[i + 1:j])
                        h += 1

                        if h == 10:
                            break
    
    with open("logs/varTv5/10" + ss[si] + ".txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith('sumW') and line.count(':') > 0:
                h = 2
                for i in range(len(line)):
                    if line[i] == ':':
                        j = i + 1
                        while j < len(line) and line[j].isdigit() == True:
                            j += 1
                        sumWv5[si][h] = int(line[i + 1:j])
                        h += 1

                        if h == 10:
                            break

    with open("logs/pzzv5varT/100" + ss[si] + ".txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith('sumW') and line.count(':') > 0:
                h = 2
                for i in range(len(line)):
                    if line[i] == ':':
                        j = i + 1
                        while j < len(line) and line[j].isdigit() == True:
                            j += 1
                        sumWpzzv5[si][h] = int(line[i + 1:j])
                        h += 1
                        if h == 10:
                            break

    with open("logs/pzzvarT/100" + ss[si] + ".txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith('sumW:'):
                h = 2
                for i in range(len(line)):
                    if line[i] == ':':
                        j = i + 1
                        while j < len(line) and line[j].isdigit() == True:
                            j += 1
                        sumWpzzv2[si][h] = int(line[i + 1:j])
                        h += 1
                        if h == 10:
                            break

for i in range(0, len(ss)):
    solve(dataSets[i], ans[i], i)

sumW = [sumWv2, sumWv5, sumWpzzv2, sumWpzzv5]

# print sumW[0][-1][3], sumW[2][-1][3]

maxZL = [[[0 for i in range(10)] for i in range(4)] for i in range(len(ss))]
maxZR = [[[0 for i in range(10)] for i in range(4)] for i in range(len(ss))]

algs= ["v2", "v5", "pzzv2", "pzzv5"]
for i in range(0, len(ss)):
    for j in range(len(algs)):
        with open("logs/maxZ/"+algs[j] +"/" + ss[i] + ".txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                if line.count('maxZ') > 0:
                    a = line.index(':')

                    h = int(line[:a])
                    if h >= 10:
                        continue

                    l = a + 1
                    while line[l].isdigit() == False:
                        l += 1
                    
                    r = l + 1
                    while line[r].isdigit():
                        r += 1

                    ml = int(line[l:r])

                    l = r + 7
                    mr = int(line[l:])

                    maxZL[i][j][h] = ml
                    maxZR[i][j][h] = mr

# for i in range(5):
#     for j in range(4):
#         print maxZL[i][j][3],
#     print

from math import factorial
 
def C(n, m):
    return factorial(n) / (factorial(m) * factorial(n - m))

PQs = [(2,3), (2,8), (3,4), (3,5), (3,9), (4, 5), 
    (4, 8), (5,3),(5,6),(5,9), (6,4),(6,7), (7,4),(7,7), (8,4),(8,8),(9,4),(9,9)]
# PQs = [(p, q) for p in range(2, 10) for q in range(2, 10)]
# for i in [-2]:
#     # for p in range(2, 10):
#     #     for q in range(2, 10):
#     for h in range(2, 10):
#         print h, sumW[0][i][h], sumW[2][i][h]

for i in [-2]:
    # for p in range(2, 10):
    #     for q in range(2, 10):
    for p, q in PQs:
        # print sumW[0][i][min(p, q)], sumW[2][i][min(p, q)]

        print "$(", p,",", q, ")$ ", 

        hCount = 1.0*realV[i][p][q]*C(max(p,q), min(p,q))


        minV = 1e12
        minJ = 2
        for j in range(len(sumW)):
            if sumW[j][i][min(p,q)] == 0:
                # print ss[i], algs[j], p, q, -1
                continue
            else:
                rho = hCount / sumW[j][i][min(p,q)]
                Z = 0
                if p > q:
                    Zl = maxZL[i][j][min(p, q)]
                    # print Zl, p-q
                    Z = C(Zl, min(Zl,p - q))
                else:
                    Zr = maxZR[i][j][min(p, q)]
                    # print "xx ",ss[i], p, q, algs[j], Zr, q-p
                    Z = C(Zr, min(Zr, q - p))

                # print ss[i], algs[j], p, q, rho, Z,
                if rho == 0:
                    # print "inf", "inf"
                    # print "& inf",
                    continue
                else:
                    # print 1.0*Z/rho, (1.0*Z/rho)**2
                    if (Z/rho)**2 < minV:
                        minV = (Z/rho)**2
                        minJ = j
                    # print "& ", "{:.1e}".format((1.0*Z/rho)**2),
        
        for j in range(len(sumW)):
            if sumW[j][i][min(p,q)] == 0:
                # print ss[i], algs[j], p, q, -1
                continue
            else:
                rho = hCount / sumW[j][i][min(p,q)]
                if p > q:
                    Zl = maxZL[i][j][min(p, q)]
                    # print Zl, p-q
                    Z = C(Zl, min(Zl,p - q))
                else:
                    Zr = maxZR[i][j][min(p, q)]
                    # print "xx ",ss[i], p, q, algs[j], Zr, q-p
                    Z = C(Zr, min(Zr, q - p))

                    
                # print ss[i], algs[j], p, q, rho, Z,
                if rho == 0:
                    # print "inf", "inf"
                    print "& inf",
                else:
                    print "& ",

                    if j == minJ:
                        print "\\textbf{", 
                    print "{:.2e}".format((Z/rho)**2),

                    if j == minJ:
                        print "} ",
        print "\\\\"
# for i in range(len(ss)):
#     for j in range(len(sumW)):
#         for p in range(2, 10):
#             for q in range(2, 10):
#                 if sumW[j][i][min(p,q)] == 0:
#                     print ss[i], algs[j], p, q, -1
#                 else:
#                     rho = 1.0*realV[i][p][q]*C(max(p,q), min(p,q)) / sumW[j][i][min(p,q)]
#                     if p > q:
#                         Zl = maxZL[i][j][min(p, q)]
#                         # print Zl, p-q
#                         Z = C(Zl, min(Zl,p - q))
#                     else:
#                         Zr = maxZR[i][j][min(p, q)]
#                         # print "xx ",ss[i], p, q, algs[j], Zr, q-p
#                         Z = C(Zr, min(Zr, q - p))

                     
#                     print ss[i], algs[j], p, q, rho, Z,
#                     if rho == 0:
#                         print "inf", "inf"
#                     else:
#                         print 1.0*Z/rho, (1.0*Z/rho)**2
            

# for i in range(len(ss)):
#     # print ss[i]
#     for p in range(2, 10):
#         for q in range(2, 10):
#             if sumWv2[i][min(p,q)] == 0:
#                 print -1,
#             else:
#                 rho = 1.0*realV[i][p][q]*C(max(p,q), min(p,q)) / sumWv2[i][min(p,q)]
#                 # Z = maxZL[i][]
#                 print rho,
#         print
#     print

# for i in range(len(ss)):
#     # print ss[i]
#     for p in range(2, 10):
#         for q in range(2, 10):
#             if sumWv2[i][min(p,q)] == 0:
#                 print -1,
#             else:
#                 print 1.0*realV[i][p][q]*C(max(p,q), min(p,q)) / sumWv5[i][min(p,q)],
#         print
#     print
#  11076