"""


Problem
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string 

(e.g., ACG is a subsequence of TATGCTAAGATC). 

The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; 

thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices,

and the same index can be reused in more than one appearance of the subsequence; 

for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. 
If multiple solutions exist, you may return any one.

Sample Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

Sample Output
3 8 10

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
            
def findSubsequenceIndices(s, t):
    indices = []
    current_position = 0
    
    # Iterate over each character in t
    for char in t:
        # Find the first occurrence of char in s starting from current_position
        position = s.find(char, current_position)
        if position != -1:
            # Store the 1-based index
            indices.append(position + 1)
            current_position = position + 1  # Update position to search after this index
        else:
            # If character not found, return an empty list (no valid subsequence)
            return []
    
    return indices




# Example usage with sample input
s = DNAs[0]
t = DNAs[1]
result = findSubsequenceIndices(s, t)

# Output the result
if result:
    print(" ".join(map(str, result)))
else:
    print("No subsequence found")
