import numpy as np
import pandas as pd
import sympy


def count_ones(binary_string):
    return binary_string.count("1")


def combine_terms(term1, term2):
    combined_term = []
    for i in range(len(term1)):
        if term1[i] == term2[i]:
            combined_term.append(term1[i])
        else:
            combined_term.append("-")
    return "".join(combined_term)


def quine_mccluskey(terms):
    num_variables = len(terms[0])
    grouped_terms = [[] for _ in range(num_variables + 1)]

    for term in terms:
        num_ones = count_ones(term)
        grouped_terms[num_ones].append(term)

    prime_implicants = []
    essential_prime_implicants = []

    for i in range(num_variables):
        current_terms = grouped_terms[i]
        next_terms = grouped_terms[i + 1]
        combined_terms = set()

        for term1 in current_terms:
            for term2 in next_terms:
                combined = combine_terms(term1, term2)
                if combined.count("-") == 1:
                    combined_terms.add(combined)

        prime_implicants.extend(current_terms)
        essential_prime_implicants.extend(current_terms)

        if not combined_terms:
            break

        next_terms = []
        for term in combined_terms:
            if term in essential_prime_implicants:
                essential_prime_implicants.remove(term)
            else:
                next_terms.append(term)

        grouped_terms[i + 1] = next_terms

    return essential_prime_implicants


if __name__ == "__main__":
    # Example usage:
    terms = ["0010", "1000", "1010", "1100", "1110"]
    essential_prime_implicants = quine_mccluskey(terms)
    print("Essential Prime Implicants:", essential_prime_implicants)
    print("hello world")
