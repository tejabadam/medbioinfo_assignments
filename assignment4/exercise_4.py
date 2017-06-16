import argparse
import math


parser = argparse.ArgumentParser(description="loading fasta files")
parser.add_argument("file", nargs='+', help='filename')
args = parser.parse_args()

seqs = {}
for f in args.file:
    with open(f) as input_file:
        lines = input_file.readlines()
        start = lines.pop(0).replace("\n", "")
        sequence = ""
        for line in lines:
            if line[0] == ">":
                seqs[start] = sequence
                sequence = ""
                start = line.replace("\n", "")
            else:
                sequence += line.replace("\n", "")
                sequence = sequence.replace("N", "")
        if sequence != "":
            seqs[start] = sequence

calc = []
for seq in seqs.values():
    counter = []
    for c in 'ATGC':
        counter.append(seq.count(c) / len(seq))
    calc.append(counter)
print(calc)


def sim(x: object) -> object:
    a = x[0]
    b = x[1]
    rms = math.sqrt((0.25*((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2+(a[3]-b[3])**2)))
    print(round(rms , 2))

sim(calc)

print(seqs.keys())

n = len(seqs.values())

#print (n)

table= [ [ 0 for i in range(n) ] for j in range(n) ]
print (table)

for p in range(n):
    for q in range(n):
        if seqs.keys([p]) == seqs.keys([q]):
            print (0, end="\n")
#        else:
#            print (sim(calc), end="\t")
#    print (tmp)
#for p in seqs.keys():
#    for q in seqs.keys():









###sqrt(0.25*(sum(square(A1-A2)+square(T1-T2)+square(G1-G2)+square(C1-C2))))
