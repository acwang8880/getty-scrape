# Getty Image Scraper

## To run script

```
# Go into project directory
❯ /home/cptbirdy/proj/webb/getty_scraper

# Start the venv
❯ workon data

# Run script
❯ python getty_scraper.py --query test --pages 5 --help
usage: getty image scraper [-h] --query QUERY --pages PAGES
                           [--extra-args EXTRA_ARGS] [--output-dir OUTPUT_DIR]

pulls images from getty image site

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY, -q QUERY
                        Query words for getty image search
  --pages PAGES, -p PAGES
                        Number of pagination attempts to retrieve images
  --extra-args EXTRA_ARGS, --e EXTRA_ARGS
                        Any additional url params that could be used to filter
                        the search. Recommended to use the website query and
                        copy from the url address bar
  --output-dir OUTPUT_DIR, -o OUTPUT_DIR
                        Path to directory to save downloaded images. Default:
                        takes the first word in the query

```



## To run jupyter

```
# Start jupyter server
❯ jupyter lab --ip 0.0.0.0 --no-browser


# In the jupyter lab interface, open up the getty_scraper.ipynb notebook
# Ctrl + Enter while selecting the cell will run it
# Enter the query phrase <fedex>
```


## Outputs

Output images will go to `output_images`. This is a configurable variable.

## Tunables

Var|Description|
------|---------------|
OUTDIR| Path to write images to on disk|
MAX_PAGES| Number of pages (pagination) to pull from getty image results|
