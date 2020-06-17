
from DNAToolkit import *
mRNA = genmRNA(33)
print("mRNA >" + mRNA)
print("\n")
print(mRNA2PEPTIDE(mRNA, start=1)) # equivalent to mRNA2PEPTIDE(mRNA) since translation starting position is 1