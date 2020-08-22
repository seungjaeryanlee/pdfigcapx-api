"""
Process HTML response from PDFigCapX.

Install beautifulsoup with `pip install beautifulsoup4`.
"""
from bs4 import BeautifulSoup


paper_id = "1904.00956"
with open(f"data/html/{paper_id}.html", "r") as f:
    html = f.read()
soup = BeautifulSoup(html, features="html.parser")

figures_and_captions = soup.select(".row > .col-md-4 > .thumbnail")
for figure_and_caption in figures_and_captions:
    figure = figure_and_caption.select(".img-responsive")[0]["src"]
    caption = figure_and_caption.select(".scrollabletextbox")[0].text
    print(figure)
    print(caption)
