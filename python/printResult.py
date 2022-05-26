import os

def walkFile(file):
    for root, dirs, files in os.walk(file):
        for f in files:
            # print(os.path.join(root, f))
            if f.startswith("pivot_") and f.endswith("_degree"):
                
                s = f[f.index('_')+1:f.index('.')]
                if s.startswith("exam"):
                    continue
                # print("\""+s+"\"", end=',')

                totalF = os.path.join(root, f)
                with open(totalF, 'r') as pF:
                    lines = pF.readlines()
                    l = lines[-1]
                    # print(l)
                    if l.startswith("time"):
                        t = float(l[l.index(':')+1 : l.index("ms")])
                        print(t / 1000, end=',')
                    else:
                        print('inf', end=',')


walkFile("../logs/")
print()
