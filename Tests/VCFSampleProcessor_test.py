import unittest
from VCFSampleProcessor import VCF_sample_processor


class VCF_sample_processor_test(unittest.TestCase):

    def setUp(self):
        self.s1={"POS":60072,"CHROM":"chrX","ALT":"T","REF":"A","DP":9}
        self.s2={"POS":60215,"CHROM":"chrX","ALT":"C","REF":"G","DP":10}
        self.s3={"POS":76667,"CHROM":"chrX","ALT":"A","REF":"A","DP":36}
        self.sample_processor1 = VCF_sample_processor(60000,70000,2)
        self.sample_processor2 = VCF_sample_processor(60000,7000,30)
        self.sample_processor3 = VCF_sample_processor(100,200,70)
        self.s4={"POS":2759966,"CHROM":"chrY","ALT":"A","REF":"G","DP":10}
        self.s5={"POS":2759968,"CHROM":"chrY","ALT":"A","REF":"G","DP":9}
        self.sample_processor4 = VCF_sample_processor(60000,7000,30)
        self.sample_processor5 = VCF_sample_processor(100,200,70)
        self.sample_processor6 = VCF_sample_processor(2759960, 2759969, 1)

    def test_filter(self):
        self.assertTrue(self.sample_processor1.filter(self.s1))
        self.assertFalse(self.sample_processor2.filter(self.s2))
        self.assertFalse(self.sample_processor3.filter(self.s3))

    def test_get_gene(self):
        self.assertIsNotNone(self.sample_processor4.get_GENE(self.s4))
        self.assertIsNotNone(self.sample_processor5.get_GENE(self.s5))

    def test_filter_and_get_gene(self):
        self.assertIsNotNone(self.sample_processor6.filter_and_get_Gene(self.s5))
        self.assertIsNone(self.sample_processor5.filter_and_get_Gene(self.s4))



if __name__ == '__main__':
    unittest.main()