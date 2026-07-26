import os
import re
import urllib.parse
from bs4 import BeautifulSoup
import requests

BASE_URL = "https://itransfer.uaic.ro/academic-expertise/"
INDEX_URL = BASE_URL + "index.html"

# Șablonul tău restaurat complet, cu toate elementele din meniu, butoane și footer intacte
TEMPLATE = """<!DOCTYPE html>
<html lang="zxx">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="IT Solutions &amp; Business Services Responsive HTML5 Bootstrap5 Website Template">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

        <!-- fav icon -->
        <link rel="icon" href="../../assets/images/fav-icon/iTransfer-fav-icon.png">

        <!-- bootstarp -->
        <link rel="stylesheet" href="../../css/vendors/bootstrap.min.css">

        <!-- animate.css file -->
        <link rel="stylesheet" href="../../css/vendors/animate.css">

        <!-- Swiper -->
        <link rel="stylesheet" href="../../css/vendors/swiper-bundle.min.css">

        <!-- flaticon -->
        <link rel="stylesheet" href="../../css/vendors/flaticon/flaticon.css">

        <!-- fontAwesome -->
        <link rel="stylesheet" href="../../css/vendors/all.min.css">

        <!-- bootstrap icons -->
        <link rel="stylesheet" href="../../css/vendors/bootstrap-icons-1.9.1/bootstrap-icons.css">

        <!-- Fancybox -->
        <link rel="stylesheet" href="../../css/vendors/jquery.fancybox.min.css">

        <!-- fonts site preconnect -->
        <link rel="preconnect" href="https://fonts.googleapis.com">

        <!-- fonts site preconnect -->
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

        <!-- Font Family -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700;800&amp;display=swap">

        <!-- main-LTR -->
        <link rel="stylesheet" href="../../css/main-LTR.css">
        <title>iTransfer | <!-- TITLE --></title>

        <style>
          .article-content-wrapper img.custom-article-img {
              display: block !important;
              margin: 30px auto 10px auto !important;
              max-width: 85% !important;
              height: auto !important;
              border-radius: 4px;
          }
          .article-content-wrapper figcaption,
          .article-content-wrapper .wp-caption-text,
          .article-content-wrapper .img-caption {
              text-align: center !important;
              font-style: italic !important;
              margin-bottom: 30px;
              color: #a0a0a0;
              display: block;
              font-size: 14px;
          }
        </style>
  </head>
  <body class=" dark-theme ">
    <!--Start Page Header-->
    <header class=" page-header   inner-page-header header-basic" id="page-header">
      <div class="header-search-box">
        <div class="close-search"></div>
        <form class="nav-search search-form" role="search" method="get" action="#">
          <div class="search-wrapper"> 
            <label class="search-lbl">Search for:</label>
            <input class="search-input" type="search" placeholder="Search..." name="searchInput" autofocus="autofocus"/>
            <button class="search-btn" type="submit"><i class="bi bi-search icon"></i></button>
          </div>
        </form>
      </div>
      <div class="container">
        <nav class="menu-navbar">
		  <div class="header-logo"><a class="logo-link" href="https://www.uaic.ro/"><img class="logo-img light-logo" loading="lazy" src="../../assets/images/logo/uaic.png" style="width:75%;height:75%;" alt="logo"/><img class="logo-img  dark-logo" loading="lazy" src="../../assets/images/logo/uaic.png" style="width:75%;height:75%;" alt="logo"/></a></div>
		  <div class="header-logo"><a class="logo-link" href="index.html"><img class="logo-img light-logo" loading="lazy" src="../../assets/images/logo/iTransfer-logo-big-size-white-dots.png" style="width:90%;height:90%;" alt="logo"/><img class="logo-img  dark-logo" loading="lazy" src="../../assets/images/logo/iTransfer-logo-big-size-white-dots.png" style="width:90%;height:90%;" alt="logo"/></a></div>
          <div class="links menu-wrapper ">
            <ul class="list-js links-list">
              <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="index.html">Home</a></li>
              <li class="menu-item has-sub-menu"><a class="menu-link  " href="#0">About<i class="fas fa-plus  plus-icon"> </i></a>
                <ul class="sub-menu ">
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="mission.html">Mission</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="team.html">Team</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="collaboration.html">Collaboration</a></li>
                </ul>
              </li>
              <li class="menu-item has-sub-menu"><a class="menu-link  " href="#0">Academy<i class="fas fa-plus  plus-icon"> </i></a>
                <ul class="sub-menu ">
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="university-consortium.html">University consortium</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="academic-expertise.html">Academic expertise</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="interdisciplinarity.html">Interdisciplinarity</a></li>
                </ul>
              </li>
              <li class="menu-item has-sub-menu"><a class="menu-link  " href="#0">Activities and services<i class="fas fa-plus  plus-icon"> </i></a>
                <ul class="sub-menu ">
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="information.html">Information</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="events.html">Events</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="cisco-academy.html">FII Cisco Academy</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="cursuri.html">Our Courses</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="funding-opportunities.html">Funding Oportunities</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="entrepreneurship.html">Entrepreneurship</a></li>
                </ul>
              </li>
              <li class="menu-item has-sub-menu"><a class="menu-link  " href="#0">Results<i class="fas fa-plus  plus-icon"> </i></a>
                <ul class="sub-menu ">
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="products.html">Products</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="prototypes.html">Prototypes</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="knowledge-transfer.html">Knowledge transfer</a></li>
                  <li class="menu-item sub-menu-item"><a class="menu-link sub-menu-link  " href="projects.html">Projects</a></li>
                </ul>
              </li>
              <li class="menu-item"><a class="menu-link  " href="contact-us.html">contact us </a></li>
            </ul>
          </div>
          <div class="controls-box">
            <!--Menu Toggler button-->
            <div class="control  menu-toggler"><span></span><span></span><span></span></div>
            <!--search Icon button-->
            <div class="control header-search-btn"><i class="bi bi-search icon"></i></div>
            <!--Dark/Light mode button-->
            <div class="mode-switcher ">
              <div class="switch-inner go-light " title="Switch To Light Mode "><i class="bi bi-sun icon "></i></div>
              <div class="switch-inner go-dark" title="Switch To Dark Mode "><i class="bi bi-moon icon "></i></div>
            </div>
            <!--mini shoping cart-->
          </div>
        </nav>
      </div>
    </header>
    <!--End Page Header-->

    <!-- Start inner Page hero-->
    <section class="d-flex align-items-center page-hero inner-page-hero" id="page-hero" style="min-height: 350px !important; height: 350px;">
      <div class="overlay-photo-image-bg parallax" data-bg-img="../../assets/images/hero/inner-page-hero.jpg" data-bg-opacity="1"></div>
      <div class="overlay-color" data-bg-opacity=".75"></div>
      <div class="container" style="margin-top:45px;">
        <div class="hero-text-area centerd">
          <h1 class="hero-title wow fadeInUp" data-wow-delay=".2s"><!-- TITLE --></h1>
        </div>
      </div>
    </section>
    <!-- End inner Page hero-->

    <!-- Start our team Section-->
    <section class="our-team mega-section " id="our-team">
      <div class="container">
        <div class="sec-heading  ">
          <div class="content-area">
            <h2 class=" title    wow fadeInUp" data-wow-delay=".4s"></h2>
          </div>
        </div>

        <div class="article-content-wrapper">
            <!-- CONTENT -->
        </div>

	  <hr>
      </div>
    </section>
    <!-- End our team Section-->

    <!-- Start  page-footer Section-->
    <footer class="page-footer dark-color-footer" id="page-footer" style="min-height: 350px !important; height: 350px;">
      <div class="overlay-photo-image-bg" data-bg-img="../../assets/images/sections-bg-images/footer-bg-1.jpg" data-bg-opacity=".25"></div>
      <div class="container">
        <div class="row footer-cols">
          <div class="col-12 col-md-8 col-lg-4  footer-col "><img class="img-fluid footer-logo" loading="lazy" src="../../assets/images/logo/iTransfer-logo-big-size-white-dots2.png" alt="logo"/>
            <div class="footer-col-content-wrapper">
              <p class="footer-text-about-us "> The iTransfer mission is to stimulate innovation and technology transfer in order to capitalize on research results by introducing them into the economic circuit in the form of innovative products and services.   </p>
            </div>
          </div>
          <div class="col-6 col-lg-2  footer-col ">
            <h2 class=" footer-col-title    ">useful links</h2>
            <div class="footer-col-content-wrapper">
              <ul class="footer-menu ">
                <li class="footer-menu-item"><i class="bi bi-arrow-right icon "></i><a class="footer-menu-link" href="../../contact-us.html">Contact Us</a> </li>
                <li class="footer-menu-item"><i class="bi bi-arrow-right icon "></i><a class="footer-menu-link" href="../../information.html">Information</a> </li>
                <li class="footer-menu-item"><i class="bi bi-arrow-right icon "></i><a class="footer-menu-link" href="../../team.html">Team</a> </li>
              </ul>
            </div>
          </div>
          <div class="col-6 col-lg-2 footer-col "> </div>
          <div class="col-12     col-lg-4 footer-col ">
            <h2 class=" footer-col-title    ">contact information</h2>
            <div class="footer-col-content-wrapper">
              <div class="contact-info-card"><i class="bi bi-envelope icon"></i><a class="text-lowercase  info" href="mailto:itransferspace@gmail.com">itransferspace@gmail.com</a></div>
              <div class="contact-info-card">
                <div class="social-icons">
                  <div class="sc-wrapper dir-row sc-size-32">
                    <ul class="sc-list">
                      <li class="sc-item " title="Facebook"><a class="sc-link" href="https://www.facebook.com/cttitransfer/?_rdc=1&_rdr" title="social media icon"><i class="fab fa-facebook-f sc-icon"></i></a></li>
                      <li class="sc-item " title="youtube"><a class="sc-link" href="https://www.youtube.com/@adsfii6229/videos" title="social media icon"><i class="fab fa-youtube sc-icon"></i></a></li>
                      <li class="sc-item " title="linkedin"><a class="sc-link" href="http://www.linkedin.com/company/centru-de-transfer-tehnologic-itransfer" title="social media icon"><i class="fab fa-linkedin sc-icon"></i></a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="copyrights ">
        <div class="container">
          <div class="row">
            <div class="col-12 col-md-6 d-flex justify-content-start">
              <p class="creadits"> 2017 - 2026 © iTransfer </p>
            </div>
          </div>
        </div>
      </div>
    </footer>
    <!-- End  page-footer Section-->
    <div class="loading-screen" id="loading-screen"><span class="bar top-bar"></span><span class="bar down-bar"></span><span class="progress-line"></span><span class="loading-counter"> </span></div>
    <div class="back-to-top" id="back-to-top"><i class="bi bi-arrow-up icon "></i></div>

        <!--     JQuery     -->
        <script src="../../js/vendors/jquery-3.6.1.min.js"></script>
        <script src="../../js/vendors/appear.min.js"></script>
        <script src="../../js/vendors/bootstrap.bundle.min.js"></script>
        <script src="../../js/vendors/jquery.countTo.js"></script>
        <script src="../../js/vendors/wow.min.js"></script>
        <script src="../../js/vendors/swiper-bundle.min.js"></script>
        <script src="../../js/vendors/particles.min.js"></script>
        <script src="../../js/vendors/vanilla-tilt.min.js"></script>
        <script src="../../js/vendors/isotope-min.js"></script>
        <script src="../../js/vendors/jquery.fancybox.min.js"></script>
        <script src="../../js/main.js"></script>
  </body>
</html>"""

