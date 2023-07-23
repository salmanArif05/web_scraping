import requests
import random


user_agent = [
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'
]

url = "https://lyricsmint.com/"

header = {
    'User-Agent' : random.choice(user_agent)
}


res = requests.get(url, headers = header)

# print(res.text, "response")
print(res.request.headers, "Request Headers")