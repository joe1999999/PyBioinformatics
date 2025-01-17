""" The Problem : 
Given three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor
m are heterozygous,
n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype).
Assuming that any two organisms can mate.
""" 

"""
We break this problem into pieces as follows, For the factor (gene) in this inheritance model, we can define 
its Dominant and Recessive alleles as 'D' and 'r' respectively, than we enumerate all possible genotype pairings and the 
fraction of individuals who have at least one dominant allele 'D'.

The probability the problem poses is then calculated by dividing the total number of possible genotypes from all pairings who have the allele 'D'
by the total number of all possible genotypes from every possible pairing:

(a) - Pairing between two DD (homozygous dominant): 
    DD×DD → 100%DD.
    Number of such pairs: k(k-1) / 2

(b) - Pairing between two Dr (heterozygous): 
    Dr×Dr → 25%DD,50%Dr,25%rr.
    Number of such pairs: m(m-1) / 2
    
(c) - Pairing between two rr (homozygous recessive): 
    rrxrr → 100%rr.
    Number of such pairs: n(n-1) / 2

(d) - Pairing between DD and Dr: 
    DD×Dr → 50%DD,50%Dr.
    Number of such pairs: k x m

(e) - Pairing between DD and rr : 
    DD×rr → 100%Dr.
    Number of such pairs: k x n

(f) - Pairing between Dr and rr: 
    Dr×rr → 50%Dr,50%rr.
    Number of such pairs: m x n

"""


# This function that calculates the number of possible genotypes that result from crossing the same type of organisms
def sameTypeGenotypeEnum(numOfOrganisms):
    return (numOfOrganisms * (numOfOrganisms - 1)) / 2

# This function calculates the number of possible genotypes that result from crossing two different types of organisms a and b
def diffTypeGenotypeEnum(numOganismA, numOrganismB): 
    return numOganismA * numOrganismB

# This function calculates the number of all possible genotypes from k,m,n
def calcAllPossibleGenotypes(k,m,n) :
    allGenotypes = 0
    i = 0
    organismsArray = [k,m,n]
    for org in organismsArray:
        allGenotypes += sameTypeGenotypeEnum(org)

    allGenotypes+= diffTypeGenotypeEnum(k,m) 
    allGenotypes+= diffTypeGenotypeEnum(k,n)
    allGenotypes+= diffTypeGenotypeEnum(m,n)
    return allGenotypes
# This returns the total number of organisms who have a dominant 'D' trait (either genotypes DD or Dr)    
def calcNumGenotypesDominantTrait(k,m,n):
    # The formula is simply obtained by applying the above mentioned Mendelian Laws (%s) for each type of crossing
    allDominantTrait = sameTypeGenotypeEnum(k) + ((3/8) * m * (m-1)) + diffTypeGenotypeEnum(k,m) + diffTypeGenotypeEnum(k,n) + (0.5 *diffTypeGenotypeEnum(m,n))
    return allDominantTrait

# This is the main function 
def calculateProbability(k,m,n): 
    numAllGenotypes = calcAllPossibleGenotypes(k,m,n)
    numAllDominantTraits = calcNumGenotypesDominantTrait(k,m,n)
    return numAllDominantTraits / numAllGenotypes

k = 15
m = 24
n = 21
print(calculateProbability(k,m,n))