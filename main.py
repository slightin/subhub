import requests
import re

suburl="https://sub.xn--lmq622c7qjhl4a.com/api/v1/client/subscribe?token=e4b320e9f72ee607a3c2af21cc3e4423"
ariurl="http://api.acnodeserver.com:25500/sub?target=clash&url=https%3A%2F%2Flink2.asia%2Flink%2F4GQweRjBlgfCu76F%3Fsub%3D3&insert=false&filename=Ari&emoji=true&list=false&tfo=false&scv=false&fdn=false&sort=false&new_name=true"
headers = {
    "User-Agent": "ClashforWindows/0.20.39"
}

subtext = requests.get(url=suburl,headers=headers).text
f1=open('亿点连接(github)','w')
f1.write(subtext)
f1.close()

aritext = requests.get(url=ariurl,headers=headers).text
aritext = re.sub(r"( \-.*steam.*\,)🎯 全球直连",r"\1🔰 节点选择", aritext)
aritext = re.sub(r"🇦🇨(.*美国)",r"🇺🇸\1", aritext)
aritext = re.sub(r"🇦🇨(.*香港)",r"🇭🇰\1", aritext)
aritext = re.sub(r"🇦🇨(.*日本)",r"🇯🇵\1", aritext)
aritext = re.sub(r"🇦🇨(.*台湾)",r"🇹🇼\1", aritext)
aritext = re.sub(r"🇦🇨(.*英国)",r"🇬🇧\1", aritext)
aritext = re.sub(r"🇦🇨(.*俄罗斯)",r"🇷🇺\1", aritext)
f2=open('Ari+','w')
f2.write(aritext)
f2.close()