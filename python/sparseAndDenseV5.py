import os
import sys
import commands 
import time

s = "dbpe you book	git	cite nips stackoverflow	mu	imdb	actor2	ama flickr movie	dblp"
ss = s.split()

ex = [0 for i in range(len(ss))]
ap = [0 for i in range(len(ss))]
hAll = [0 for i in range(len(ss))]
hDense = [0 for i in range(len(ss))]

def walkFile(file):
    for root, dirs, files in os.walk(file):
        i = 0

        for f in files:
            if f.startswith("11") == False or f[2].isdigit() == True:
                continue
            print f

            j = 0
            while(j < len(ss) and f.count(ss[j]) == 0):
                j += 1
            if j == len(ss):
                continue

            totalF = os.path.join(root, f)
            
            with open(totalF, "r") as f:
                lines = f.readlines()

                for line in lines:
                    if line.startswith("exact:"):
                        st = line.index(":")
                        ex[j] = int(line[st + 1:])
                    elif line.startswith("sample:"):
                        st = line.index(":")
                        ap[j] = int(line[st + 1:])

                    if line.startswith('sumW'):
                        h = 2
                        for i in range(len(line)):
                            if line[i] == ':':
                                jj = i + 1
                                while jj < len(line) and line[jj].isdigit() == True:
                                    jj += 1
                                if h == 7:
                                    hDense[j] = int(line[i + 1:jj])
                                    break
                                h += 1

for si in range(len(ss)):
    with open("logs/varHv5/11" + ss[si] + ".txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            # print line
            if line.startswith('sumW'):
                h = 2
                for i in range(len(line)):
                    if line[i] == ':':
                        j = i + 1
                        while j < len(line) and line[j].isdigit() == True:
                            j += 1
                        if h == 7:
                            # if ss[si] == "cite":
                            #     print line
                            #     print int(line[i + 1:j])
                            hAll[si] = int(line[i + 1:j])
                            # if ss[si] == "cite":
                            #     print hAll[si]
                            break
                        h += 1
    if ss[si] == "cite":
        print hAll[si]

walkFile("logs/pzzv51e5VarH/")

print ex, ap, hDense, hAll

print hAll
realNameStr = "Dbpedia	Youtube	Bookcrossing Github	Citeseer Nips Stackoverflow	Twitter	IMDB Actor2	Amazon Flickr Movielens	DBLP"
# realNameStr = "Dbpedia	Youtube	Bookcrossing Github	Citeseer Stackoverflow	Twitter	IMDB Actor2	Amazon	DBLP"
realName = realNameStr.split()

for n, a,b,c,d in zip(realName, ex, ap, hDense, hAll):
    if c > d:
        c = d #float issue

    print "\\textbf{"+n+"}",
    print "& ", format(a,","), "& ", format(b,","), "& ", "{:.2e}".format(c), "& ", "{:.2e}".format(d),
    print "\\\\"
