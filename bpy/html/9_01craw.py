import urllib.request
import bs4

url = "https://www.nate.com"
res = urllib.request.urlopen(url)
#html = res.read()

bsObject = bs4.BeautifulSoup(res,'html.parser')
tag_div = bsObject.find('div')
#print(bsObject)
print(tag_div)

tag_id = tag_div.findAll('news_area')
print(tag_id)