import gzip
import requests


class VCF_reader:

    def __init__(self,url,local_filepath="./downloads/cls.download_dir", output_filepath="./downloads/vcf_file.vcf"):
        self.url=url
        self.local_filepath=local_filepath
        self.output_filepath= output_filepath

    def download(self):
        """
        Download the gzipped vcf from AWS S3.
        """
        s3_url_parts = self.url.split("/")
        bucket_name = s3_url_parts[2]
        object_key = "/".join(s3_url_parts[3:])


        url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                with open(self.local_filepath, "wb") as f:
                    f.write(response.content)
                print(f"File downloaded successfully to {self.local_filepath}")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    def extract(self):
        """
        extract the gzip file to a local directory
        """
        gzip_filepath= self.local_filepath
        with gzip.open(gzip_filepath, "rb") as f_in:
            with open(self.output_filepath, "wb") as f_out:
                f_out.write(f_in.read())
        print(f"File extracted to {self.output_filepath}")

    def download_and_extract(self):
        self.download()
        self.extract()

