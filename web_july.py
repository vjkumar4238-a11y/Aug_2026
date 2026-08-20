import requests
from bs4 import BeautifulSoup
import pandas as pd
response = requests.get("https://books.toscrape.com/")
#print(response)
soup = BeautifulSoup(response.content,'html.parser')
#print(soup)

names = soup.find_all('a',title=True)
#print(names)

name=[]

for i in names[0:10]:
    result=i["title"]
    name.append(result)
#print(name)

prices=soup.find_all("p", class_="price_color")
#print(prices)

price=[]

for i in prices[0:10]:
    result = i.get_text()
    price.append(result)
#print(price)

result= [float(i.replace("£","")) for i in price]
#print(result)

images=soup.find_all("img", class_="thumbnail")

image=[]
for i in images[0:10]:
    url=i['src']
    image.append(url)

sample="https://books.toscrape.com/"

furl=(sample+i for i in image)

df=pd.DataFrame()
#print(df)

df["Names"]=name
df["Price"]=result
df["Images"]=image

#print(df)

#df.to_csv("books.csv")

df=pd.read_csv("books.csv")

print(df.head())