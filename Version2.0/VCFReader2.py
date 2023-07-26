import gzip
import requests
import io


class VCF_reader:

    def __init__(self, url):
        self.url = url

    def download_and_process(self):
        """
        get the conent of the gzipped vcf from AWS S3 and process it.
        """
        s3_url_parts = self.url.split("/")
        bucket_name = s3_url_parts[2]
        object_key = "/".join(s3_url_parts[3:])

        url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                return self.process_vcf_content(response.content)
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    def process_vcf_content(self, content):
        """
        Process the content of the gzipped VCF file.
        """
        try:
            with gzip.GzipFile(fileobj=io.BytesIO(content), mode='rb') as f:
                vcf_content = f.readlines()
                # print(vcf_content)
                vcf_content2 = [b.decode() for b in vcf_content]
                return vcf_content2
        except Exception as e:
            print(f"Error processing VCF content: {e}")


if __name__ == '__main__':
    url = "s3://resources.genoox.com/homeAssingment/demo_vcf_multisample.vcf.gz"
    vcf_reader = VCF_reader(url)
    vcf_reader.download_and_process()
