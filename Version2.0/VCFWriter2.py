import threading


class VCF_writer:

    def __init__(self,vcf_data,processor,limit):
        self.origin_data=vcf_data
        self.filterd_file="data_filtered.vcf"
        self.processor=processor
        self.counter=0
        self.limit=limit
        self.counter_lock = threading.Lock()

    def main_writer(self):
        """
        this method read the vcf and write the filtered one
        """
        filtered= open(self.filterd_file,"w")
        index_line=0
        while self.origin_data[index_line].startswith("#"):
            filtered.write(self.origin_data[index_line])
            index_line+=1
        else:
            filtered.close()
            header_col = self.origin_data[index_line - 1].strip("#")
            chunks=self.split_list_into_chunks(self.origin_data[index_line:],4)
            threads=[]
            for chunk in chunks:
                thread = threading.Thread(target=self.chunk_method, args=(chunk,header_col))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

        filtered.close()

    def split_list_into_chunks(self,lst, num_chunks):
        chunk_size = len(lst) // num_chunks
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        return chunks

    def chunk_method(self,chunk,header_col):
        filtered = open(self.filterd_file, "a")
        for line in chunk:
            new_line = self.process_line(line, header_col)
            if new_line != None:
                with self.counter_lock:
                    if self.counter == self.limit:
                        break
                    self.counter += 1
                    filtered.write(new_line)

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
                    final_dict[col_name.strip("\n")] = col_val.strip("\n")
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

