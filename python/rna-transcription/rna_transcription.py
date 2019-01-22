import string

def to_rna(dna_strand):
    complements = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(complements)
