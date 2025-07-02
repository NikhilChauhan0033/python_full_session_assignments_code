# import json #json in module inbuild module
# import requests  # is library  
#how download the library 1st take name of library. after that go to browser write like this requests pypi and enter after that go to official website and copy command and paste to terminal and re run

# API [application programing interface]
# by defalut API data type is String
# API works is connect between frontend and backend
# Two Types Of API  
# import json [json full form javascript object notation]
# import requests
# free api link "https://jsonplaceholder.typicode.com/" go to Resources and selecte /posts	100 posts
import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

# 3 steps of api 
# 1st check status code if 200 then go ahed other wise solve error
# 2nd get text[data] from api
# 3rd convert text to json formate

# data  = requests.get(url) #using requests.get() you can get a status code
# print(data)      #here you will get status code 200

# plain_text = data.text #here you will get data from api  [using .text you will get data from api]
# print(plain_text)   #here you will get all the data means text from api by default type is string
# print(type(plain_text))

# res  = json.loads(plain_text)   #here you will convert the string data to json [using json.loads you can convert data string to json]
# print(res)   #here you will get json formate data[text]
# print(type(res))

# fetching API in one line 
res = json.loads(requests.get(url).text)
print(res)
print()

# fetching only title from api
for i in res:
    print(i['title'])    #inside i you will get seprate seprate dict
    print()


# two types of api [free and paid]

# this is exapmle of paid API if you buy in feature API by pay how you can use it
# paid api for free https://www.weatherbit.io/ [free only for 21 days]
#username : Nikhil Password : Nikhil@2003
# and inside url variable "https://api.weatherbit.io/v2.0/current?city=" this link come from in this link https://www.weatherbit.io/ after open this link logIn go to resources -> API documentation -> scroll down click on Current Weather below button Documentation scroll down down down there is a Example Request:this is full url but we want only till current? after we creacte over own API on requirements https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely

key = "d2d43eba52e743bcbe3f3ddac078d4ad"  #enter key from the created
city_name = input("Enter City Name: ")
url = "https://api.weatherbit.io/v2.0/current?city="+city_name+"&key="+key

print(url)

res = json.loads(requests.get(url).text)
print(res['data'][0]['temp'])

# kush friend code
# key = "787902647d964784a30b79618eb0559f"
# city_name = input("City Name:")
# url ="https://api.weatherbit.io/v2.0/current?city="+city_name+"&key="+key

# # print(url)

# res=json.loads(requests.get(url).text)
# print(res['data'][0]['temp'])
