""" Probem 

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, 
which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity
in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m
months.

"""




def mortal_fibonacci_rabbits(n, m):
    # Initialize a list to store the number of rabbits born each month
    rabbits = [0] * (n + 1)
    rabbits[1] = 1  # Start with one pair of rabbits in month 1
    
    # Loop through each month
    for i in range(2, n + 1):
        # Rabbits born in this month are the sum of the reproducing rabbits
        rabbits[i] = sum(rabbits[max(i - m, 0):i - 1])
    
    # Total number of rabbits alive in the nth month
    return sum(rabbits[max(0, n - m + 1):n + 1])

# Example usage
n = 81
m = 19
print(mortal_fibonacci_rabbits(n, m))  # Output: 4