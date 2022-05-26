# from cProfile import label
# import matplotlib.pyplot as plt
import sys

# f1 = "../data/pivot_dblp.txt_degree"
# f2 = "../data/dblpv2noBug.txt"
# f2 = "../data/dblpapm0.5.txt"
# f2 = "../data/dblpcpDP100000.txt"
# f2 = "../data/dblpV3100000.txt"
# f2 = "../data/appAll_dblp_degree.txt"
# f2 = "../data/appAll_dblp_core_100000.txt"
# f2 = "../data/cppm_dblp_degree_100000_O3.txt"

# f1 = "../data/pivot_actor2.txt_degree"
# f2 = "../data/cppm_actor2_degree_1000000_O3.txt"

# f1 = "../data/pivot_github.txt_degree"
# f2 = "../data/cppm_github_degree_100000_O3.txt"
# f2 = "../data/git_bar200.txt"
# f2 = "../data/appAll_v2_git_nobug1e6.txt"

# f2 = "../data/cppm_dblp_degree_100000_bar1000"
# f2 = "../data/appAll_actor2_dp_100000.txt"
# f2 = "../data/tmp.txt"

f1 = sys.argv[1]
f2 = sys.argv[2]

print(f1)
print(f2)

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

            # if p==2 and q==2:
            #     print line

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

# a = 0.0

# e5 = 0.0
# c5 = 0
# e3 = 0.0
# c3 = 0

# c = 0
# for p,q,v in zip(ps, qs, vs):
#     if p == 2 and q == 2:
#         print v
# for p,q,v in zip(ps2, qs2, vs2):
#     if p == 2 and q == 2:
#         print v      

# for p,q,v in zip(ps, qs, vs):

#     if p > 10 or q > 10:
#         c += 1
#         continue
#     f = False
#     if p <= 5 and q <= 5:
#         c5 += 1
#     if p <= 3 and q <= 3:
#         c3 += 1

#     # print p,"-",q,":",
#     for p2,q2,v2 in zip(ps2, qs2, vs2):
#         if p == p2 and q == q2:
#             # print abs(1.0*v - v2) / v
#             a += abs(1.0*v - v2) / v
#             f = True

#             if p <= 5 and q <= 5:
#                 e5 += abs(1.0*v - v2) / v
#             if p <= 3 and q <= 3:
#                 e3 += abs(1.0*v - v2) / v
#             break
#     if f == False:
#         a += 1
#         # print 1
#         if p <= 5 and q <= 5:
#             e5 += 1
#         if p <= 3 and q <= 3:
#             e3 += 1
# print(a / (len(ps)-c))
# print(e5 / c5)
# print(e3 / c3)

# print

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

print(sumE5 / cnt4)
print(sumE50 / cnt50)
print(sumE / cnt2)
print("{}/{}/{}".format(cnt3, cnt, cnt2))
# print(len(ps), len(ps2))
print(1.0*tm/1000)

# for h in range(5, 11):
#     s = 0.
#     c = 0
#     for p in range(2, h + 1):
#         for q in range(2, h + 1):
#             if hot[p][q] > 0:
#                 s += hot[p][q]
#                 c += 1
#     print(s / c)

# for i in range(2, 100):
#     if cntAll[i] > 0:
#        print i, sumEAll[i]/cntAll[i]

# print(hot[:xhot][:yhot])
# x = 1446272193519243586043682213813997609550616871565901180549663326457561088.00
# y = 1446272193519243193724823752146449869813777921086750174152448047455404032
# print((x - y) / x)

# l = ["{}-{}".format(ps[i], qs[i]) for i in range(len(ps))]
# print(l)

# plt.bar(l, vs)
# plt.plot([i for i in range(len(ps))], vs)
# plt.xticks(x =[i for i in range(len(ps))], 
#     labels=l
#     , rotation='vertical')

# plt.show()

