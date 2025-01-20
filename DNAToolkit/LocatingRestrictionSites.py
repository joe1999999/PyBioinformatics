""" Problem 

A DNA string is a reverse palindrome if it is equal to its reverse complement. 
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
You may return these pairs in any order

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4


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
            


def findReversePalindromes(dnaString):
    results = []
    n = len(dnaString)
    
    for length in range(4, 13):  # Lengths between 4 and 12
        for i in range(n - length + 1):  # Start index of the substring
            substring = dnaString[i:i + length]
            if substring == DNAReverseComplement(substring):
                results.append((i + 1, length))  # 1-based index
    
    return results


# Finding reverse palindromes
reversePalindromes = findReversePalindromes(DNAs[0])

# Sample Output
for position, length in reversePalindromes:
    print(position, length)
