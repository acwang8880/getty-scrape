# /usr/bin/env python3

import argparse
import urllib.request
from pathlib import Path
from time import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

main_parser = argparse.ArgumentParser(
    prog="getty image scraper",
    description="pulls images from getty image site",
)

main_parser.add_argument(
    "--query", "-q",
    help="Query words for getty image search",
    required=True
)
main_parser.add_argument(
    "--pages", "-p",
    help="Number of pagination attempts to retrieve images",
    required=True
)
main_parser.add_argument(
    "--extra-args", "--e",
    help="Any additional url params that could be used to filter the search. Recommended to use the website query and copy from the url address bar"
)
main_parser.add_argument(
    "--output-dir", "-o",
    help="Path to directory to save downloaded images. Default: takes the first word in the query"
)


def getty_ddos(phrase, max_pages, extra_query = ""):
    MAX_PAGES = max_pages

#     phrase = input("Phrase: ")

    base_query = phrase.split()[0] if " " in phrase else phrase

    # create output dir if it doesn't exist
    OUTDIR = f"output_images_{base_query}"
    Path(OUTDIR).mkdir(exist_ok=True)

    page = 0
    count = 0
    while count <= MAX_PAGES:
        get_soup = requests.get(
            f"https://www.gettyimages.com/photos/{base_query}?page={page}&phrase={phrase}&sort=mostpopular{extra_query}"
        )
        soup = BeautifulSoup(get_soup.text, "lxml")
        pics = tqdm(soup.findAll("img", {"class": "MosaicAsset-module__thumb___YJI_C"}))

        for pic in pics:
            pics.set_description(f"Page: {count}/{MAX_PAGES} - Crawling Pictures [{phrase}]")
            try:
                image_name = str(time())
                urllib.request.urlretrieve(pic.get("src"), f"{OUTDIR}/{image_name}.jpg")
            except:
                pass

        count += 1
        page +=1


if __name__ == "__main__":
    args = main_parser.parse_args()

    getty_ddos(phrase=args.query, max_pages=int(args.pages), extra_query=args.extra_args)
