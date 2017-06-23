import test_driven as td
import pytest
import bioinfo_dicts

# def test_n_neg():
#     """Perform unit tests on n_neg."""
#
#     assert td.n_neg('E') == 1
#     assert td.n_neg('D') == 1
#     assert td.n_neg('') == 0
#     assert td.n_neg('ACKLWTTAE') == 1
#     assert td.n_neg('DDDDEEEE') == 8
#     assert td.n_neg('acklwttae') == 1





def test_n_neg_for_single_E_or_D():
    """Perform unit tests on n_neg."""

    assert td.n_neg('E') == 1
    assert td.n_neg('D') == 1

def test_n_neg_for_empty_sequence():
    assert td.n_neg('') == 0

def test_n_neg_for_longer_sequences():
    assert td.n_neg('ACKLWTTAE') == 1
    assert td.n_neg('DDDDEEEE') == 8

def test_n_neg_for_lower_case_sequences():
    assert td.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        td.n_neg('Z')
    excinfo.match("Z is not a valid amino acid")

    with pytest.raises(RuntimeError) as excinfo:
        td.n_neg('O')
    excinfo.match("O is not a valid amino acid")
