""" Problem : 
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s

We can represent t (the substring) using s, we get :

t = s[j,k]

note = python indexing arrays start at 0

Dataset : 
GATATATGCATATACTT

ATAT

Sample Output
2 4 10

"""
from DNAToolkit import *




# A for loop with our desired frame scanning through the string while adding g(starting position) values to a position array which gets returned after the checking has completed 
def locateSubstring(DNA, FRAME):
    g = 0
    h = len(FRAME)
    positions = [] 
    for g in range (0, nucAllCount(DNA) - (h-1) ):
        if (DNA[g:h] == FRAME):
            positions.append(g+1) 
        g+=1
        h+=1        
    return positions

# Because we re-use the locateSubstring function above
# We check if this code is being imported or run directly 
if __name__ == "__main__":
    DNA = "GATATATGCATATACTT"
    FRAME = "ATAT"

    for num in locateSubstring(DNA,FRAME) :
        print(num)

