import requests

suburl="https://sub.xn--lmq622c7qjhl4a.com/api/v1/client/subscribe?token=e4b320e9f72ee607a3c2af21cc3e4423"
headers = {
    "User-Agent": "ClashforWindows/0.20.36"
}

subtext = requests.get(url=suburl,headers=headers).text
f=open('亿点连接(github)','w')
f.write(subtext)
f.close()
