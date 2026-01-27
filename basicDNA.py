seq = "ATGCAGTAGCACACAGTACAGTGTGACT"
seq = seq.upper().replace("\n", "").replace(" ", "")

print("Sequenz:", seq)
length = len(seq)

A = seq.count("A")
C = seq.count("C")
G = seq.count("G")
T = seq.count("T")
bp = A + C + G + T

while length != bp:
    seq = input("Sequence invalid (contains NOT only A/C/G/T). Enter new sequence:")
    length = len(seq)
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")
    bp = A + C + G + T

print("length (in bp):", length)
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)
gc_percent = (G + C) / length * 100
print(f"GC%: {gc_percent:.2f}")