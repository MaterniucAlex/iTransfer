#!/usr/bin/python3

import requests
import urllib
import re
from bs4 import BeautifulSoup

url = "https://itransfer.uaic.ro/academic-expertise/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


sciPost = soup.find_all("div", class_="scientific-news-for-the-industry");
absPost = soup.find_all("div", class_="abstracts-and-outcomes-of-academic-research");
phdPost = soup.find_all("div", class_="research-results-during-phd-studies");
masPost = soup.find_all("div", class_="research-results-during-master-or-bachelor-studies");

posts = soup.find_all("div", class_="premium-blog-post-container")

def writePost(f, posts, clas):
    for post in posts:
            
        parsed_url = urllib.parse.urlparse(post.h2.a['href'])
        path_parts = [p for p in parsed_url.path.split('/') if p]
        if not path_parts: continue
        article_id = path_parts[-2] if path_parts[-1] == 'index.html' and len(path_parts) > 1 else path_parts[-1].replace('.html', '')

        title = post.h2.text.strip()
        href="./article/" + article_id + "/index.html"
        #if post.img:
            #img = post.img['src']
            #line=f"<li><a href=\"{href}\" class=\"col-12   col-lg-4  portfolio-item scien \"><div style=\"background:#00345e;padding:10px;border-radius:15px;\"><img src=\"{img}\" style=\"width:100%;height:100%\"><p>{title}</p></div></a></li>\n"
        #else:
        line=f"<li><a href=\"{href}\" class=\"col-12   col-lg-4  portfolio-item {clas} \"><div style=\"background:#00345e;padding:10px;border-radius:15px;\"><p>{title}</p></div></a></li>\n"
        f.write(line)

with open("ugh.html", "w", encoding='utf-8') as f:
    f.write("")
    writePost(f, sciPost, "sci")
    writePost(f, absPost, "abs")
    writePost(f, phdPost, "phd")
    writePost(f, masPost, "mas")
