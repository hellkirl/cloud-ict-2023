import json
import requests
from datetime import datetime
import re
import os

files_directory = 'files'

all_files = sorted(os.listdir(files_directory), key=lambda x: os.path.getmtime(os.path.join(files_directory, x)),
                   reverse=True)

latest_file = all_files[0] if all_files else None

if latest_file:
    with open(os.path.join(files_directory, latest_file), 'r', encoding='utf-8') as f:
        data = json.load(f)
        if data['link']:
            response = requests.get(data['link'])

    link = re.search(r'(\w+\.\w+)', data['link']).group(0)

    filename = (
        f'reports/{datetime.now().strftime("%d.%m.%Y-%H:%M:%S")}-{link}.json'
    )

    with open(
            filename,
            'a',
            encoding='utf-8',
    ) as t:
        d = dict(
            url=response.url,
            status=response.status_code,
            datetime=datetime.now().strftime('%d.%m.%Y-%H:%M:%S'),
        )
        json.dump(d, t, ensure_ascii=False, indent=2)
else:
    print("No files found in the specified directory.")
