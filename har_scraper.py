import requests

url = 'https://qiita.com/derodero24'
res = requests.get('http://localhost:8050/render.har',
                   params={'url': url, 'wait': 0.5})

with open('test.har', 'wb') as f:
    f.write(res.content)
