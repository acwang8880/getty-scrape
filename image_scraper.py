# /usr/bin/env python3

import sys

if sys.version_info.major < 3:
    raise Exception("Activate the venv with: 'workon data'")

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

main_parser.add_argument("--query",
                         "-q",
                         help="Query words for getty image search",
                         required=True)
main_parser.add_argument(
    "--pages",
    "-p",
    help="Number of pagination attempts to retrieve images",
    required=True)
main_parser.add_argument("--sort",
                         "-s",
                         help="Type of image sort filter. Default: best",
                         choices=["best", "mostpopular", "newest", "oldest"],
                         default="best",
                         required=False)
main_parser.add_argument(
    "--extra-args",
    "--e",
    help=("Any additional url params that could be used to filter the search. "
          "Recommended to use the website query and copy from the "
          "url address bar"))
main_parser.add_argument("--output-dir",
                         "-o",
                         help=("Path to directory to save downloaded images. "
                               "Default: takes the first word in the query"))


def grab_images(phrase: str,
                max_pages: int,
                sort: str,
                extra_query: str = "") -> None:
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
            f"https://www.gettyimages.com/photos/{base_query}"
            "?page={page}&phrase={phrase}&sort={sort}{extra_query}")
        soup = BeautifulSoup(get_soup.text, "lxml")
        pics = tqdm(
            soup.findAll("img",
                         {"class": "MosaicAsset-module__thumb___YJI_C"}))

        for pic in pics:
            pics.set_description(
                f"Page: {count}/{MAX_PAGES} - Crawling Pictures [{phrase}]")
            try:
                image_name = str(time())
                urllib.request.urlretrieve(pic.get("src"),
                                           f"{OUTDIR}/{image_name}.jpg")
            except Exception:
                pass

        count += 1
        page += 1


if __name__ == "__main__":
    args = main_parser.parse_args()

    grab_images(phrase=args.query,
                max_pages=int(args.pages),
                sort=args.sort,
                extra_query=args.extra_args)
