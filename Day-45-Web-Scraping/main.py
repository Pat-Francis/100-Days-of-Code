from bs4 import BeautifulSoup

# encoding is included to fix a UnicodeDecodeError
with open("website.html", encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)

all_anchors = soup.find_all(name="a")
print(all_anchors)

# Get text from all anchor tags
for anchor in all_anchors:
    # print(anchor.getText())
    print(anchor.get("href"))

# Get first item that matches given criteria
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

# Get anchor using selectors
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)
