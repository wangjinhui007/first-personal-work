import jieba
import json

commentList = open('zyq.txt', 'r', encoding='utf-8').read()

words = jieba.lcut(commentList)
wordCounts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        wordCounts[word] = wordCounts.get(word, 0) + 1
items = list(wordCounts.items())
items.sort(key=lambda x: x[1], reverse=True)

countList = []
for i in range(len(items)):
    countDict = {}
    word, count = items[i]
    if count >= 10:
        countDict['name'] = word
        countDict['value'] = count
        countList.append(countDict)
# print(countList)
Sum = {}
Sum['Sum'] = countList
print(Sum)
with open('zyq.json', 'w', encoding='utf-8') as f:
    json.dump(Sum, f, ensure_ascii=False, indent=4)
