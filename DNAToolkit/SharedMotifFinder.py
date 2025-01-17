""" Problem 

Given: A collection of k(k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 

(If multiple solutions exist, you may return any single solution.)

Sample Dataset (k = 3)

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Output ==> AC

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



def genPossibleSubSeq(seq):
    # List to store all subsequences
    all_subsequences = []
    # Generate all possible subsequences
    for start in range(len(seq)):  # Starting index
        for end in range(start + 1, len(seq) + 1):  # Ending index (exclusive)
            all_subsequences.append(seq[start:end])
    return all_subsequences


with open("fasta.fasta") as fp:
        for name, seq in parseFasta(fp):
            #print(name, seq)\
            DNAs.append(seq)
        shortest_seq =  min(DNAs, key=len)
        longest_motif = ""
        

        # Try every substring in the shortest sequence
        for length in range(1, len(shortest_seq) + 1):
            for start in range(len(shortest_seq) - length + 1):
                motif = shortest_seq[start:start + length]
                if all(motif in seq for seq in DNAs):
                    if len(motif) > len(longest_motif):
                        longest_motif = motif
        print(longest_motif) 
   
