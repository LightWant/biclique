import os
import commands 

def walkFile(file):
    for root, dirs, files in os.walk(file):
        i = 0
        for f in files:
            # print(os.path.join(root, f))
            if f.endswith(".txt") and f.startswith('exam') == False:
                # if f.startswith("youtube") == False:
                #     continue

                totalF = os.path.join(root, f)
                outF = "../logs/pivotf_"+f+"_"+"degree"
                print(totalF)

                run = "../bin/run -f "+totalF+" -p 4 -q 4 -fpm "+"> "+outF
                # print(run)
                print(commands.getstatusoutput(run))

                i = i + 1
            
            # if i >= 5:
            #     break
        
        # if i >= 5:
        #     break

walkFile("../data/")
