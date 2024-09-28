import requests
import re

suburl="https://sub2.meco.us.kg/api/v1/client/subscribe?token=e4b320e9f72ee607a3c2af21cc3e4423"
ariurl="https://suo.yt/TsYctUa"
headers = {
    "User-Agent": "ClashforWindows/0.20.39"
}

subtext = requests.get(url=suburl,headers=headers).text
f1=open('亿点连接(github)','w')
f1.write(subtext)
f1.close()

# aritext = requests.get(url=ariurl,headers=headers).text
# aritext = re.sub(r"( \-.*steam.*\,)🎯 全球直连",r"\1🔰 节点选择", aritext)
# aritext = re.sub(r"\[高速\]ACSS-","", aritext)
# aritext = re.sub(r"🇦🇨(.*美国)",r"🇺🇸\1", aritext)
# aritext = re.sub(r"🇦🇨(.*香港)",r"🇭🇰\1", aritext)
# aritext = re.sub(r"🇦🇨(.*日本)",r"🇯🇵\1", aritext)
# aritext = re.sub(r"🇦🇨(.*台湾)",r"🇹🇼\1", aritext)
# aritext = re.sub(r"🇦🇨(.*英国)",r"🇬🇧\1", aritext)
# aritext = re.sub(r"🇦🇨(.*俄罗斯)",r"🇷🇺\1", aritext)
# f2=open('Ari+','w')
# f2.write(aritext)
# f2.close()
