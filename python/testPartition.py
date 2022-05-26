# import matplotlib.pyplot as plt

from curses.ascii import isdigit


maxD = 50000
p = [0 for i in range(maxD)]
a = [0 for i in range(maxD)]
ts = []
ds = []
cnt = 0
cnt2 = 0

with open("../logs/edgedensityActor2Pivot.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        if isdigit(line[0]) and line.count('-') == 0:
            y = line.split(',')
            
            t = int(y[-1][1:-4])
            # ts.append(t)
            dSum = int(y[1])
            # ds.append(dSum)

            # avg = float(y[3][1:])

            # avg = int(avg)

            # if dSum >= maxD or dSum < 0:
            # print(dSum,t)

            p[dSum] += t
            a[dSum] += 1
            # p[avg] += t
            # a[avg] += 1


c = [0 if a[i]==0 else p[i]/a[i] for i in range(len(p))]
for i in range(len(c)):
    if c[i] > 0:
        print(i, c[i])

# b = []
# xx = 10
# for i in range(maxD//xx):
#     x = 0
#     for j in range(i*xx, (1+i)*xx):
#         x += p[j]
#     y = 0
#     for j in range(i*xx, (1+i)*xx):
#         y += a[j]
#     if y == 0:
#         b.append(0)
#     else:
#         b.append(x / y)

# print(b)


# print(ts)

# s = 0
# st = 150000
# ed = len(ds)
# for i in range(st, ed):
#     s += ds[i]

# print(s / (ed - st))