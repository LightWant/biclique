import math
import os

s = "dbpe you book	git	cite nips stackoverflow	mu	imdb	actor2	ama flickr movie dblp"

ss = s.split()
realNameStr = "Dbpedia	Youtube	Bookcrossing Github	Citeseer Nips Stackoverflow	Twitter	IMDB Actor2	Amazon Flickr Movielens	DBLP"
realName = realNameStr.split()


dataSets = ['' for i in range(len(ss))]
# dataSets = []
n1 = [0 for i in range(len(ss))]
n2 = [0 for i in range(len(ss))]
m = [0 for i in range(len(ss))]

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
            # dataSets[j] = totalF
            dataSets[j] = realName[j]
            # dataSets.append(f[:-4])

            with open(totalF, 'r') as pF:
                    l = pF.readline()
                    print l
                    x,y,z = map(int, l.split(' '))
                    # n1.append(x)
                    # n2.append(y)
                    # m.append(z)
                    n1[j] = x
                    n2[j] = y
                    m[j] = z


walkFile2("data/")

xx = zip(dataSets, n1, n2, m)
dataSets = sorted(xx, key=lambda x:x[3])

for na, x, y, z in dataSets:
    print "\\textbf{"+na+"}",  
    print " & " + format(x,","), 
    print " & " + format(y,","), 
    print " & " + format(z, ","),

    print " & {:.2f} ".format(1.0*z/x),
    print " & {:.2f} ".format(1.0*z/y),

    print "\\\\"
# print xx

# for na, x,y,z in zip(dataSets, n1, n2, m):
#     print na, x, y, z

# print dataSets




# a = [10,113, 201,360,304,44,51,253,111,71]
# b = [3,8,12]
# alg = ['amazon0601', 'com-DBLP' ,'web-BerkStan', 'com-LiveJournal', 'com-Friendster', 
#     'web-Google', 'loc-Gowalla', 'com-Orkut', 'as-Skitter', 'web-Stanford']
# c = [[403394, 4886816, 10],[425957, 1049866*2,113],[685230, 13298940, 201],[4036538, 69362378, 360],[65608366, 1806067135*2,304],[916428, 8644102, 44],
#     [196591, 1900654, 51],[3072627, 117185083*2, 253],[1696415, 22190596, 111], [281903, 3985272, 71]
# ]


# sortByNode = {}
# for x in range(len(alg)):
#     sortByNode[c[x][0]] = alg[x]
# ns = sorted(sortByNode)
# print("[", end="")
# for xx in ns:
#     print("'"+sortByNode[xx], end="',")
# print("]")

# for xx in range(len(a)):
#     aName = sortByNode[ns[xx]]
#     x = 0
#     while alg[x] != aName:
#         x = x + 1
#     i = a[x]
#     print("\\textbf{"+alg[x]+"}", end="")
#     # print(" &{}".format(i), end="")

#     print(" & " + format(c[x][0],","), end="")
#     print(" & " + format(int(c[x][1]/2),","), end="")
#     print(" & {} ".format(c[x][2]), end="")

#     print("\\\\")