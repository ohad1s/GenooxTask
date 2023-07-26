import requests

class API_fetcher:

    def __init__(self):
        self.api_url="https://test.genoox.com/api/fetch_variant_details"

    def fetch_variant_gene(self, chrom, pos, ref, alt, reference_version):
        """

        :param chrom:
        :param pos:
        :param ref:
        :param alt:
        :param reference_version:
        this method send all the params to an API and get back variant_gene
        :return: variant_gene
        """

        payload = {
            "chr": chrom,
            "pos": pos,
            "ref": ref,
            "alt": alt,
            "reference_version": reference_version
        }


        try:
            response = requests.post(self.api_url, json=payload)

            if response.status_code == 200:
                data = response.json()
                return data

            else:
                print(f"Error: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

