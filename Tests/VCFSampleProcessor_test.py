import unittest
from VCFSampleProcessor import VCF_sample_processor


class VCF_sample_processor_test(unittest.TestCase):

    def setUp(self):
        s1={"POS":60072,"CHROM":"chrX","ALT":"T","REF":"A","DP":9}
        s2={"POS":60215,"CHROM":"chrX","ALT":"C","REF":"G","DP":10}
        s3={"POS":76667,"CHROM":"chrX","ALT":"A","REF":"A","DP":36}
        self.sample_processor1 = VCF_sample_processor(s1,60000,70000,2)
        self.sample_processor2 = VCF_sample_processor(s2,60000,7000,30)
        self.sample_processor3 = VCF_sample_processor(s3,100,200,70)
        s4={"POS":2759966,"CHROM":"chrY","ALT":"A","REF":"G","DP":10}
        s5={"POS":2759968,"CHROM":"chrY","ALT":"A","REF":"G","DP":9}
        self.sample_processor4 = VCF_sample_processor(s4,60000,7000,30)
        self.sample_processor5 = VCF_sample_processor(s5,100,200,70)

    def test_filter(self):
        self.assertTrue(self.sample_processor1.filter())
        self.assertFalse(self.sample_processor2.filter())
        self.assertFalse(self.sample_processor3.filter())

    def test_get_gene(self):
        self.assertIsNotNone(self.sample_processor4.get_GENE())
        self.assertIsNotNone(self.sample_processor5.get_GENE())




if __name__ == '__main__':
    unittest.main()