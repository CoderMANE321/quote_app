import requests
import json

# get quote from zen api
def send_request(quotes) -> list:
    try:    
        r = requests.get('https://zenquotes.io/api/quotes')
        to_quote = r.json()
        for item in to_quote:
            quotes.append(item['q']) 
        return quotes    
    except requests.exceptions.RequestException as e:
        print (f"{e}")
        return []