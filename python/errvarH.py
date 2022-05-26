import os
import sys
import commands 

# s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
s = "actor2"
ss = s.split()
# fs = ['varH', 'varHv5', 'pzz1e5VarH', 'pzzv51e5VarH']
fs = ['varT', 'varTv5', 'pzzvarT', 'pzzv5varT']
# fs = ['varT']
# print(ss)

def walkFile(file):
    fileNames = [' ' for i in range(len(ss))]
    for root, dirs, files in os.walk(file):
        i = 0
        for f in files:
            if f.endswith(".txt") and f.startswith("50") and f[2].isdigit() ==False:

                totalF = os.path.join(root, f)
                
                j = 0
                while(j < len(ss) and totalF.count(ss[j]) == 0):
                    j += 1
                if j == len(ss):
                    continue

                fileNames[j] = totalF
    return fileNames

ans = ['' for i in range(len(ss))]
def walkFile2(file):
    global ans
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

# walkFile(sys.argv[1])
# print fileNames

walkFile2("logs/")
# print ans

# outF = sys.argv[1]

for d in fs:
    fileNames = walkFile("logs/" + d)
    print d

    for f2, f1 in zip(fileNames, ans):
        print f1, f2
        ps = []
        qs = []
        vs = []

        with open(f1, 'r') as f:
            lines = f.readlines()

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

        ps2 = []
        qs2 = []
        vs2 = []

        tm = 0

        with open(f2, 'r') as f:
            lines = f.readlines()

            for line in lines:
                if line.startswith("time:"):
                    # print("there")
                    i = line.index(':')
                    j = line.index('ms')
                    # print(i, j)

                    # print(line[i + 1:j])

                    tm = int(line[i + 1:j])

                if line.count('-') > 0 and line.count(':') > 0:
                    p1 = line.index('-')
                    p2 = line.index(':')

                    p = int(line[:p1])
                    q = int(line[p1 + 1 : p2])

                    if p == 1 or q == 1:
                        continue
                        
                    if line[p2 + 1] == ' ':
                        p2 += 1
                    
                    v = int(line[p2 + 1:-1])
                    if line[-1].isdigit():
                        v = int(line[p2 + 1:])

                    ps2.append(p)
                    qs2.append(q)
                    vs2.append(v)



        cnt = 0
        cnt3 = 0
        sumE = 0
        cnt2 = 0

        sumE5 = 0
        cnt4 = 0

        sumE50 = 0
        cnt50 = 0

        hot = [[0 for i in range(100)] for i in range(100)]

        xhot = 0
        yhot = 0

        sumEAll = [0. for i in range(100)]
        cntAll = [0 for i in range(100) ]

        j = 0
        for i in range(len(ps)):
            p = ps[i]
            q = qs[i]
            vReal = vs[i]
            hot[p][q] = 1

            if p > 200 or q > 200:
                continue

            while j < len(ps2):
                if p > ps2[j]:
                    j += 1
                elif p == ps2[j] and q > qs2[j]:
                    j += 1
                elif p == ps2[j] and q == qs2[j]:
                    vApp = vs2[j]

                    err = abs((1.0*vReal - vApp) / vReal)
                    # print p,q,err

                    sumE += err
                    cnt2 += 1

                    hot[p][q] = err
                    xhot = max(xhot, p)
                    yhot = max(yhot, q)

                    sumEAll[min(p,q)] += err
                    cntAll[min(p, q)] += 1

                    if p <= 5 and q <= 5:
                        sumE5 += err
                        cnt4 += 1

                    if p <= 50 and q <= 50:
                        sumE50 += err
                        cnt50 += 1

                    if err > 0.05:
                        # print("{}-{}:{:.7f} real:{} appro:{}".format(p, q, err, vReal, vApp))
                        # print("{}-{}:{:.7f}".format(p, q, abs(err)))
                        cnt = cnt + 1

                        if err > 0.1:
                            cnt3 += 1

                    j += 1
                    break
                else:
                    break

        # print(sumE5 / cnt4)
        # print(sumE50 / cnt50)
        # print(sumE / cnt2)
        # print("{}/{}/{}".format(cnt3, cnt, cnt2))
        # # print(len(ps), len(ps2))
        # print(1.0*tm/1000)

        for p in range(2,10):
            for q in range(2,10):
                print hot[p][q],
                # print abs((1.0*vReal - vApp) / vReal)
            print
        print



        

