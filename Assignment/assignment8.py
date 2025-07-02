# https://www.cricbuzz.com/cricket-news print all the headlines from this link

from bs4 import BeautifulSoup
import requests

url = "https://www.cricbuzz.com/cricket-news"

data = requests.get(url)
print(data)

plain_text = data.text
print(type(plain_text))
print(plain_text)

res = BeautifulSoup(plain_text,"html.parser")
print(type(res))
print()
print(res)
print()

ans = res.findAll("a",{"cb-nws-hdln-ancr text-hvr-underline"})
print(ans)
print()

for i in ans:
    print(i.text)
    print()