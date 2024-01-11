import pytest

from exercise_sheet8 import *
from helpers import *

"""
a' = AAGTACTTT+AGGTAACACGTTTAGTCA+AAATTCCTA+AGTTTACCGGGTTAATCA
b' = AAATTCCTA+AGTTTACCGGGTTAATCA+AAGTACTTT+AGGTAACACGTTTAGTCA

Symmetric alignments are required to get symmetric counts in order to get a reversible Marov Chain model.
"""


@pytest.mark.parametrize(
    "sym_align",
    [
        (
                "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
        ),
    ]
)
def test_exercise_2a(sym_align):
    actual = nucleotide_freq_calculation(sym_align)
    expected = nucleotide_freq_calculation_correct(sym_align)
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    assert np.allclose(actual, expected)


@pytest.mark.parametrize(
    "sym_align",
    [
        (
                "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
        ),
    ]
)
def test_exercise_2b(sym_align):
    actual = mutation_calculation(sym_align=sym_align)
    expected = mutation_calculation_correct(sym_align)
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    assert np.allclose(actual, expected)


@pytest.mark.parametrize(
    "sym_align",
    [
        (
                "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
        ),
    ]
)
def test_exercise_2c(sym_align):
    actual = scores_calculation(sym_align)
    expected = scores_calculation_correct(sym_align)
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    assert np.allclose(actual, expected)


@pytest.mark.parametrize(
    "sym_align",
    [
        (
                "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
        ),
    ]
)
def test_exercise_2d(sym_align):
    actual = gamma_calculation(sym_align)
    expected = gamma_calculation_correct(sym_align)
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    assert np.allclose(actual, expected)


@pytest.mark.parametrize(
    "sym_align",
    [
        (
                "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
        ),
    ]
)
def test_exercise_2e(sym_align):
    actual = probabilities_calculation(sym_align)
    expected = probabilities_calculation_correct(sym_align)
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    assert np.allclose(actual, expected)


@pytest.mark.parametrize(
    "sym_align",
    [
        (
                "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
        ),
    ]
)
def test_exercise_2f(sym_align):
    actual = norm_probabilities_calculation(sym_align)
    expected = norm_probabilities_calculation_correct(sym_align)
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    assert np.allclose(actual, expected)


@pytest.mark.parametrize(
    "sym_align,power",
    [
        (
                (
                        "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                        "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
                ),
                1,
        ),
        (
                (
                        "AAGTACTTTAGGTAACACGTTTAGTCAAAATTCCTAAGTTTACCGGGTTAATCA",
                        "AAATTCCTAAGTTTACCGGGTTAATCAAAGTACTTTAGGTAACACGTTTAGTCA",
                ),
                50,
        ),
    ]
)
def test_exercise_2g(sym_align, power):
    actual = pam_calculation(sym_align, power)
    expected = pam_calculation_correct(sym_align, power)
    assert actual == expected
