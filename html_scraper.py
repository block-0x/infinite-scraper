import requests

url = 'https://qiita.com/___xxx_'
res = requests.get('http://localhost:8050/render.html',
                   params={'url': url, 'wait': 0.5})

with open('test.html', 'wb') as f:
    f.write(res.content)
