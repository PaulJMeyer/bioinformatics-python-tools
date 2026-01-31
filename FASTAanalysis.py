fasta_text = """>seq1
ATGCGTA CGTA
CGTACGATCG
>seq2
TTTGGGCCC
AAA"""

allowed = {"A", "C", "G", "T", "N", "R", "Y", "K", "M", "S", "W", "B", "D", "H", "V", "-"}
comp = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N", "R": "Y", "Y": "R", "K": "M", "M": "K", "S": "S", "W": "W", "B": "V", "V": "B", "D": "H", "H": "D", "-": "-"}

def clean_sequence(s):
    return s.upper().replace("\n", "").replace(" ", "").replace("\t", "")

def is_valid_sequence(seq, allowed):
    return set(seq).issubset(allowed)

def reverse_complement(seq, comp):
    complement = ""
    for base in seq:
        complement += comp[base]

    rev_comp = complement[::-1]
    return rev_comp

def transcribe_to_rna(seq, seq_type, comp):
    if seq_type == "coding":
        rna_seq = seq.replace("T", "U")
    elif seq_type == "template":
        rev_comp = reverse_complement(seq, comp)
        rna_seq = rev_comp.replace("T", "U")
    else:
        rna_seq = "Choose sequence type (coding or template)!"
    return rna_seq

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
        current_seq += clean_sequence(line)

if current_header != None:
    results.append((current_header, current_seq))

print(results)