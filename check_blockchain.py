import os
import sys
from datetime import datetime
import requests


def check():
    print(datetime.now())
    txt = '<span class="sc-1rs1xpb-0 ktfYhX sc-1mclc94-0 sc-5mgfmd-0 cVgBQs cicUjF">Unconfirmed</span>'
    url = 'https://www.blockchain.com/btc/tx/dc000cff0462577928f0d53bea02227473e62f1b0da98f7c8ac6bab3920ed134'

    response = requests.get(url)
    content = response.text
    open('b.html', 'w').write(content)
    print('Download')

    return txt in content


import time

while True:
    try:
        is_found = check()
    except:
        pass

    else:
        if is_found:
            print('Found')
            time.sleep(60)
        else:
            print('Not found')
            os.system('telegram-send 比特币已经到账')
            raise SystemExit
