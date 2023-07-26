import unittest
from VCFSampleProcessor import VCF_sample_processor
from VCFWriter import VCF_writer


class VCF_writer_test(unittest.TestCase):

    def setUp(self):
        self.header="CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	father	mother	proband"
        self.line1="chrY	2759966	.	G	A	34.68	.	FS=0;MQ=50.06;MQRankSum=0.762;QD=3.47;ReadPosRankSum=-0.762;SOR=2.199;FractionInformativeReads=0.9;DP=10;AF=0.5;AN=2;AC=1	GT:AD:AF:DP:GQ:PL:SB	0/1:7,2:0.222:9:63:63,0,288:0,7,2,0	./.:.:.:.:.:.:.	./.:.:.:.:.:.:."
        self.line2="chrX	60072	.	G	T	406.46	.	FS=20.959;MQ=59.28;MQRankSum=-0.042;QD=11.29;ReadPosRankSum=-0.753;SOR=1.404;FractionInformativeReads=0.833;DP=36;AF=0.5;AN=2;AC=1	GT:AD:AF:DP:GQ:PL:SB	./.:.:.:.:.:.:.	./.:.:.:.:.:.:.	0/1:17,13:0.433:30:99:435,0,530:14,3,4,9"
        self.line3="chrX	60215	.	A	C	535.11	.	FS=8.08;MQ=60;MQRankSum=0.296;QD=15.61;ReadPosRankSum=1.443;SOR=1.018;FractionInformativeReads=0.969;DP=76;AF=0.5;AN=4;AC=2	GT:AD:AF:DP:GQ:PL:SB	./.:.:.:.:.:.:.	0/1:15,16:0.516:31:99:528,0,448:10,5,6,10	0/1:21,19:0.475:40:99:563,0,682:13,8,10,9"
        self.processor= VCF_sample_processor(60000,70000,10)
        self.Writer= VCF_writer("fake_file",self.processor)

    def test_process_line(self):
        self.assertIsNone(self.Writer.process_line(self.line1,self.header))
        self.assertIsNotNone(self.Writer.process_line(self.line2,self.header))
        self.assertIsNotNone(self.Writer.process_line(self.line3,self.header))


if __name__ == '__main__':
    unittest.main()