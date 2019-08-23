from bs4 import BeautifulSoup
#Getting data from Html or xml tags

import requests
#make a request to the url

from csv import writer
#store the scraped data into csv or excel file(comma separated value)


response=requests.get("https://www.ebay.com/sch/i.html?_nkw=mobile+phones&_sop=12")
#page code

soup=BeautifulSoup(response.text,"html.parser")
#second parameter is used to denote we are scraping html (Html/xml)

mobile_list=soup.find_all("li",class_="s-item")
#gets all li tags with speific class name stores in a list
#using class_ as class is a keyword in python and it raises error


with open("ebay_scraper.csv",'w',encoding="utf-8") as ebay:
    file=writer(ebay)
    file.writerow(["Brand","Price","Rating"])
    
    #column names 

    for mobile in mobile_list:
        name=mobile.find('h3').get_text()
        
        price_list=mobile.find_all("span",class_="s-item__price")
        #find_all returns a list with span tag and specific class name 
        #loop trough list to get the price

        for x in price_list:
            price=x.get_text()
            


        rating_list=mobile.find_all("span",class_="clipped")
        for x in rating_list:
            if rating_list.index(x)%2 == 0: #repeating twice so considering alternates
                rating=x.get_text()
                
                if rating=="Time left":     #skipping all rating with value as Time left
                    continue
                file.writerow([name,price,rating])
                    
                
        

  

