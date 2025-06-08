#creating command line utility
import requests
import argparse

def download_file(url,local_filename):
    local_filename=url.split('/')[-1]
    #NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename


parser=argparse.ArgumentParser()
#Add Command line arguments
parser.add_argument("url",help="Url of file to downlaod")

parser.add_argument("output",help="by which  name to save")

args=parser.parse_args()
print(args.url)
print(args.output)
download_file(args.url,args.output)


