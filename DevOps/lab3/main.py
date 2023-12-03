import json
import requests
from datetime import datetime

try:
    with open('main.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        if data['link']:
            response = requests.get(data['link'])

    with open(
            'output.json',
            'a',
            encoding='utf-8',
    ) as t:
        d = dict(
            url=response.url,
            status=response.status_code,
            datetime=datetime.now().strftime('%d.%m.%Y-%H:%M:%S'),
        )
        json.dump(d, t, ensure_ascii=False, indent=2)
except Exception as err:
    with open(f'output.json', 'a', encoding='utf-8'):
        d = dict(
            error=str(err),
            datetime=datetime.now().strftime('%d.%m.%Y-%H:%M:%S'),
        )
