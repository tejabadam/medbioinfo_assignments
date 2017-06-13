def from_sequence_to_proteins(sequence, mapping):
    splits = [sequence[i * 3: i * 3 + 3] for i in range(int(len(sequence) / 3))]
    results = []
    result = ""
    for subset in splits:
        read = mapping.get(subset, "X")
        result += read
        if read == "*":
            results.append(result)
            result = ""

    if result != "":
        results.append(result)
    return results


def get_reverse_complement(sequence):
    translation = str.maketrans("ACGT", "TGCA")
    reverse = sequence.translate(translation)
    return reverse[::-1]


if __name__ == '__main__':
    mapping = dict(TTT="F", TTC="F", TTA="L", TTG="L", TCT="S", TCC="s",
                   TCA="S", TCG="S", TAT="Y", TAC="Y", TAA="*", TAG="*",
                   TGT="C", TGC="C", TGA="*", TGG="W", CTT="L", CTC="L",
                   CTA="L", CTG="L", CCT="P", CCC="P", CCA="P", CCG="P",
                   CAT="H", CAC="H", CAA="Q", CAG="Q", CGT="R", CGC="R",
                   CGA="R", CGG="R", ATT="I", ATC="I", ATA="I", ATG="M",
                   ACT="T", ACC="T", ACA="T", ACG="T", AAT="N", AAC="N",
                   AAA="K", AAG="K", AGT="S", AGC="S", AGA="R", AGG="R",
                   GTT="V", GTC="V", GTA="V", GTG="V", GCT="A", GCC="A",
                   GCA="A", GCG="A", GAT="D", GAC="D", GAA="E", GAG="E",
                   GGT="G", GGC="G", GGA="G", GGG="G")

    filename = input("File name > ")

    with open(filename) as input_file:
        lines = input_file.readlines()
        start = lines.pop(0).replace("\n", "")
        seqs = list()
        sequence = ""
        for line in lines:
            if line[0] == ">":
                seqs.append((start, sequence))
                sequence = ""
                start = line.replace("\n", "")
            else:
                sequence += line.replace("\n", "")
        if sequence != "":
            seqs.append((start, sequence))

    longest_orfs = ""
    for start_line, sequence in seqs:
        sequence = sequence.upper()
        found_orfs = from_sequence_to_proteins(sequence, mapping)
        sequence = get_reverse_complement(sequence)
        found_orfs += from_sequence_to_proteins(sequence, mapping)
        sorted_orfs = sorted(found_orfs, key=len, reverse=True)

        for longest_orfs in sorted_orfs :
            if len(sorted_orfs) > 0:
                longest_orfs = sorted_orfs[0]
            else:
                longest_orfs = ""
        if longest_orfs == "*":
            longest_orfs = sorted_orfs[1]

        print(start_line)
        print(longest_orfs)