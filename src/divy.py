#!/usr/bin/env python3

import sys
if __name__ == "__main__":
    infn = sys.argv[1]
    outdir = sys.argv[2]
    inf = open(infn, "r")
    header = inf.readline()

    splitxt = [[], [], [], []]
    dex = 0
    for line in inf:
        splitxt[dex].append(line)
        dex = (dex + 1) % len(splitxt)


    names = ["andrew", "daniel", "hershey", "curry"]

    for d in range(0,4):
        outf = open(outdir + names[d] + "_" + infn, "w+")
        outf.write(header)
        for txt in splitxt[d]:
            outf.write(txt)
        outf.close()
