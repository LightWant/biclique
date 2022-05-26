import os

s = "dbpe you book	git	cite stackoverflow	mu	imdb	actor2	ama	dblp"
ss = s.split()
cnt = [0. for i in range(len(ss))]
cnt2 = [0 for i in range(len(ss))]
cnt3 = [0. for i in range(len(ss))]


def walkFile(file):
    for root, dirs, files in os.walk(file):
        for f in files:
            # print f
            i = f.index('_')
            j = i + 1
            while f[j] != '_':
                j += 1
            k = f.index('.')


            pf = 0
            while ss[pf] != f[:i]:
                pf += 1

            p = int(f[i+1:j])
            q = int(f[j+1:k])
            cnt2[pf] += 1
            # print ss[pf],p,q

            totalF = os.path.join(root, f)
            with open(totalF, 'r') as pF:
                lines = pF.readlines()

                for l in lines:
                    if l.startswith("Construct graph: using"):
                        h = 0
                        while l[h].isdigit() == False:
                            h += 1
                        
                        t = h + 1
                        while l[t].isdigit() or l[t] == '.':
                            t += 1

                        ti = float(l[h : t])
                        cnt3[pf] += ti

                if p == 2 and q == 2:
                    l = lines[-2]
                    # Count butterflies: using 0.05 seconds.
                    # print l

                    v = l[l.index("g ") + 2: l.index(" s")]
                    v = float(v)
                    cnt[pf] += v
                    # print v
                else:
                    l = lines[-3]
                    # Computing biclique: using 26999 mseconds.
                    # print l

                    if l.count("using") > 0:
                        v = l[l.index("using ") + 6: l.index(" msec")]
                        v = float(v)
                        cnt[pf] += v / 1000

                        # if ss[pf] == 'dblp':
                        #     print p,q,v
                    

walkFile("bclist/all/")
print ss
print cnt
print cnt2
print cnt3

cnt4 = [cnt2[i] + cnt3[i]/cnt2[i] for i in range(len(cnt2))]
print cnt4
# Computing biclique: using 10916350 mseconds.