from APIFetcher import API_fetcher

class VCF_sample_processor:

    def __init__(self,sample,start,end,minDP):
        self.sample=sample
        self.start=start
        self.end=end
        self.minDP=minDP
        self.API_fetcher=API_fetcher()

    def filter(self):
        pos= self.sample["POS"]
        if self.start<=pos<=self.end:
            dp= self.sample["DP"]
            if dp>self.minDP:
                return True
            return False
        return False

    def get_GENE(self):
        chrom=self.sample["CHROM"]
        pos=self.sample["POS"]
        alt=self.sample["ALT"]
        ref=self.sample["REF"]
        ref_ver="hg19"
        data= self.API_fetcher.fetch_variant_gene(chrom,pos,ref,alt,ref_ver)
        gene= data["gene"]
        return gene
