from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
session = HTMLSession()
response = session.get('https://etherscan.io/gastracker')
soup = BeautifulSoup(response.content, 'html.parser')
import regex as re
import random
import pandas as pd
import yfinance as yf 
from datetime import datetime

transfer = soup.find('div',attrs={'class': 'table-responsive'})

score1 = soup.find('div',attrs={'class': 'col-md-4 mb-1 mb-md-0'})
#score1

rows=list()
for div in score1.findAll('div', attrs={'class': 'text-secondary'}):
    rows.append(div)
    
gwei_d = str(rows[1])
gwei_d = gwei_d[28:33]


rows=list()
for row in transfer.findAll("td"):
    rows.append(row)
    
# ERC Average Transfer: 
average_erc2 = rows[2]
average_erc2 = str(average_erc2)
#type(average_erc2)
average_erc2 = re.sub("<[^<]+?>", "", average_erc2)

# Uniswap Swap

average_uniswap = str(rows[6])
average_uniswap = re.sub("<[^<]+?>", "", average_uniswap)

gwei= soup.find('span', {'id': 'spanLowPrice'}).text
gwei_price = int(gwei)

random_images = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpXB13jMp4awmixPvpN0DW-l0W5gdXZ0Bmzg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxjUsC6DnBt1giE0uMTVH0d6M3UvCpypKLWQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT92AVVymoP6MnLOnC_vNc7eYaHiO0BcIRaVymqNkLC4y4BrJ3Bvf0N1rEV2u1LfQH9Tg8&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSK-TUk7IzP7tZInOiJZVZpGbKrLkEK2OSrCA&usqp=CAU',
    'https://images7.alphacoders.com/113/thumb-1920-1135135.jpg',
    'https://i.pinimg.com/originals/b4/0b/a9/b40ba97de4d41ee8c01975f05120316d.png'
]

if gwei_price < 50:


    ticker = 'ETH-USD'
    period = '5d'
    data = yf.download(ticker, period=period, interval='1d')
    data_adj = pd.DataFrame(data['Adj Close'])
    current_eth = data_adj['Adj Close'][-1]
    current_eth = "{:.2f}".format(current_eth)
    #current_eth = str(current_eth)

    mUrl = "WEBHOOK URL"
    data = {"embeds": 
        [{
       
        "title": "Low Ethereum Gas Fees",
        "url": "https://etherscan.io/gastracker",
        "description": " ",
        "color": 2123412,
            
        "fields": [
        {
        "name": "Gwei and Swap Values",
        "value": "Current Gwei: " + gwei + "\nGwei USD: " + gwei_d + "\nERC20 Average Transfer: " + average_erc2 + "\nUniswap Average Swap: " + average_uniswap,
        "inline": True }],
        
            
        "thumbnail": {
        "url": "https://uploads-ssl.webflow.com/6063626728ce7dfd0c61a317/61310213173d2e0c9de6c733_Hodlnaut-Resources-Ethereum-Gas-System-p-2000.jpeg"},  
        
        "image": {
        "url": random.choice(random_images)}, 

	"footer": {"text": "Current ETH-USD: " + current_eth}
 
        }]}

        
    response = requests.post(mUrl, json=data)

elif gwei_price > 50 and gwei_price <= 100:

    ticker = 'ETH-USD'
    period = '5d'
    data = yf.download(ticker, period=period, interval='1d')
    data_adj = pd.DataFrame(data['Adj Close'])
    current_eth = data_adj['Adj Close'][-1]
    current_eth = "{:.2f}".format(current_eth)
    #current_eth = str(current_eth)

    mUrl = "ENTER WEBHOOK URL "
    data = {"embeds": 
        [{
       
        "title": "Mid Ethereum Gas Fees",
        "url": "https://etherscan.io/gastracker",
        "description": " ",
        "color": 2123412,
            
        "fields": [
        {
        "name": "Gwei and Swap Values",
        "value": "Current Gwei: " + gwei + "\nGwei USD: " + gwei_d + "\nERC20 Average Transfer: " + average_erc2 + "\nUniswap Average Swap: " + average_uniswap,
        "inline": True }],
        
            
        "thumbnail": {
        "url": "https://uploads-ssl.webflow.com/6063626728ce7dfd0c61a317/61310213173d2e0c9de6c733_Hodlnaut-Resources-Ethereum-Gas-System-p-2000.jpeg"},  
        
        "image": {
        "url": random.choice(random_images)}, 

	"footer": {"text": "Current ETH-USD: " + current_eth}
 
        }]}

        
    response = requests.post(mUrl, json=data)

elif gwei_price > 101:

    ticker = 'ETH-USD'
    period = '5d'
    data = yf.download(ticker, period=period, interval='1d')
    data_adj = pd.DataFrame(data['Adj Close'])
    current_eth = data_adj['Adj Close'][-1]
    current_eth = "{:.2f}".format(current_eth)
    #current_eth = str(current_eth)

    mUrl = "ENTER WEBHOOK URL"
    data = {"embeds": 
        [{
       
        "title": "High Ethereum Gas Fees",
        "url": "https://etherscan.io/gastracker",
        "description": " ",
        "color": 2123412,
            
        "fields": [
        {
        "name": "Gwei and Swap Values",
        "value": "Current Gwei: " + gwei + "\nGwei USD: " + gwei_d + "\nERC20 Average Transfer: " + average_erc2 + "\nUniswap Average Swap: " + average_uniswap,
        "inline": True }],
        
            
        "thumbnail": {
        "url": "https://uploads-ssl.webflow.com/6063626728ce7dfd0c61a317/61310213173d2e0c9de6c733_Hodlnaut-Resources-Ethereum-Gas-System-p-2000.jpeg"},  
        
        "image": {
        "url": random.choice(random_images)}, 

	"footer": {"text": "Current ETH-USD: " + current_eth}
 
        }]}

        
    response = requests.post(mUrl, json=data)
