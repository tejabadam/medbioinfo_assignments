import random

N = int(input("Length:"))
nucleotides = ['A', 'T', 'G', 'C']

dna = [random.choice(nucleotides) for i in range(N)]
dna = ''.join(dna)

print(">myrandomsequence")
print(dna)
