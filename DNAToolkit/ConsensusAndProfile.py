""" Problem 


Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)


Sample Dataset : 

>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

"""

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

NUCLEOTIDES = {
    "A" : [0 for x in range(0, len(DNAs[0]))],
    "C" : [0 for x in range(0, len(DNAs[0]))],
    "G" : [0 for x in range(0, len(DNAs[0]))],
    "T" : [0 for x in range(0, len(DNAs[0]))]
}

for col in range (0, len(DNAs[0])):

    for row in DNAs:
    
        if (row[col]) == "A":
            NUCLEOTIDES["A"][col]+=1
        if (row[col]) == "C":
            NUCLEOTIDES["C"][col]+=1
        if (row[col]) == "G":
            NUCLEOTIDES["G"][col]+=1
        if (row[col]) == "T":
            NUCLEOTIDES["T"][col]+=1

# Flipping the list around, I did not want to use numpy, this is vanilla Python
vertical = [[] for _ in range(len(DNAs[0]))]
for v in range (0, len(DNAs[0])):
    for value in NUCLEOTIDES.values():
        vertical[v].append(value[v])

nuc = ["A","C","G","T"] # We use this list to match the most repeated nucleotide at a column with its symbol
maxes = []
for column in vertical :
    max_value = max(column)
    max_index = column.index(max_value)
    maxes.append(nuc[max_index])


# Flatten the lists and join them into a single string
joined_string = ''.join([item for sublist in [maxes] for item in sublist])


print(joined_string)

for key, value in NUCLEOTIDES.items():
    joined_str = ' '.join(map(str, value))
    print(key + ': ' +  joined_str)



"""
Future note to self :
This problem was a pain in the ass

"""



