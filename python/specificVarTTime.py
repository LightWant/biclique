import os
import sys
import commands 
import time

s = "dblp"
ss = s.split()


def walkFile(file, data, ti):
    for root, dirs, files in os.walk(file):

        for f in files:
            if f.count(data) == 0:
                continue

            b = f.index(".txt")
            a = b
            while f[a] != '_':
                a -= 1
            
            t = int(f[a + 1:b])
            if t != ti:
                continue
            
            with open(os.path.join(root, f), "r") as f:
                lines = f.readlines()

                for line in lines:
                    if line.startswith("time"):
                        a = line.index(":")
                        b = line.index("ms")

                        rt = int(line[a + 1:b])

                        return rt
                        
def walkFileError(file, data, ti):
    for root, dirs, files in os.walk(file):

        for f in files:
            if f.count(data) == 0:
                continue

            b = f.index(".txt")
            a = b
            while f[a] != '_':
                a -= 1
            
            t = float(f[a + 1:b])
            if t != ti:
                continue
            
            with open(os.path.join(root, f), "r") as f:
                lines = f.readlines()

                for line in lines:
                    if line.startswith("error"):
                        a = line.index(":")

                        rt = float(line[a + 1:])

                        return rt

alg = ['v2', 'v5', 'bcv2', 'bcv5']
# ts = [0.0001,0.002, 0.004, 0.006, 0.008, 0.01,
#     1, 2, 5,7,10, 15,20,30,40,50,60,70,80,90,100]
ts = [0.0001,0.001,0.01,0.1,1]
# ts = [1, 5, 10, 30, 60, 100]

# for i in range(len(ss)):
#     for j in range(len(alg)):
#         # print alg[j]
#         tts = []
#         for ti in ts:
#             t = walkFile("logs/specificVarT/" + alg[j], ss[i], ti)
#             tts.append(t)
#         for t in tts:
#             print 1.0*t/1000,
#         print
#         # print tts
print "error"
for i in range(len(ss)):
    for j in range(len(alg)):
        # print alg[j]
        tts = []
        for ti in ts:
            t = walkFileError("logs/specificVarT/" + alg[j], ss[i], ti)
            tts.append(t)
        for t in tts:
            print t,
        print