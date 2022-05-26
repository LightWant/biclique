import sys

# a = 2212471124668450404893683833896960.0
# b = 2192064860692529391558761465774080.0

# print(b - a)

# print(abs(b - a) / b)

ls = ['' for i in range(7)]

with open(sys.argv[1]) as f:
    lines = f.readlines()

    i = 0
    j = 0

    for line in lines:
        if i == 2 or i == 4 or i == 5:
            if line[-1].isdigit() == False:
                line = line[0:-1]
            
            ls[i] += ' ' + line
            # print line,
            # j += 1
            # if j >= 12:
            #     print line,
        if i == 6:
            if line[-1].isdigit() == False:
                line = line[0:-1]
            print line,

        i += 1
        i %= 7

for s in ls:
# print(ls)
    print s

# a = 3.29113e+10
# b = 32911325230
# print (b - a) / a
