import shutil
import unittest
from VCFReader import VCF_reader
import os


class VCF_reader_testing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.download_dir = "./downloads_test"
        os.makedirs(cls.download_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.download_dir)

    def setUp(self):
        self.test_url = "s3://resources.genoox.com/homeAssingment/demo_vcf_multisample.vcf.gz"
        self.vcf_reader = VCF_reader(self.test_url,self.download_dir,self.download_dir)


    def test_download(self):
        self.vcf_reader.download()

        local_filepath = os.path.join(self.download_dir, "vcfgzip.gz")
        print(local_filepath)
        self.assertTrue(os.path.exists(local_filepath))

    def test_extract(self):
        self.vcf_reader.extract()

        extracted_filepath = os.path.join(self.download_dir, "vcf_file.vcf")
        self.assertTrue(os.path.exists(extracted_filepath))


if __name__ == '__main__':
    unittest.main()