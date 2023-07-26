import unittest
from APIFetcher import API_fetcher


class VCF_reader_testing(unittest.TestCase):

    def setUp(self):
        self.api_fetcher = API_fetcher()

    def test_fetch_variant_gene_success(self):
        chrom = "chrX"
        pos = "60337"
        ref = "C"
        alt = "T"
        reference_version = "hg19"

        result = self.api_fetcher.fetch_variant_gene(chrom, pos, ref, alt, reference_version)
        print(result)
        self.assertIsNotNone(result)

    def test_fetch_variant_gene_invalid_input(self):
        chrom = "chrX"
        pos = "60337"

        with self.assertRaises(Exception):
            self.api_fetcher.fetch_variant_gene(chrom, pos)

    def test_fetch_variant_gene_api_error(self):
        chrom = "chrX"
        pos = "60337"
        ref = "C"
        alt = "T"
        reference_version = "hg19"

        self.api_fetcher.api_url = "https://test.genoox.com/api/invalid_url"
        result = self.api_fetcher.fetch_variant_gene(chrom, pos, ref, alt, reference_version)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()