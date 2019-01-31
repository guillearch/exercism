def proteins(strand):

    conversion = {'AUG': 'Methionine',
                  'UUU': 'Phenylalanine',
                  'UUC': 'Phenylalanine',
                  'UUA': 'Leucine',
                  'UUG': 'Leucine',
                  'UCU': 'Serine',
                  'UCC': 'Serine',
                  'UCA': 'Serine',
                  'UCG': 'Serine',
                  'UAU': 'Tyrosine',
                  'UAC': 'Tyrosine',
                  'UGU': 'Cysteine',
                  'UGC': 'Cysteine',
                  'UGG': 'Tryptophan',
                  'UAA': 'STOP',
                  'UAG': 'STOP',
                  'UGA': 'STOP'
                  }

    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    proteins = []

    for codon in codons:
        if codon in conversion.keys():
            if conversion[codon] == 'STOP':
                return proteins
            else:
                proteins.append(conversion[codon])

    return proteins
