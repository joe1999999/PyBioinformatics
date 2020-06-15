#DNA Toolkit File
import random 

# For Re-Use Purposes
NUCLEOTIDES = ["A","C","T","G"]

# Checks the Validity of a DNA Sequence
def isValidDNA(DNA):
	upperDNA = DNA.upper()
	for nucleotide in upperDNA:
		if nucleotide not in NUCLEOTIDES:
			return False
	return upperDNA

# Generates a Valid Random DNA Sequence With a Given Length 
def genDNA(length):
	randomDNASequence = "".join([random.choice(NUCLEOTIDES) for nucleotide in range(length)])
	return randomDNASequence

# Counts the Number of Nucleotides in a Given DNA Sequence
def nucCount(DNA):
	if(isValidDNA(DNA) == False):
		return "Invalid DNA Sequence!"
	numNucleotides = 0
	for nucleotide in DNA : 
		numNucleotides+=1 
	return numNucleotides

# Counts The Frequency of Each Nucleotide in a Given DNA Sequence	
def nucFrequencyCount(DNA):
	if(isValidDNA(DNA) == False):
		return "Invalid DNA Sequence!"
	NucleotideFrequencies = {"A" : 0 , "C" : 0 , "T" : 0 , "G" : 0 }
	for nucleotide in DNA : 
		NucleotideFrequencies[nucleotide] += 1 
	return NucleotideFrequencies	
