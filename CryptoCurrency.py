#Write a script that fetches the real-time prices of the top 5 cryptocurrencies in Rupees and Dollars
import requests
import json

API_Key = 'JSU8K5QD42YYDG21'
currency=['BTC','LTC'] #'NMC','PPC','DOGE']
for i in currency:
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+i+'&to_currency=USD&apikey='+API_Key
    response = requests.get(url)
    ans=json.loads(response.text)
    print(ans)

for j in currency:
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+j+'&to_currency=INR&apikey='+API_Key
    response = requests.get(url)
    ans=json.loads(response.text)
    print(ans)