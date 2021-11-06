from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

# # Scrape from Y Combinator front page
# response = requests.get(url="https://news.ycombinator.com/")
#
# y_combinator_page = response.text
#
# soup = BeautifulSoup(y_combinator_page, "html.parser")
#
# articles = soup.find_all(name="a", class_="titlelink")
#
# article_texts = []
# article_links = []
#
# for article in articles:
#     text = article.getText()
#     article_texts.append(text)
#     link = article.get("href")
#     article_links.append(link)
#
# # list comprehension to convert list of strings e.g. "74 points" to list of ints e.g. 74
# article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_scores)
#
# highest_score = max(article_scores)
# highest_score_index = article_scores.index(highest_score)
#
# print(article_texts[highest_score_index])
# print(article_links[highest_score_index])
# print(article_scores[highest_score_index])



# encoding is included to fix a UnicodeDecodeError
# with open("website.html", encoding='utf-8') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
#
# all_anchors = soup.find_all(name="a")
# print(all_anchors)
#
# # Get text from all anchor tags
# for anchor in all_anchors:
#     # print(anchor.getText())
#     print(anchor.get("href"))
#
# # Get first item that matches given criteria
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# # Get anchor using selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)
