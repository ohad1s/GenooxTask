from APIFetcher2 import API_fetcher

class VCF_sample_processor:

    def __init__(self,start,end,minDP,deNovo):
        self.start=start
        self.end=end
        self.minDP=minDP
        self.API_fetcher=API_fetcher()
        self.deNovo=deNovo

    def filter(self,sample):
        """
        this method get a sample from the vcf and return true if its match the filter values
        :param sample:
        :return: boolean value if filtered or not
        """
        pos= sample["POS"]
        if self.start<=pos<=self.end:
            dp=sample["DP"]
            if dp>self.minDP:
                return True
            return False
        return False

    def get_GENE(self,sample):
        """
        this method get a sample from the vcf and return its variant_gene
        :param sample:
        :return: variant_gene
        """
        chrom=sample["CHROM"]
        pos=sample["POS"]
        alt=sample["ALT"]
        ref=sample["REF"]
        ref_ver="hg19"
        data= self.API_fetcher.fetch_variant_gene(chrom,pos,ref,alt,ref_ver)
        gene= data["gene"]
        return gene


    def deNovo_filter(self,sample):
        father=sample["father"].split(":")[0]
        mother=sample["mother"].split(":")[0]
        proband=sample["proband"].split(":")[0]

        if self.deNovo:
            if proband not in ["0/0", "./."] and mother == "./." and father == "./.":
                return True
            return False
        else:
            if proband not in ["0/0", "./."] and (mother != "./." or father != "./."):
                return True
            return False

    def filter_and_get_gene(self,sample):
        if self.filter(sample) and self.deNovo_filter(sample):
            return self.get_GENE(sample)
        return None
