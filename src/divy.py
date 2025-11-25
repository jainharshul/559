#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    infn = sys.argv[1]
    outdir = ""
    if len(sys.argv) == 3:
        outdir = sys.argv[2]
    inf = open(infn, "r")
    header = inf.readline()

    names = ["andrew", "daniel", "hershey", "curry"]
    splitxt = [[] for n in names]
	# [[]] * len(names) results in copies of the reference at each index, which is to say doesn't work
    assert len(splitxt) == len(names)
    dex = 0
    for line in inf:
        splitxt[dex].append(line)
        dex = (dex + 1) % len(splitxt)



    for d in range(0,len(names)):
        outf = open(outdir + names[d] + "_" + infn, "w+")
        outf.write(header)
        for txt in splitxt[d]:
            outf.write(txt)
        outf.close()
