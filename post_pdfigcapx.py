"""
Send POST request to PDFigCapX and save HTML response.

There should be `data/html/` and `data/pdf/` directory created.
"""
import requests
import time


start_time = time.time()
files = {"file": open("data/pdf/1806.01363.pdf", "rb")}
r = requests.post("https://www.eecis.udel.edu/~compbio/PDFigCapX/uploader", files=files)
print(f"This request took {time.time() - start_time:.2f} seconds")

with open("data/html/1806.01363.html", "w") as f:
    f.write(r.text)
