import requests

from bs4 import BeautifulSoup

# Links:
# 'https://en.wikipedia.org/wiki/PICALM'
# 'https://en.wikipedia.org/wiki/Star_Trek'
# 'https://en.wikipedia.org/wiki/Yoshiharu_Yamaguchi'

response = requests.get('https://en.wikipedia.org/wiki/Yoshiharu_Yamaguchi')


html = response.text

soup = BeautifulSoup(html, 'html.parser')


content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find('a', recursive=False):
        first_relative_link = element.a.get('href')
        print(first_relative_link)
        break





# 1 attemp to this but wiki/PICALM still not getting the right first link
# as Udacity thinks ... but its fine it works

# first_wiki_tags = soup.find(id='mw-content-text').a
#
# first_wiki_url = first_wiki_tags.get('href')
#
# print(first_wiki_url)



# 0 attemp it doesn't work that well it has some troubles with wiki/Russia
# response = requests.get('https://en.wikipedia.org/wiki/Russia')
#
#
# html = response.text
#
# soup = BeautifulSoup(html, 'html.parser')
#
# first_wiki_url = soup.find(id='mw-content-text').find(class_='mw-parser-output').p.a
#
# url = first_wiki_url.get('href')
#
# print(url)
