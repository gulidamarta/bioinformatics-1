from math import log10
from typing import Tuple, List

import numpy as np


def get_index(character: str) -> int:
    return 'ACTG'.index(character)


def nucleotide_freq_calculation(sym_align: Tuple[str, str]) -> List[float]:
    """
    Implement the calculation of the nucleotide frequencies for a symmetric
    alignment. Make sure that the indexing works the followin way:
    [0] = A
    [1] = C
    [2] = T
    [3] = G
    sym align: Tuple of strings representing the symmetric alignment
    """
    first_seq, second_seq = sym_align
    freq_list = [0] * 4  # Frequencies should be in order A,C,T,G

    for character in first_seq:
        freq_list[get_index(character)] += 1

    return [frequency / sum(freq_list) for frequency in freq_list]


def mutation_calculation(sym_align: Tuple[str, str]) -> List[List[float]]:
    """
    Implement the calculation of the mutations remember indexing in any
    dimension should be done in order:
    [0] = A
    [1] = C
    [2] = T
    [3] = G
    Hint: You can use your already implemented functions here
    """
    first_seq, second_seq = sym_align
    freq_matrix = [[0] * 4 for _ in range(4)]

    for character_1, character_2 in zip(first_seq, second_seq):
        index_1, index_2 = get_index(character_1), get_index(character_2)
        freq_matrix[index_1][index_2] += 1

    frequency_sum = sum([sum(row) for row in freq_matrix])
    freq_matrix = [[element / frequency_sum for element in row] for row in freq_matrix]

    return freq_matrix


def scores_calculation(sym_align: Tuple[str, str]) -> List[List[int]]:
    """
    Implement the calculation of the scores remember indexing in any
    dimension should be done in order:
    [0] = A
    [1] = C
    [2] = T
    [3] = G
    Hint: You can use your already implemented functions here
    """
    freq_nucleotides = nucleotide_freq_calculation(sym_align)
    freq_matrix = mutation_calculation(sym_align)

    score_matrix = [[0] * 4 for _ in range(4)]
    for row_index, row in enumerate(freq_matrix):
        for column_index, _ in enumerate(row):
            score_matrix[row_index][column_index] = freq_matrix[row_index][column_index] / (
                    freq_nucleotides[row_index] * freq_nucleotides[column_index])

    score_matrix = [[round(10 * log10(element)) for element in row] for row in score_matrix]
    return score_matrix


def gamma_calculation(sym_align: Tuple[str, str]) -> float:
    """
    Implement the calculation of gamma.
    Hint: You can use your already implemented functions here
    """
    freq_matrix = mutation_calculation(sym_align)
    sum_non_diagonal_elements = sum([column for row_index, row in enumerate(freq_matrix)
                                     for column_index, column in enumerate(row)
                                     if row_index != column_index
                                     ])
    gamma = 0.01 / sum_non_diagonal_elements
    return gamma


def probabilities_calculation(sym_align: Tuple[str, str]) -> List[List[float]]:
    """
    Implement the calculation of probabilities matrix.
    Hint: You can use your already implemented functions here
    """
    probability_matrix = [[0] * 4 for _ in range(4)]
    freq_matrix = mutation_calculation(sym_align)
    freq_nucleotides = nucleotide_freq_calculation(sym_align)

    for row_index, row in enumerate(freq_matrix):
        for column_index, column in enumerate(row):
            probability_matrix[row_index][column_index] = freq_matrix[row_index][column_index] / freq_nucleotides[
                row_index]

    return probability_matrix


def norm_probabilities_calculation(sym_align: Tuple[str, str]) -> List[List[float]]:
    """
    Implement the calculation of normalized probabilities matrix.
    Hint: You can use your already implemented functions here
    """
    norm_matrix = [[0] * 4 for _ in range(4)]
    probabilistic_matrix = probabilities_calculation(sym_align)
    gamma = gamma_calculation(sym_align)

    sum_non_diagonal = [0] * 4
    for row_index, row in enumerate(probabilistic_matrix):
        for column_index, column in enumerate(row):
            if column_index != row_index:
                multiplication_result = gamma * probabilistic_matrix[row_index][column_index]
                norm_matrix[row_index][column_index] = multiplication_result
                sum_non_diagonal[row_index] += multiplication_result

    for row_index, _ in enumerate(probabilistic_matrix):
        norm_matrix[row_index][row_index] = 1 - sum_non_diagonal[row_index]

    return norm_matrix


def pam_calculation(sym_align: Tuple[str, str], power: int) -> List[List[int]]:
    """
    Implement the calculation of pam matrix Make sure to round values to
    integers. ( Notice that casting to int does not do the correct
    rounding)
    power: the power of the PAM matrix e.g. PAM1 or PAM250
    Hint: You can use your already implemented functions here
    """
    pam = [[0] * 4 for _ in range(4)]
    norm_probabilistic_matrix = norm_probabilities_calculation(sym_align)
    frequency_nucleotides = nucleotide_freq_calculation(sym_align)

    probability_matrix = norm_probabilistic_matrix
    for i in range(power - 1):
        probability_matrix = np.dot(norm_probabilistic_matrix, probability_matrix)

    for row_index, row in enumerate(probability_matrix):
        for column_index, column in enumerate(row):
            pam[row_index][column_index] = round(
                10 * log10(probability_matrix[row_index][column_index] / frequency_nucleotides[column_index])
            )

    return pam
