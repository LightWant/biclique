import os
import sys
import commands 

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
# s = "mu"
ss = s.split()

# fs = ['varT']
# print(ss)

def walkFile(file, t):
    fileNames = [' ' for i in range(len(ss))]
    for root, dirs, files in os.walk(file):
        i = 0
        for f in files:
            if f.endswith(".txt") and f.startswith(str(t)) and f[len(str(t))].isdigit() == False:

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
def solve(f1, f2):
    real = [[0 for i in range(100)] for i in range(100)]

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

                real[p][q] = v

    # print real
    appro = [[0 for i in range(100)] for i in range(100)]

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

                appro[p][q] = v
    # print appro
    sumE = 0.
    t = 0

    z = 11
    for p in range(2, z):
        for q in range(2, z):
            if real[p][q] == 0:
                continue
            t += 1
            sumE += abs(1.0*real[p][q] - appro[p][q]) / real[p][q]

    
    return sumE / t

fs = ['varT', 'varTv5', 'pzzvarT', 'pzzv5varT']
# fs = ['varTv5']
for d in fs:
    # print "algorithm", d
    # for t in range(1, 11):
    
    # for t in range(10, 110, 10):
    # for t in [1, 5, 10, 50, 100]:
    for t in [1, 10, 30, 60, 100]:
        # print t,":",
        fileNames = walkFile("logs/"+d, t)
        # print fileNames
        # print t

        for f2, f1 in zip(fileNames, ans):
            print "{:.6f}".format(solve(f1, f2)),
            # print f2, f1
        print


            
# 69284
