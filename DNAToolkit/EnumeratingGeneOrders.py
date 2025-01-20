"""
Problem
A permutation of length n
 is an ordering of the positive integers {1,2,…,n}
. For example, π=(5,3,2,1,4)
 is a permutation of length 5
.

Given: A positive integer n≤7
.

Return: The total number of permutations of length n
, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1


"""

import itertools

def generatePermutations(n):
    # Generate all permutations of the list [1, 2, ..., n]
    nums = list(range(1, n+1))
    perms = list(itertools.permutations(nums))
    
    # Output the number of permutations
    print(len(perms))
    
    # Output each permutation
    for perm in perms:
        print(" ".join(map(str, perm)))

# Example usage with n = 6
generatePermutations(6)




