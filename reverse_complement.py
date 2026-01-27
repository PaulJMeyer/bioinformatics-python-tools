seq = "ACTGCTGCAGTCAGTCAGTCAGTCGTCATGCATCTTGCTA"
seq = seq.upper().replace("\n", "").replace(" ", "")

allowed = {"A", "C", "G", "T", "N", "R", "Y" "K", "M", "S", "W"}
comp = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N", "R": "Y", "Y": "R", "K": "M", "M": "K", "S": "S", "W": "W"}

print("Sequenz:", seq)

while True:

    if set(seq).issubset(allowed):
        print("Sequence valid.")
        break
    else:
        seq = input("Sequence invalid (contains NOT only A/C/G/T/N/R/Y/K/M/S/W). Enter new sequence:")
        seq = seq.upper().replace("\n", "").replace(" ", "")

complement = ""
for base in seq:
    complement += comp[base]

rev_complement = complement[::-1]

print("Reverse Complement:", rev_complement)
