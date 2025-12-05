#!/usr/bin/env python3

import sys

def verify(d, h, l):
    if h not in d.keys():
        print(h)
        d[h] = []

    d[h].append(l)
    return d

if __name__ == "__main__":
    infn = sys.argv[1]
    outdir = ""
    if len(sys.argv) == 3:
        outdir = sys.argv[2]
    inf = open(infn, "r")
    header = inf.readline()

    hdex = len(header)
    print(header)
    splead = header.split(",")
    for head in range(0,len(splead)):
        hdex = head if splead[head] == "HLA" else hdex
    print(hdex)

    names = ["andrew", "daniel", "hershey", "curry"]
    names = set()
    splitxt = [[] for n in names]
    buckets = dict()
	# [[]] * len(names) results in copies of the reference at each index, which is to say doesn't work
    assert len(splitxt) == len(names)
    dex = 0
    for line in inf:
        hla = line.split(",")[hdex]
        buckets = verify(buckets, hla, line)
        #splitxt[dex].append(line)
        #dex = (dex + 1) % len(splitxt)

    names = list(buckets.keys())
    print(names)
    #names = [name.replace("/", "|") for name in names]



    for d in range(0,len(names)):
        #break
        nm = outdir + names[d].replace("/", "|") + "_" + infn
        outf = open(nm, "w+")
        outf.write(header)
        for txt in buckets[names[d]]:
            outf.write(txt)
        outf.close()
