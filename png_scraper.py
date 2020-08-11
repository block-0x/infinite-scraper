import requests

url = 'https://qiita.com/___xxx_'
res = requests.get('http://localhost:8050/render.png',
                   params={'url': url, 'wait': 1, 'viewport': '2560x1600', 'render_all': 1})

with open('test.png', 'wb') as f:
    f.write(res.content)
