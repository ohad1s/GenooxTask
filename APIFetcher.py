import requests

class API_fetcher:

    def __init__(self):
        self.api_url="https://test.genoox.com/api/fetch_variant_details"

    def fetch_variant_gene(self, chrom, pos, ref, alt, reference_version):

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
                # print(data)

            else:
                print(f"Error: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

