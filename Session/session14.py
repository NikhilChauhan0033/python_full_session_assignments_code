# BeautifulSoup install from this command pip3 install beautifulsoup4   [always add 3 after pip bcz your python version is 3]
# the command come from link https://pypi.org/project/beautifulsoup4/ type on internet beautifulsoup pypi and enter
# for check use this from bs4 import BeautifulSoup and run if black then succsesfully install

# web scrapping
# the data is in form of HTML 
# use of scrapping easy way to use data from any website  [easy to fetch live data]
from bs4 import BeautifulSoup
import requests

#here we will do diplay the puma website data using web scrapping  

url = "https://in.puma.com/in/en/search?q=shoes"    #puma website 

data =   requests.get(url)   #we checked if status code is 200 or not [so yes here 200]
print(data)

plain_text = data.text
print(type(plain_text))   #here the type is string
print()
print(plain_text)    #you will get data inside html tag


res = BeautifulSoup(plain_text,"html.parser")   #here you convert your data from string to BeautiFulSoup
print(type(res))  #here the type is 
print()
print(res)   #here also you will get inside html tag but data datatype is change now you can access data from url

# print only all the title
# use of find all find all the data depend on you condition 
# use of h3 is the title in preset inside the h3 so findAll give me all the h3 tag
# after that anter h3 class name bcz i want only data related to this class name
# how you can find class name go to website click on inspect after that hover on title and see the data present where and use those tag you can easly diplay a data 
ans  = res.findAll("h3",{"class":"w-full mobile:text-sm mobile:pr-0 font-bold text-base pr-5 line-clamp-2"})
print(ans)

for i in ans:
    print(i.text)
    print()

# find all prices which is betweek 3k to 5k 
price = res.findAll("span",{"whitespace-nowrap text-base text-puma-red font-bold"})
print(price)

for j in price:
    k = j.text.replace("₹","").replace(",","")
    if(int(k) > 3000 and int(k) < 5000):
        print(j.text)
        print()
        print(k)

# diffrence between j.text and k is inside the j value in form of  ₹3,444 inside k in form of 4339 that why we print j.text
