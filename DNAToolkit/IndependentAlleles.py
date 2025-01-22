"""
Problem

Two events A and B are independent if Pr(A and B) is equal to Pr(A)×Pr(B).
 In other words, the events do not influence each other,
  so that we may simply calculate each of the individual probabilities separately and then multiply.

More generally, random variables X and Y are independent if whenever A and B are respective events for X and Y, 
Aand B are independent (i.e., Pr(A and B)=Pr(A)×Pr(B)).

As an example of how helpful independence can be for calculating probabilities, let X and Y
represent the numbers showing on two six-sided dice.
Intuitively, the number of pips showing on one die should not affect the number showing on the other die.
If we want to find the probability that X+Y is odd,
then we don't need to draw a tree diagram and consider all possibilities. We simply first note that for X+Y to be odd, 
either X is even and Y is odd or X is odd and Y is even.
In terms of probability, Pr(X+Y is odd)=Pr(X is even and Y is odd)+Pr(X is odd and Y is even).
Using independence, this becomes [Pr(X is even)×Pr(Y is odd)]+[Pr(X is odd)×Pr(Y is even)].

Sample Dataset
2 1
Sample Output
0.684
"""




from math import comb, pow

def mendelsSecondLaw(k, N):
    """
    Calculate the probability that at least N Aa Bb organisms will belong
    to the k-th generation of Tom's family tree.

    :param k: Generation number (1 <= k <= 7)
    :param N: Minimum number of Aa Bb organisms (1 <= N <= 2^k)
    :return: Probability of having at least N Aa Bb organisms in the k-th generation
    """
    # Total number of offspring in the k-th generation
    total_offspring = 2 ** k

    # Probability of an offspring being Aa Bb
    prob_aa_bb = 0.25  # Mendel's second law

    # Calculate the cumulative probability of having fewer than N Aa Bb organisms
    prob_less_than_N = 0
    for i in range(N):
        prob_less_than_N += comb(total_offspring, i) * pow(prob_aa_bb, i) * pow(1 - prob_aa_bb, total_offspring - i)

    # Probability of having at least N Aa Bb organisms
    prob_at_least_N = 1 - prob_less_than_N

    return prob_at_least_N

k = 7  # Generation
N = 32  # Minimum number of Aa Bb organisms
result = mendelsSecondLaw(k, N)
print(f"The probability of having at least {N} Aa Bb organisms in the {k}-th generation is {result:.6f}")
