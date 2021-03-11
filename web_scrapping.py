import requests
from bs4 import BeautifulSoup
import pprint

mega_links=[]
mega_subtext=[]

for i in range(1,7):
 url='https://news.ycombinator.com/news?p=' + str(i)
 res=requests.get(url)
 soup=BeautifulSoup(res.text, 'html.parser')
 links = soup.select('.storylink')
 subtext = soup.select('.subtext')
 mega_links.extend(links)
 mega_subtext.extend(subtext)
 links.clear()
 subtext.clear()
 


def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
