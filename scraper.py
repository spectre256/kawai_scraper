from bs4 import BeautifulSoup as bs
import requests
import re

urls = [
    "https://store.kawaius.com/products/productdetail/part_number=C11-CN301SB/1772.0.1.1",
    "https://kawaius.com/product/gl-10/",
    ]

def parse_float(str):
    return "".join([chr for chr in str if chr.isdigit() or chr == "."])

def parse_urls(urls):
    prices = {}
    for url in urls:
        html = requests.get(url).content
        tree = bs(html, "lxml")
        msrp = 0
        map = 0
        name = ""

        store_page = re.compile(r"https://store.kawaius.com/products/.*")
        product_page = re.compile(r"https://kawaius.com/product/.*")

        if re.match(product_page, url):
            msrp = tree.find("strong", re.compile(r"MSRP: \$\d+"))
            if msrp:
                msrp = parse_float(msrp.text)
            else:
                msrp = 0

            listing = {
                "name": name,
                "map": map,
                "msrp": float(msrp),
            } 

            prices[url] = listing

        elif re.match(store_page, url):
            msrp = tree.find("span", class_ = "prce")
            sale_price = tree.find("span", class_ = "sale_price")

            msrp = parse_float(msrp.text)
            sale_price = parse_float(sale_price.text)

            listing = {
                "name": name,
                "map": float(sale_price),
                "msrp": float(msrp)
            }

            prices[url] = listing

    return prices


if __name__ == "__main__":
    prices = parse_urls(urls)
    for url, data in prices.items():
        print("{}: {}\nMSRP: {}\nMAP: {}\n".format(data["name"], url, data["msrp"], data["map"]))

