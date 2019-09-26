#!/usr/bin/env python
# coding: utf-8

# In[142]:


import requests
from bs4 import BeautifulSoup
import smtplib, ssl


# In[143]:


URL = 'https://www.jumia.ma/32-led-hd-tv-tnt-led32m5006dk-noir-daiko-mpg53778.html'


# In[144]:


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


# In[166]:


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.select('h1.title')[0].text.strip()
    price = soup.select('span.price')[0].text.strip()
    converted_price =(price.strip('Dhs')) 
    converted_price = converted_price.replace(" ","").split()
    converted_price = "".join(converted_price)
    converted_price = float(converted_price)    
        
    print(title)
    print(converted_price)  
    
    if (converted_price > 1298.0):
        send_mail()
def send_mail():
    try:
        server = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('mouhssineaitelbouhali@gmail.com', 'password')
        subject = 'Coucou, le prix a baissé !'
        body = 'Visitez le lien Jumia: https://www.jumia.ma/32-led-hd-tv-tnt-led32m5006dk-noir-daiko-mpg53778.html'

        msg = ("{Subject} \n\n{Body}".format(Subject=subject,Body=body)).encode('utf-8')

        server.sendmail(
            'mouhssineaitelbouhali@gmail.com',
            'sarta20102010@hotmail.com',
            msg
        )
        print ('Email Has Been Sent Succefully!')
    except Exception as e:
        print(e)
    finally:
        server.quit()


# In[167]:


check_price()


# In[ ]:




