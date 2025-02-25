""" Problem

For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).


Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC


Sample Output
ATTAGACCTGCCGGAATAC
"""

DNAs = []

superString = ""

def parseFasta(fp):
    """
    Parses a FASTA file and yields tuples of (name, sequence).
    """
    name, seq = None, []
    for line in fp:
        line = line.strip()
        if line.startswith(">"):
            if name: 
                yield (name, ''.join(seq))
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name: 
        yield (name, ''.join(seq))

def constructSuperString(DNAs):
    """
    Constructs the shortest superstring by merging overlapping DNA sequences.
    """
    global superString
    while DNAs:
        # Take the first DNA sequence as the initial superstring
        if not superString:
            superString = DNAs.pop(0)
            continue
        
        best_match = None
        best_overlap = 0
        
        # Find the best overlapping sequence
        for seq in DNAs:
            overlap_suffix = 0
            overlap_prefix = 0
            
            # Check suffix overlap
            for i in range(1, len(seq)):
                if superString.endswith(seq[:i]):
                    overlap_suffix = i
            
            # Check prefix overlap
            for i in range(1, len(seq)):
                if superString.startswith(seq[-i:]):
                    overlap_prefix = i
            
            # Determine the best overlap (suffix or prefix)
            if overlap_suffix > best_overlap:
                best_overlap = overlap_suffix
                best_match = (seq, "suffix")
            if overlap_prefix > best_overlap:
                best_overlap = overlap_prefix
                best_match = (seq, "prefix")
        
        # Merge the best match into the superstring
        if best_match:
            seq, overlap_type = best_match
            if overlap_type == "suffix":
                superString += seq[best_overlap:]
            elif overlap_type == "prefix":
                superString = seq[:-best_overlap] + superString
            DNAs.remove(seq)
        else:
            # No overlaps found, append the remaining sequence
            superString += DNAs.pop(0)

# Main Program
with open("fasta.fasta") as fp:
    for name, seq in parseFasta(fp):
        DNAs.append(seq)

constructSuperString(DNAs)
print(superString)
