
from DNAToolkit import *
dna = genDNA(33)
print("DNA >" + dna)
print("\n")
print(DNA2PEPTIDE(dna, start=1)) # equivalent to DNA2PEPTIDE(dna) since translation starting position is 1