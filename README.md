# bioinformatics-python-tools
A collection of Python tools for DNA sequence analysis, built from scratch as an introduction to bioinformatics programming. The project covers sequence validation, FASTA file parsing, reverse complementing, and RNA transcription — with further functionality planned.

# Tools
## basicDNA.py
Basic sequence analysis for a hardcoded DNA string.

Validates that the sequence contains only standard bases (A, C, G, T)
Counts individual nucleotide frequencies
Calculates GC content (in %)


## reverse_complement.py
Computes the reverse complement and RNA transcript of a DNA sequence.

Supports standard bases as well as IUPAC ambiguity codes and gaps
Validates the input sequence; prompts for re-entry if invalid
Handles both coding and template strand logic for RNA transcription


## FASTAstring.py
Parser for FASTA-formatted sequences, tested against a range of edge cases.
Handles:

Whitespace and tab characters in sequences
Empty lines between sequence blocks
Comment-like lines with invalid characters (silently skipped)
Multi-word headers (only the sequence ID is retained)
Headers with no associated sequence
Leading whitespace before >

Returns: a list of (header, sequence) tuples

## FASTAanalysis.py
Applies the FASTA parser to a real sequence file and runs a full analysis pipeline.
For each parsed sequence:

Validates the sequence and reports its length in base pairs
Computes the reverse complement
Transcribes to RNA (coding or template strand mode)

Test data (sequence.fasta): two E. coli genes sourced from NCBI

NC_000913.3 — E. coli K-12 MG1655
NC_002695.2 — E. coli O157:H7 str. Sakai


Supported IUPAC Codes
SymbolMeaningA, C, G, TStandard basesNAny baseRA or G (purine)YC or T (pyrimidine)KG or TMA or CSG or CWA or TB, D, H, VThree-base ambiguity codes-Gap

Planned Features

GC content and nucleotide statistics for FASTA files
ORF (Open Reading Frame) detection
Codon usage analysis
Support for protein sequences (FASTA amino acid format)
Command-line interface (argparse)


Requirements
Python 3.x — no external dependencies.