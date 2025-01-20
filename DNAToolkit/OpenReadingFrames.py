""" Problem

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, 
without any other stop codons in between. Thus, a candidate protein string is derived by translating
an open reading frame into amino acids until a stop codon is reached.


Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s.
Strings can be returned in any order.



"""


from DNAToolkit import *


DNAs = []
possibleCandidateProteins = []

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
            DNAs.append(DNAReverseComplement(seq))

""" 
The START codon -> "ATG": "M",
The STOP codons -> "TAA": "_", "TAG": "_", "TGA": "_"
"""


def branchingPossibilities(startToEndSeq):
    tempCandidate = [] #temporary empty list to hold the current protein chain
    for codon in range (0, len(startToEndSeq)-2, 3):
        if DNA_Peptide_Codons[startToEndSeq[codon:codon+3]] != "_":
            tempCandidate.append(DNA_Peptide_Codons[startToEndSeq[codon:codon+3]])
        else:
            if tempCandidate not in possibleCandidateProteins:
                possibleCandidateProteins.append(tempCandidate) 
            break


readingFrames = []

for dnaSeq in DNAs:
    for possibleReadingFrameIndex in range (0, 3):
        readingFrames.append(dnaSeq[possibleReadingFrameIndex:])


for frame in readingFrames:
    for nuc in range(0, len(frame)-2, 3):  # Start at nucleotide index 0
        if (DNA_Peptide_Codons[frame[nuc:nuc+3]] == "M"): # Checking if our codon is a start codon 
                # Here we can start adding the possible peptide chain for this particular detected ORF
                restOfSeq =  frame[nuc:]
                branchingPossibilities(restOfSeq)

for prtnseq in possibleCandidateProteins:
    print("".join(prtnseq))


