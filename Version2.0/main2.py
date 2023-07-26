from VCFSampleProcessor2 import VCF_sample_processor
from VCFWriter2 import VCF_writer
from VCFReader2 import VCF_reader
import sys

def main_process(limit,start=0,end=1000000,minDP=0):
    if limit>=10:
        raise ValueError("limit must be an int < 10")
    if type(limit)!=int:
        raise TypeError("limit must be an int < 10")
    reader= VCF_reader("s3://resources.genoox.com/homeAssingment/demo_vcf_multisample.vcf.gz")
    data= reader.download_and_process()
    proc=VCF_sample_processor(start,end,minDP)
    vw= VCF_writer(data,proc,limit)
    vw.main_writer()



if __name__ == '__main__':
    if len(sys.argv)==2:
        limit = int(sys.argv[1])
        main_process(limit)

    elif  not (2<=len(sys.argv)<=5):
        print("Usage: python3 main2.py <limit> <start> <end> <minDP>")

    else:
        limit = int(sys.argv[1])

        if len(sys.argv)==3:
            start = float(sys.argv[2])
            main_process(limit,start)
        elif len(sys.argv)==4:
            start = float(sys.argv[2])
            end = float(sys.argv[3])
            main_process(limit, start, end)
        else:
            start = float(sys.argv[2])
            end = float(sys.argv[3])
            minDP = float(sys.argv[4])
            main_process(limit,start, end, minDP)
