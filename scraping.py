import re

from bs4 import BeautifulSoup

with open("main.html") as file:
    src = file.read()
print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)
print(title.text)
print(title.string)

page_h1 = soup.find("h1")
print(page_h1)

page_all_h1 = soup.find_all("h1")
print(page_all_h1)

for item in page_all_h1:
    print(item.text)

first_tour = soup.find("h3", class_="first_tour")
print(first_tour.text)

social_links = soup.find(class_="social_networks").find("ul").find_all("a")
print(social_links)

all_a = soup.find_all("a")
for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")


tour_description = soup.find(class_="tour_description").find_parent()
print(tour_description)

tour_description = soup.find(class_="tour_description").find_parent("div", "services")
print(tour_description)

tour_description = soup.find(class_="tour_description").find_parents()
print(tour_description)


next_el = soup.find(class_="service").next_element.next_element
print(next_el)

next_el = soup.find(class_="first_link").find_next().text
print(next_el)

prev_el = soup.find(id="section1").previous_element.previous_element
print(prev_el)

prev_el = soup.find(id="section1").find_previous()
print(prev_el)

next_sib = soup.find(class_="first_link").find_next_sibling()
print(next_sib)

prev_sib = soup.find(class_="second_link").find_previous_sibling()
print(prev_sib)

link_text = soup.find(class_="second_link").find_previous_sibling().find_next().text
print(link_text)

links = soup.find(class_="social_networks").find_all("a")

for item in links:
    link_href_atr = item.get("href")
    link_href_atr1 = item["href"]

    link_data_atr = item.get("data-attr")
    link_data_atr1 = item["data-attr"]

    print(link_href_atr1)
    print(link_data_atr1)

find_a_by_text = soup.find("a", string="Twitter")
print(find_a_by_text)

find_a_by_text = soup.find_all(string=re.compile("([Aa]gency)"))
print(find_a_by_text)