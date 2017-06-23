import pytest
import bioinfo_dicts

def n_neg(seq):
    """Number of negative residues a protein sequence"""

    # Convert sequence to upper case
    seq = seq.upper()


    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    #Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')





    # # Count E's and D's, since these are the negative residues
    # return seq.count('E') + seq.count('D')
    #
    #
    # if seq == 'Z':
    #     raise RuntimeError('Z is not a valid amino acid.')



# def test_n_neg():
#     """Perform unit tests on n_neg."""
#
#     assert n_neg('E') == 1
#     assert n_neg('D') == 1
#     assert n_neg('') == 0
#     assert n_neg('ACKLWTTAE') == 1
#     assert n_neg('DDDDEEEE') == 8
#     assert n_neg('acklwttae') == 1
