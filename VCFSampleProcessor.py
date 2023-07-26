from APIFetcher import API_fetcher

class VCF_sample_processor:

    def __init__(self,start,end,minDP):
        self.start=start
        self.end=end
        self.minDP=minDP
        self.API_fetcher=API_fetcher()

    def filter(self,sample):
        pos= sample["POS"]
        if self.start<=pos<=self.end:
            dp=sample["DP"]
            if dp>self.minDP:
                return True
            return False
        return False

    def get_GENE(self,sample):
        chrom=sample["CHROM"]
        pos=sample["POS"]
        alt=sample["ALT"]
        ref=sample["REF"]
        ref_ver="hg19"
        data= self.API_fetcher.fetch_variant_gene(chrom,pos,ref,alt,ref_ver)
        gene= data["gene"]
        return gene

    def filter_and_get_gene(self,sample):
        if self.filter(sample):
            return self.get_GENE(sample)
        return None
