from bs4 import BeautifulSoup as bs
import requests
import re

urls = [
    "https://store.kawaius.com/products/productdetail/part_number=C11-CN301SB/1772.0.1.1",
    "https://kawaius.com/product/gl-10/",
    ]

def parse_float(str):
    return "".join([chr for chr in str if chr.isdigit() or chr == "."])

def make_listing(name_result, msrp_result, map_result):
    listing = {
        "name": "",
        "msrp": 0,
        "map": 0
    }

    if name_result:
        name = name_result.text.strip()
        listing["name"] = name
    if msrp_result:
        listing["msrp"] = parse_float(msrp_result.text)
    if map_result:
        listing["map"] = parse_float(map_result.text)

    return listing

def parse_urls(urls):
    prices = {}
    product_page = re.compile(r"https://kawaius.com/product/.*")
    store_page = re.compile(r"https://store.kawaius.com/products/.*")

    for url in urls:
        html = requests.get(url).content
        tree = bs(html, "lxml")

        # scrape web page based on url; different pages have different styles
        if re.match(product_page, url):
            name_result = tree.find("h1", class_ = "product-title product_title entry-title")

            # finds first span tag with "MSRP" in it inside a strong tag
            for tag in tree.find_all("strong"):
                if tag.find("span", string = re.compile("MSRP")):
                    # these pages don't have a MAP
                    prices[url] = make_listing(name_result, tag, None)
                    break
        elif re.match(store_page, url):
            name_result = tree.find("div", class_ = "titles")
            msrp_result = tree.find("span", class_ = "prce")
            map_result = tree.find("span", class_ = "sale_price")

            prices[url] = make_listing(name_result, msrp_result, map_result)

    return prices


if __name__ == "__main__":
    prices = parse_urls(urls)
    for url, data in prices.items():
        print("{}: {}\nMSRP: {}\nMAP: {}\n".format(data["name"], url, data["msrp"], data["map"]))

