import requests
from plyer import notification
from bs4 import BeautifulSoup
import time

def notifyMe(title, message): #To Show The Notification
    notification.notify(
        title= title,
        message = message,
        app_icon = "favicon.ico",
        timeout = 20 #Timeout Settings In Seconds
    )

def webData(url): #Getting The Data From The Website
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        html_doc = webData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(html_doc, 'html.parser') #Parsing The Data
        mystr = ""

        for tr in soup.find_all ('tbody')[1].find_all('tr'):
            mystr += tr.get_text() #Converting the Parsed Data to a String        
        mystr = mystr[1:]
        myList = (mystr.split("\n\n")) 


        states = ['Delhi','West Bengal', 'Maharashtra',] # Enter Your State Name Here (Dont Enter More Than 5 States)
        for item in myList[0:25]:
            dataList = (item.split('\n'))
            if dataList[1] in states:
                notify_title= 'Cases of Covid-19 In India'
                notify_text= f" State: {dataList[1]}\n Indian Cases : {dataList[2]} & Foreign Cases : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
                notifyMe(notify_title, notify_text)
                time.sleep(2)
        time.sleep(3600) #Loop For 1 Hour (1 hour = 3600 seconds)
