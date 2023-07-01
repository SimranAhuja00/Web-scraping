import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []

for i in range(2,12):

    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text,"lxml")

    names = soup.find_all("div",class_="_4rR01T")
    #print(names)
    
    for i in names:
        name = i.text
        Product_name.append(name)

    prices = soup.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)

    desc = soup.find_all("ul",class_="_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)


df = pd.DataFrame({"Product Name" : Product_name,"Price" : Prices,"Description" : Description})
# print(df)

df.to_csv("flipkart_mobiles_under_50000.csv")