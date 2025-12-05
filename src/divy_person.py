#!/usr/bin/env python3

import sys
if __name__ == "__main__":
    infn = sys.argv[1]
    outdir = sys.argv[2]
    inf = open(infn, "r")
    header = inf.readline()

    names = ["daniel", "hershey", "curry"]
    splitxt = [[] for x in range(0,len(names))]
    dex = 0
    for line in inf:
        #print(line)
        splitxt[dex].append(line)
        dex = (dex + 1) % len(splitxt)

    for d in range(0,len(names)):
        outf = open(outdir + names[d] + "_" + infn, "w+")
        outf.write(header)
        for txt in splitxt[d]:
            #print(f"Writing: {txt}")
            outf.write(txt)
        outf.close()
