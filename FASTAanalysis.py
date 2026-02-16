allowed = {"A", "C", "G", "T", "N", "R", "Y", "K", "M", "S", "W", "B", "D", "H", "V", "-"}
comp = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N", "R": "Y", "Y": "R", "K": "M", "M": "K", "S": "S", "W": "W", "B": "V", "V": "B", "D": "H", "H": "D", "-": "-"}
seq_type = "coding"


def clean_sequence(seq: str) -> str:
    return seq.upper().replace("\n", "").replace(" ", "").replace("\t", "")


def parse_fasta(fasta_text: str) -> list(tuple):
    lines = fasta_text.splitlines()

    current_header = None
    current_seq = ""
    results = []

    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if current_header != None:
                results.append((current_header, current_seq))
            current_header = line[1:].split()[0]
            current_seq = ""
        else:
            clean_line = clean_sequence(line)
            if clean_line == "":
                continue
            if not set(clean_line).issubset(allowed):
                continue
            else:
                current_seq += clean_line

    if current_header != None:
        results.append((current_header, current_seq))
    return results


def is_valid_sequence(seq: str):
    return set(seq).issubset(allowed)


def reverse_complement(seq: str) -> str:
    complement = ""
    for base in seq:
        complement += comp[base]

    rev_comp = complement[::-1]
    return rev_comp


def transcribe_to_rna(seq: str) -> str:
    if seq_type == "coding":
        rna_seq = seq.replace("T", "U")
    elif seq_type == "template":
        rev_comp = reverse_complement(seq, comp)
        rna_seq = rev_comp.replace("T", "U")
    else:
        rna_seq = "Choose sequence type (coding or template)!"
    return rna_seq

with open ("sequence.fasta", "r") as f:
    fasta_sequence = f.read()

print("Sequences:", parse_fasta(fasta_sequence))
results = parse_fasta(fasta_sequence)

for header, seq in results:
    if is_valid_sequence(seq) == True:
        print("The sequence is valid. Gene:", header, "bp:", len(seq))
    else:
        print("The sequence is invalid. Gene:", header)

    print("Reverse complement of", header + ":", reverse_complement(seq))
    print("RNA of", header + ":", transcribe_to_rna(seq))
    