from bs4 import BeautifulSoup
import requests
import re
from random import sample
import numpy as np
from summarize import get_article_summary

# function to extract html document from given url
def getHTMLdocument(url):
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


def scrape_article(article_url):
    html_document = getHTMLdocument(article_url)
    soup = BeautifulSoup(html_document, 'html.parser')
    body = soup.find_all('div', class_='article-content-main')
    paragraphs = body[0].find_all('p')
    list_paragraphs = []
    final_article = ""
    for p in np.arange(0, len(paragraphs)):
        paragraph = paragraphs[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
    return final_article


# assign required credentials
# assign URL
url_to_scrape = "https://www.enn.com/"

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soap object
soup = BeautifulSoup(html_document, 'html.parser')
articles = []

for link in soup.find_all('a', attrs={'href': re.compile("/articles")}):
    # display the actual urls
    articles.append(link.get('href'))

articles = sample(articles, 5)
article_summaries = {}

for article in articles:
    article_url = "https://www.enn.com"+article
    article_summaries[article_url] = get_article_summary(scrape_article(article_url))

print(article_summaries)
