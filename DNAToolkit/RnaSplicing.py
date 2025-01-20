"""Problem
After identifying the exons and introns of an RNA string, 
we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s(of length at most 1 kbp) and a collection of substrings of s acting as introns. 
All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s.
(Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT


Sample Output
MVYIADKQHVASREAYGHMFKVCA


"""

from DNAToolkit import *




DNAs = []

def parseFasta(fp):
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))



with open("fasta.fasta") as fp:
        for name, seq in parseFasta(fp):
            #print(name, seq)\
            DNAs.append(seq)

#This function returns a list of lists containing the starting positions of the introns in the main DNA strand (DNAs[0]) 
def SpliceRNA(DNAs):
    for intron in DNAs[1:]:
        DNAs[0] = DNAs[0].replace(intron, '') # Replace the intron with a an empty '' (deleting introns)
    return DNA2PEPTIDE(DNAs[0]) # This is a function the DNAToolkit
    

#Print the final protein sequence (deleting the stop codon "_")
print("".join(SpliceRNA(DNAs)).replace("_",""))