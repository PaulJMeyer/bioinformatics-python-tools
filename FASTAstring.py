fasta_text = """>seq1
ATGCGTA CGTA
CGTACGATCG
>seq2
TTTGGGCCC
AAA"""   # clean FASTA

fasta_text2 = """
# this is a comment line

>seq1
ATGCATGC
"""   #text/space before first header should be ignored

fasta_text3 = """>seq1
ATGCATGC

GATTACA
"""   #empty lines should be ignored


fasta_text4 = """>seq1 Homo sapiens BRCA1 gene
ATGCATGC
"""   #description of sequence should not be included

fasta_text5 = """>seq1
>seq2
ATGC
"""   #header without sequence -> ignore or include without crash

fasta_text6 = """   >seq1
ATGCATGC
"""   #whitespace before >, header should still be recognised

fasta_text7 = """>seq1
ATGCATGC
### bookmark ###
GATTACA
"""   #lines with invalid symbols should be ignored

fasta_text8 = """>seq1
ATGC\tAT GC
GAT\tTACA
"""   #spaces and tabs should be removed

allowed = {"A", "C", "G", "T", "N", "R", "Y", "K", "M", "S", "W", "B", "D", "H", "V", "-"}


def clean_sequence(seq: str) -> str:
    return seq.upper().replace("\n", "").replace(" ", "").replace("\t", "")

# parse_fasta returning a list:
def parse_fasta(fasta_text: str) -> list(tuple(str), ):
    lines = fasta_text.splitlines()

    current_header = None
    current_seq = ""
    results = []

    for line in lines:
        line = line.strip()   #gets rid of whitespaces
        if line.startswith(">"):
            if current_header != None:
                results.append((current_header, current_seq))
            current_header = line[1:].split()[0]    #removes every word of the header except the first one
            current_seq = ""
        else:
            clean_line = clean_sequence(line)
            if clean_line == "":                        #ignores empty lines
                continue
            if not set(clean_line).issubset(allowed):   #ignores lines that have invalid symbols
                continue
            else:
                current_seq += clean_line

    if current_header != None:
        results.append((current_header, current_seq))
    return results

print("1", parse_fasta(fasta_text))
print("2", parse_fasta(fasta_text2))
print("3", parse_fasta(fasta_text3))
print("4", parse_fasta(fasta_text4))
print("5", parse_fasta(fasta_text5))
print("6", parse_fasta(fasta_text6))
print("7", parse_fasta(fasta_text7))
print("8", parse_fasta(fasta_text8))