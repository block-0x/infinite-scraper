import requests

url = 'https://qiita.com/___xxx_'
res = requests.get('http://localhost:8050/render.jpeg',
                   params={'url': url, 'wait': 1, 'width': 1000, 'quality': 100})

with open('test.jpg', 'wb') as f:
    f.write(res.content)
