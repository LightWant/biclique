import os

datasets = ["citeseer","movielens","ama","dblp","mummun","github","youtube","editidwiki","imdb","editenwiki","actor2","stackoverflow","dbpedia","bookcrossing"]
dt = {}
for i in range(len(datasets)):
    dt[datasets[i]] = i
n1 = [0 for i in range(len(datasets))]
n2 = [0 for i in range(len(datasets))]
m = [0 for i in range(len(datasets))]

def walkFile(file):
    for root, dirs, files in os.walk(file):
        for f in files:
            # print(os.path.join(root, f))
            if f.endswith(".txt") and f.startswith("exam")==False:
                # s = f[f.index('_')+1:f.index('.')]
                j = 0
                for i in range(len(datasets)):
                    if datasets[i].count(f[:f.index('.')]) > 0:
                        j = i
                        break
                
                totalF = os.path.join(root, f)
                # print(totalF)

                with open(totalF, 'r') as pF:
                    l = pF.readline()
                    x,y,z = map(int, l.split(' '))
                    n1[j] = x
                    n2[j] = y
                    m[j] = z
                    # print(l, end=' ')

walkFile("../data/")
# print(n1, n2, m)
for x in n1:
    print(x, end=' ')
print()
for x in n2:
    print(x, end=' ')
print()
for x in m:
    print(x, end=' ')
print()
