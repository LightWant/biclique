import os
import sys
import commands 

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
ss = s.split()

ans = ['' for i in range(len(ss))]
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
            ans[j] = totalF

walkFile2("data/")
print ans

for H in range(5, 12):
    for i in range(len(ss)):
        run = "run -f "+ ans[i] + " -v5 -pp -t 100000 -H "+str(H)+" > logs/pzzv51e5VarH/" +str(H)+ ss[i] + ".txt"
        # print run
        print(commands.getstatusoutput(run))
# 30426

# for a, b in zip(files, ans):
#     print a, b

#     run = "python python/plotErr.py "+b +" " + a + " >> logs/pzz/total.txt"
#     print(commands.getstatusoutput(run))


    

