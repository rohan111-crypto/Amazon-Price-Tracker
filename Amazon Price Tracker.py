#!/usr/bin/env python
# coding: utf-8

# In[182]:


import requests
from bs4 import BeautifulSoup
import smtplib


# In[183]:


URL = 'https://www.flipkart.com/samsung-galaxy-s20-ultra-cosmic-gray-128-gb/p/itma25b4687846b4'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}


# In[184]:


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rohanm80766@gmail.com','gptocjiyiypjktsw')
    subject = 'Hey! your product is having a price drop'
    body = 'https://www.flipkart.com/samsung-galaxy-s20-ultra-cosmic-gray-128-gb/p/itma25b4687846b4'
    main_msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('rohanm80766@gmail.com','rohanmaurya91@yahoo.in',main_msg)
    print('EMAIL HAS BEEN SENT!')
    server.quit()


# In[185]:


def price_checker():
    page = requests.get(URL,params=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
    converted_price=float(price[1:3])
    if(converted_price<100.0):
        send_mail()


# In[187]:


price_checker()


# In[ ]:




