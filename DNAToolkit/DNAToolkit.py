#DNA Toolkit File
import random 
# import collections

# For Re-Use Purposes
NUCLEOTIDES = ["A","C","T","G"]
NUCLEOTIDESREVERSECOMPLEMENT = {"A":"T", "T":"A", "C":"G", "G":"C"}

# Checks the Validity of a DNA Sequence
def isValidDNA(DNA):
	upperDNA = DNA.upper()
	for nucleotide in upperDNA:
		if nucleotide not in NUCLEOTIDES:
			return False
	return True

# Generates a Valid Random DNA Sequence With a Given Length 
def genDNA(length):
	randomDNASequence = "".join([random.choice(NUCLEOTIDES) for nucleotide in range(length)])
	return randomDNASequence

# Counts the Total Number of All Nucleotides in a Given DNA Sequence
def nucAllCount(DNA):
	numNucleotides = 0
	for nucleotide in DNA : 
		numNucleotides+=1 
	return numNucleotides

# Counts The Frequency of Each Nucleotide in a Given DNA Sequence	
def nucFrequencyCount(DNA):
	NucleotideFrequencies = {"A" : 0 , "C" : 0 , "T" : 0 , "G" : 0 }
	for nucleotide in DNA : 
		NucleotideFrequencies[nucleotide] += 1 
	return NucleotideFrequencies	
	# return dict(collections.Counter(seq))

# DNA Transcription to RNA
def DNA2RNA(DNA) :
	return DNA.replace("T","U")

# Generates a Reverse Complement of a DNA Strand
def DNAReverseComplement(DNA):
	return ''.join([NUCLEOTIDESREVERSECOMPLEMENT[nuc] for nuc in DNA])[::-1]
	