def get_article_links():
    response = requests.get(INDEX_URL)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        if href.startswith(('http', '#', 'mailto:', 'javascript:')) or href in ['', 'index.html', '../index.html']:
            continue
        full_url = urllib.parse.urljoin(BASE_URL, href)
        if full_url not in links:
            links.append(full_url)
    return links

def download_article_image(img_url, article_url, article_dir):
    if any(x in img_url.lower() for x in ['logo', 'fav-icon', 'avatar', 'bg-', 'theme', 'uaic']):
        return None
    abs_img_url = urllib.parse.urljoin(article_url, img_url)
    parsed_path = urllib.parse.urlparse(abs_img_url).path
    filename = os.path.basename(parsed_path)
    if not filename:
        return None
    name, ext = os.path.splitext(filename)
    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', name) + ext
    local_path = os.path.join(article_dir, safe_name)

    if not os.path.exists(local_path):
        try:
            img_data = requests.get(abs_img_url, timeout=10).content
            with open(local_path, 'wb') as f:
                f.write(img_data)
        except Exception:
            return img_url
    return safe_name

def process_article(url):
    parsed_url = urllib.parse.urlparse(url)
    path_parts = [p for p in parsed_url.path.split('/') if p]
    if not path_parts: return

    article_id = path_parts[-2] if path_parts[-1] == 'index.html' and len(path_parts) > 1 else path_parts[-1].replace('.html', '')
    if article_id.lower() in ['index', 'academic-expertise']: return

    article_dir = os.path.join("article", article_id)
    os.makedirs(article_dir, exist_ok=True)

    print(f"Generare pagină completă: [{article_id}]")
    response = requests.get(url)
    if response.status_code != 200: return

    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else article_id.replace('-', ' ').title()

    content_node = (
        soup.find('div', class_='entry-content') or
        soup.find('article') or
        soup.find('div', class_='post-content') or
        soup.find('main')
    )

    if not content_node:
        content_node = soup.find('div', class_='radiantthemes-website-layout')

    if not content_node:
        content_node = soup.find('body')

    if not content_node: return

    # Folosim o clono-structură curată a articolului vechi
    clean_soup = BeautifulSoup(str(content_node), 'html.parser')

    # Eliminăm elementele globale parazite din vechiul layout ca să nu interfereze deloc
    for junk in clean_soup.find_all(['header', 'footer', 'nav', 'aside', 'script', 'style', 'noscript', 'iframe']):
        junk.decompose()

    for wpjunk in clean_soup.find_all('div', class_=re.compile(r'(radiantthemes-website-layout|scrollup|overlay|sidemenu|menu|sidebar|mobile-menu|top-bar)', re.I)):
        if any(c in wpjunk.get('class', []) for c in ['scrollup', 'overlay']):
            wpjunk.decompose()

    for tag in clean_soup.find_all(True):
        if tag.has_attr('id'): del tag['id']
        if tag.has_attr('style'): del tag['style']

    # Procesare imagini
    for img in clean_soup.find_all('img'):
        actual_src = img.get('src') or img.get('data-src')
        if img.has_attr('srcset'): del img['srcset']
        if img.has_attr('sizes'): del img['sizes']

        if actual_src:
            new_src = download_article_image(actual_src, url, article_dir)
            if new_src:
                img['src'] = new_src
                img['class'] = ['img-fluid', 'custom-article-img']
            else:
                img.decompose()
        else:
            img.decompose()

    # Preluăm textul curățat structural din parser
    article_html = clean_soup.decode_contents()

    # Executăm un înlocuitor text strict bazat pe markeri expliciți.
    # Acest lucru garantează că header-ul și footer-ul rămân intacte.
    final_html = TEMPLATE.replace("<!-- TITLE -->", title).replace("<!-- CONTENT -->", article_html)

    output_file = os.path.join(article_dir, "index.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)

def main():
    links = get_article_links()
    for link in links:
        process_article(link)
    print("\nMigrare finalizată! Header-ul, meniul și footer-ul sunt acum 100% complete și sigure.")

if __name__ == "__main__":
    main()
