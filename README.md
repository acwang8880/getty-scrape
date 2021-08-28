# Getty Image Scraper

## To run

```
# Start the venv
❯ workon data

# Go into project directory
❯ /home/cptbirdy/proj/webb/getty_scraper


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
