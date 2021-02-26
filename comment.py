import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

sou='1613797087640'
cursor = '0'
new_list = []

for item in range(0,100):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + str(sou)
    source = requests.get(url, headers=headers).content.decode()
    result = re.findall('"content":"(.*?)",', source, re.S)
    new_list.append(result)
    cursor = re.findall('"last":"(.*?)","', source, re.S)[0]

with open("comments.txt", "w", encoding="utf-8") as f:
    for item in new_list:
        for i in item:
            f.write(i)
            f.write("\n")
