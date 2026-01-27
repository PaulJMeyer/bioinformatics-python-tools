seq = "ACTGCTGCAGTCAGTCAGTCAGTCGTCATGCATCTTGCTA"
seq = seq.upper().replace("\n", "").replace(" ", "")

base = {"A", "C", "G", "T", "N"}
comp = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}

print("Sequenz:", seq)

while True:

    length = len(seq)
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")
    N = seq.count("N")
    bp = A + C + G + T + N

    if length == bp:
        break
    else:
        seq = input("Sequence invalid (contains NOT only A/C/G/T/N). Enter new sequence:")
        seq = seq.upper().replace("\n", "").replace(" ", "")

complement = ""
for base in seq:
    complement += comp[base]

rev_complement = complement[::-1]

print("Reverse Complement:", rev_complement)
