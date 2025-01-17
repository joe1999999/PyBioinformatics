""" The Problem : 
Given Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples having the following genotypes:

1-AA-AA
2-AA-Aa
3-AA-aa
4-Aa-Aa
5-Aa-aa
6-aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.




Problem breakof : 
We need to use Mendel's laws to calculated the % of offspring who possess at least on Dominant Allele 'A'
We need to do that for each pair of the 6 given genotypes, then simply we multiply by the number of total pairs

for example, class 1 (AA-AA) will have a 100% chance of giving 2 offsprings with the dominant allele A
So, for n pair of couples, we get 2n x 100% offspring with a dominant phenotype.   

It follows that : 
class 2 : 50% AA, 50% Aa (100% Dominant phenotype)
class 3 : 100% Aa (100% Dominant phenotype)
class 4 : 50 % Aa, 25% AA, 25% aa (75% Dominant phenotype)
class 5 : 50 % Aa, 50% aa (50% Dominant phenotype)
class 6 : 100% aa (0% Dominant phenotype)   

"""

def calcExpectedDomOffspring(a,b,c,d,e,f):
    # Expected dominant offspring given a,b,c,d,e,f number of pairs for each class
    EDO = 2 * (a + b + c + 0.75*d + 0.5*e + 0*f) 
    return EDO

     
a = 17426
b = 16699
c= 16410
d = 18192
e = 18717
f= 18738

print(calcExpectedDomOffspring(a,b,c,d,e,f))