import requests

url = "https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a"
pachong = requests.get(url,headers={'user-agent':'chrome'})
xiaoshengke = pachong.json()
# print(type(xiaoshengke),len(xiaoshengke))
# print(xiaoshengke)
print(xiaoshengke['image'],type(xiaoshengke['image']))
haibao = requests.get(xiaoshengke['image'],headers={'user-agent':'chrome'})
with open("haibao.jpg","wb") as code:
    code.write(haibao.content)