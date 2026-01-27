seq = "ACTGCTGCAGTCAGTCAGTCAGTCGTCATGCATCTTGCTA"
seq = seq.upper().replace("\n", "").replace(" ", "")

base = {"A", "C", "G", "T"}
comp = {"A": "T", "T": "A", "G": "C", "C": "G"}

print("Sequenz:", seq)

while True:

    length = len(seq)
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")
    bp = A + C + G + T

    if length == bp:
        break
    else:
        seq = input("Sequence invalid (contains NOT only A/C/G/T). Enter new sequence:")
        seq = seq.upper().replace("\n", "").replace(" ", "")

complement = ""
for base in seq:
    complement += comp[base]

print("Complement:", complement)