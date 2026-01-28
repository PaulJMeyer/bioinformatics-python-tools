seq = "ACTGCTGCAGTCAGTCAGTCAGTCGTCATGCATCTTGCTA"
seq = seq.upper().replace("\n", "").replace(" ", "")
seq_type = "coding"

allowed = {"A", "C", "G", "T", "N", "R", "Y", "K", "M", "S", "W", "B", "D", "H", "V", "-"}
comp = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N", "R": "Y", "Y": "R", "K": "M", "M": "K", "S": "S", "W": "W", "B": "V", "V": "B", "D": "H", "H": "D", "-": "-"}

print("Coding sequence:", seq)

while True:

    if set(seq).issubset(allowed):
        print("Sequence valid.")
        break
    else:
        seq = input("Sequence invalid (contains NOT only A/C/G/T/N/R/Y/K/M/S/W/B/D/H/V/-). Enter new sequence:")
        seq = seq.upper().replace("\n", "").replace(" ", "")

complement = ""
for base in seq:
    complement += comp[base]

rev_complement = complement[::-1]

rna = seq.replace("T", "U")

print("Reverse Complement:", rev_complement)
print("RNA transcript:", rna)
