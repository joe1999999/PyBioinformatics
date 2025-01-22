from itertools import product

def generate_strings(alphabet, n):
    """
    Generate all strings of length up to n formed from the alphabet, ordered lexicographically.

    :param alphabet: A list of symbols defining the custom ordered alphabet
    :param n: The maximum length of the strings
    :return: A list of strings sorted lexicographically based on the custom alphabet
    """
    # Generate strings of length 1 to n
    strings = []
    for length in range(1, n + 1):
        strings.extend([''.join(p) for p in product(alphabet, repeat=length)])
    
    # Sort strings based on the order in the custom alphabet
    alphabet_index = {symbol: idx for idx, symbol in enumerate(alphabet)}
    strings.sort(key=lambda s: [alphabet_index[char] for char in s])
    
    return strings

# Example usage
if __name__ == "__main__":
    # Custom alphabet (ordered as provided)
    alphabet = list("KNDSXBVGLAO")
    # Maximum length of strings
    n = 4
    
    # Generate and print the strings
    result = generate_strings(alphabet, n)
    with open('example.txt', 'w') as file:
        for string in result:
            file.write(string)
            file.write('\n')
        
        
    
