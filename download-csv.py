import os.path
import urllib.request

import bs4

BASE_URL = "https://www.jpx.co.jp"
PAGE_PATH = "/markets/derivatives/jnet-derivative/index.html"


def get_csv_path() -> str:
    url = BASE_URL + PAGE_PATH
    with urllib.request.urlopen(url) as f:
        content = f.read()

    soup = bs4.BeautifulSoup(content, "html.parser")
    a_tags = soup.find_all("a")

    for a_tag in a_tags:
        href = a_tag.get("href")
        if href and ".csv" in href:
            return href

    raise Exception("failed to find CSV link")


def download_csv(csv_path) -> None:
    url = BASE_URL + csv_path
    csv_file = os.path.join("csv", os.path.basename(csv_path))
    with urllib.request.urlopen(url) as f:
        with open(csv_file, "wb") as g:
            g.write(f.read())


if __name__ == "__main__":
    csv_path = get_csv_path()
    download_csv(csv_path)
