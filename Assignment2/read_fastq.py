fastq_list = []
sequence = []
nucleotides = ["A", "T", "G", "C"]
with open("test.fastq") as input_file:
    for line in input_file.readlines():
        if line[0] == "@":
            fastq_list.append(line[1:].replace("\n", ""))
        elif line[0] in nucleotides:
            sequence.append(line.replace("\n", ""))

print(len(fastq_list))
for element in fastq_list:
    print(element)
print("========")
for seq in sequence:
    print(seq)
