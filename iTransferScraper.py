#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = "https://itransfer.uaic.ro/academic-expertise/index.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_="premium-blog-post-outer-container")


with open("/home/Alex/Projects/websites/iTransfer/academic expertise/article-template.html", "r") as f:
  contents = f.readlines()

#article = articles[0]
for article in articles:
  innerPage = article.h2.a['href']
  newUrl = "https://itransfer.uaic.ro/academic-expertise/" + innerPage

  response2 = requests.get(newUrl)
  if response2.status_code != 200:
    continue
  soup2 = BeautifulSoup(response2.text, "html.parser")

  title = soup2.select("h1.entry-title")[0].text
  blog  = soup2.select("div.elementor-text-editor")[0].decode_contents()

  pageUrl = "/home/Alex/Projects/websites/iTransfer/academic expertise/" + title + ".html"

  with open(pageUrl, "x") as page:
    ughh = contents
    ughh.insert(136, title)
    ughh.insert(142, blog)
    ughh = "".join(ughh)

    page.write(ughh)
    print(title + " done!")
