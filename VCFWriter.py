class VCF_writer:

    def __init__(self,vcf_to_read,processor,limit):
        self.origin_vcf=vcf_to_read
        self.filterd_file=f"{self.origin_vcf[:-4]}_filtered.vcf"
        self.processor=processor
        self.counter=0
        self.limit=limit

    def main_writer(self):
        """
        this method read the vcf and write the filtered one
        """
        filtered= open(self.filterd_file,"w")
        with open(self.origin_vcf,"r") as origin:
            lines= origin.readlines()
            for line in lines:
                if line.startswith("##"):
                    filtered.write(line)
                elif line.startswith("#"):
                    filtered.write(line)
                    header_col=line.strip("#")
                else:
                    new_line= self.process_line(line,header_col)
                    if new_line!=None:
                        filtered.write(new_line)
                        self.counter+=1
                    if self.counter==self.limit:
                        break
        filtered.close()

    def process_line(self,line,header_col):
        """
        this method get a line and process it to the filtered vcf
        :param line:
        :param header_col:
        :return: new line or None
        """
        final_dict={}
        splited_line=line.split("\t")
        splited_header=header_col.split("\t")
        for i in range(len(splited_header)):
            col_name=splited_header[i]
            col_val=splited_line[i]
            if col_name=="INFO":
                info=col_val.split(";")
                for val in info:
                    if val.startswith("DP"):
                        dp= val.split("=")
                        final_dict["DP"]=float(dp[1])
                        final_dict["INFO"]=col_val
            else:
                try:
                    final_dict[col_name]=float(col_val)
                except Exception:
                    final_dict[col_name] = col_val
        gene= self.processor.filter_and_get_gene(final_dict)
        if  gene != None:
            return self.build_new_line(gene,final_dict)
        return None



    def build_new_line(self,gene,final_dict):
        """
        this method get the gene and the other values and build a new line for the filtered vcf
        :param gene:
        :param final_dict:
        :return: new line (str)
        """
        final_dict.pop("DP")
        print(final_dict)
        final_dict["INFO"]=final_dict["INFO"]+f";GENE={gene}"
        new_line="\t".join(str(x) for x in final_dict.values())
        return new_line

