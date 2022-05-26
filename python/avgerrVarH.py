import os
import sys
import commands 

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
# s = "dbpe you"
ss = s.split()
fs = ['varH', 'varHv5', 'pzz1e5VarH', 'pzzv51e5VarH']

def walkFile(file):
    fileNames = [' ' for i in range(len(ss))]
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
    return fileNames

