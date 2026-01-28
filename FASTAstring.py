fasta_text = """>seq1
ATGCGTACGTA
CGTACGATCG
>seq2
TTTGGGCCC
AAA"""

lines = fasta_text.splitlines()

current_header = None
current_seq = ""
results = []

for line in lines:
    if line.startswith(">"):
        if current_header != None:
            results.append((current_header, current_seq))
        current_header = line[1:]
        current_seq = ""
    else:
        current_seq += line

if current_header != None:
    results.append((current_header, current_seq))


print(results)