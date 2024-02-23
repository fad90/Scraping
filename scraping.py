from bs4 import BeautifulSoup

with open("main.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)
#
# for item in page_all_h1:
#     print(item.text)

# first_tour = soup.find("h3", class_="first_tour")
# print(first_tour.text)

# social_links = soup.find(class_="social_networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")