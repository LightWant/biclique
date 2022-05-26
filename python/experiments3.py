import os
import sys
import commands 

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
ss = s.split()
# print(ss)

fileNames = [' ' for i in range(len(ss))]

def walkFile(file):
    for root, dirs, files in os.walk(file):
        i = 0
        for f in files:
            if f.endswith(".txt") and f.startswith("11"):

                totalF = os.path.join(root, f)
                
                j = 0
                while(j < len(ss) and totalF.count(ss[j]) == 0):
                    j += 1
                if j == len(ss):
                    continue

                fileNames[j] = totalF

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

walkFile(sys.argv[1])
print fileNames

walkFile2("logs/")
print ans

outF = sys.argv[2]

for a, b in zip(fileNames, ans):
    print a, b

    run = "python python/plotErr.py "+ b +" " + a + " >> "+ outF
    # print run
    print(commands.getstatusoutput(run))


    

