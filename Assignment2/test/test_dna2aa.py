import unittest

from Assignment2.dna2aa import from_sequence_to_proteins, get_reverse_complement


class TestDNA2AA(unittest.TestCase):
    def test_SequenceWithStopCodonAtTheEnd(self):
        sequence = "ATGGCAAAC"
        mapping = {
            "ATG": "R", "GCA": "S", "AAC": "L"
        }
        expected = ["RSL"]
        actual = from_sequence_to_proteins(sequence, mapping)
        self.assertEqual(expected, actual)

    def test_SequenceWithStopCodonInTheMiddle(self):
        sequence = "ATGAACGCAATGAAC"
        mapping = {
            "ATG": "R", "GCA": "S", "AAC": "*"
        }
        expected = ["R*", "SR*"]
        actual = from_sequence_to_proteins(sequence, mapping)
        self.assertEqual(expected, actual)

    def test_SequenceWithAmbiguity(self):
        sequence = "ATGAACGNAATGAAC"
        mapping = {
            "ATG": "R", "GCA": "S", "AAC": "*"
        }
        expected = ["R*", "XR*"]
        actual = from_sequence_to_proteins(sequence, mapping)
        self.assertEqual(expected, actual)

    def test_SequenceGetLongest(self):
        sequence = "ATGAACGNAATGAAC"
        mapping = {
            "ATG": "R", "GCA": "S", "AAC": "*"
        }
        orfs = from_sequence_to_proteins(sequence, mapping)
        sorted_orfs = sorted(orfs, key=len, reverse=True)
        expected = "XR*"
        actual = sorted_orfs[0]
        self.assertEqual(expected, actual)

    def test_ReverseComplement(self):
        sequence = "ATGC"
        expected = "GCAT"
        actual = get_reverse_complement(sequence)
        self.assertEqual(expected, actual)
