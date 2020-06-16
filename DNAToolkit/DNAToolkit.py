# DNA Toolkit File
from sequences import *
import random
# import collections


# Checks the Validity of a DNA Sequence
def isValidDNA(DNA):
    upperDNA = DNA.upper()
    for nucleotide in upperDNA:
        if nucleotide not in NUCLEOTIDES:
            return False
    return True

# Generates a Valid Random DNA Sequence With a Given Length


def genDNA(length):
    randomDNASequence = "".join([random.choice(NUCLEOTIDES)
                                 for nucleotide in range(length)])
    return randomDNASequence

# Counts the Total Number of All Nucleotides in a Given DNA Sequence


def nucAllCount(DNA):
    numNucleotides = 0
    for nucleotide in DNA:
        numNucleotides += 1
    return numNucleotides

# Counts The Frequency of Each Nucleotide in a Given DNA Sequence


def nucFrequencyCount(DNA):
    NucleotideFrequencies = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nucleotide in DNA:
        NucleotideFrequencies[nucleotide] += 1
    return NucleotideFrequencies
    # return dict(collections.Counter(seq))

# DNA Transcription to RNA


def DNA2RNA(DNA):
    return DNA.replace("T", "U")

# Generates a Reverse Complement of a DNA Strand


def DNAReverseComplement(DNA):
    return ''.join([NUCLEOTIDESREVERSECOMPLEMENT[nuc] for nuc in DNA])[::-1]

# Calculates CG Content % , use optional arguments 'start' and 'end' to select a specefic sub-sequence


def GCContent(DNA, **kwargs):
    subSeqStart = kwargs.get('start', None)
    subSeqEnd = kwargs.get('end', None)
    if (subSeqEnd and subSeqEnd > 0 and subSeqEnd and subSeqEnd < nucAllCount(DNA)):
        subSequence = DNA[subSeqStart-1:subSeqEnd]
        return ((subSequence.count("C") + subSequence.count("G")) / nucAllCount(subSequence)) * 100
    return ((DNA.count("C") + DNA.count("G")) / nucAllCount(DNA)) * 100
