import requests
from bs4 import BeautifulSoup
import openpyxl


wb = openpyxl.load_workbook('Imported.xlsx')
sheet = wb['Sheet1']

count = 0
pages = 10

for i in range(pages):
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    print("Page scrapping: "+url )
    res = requests.get(url)

    soup = BeautifulSoup(res.content,'html.parser')

    containers = soup.findAll("div",{"class":"_3liAhj"})

    for container in containers:

        count = count+1

        soup_name = container.a.img["alt"]

        soup_desc_cont = container.findAll("div",class_="_1rcHFq")
        soup_desc = soup_desc_cont[0].text
        
        soup_price_cont = container.findAll("div",class_="_1vC4OE")
        soup_price = soup_price_cont[0].text

        sheet["A"+str(count)] = count
        sheet["B"+str(count)] = soup_name
        sheet["C"+str(count)] = soup_desc
        sheet["D"+str(count)] = soup_price
'''
        print("Serial no: "+ str(count))
        print("Name:" + soup_name)
        print("Description:" + soup_desc)
        print("Price:" + soup_price)
'''
wb.save('Imported.xlsx')
wb.close()
