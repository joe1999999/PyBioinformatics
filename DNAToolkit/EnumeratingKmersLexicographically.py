""" Problem
Assume that an alphabet A has a predetermined order;
that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak.
For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n , we say that s precedes t in the lexicographic order 
(and write s <lex t ) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2
Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
"""

from itertools import product

def generateLexicographicStrings(alphabet, n):
    """
    Generate all strings of length n from the given alphabet, ordered lexicographically.

    :param alphabet: A collection of symbols defining an ordered alphabet
    :param n: Length of the strings to generate
    :return: A list of lexicographically ordered strings
    """
    # Sort the alphabet to ensure lexicographic order
    sorted_alphabet = sorted(alphabet)

    # Use itertools.product to generate all combinations of length n
    strings = [''.join(p) for p in product(sorted_alphabet, repeat=n)]

    return strings

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Example alphabet
n = 3  # Length of strings to generate
result = generateLexicographicStrings(alphabet, n)
print("\n".join(result))
