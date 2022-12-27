# Kawai Scraper

## Description

Simple CLI web scraper for Kawai US website product pages.
It gets prices based on URLs in spreadsheet,
then updates spreadsheet accordingly.

## Install

To begin, make sure to have the latest
versions of python3 and pip installed.
Once you've done that, install the dependencies.

```
$ pip install beautifulsoup4 openpyxl
```

Next, clone this repository and enter its directory

```
$ git clone https://github.com/spectre256/kawai_scraper.git && cd kawai_scraper
```

You're all set!

## Usage

To begin using the tool, first create an Excel spreadsheet
in the same directory where you cloned this repo.
Give it a name, like `data.xlsx`
Next, open it and start adding URLs!
The spreadsheet should be structured like the following:

| URL                | Name            | MSRP | MAP |
|--------------------|-----------------|------|-----|
|https://example.com | Example Product | 1000 | 800 |
|https://...         | ...             | ...  | ... |

Thus, you must put the URLs on the far left column after
the second row.
Any URL placed on the title row will be ignored, and written over.
If you put an invalid URL, you will receive a crypic error message,
so make sure to spell everything correctly and remove any extraneous
quotes or commas.


This tool only works for Kawai US websites with URLs that start with
any of the following:

- https://kawaius.com/product/
- https://store.kawaius.com/product/
- https://store.kawaius.com/p/

If the name is blank or either the MSRP or MAP fields are 0,
the information could not be found on the website

Note that this tool also automatically removes duplicate entries.


After you have set up the spreadsheet and added URLs,
you may run the scraper with the following command:

```
$ python3 scraper.py <filename>
```

where `<filename>` is the full name of the spreasheet,
such as `data.xlsx`
You may also use a file located in another directory,
but be sure to put the full path to that file.

The spreadsheet will be written to, and any items that were
updated will be printed.


## Contact Me

If you have any issues with the tool, contact me at egibbons256@gmail.com

