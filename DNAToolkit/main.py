
from DNAToolkit import *
DNA = genDNA(1000)
print(DNA)
print(DNA2PEPTIDE(DNA))
# Displays Alanine CODONS with their Respective Usage Frequencies
print(CodonUsageFreq(DNA, "A")) # A Refers to Alanine - ALA 