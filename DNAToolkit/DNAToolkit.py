#DNA Toolkit File

# For Re-Use Purposes
NUCLEOTIDES = ["A","C","T","G"]

# Checking the Validity of a DNA Sequence
def isValidDNA(DNA):
	#Transform DNA Strand to Upper Case Letters
	upperDNA = DNA.upper()
	for nucleotide in upperDNA:
		if nucleotide not in NUCLEOTIDES:
			return False
	return upperDNA


