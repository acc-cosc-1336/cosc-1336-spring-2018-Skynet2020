import unittest
from homework6 import get_point_mutations
from homework6 import get_dna_complement
from homework6 import transcribe_dna_into_rna
from homework6 import get_gc_content
#write import statement for homework 6 file


class TestHomework6(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    #create a test case for function find_motif_in_dna with arguments GATATATGCATATACTT and ATAT
    #the result should be 2 4 10 (three different integers)


    #create a test case for function get_point_mutations with arguments GAGCCTACTAACGGGAT and CATCGTAATGACGGCCT
    #the result should be 7
    def test_get_point_mutations_w_GAGCCTACTAACGGGAT_and_CATCGTAATGACGGCCT_arguments(self):
        self.assertEqual(7, get_point_mutations('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'));


    #create a test case for function get_dna_complement with argument AAAACCCGGT the result should be ACCGGGTTTT
    def test_get_dna_complement_w_AAAACCCGGT_argument(self):
        self.assertEqual('ACCGGGTTTT', get_dna_complement('AAAACCCGGT'));

    #create a test case for function transcribe_dna_to_rna with argument GATGGAACTTGACTACGTAAATT
    #the result should be GAUGGAACUUGACUACGUAAAUU
    def test_transcribe_dna_to_rna_w_GATGGAACTTGACTACGTAAATT_argument(self):
        self.assertEqual('GAUGGAACUUGACUACGUAAAUU', transcribe_dna_into_rna('GATGGAACTTGACTACGTAAATT'))

    #create a test case for function get_gc_content with arguments
    #CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
    #the result should be 60.919540
    def test_get_gc_content_w_CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT_argument(self):
        self.assertEqual(60.919540, get_gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'))


unittest.main(verbosity = 2)
