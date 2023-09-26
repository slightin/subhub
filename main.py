import requests

suburl="https://sub.xn--lmq622c7qjhl4a.com/api/v1/client/subscribe?token=e4b320e9f72ee607a3c2af21cc3e4423"

subtext = requests.get(suburl).text
f=open('sub1','w')
f.write(subtext)
f.close()