


def levenshtein_substitution(sequence1, sequence2):
    """
    Implement the function levenshtein_substitution() which takes two sequences
    of the same length and computes the minimum number of substitutions to
    transform one into another.
    """
    number_substitutions = sum(sequence1[i] != sequence2[i] for i in range(len(sequence1)))
    return number_substitutions


def levenshtein_deletions(sequence1, sequence2):
    """
    Implement the function levenshtein_deletion() which takes two sequences
    and returns the positions of characters from the longest sequences which
    should be deleted to transform the sequence into the other one.
    This should be returned as a list of indices (int). 
    If such deletion can not be done the function should return None. 
    Also, if there are no editing operations needed the function should return an empty list.
    """
    deletions_indexes = []
    if len(sequence1) == len(sequence2):
        return None

    return deletions_indexes
