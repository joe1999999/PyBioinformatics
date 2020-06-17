# DNA Toolkit File
from sequences import *
import random
# import collections


# Checks the Validity of a DNA Sequence
def isValidDNA(DNA):
    upperDNA = DNA.upper()
    for nucleotide in upperDNA:
        if nucleotide not in NUCLEOTIDES["DNA"]:
            return False
    return True

# Checks the Validity of a mRNA Sequence
def isValidmRNA(mRNA):
    uppermRNA = mRNA.upper()
    for nucleotide in uppermRNA:
        if nucleotide not in NUCLEOTIDES["RNA"]:
            return False
    return True

# Generates a Valid Random DNA Sequence With a Given Length
def genDNA(length):
    randomDNASequence = "".join([random.choice(NUCLEOTIDES["DNA"])
                                 for nucleotide in range(length)])
    return randomDNASequence

# Generates a Valid Random mRNA Sequence With a Given Length
def genmRNA(length):
    randommRNASequence = "".join([random.choice(NUCLEOTIDES["RNA"])
                                 for nucleotide in range(length)])
    return randommRNASequence

# Counts the Total Number of All Nucleotides in a Given Sequence
def nucAllCount(sequence):
    numNucleotides = 0
    for nucleotide in sequence:
        numNucleotides += 1
    return numNucleotides

# Counts The Frequency of Each Nucleotide in a Given DNA Sequence
def DNANucFrequencyCount(DNA):
    NucleotideFrequencies = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nucleotide in DNA:
        NucleotideFrequencies[nucleotide] += 1
    return NucleotideFrequencies
    # return dict(collections.Counter(DNA))

# Counts The Frequency of Each Nucleotide in a Given mRNA Sequence
def mRNANucFrequencyCount(mRNA):
    NucleotideFrequencies = {"A": 0, "C": 0, "U": 0, "G": 0}
    for nucleotide in mRNA:
        NucleotideFrequencies[nucleotide] += 1
    return NucleotideFrequencies
    # return dict(collections.Counter(mRNA))

# DNA Sequence Transcription into mRNA
def DNA2mRNA(DNA):
    return DNA.replace("T", "U")

# DNA Sequence Translation into a Peptide Chain
def DNA2PEPTIDE(DNA, **kwargs):
    if (kwargs.get('start', None) is not None):
        initializeCodonPosition = kwargs.get('start', None) - 1
    else:
        initializeCodonPosition = 0
    return [DNA_Peptide_Codons[DNA[readPointer:readPointer+3]] for readPointer in range(initializeCodonPosition, len(DNA) - 2, 3)]

# mRNA Sequence Translation into a Peptide Chain
def mRNA2PEPTIDE(mRNA, **kwargs):
    if (kwargs.get('start', None) is not None):
        initializeCodonPosition = kwargs.get('start', None) - 1
    else:
        initializeCodonPosition = 0
    return [mRNA_Peptide_Codons[mRNA[readPointer:readPointer+3]] for readPointer in range(initializeCodonPosition, len(mRNA) - 2, 3)]

# Generates a Reverse Complement of a DNA Strand
def DNAReverseComplement(DNA):
    return ''.join([NUCLEOTIDESREVERSECOMPLEMENT[nuc] for nuc in DNA])[::-1]

# Calculates CG Content % , use optional arguments 'start' and 'end' to select a specific sub-sequence
def GCContent(sequence, **kwargs):
    subSeqStart = kwargs.get('start', None)
    subSeqEnd = kwargs.get('end', None)
    if (subSeqEnd and subSeqEnd > 0 and subSeqEnd and subSeqEnd < len(sequence)):
        subSequence = sequence[subSeqStart-1:subSeqEnd]
        return ((subSequence.count("C") + subSequence.count("G")) / len(subSequence)) * 100
    return ((sequence.count("C") + sequence.count("G")) / len(sequence)) * 100

