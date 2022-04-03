from typing import List

import requests
import const


def push_deer(append_str):
    params = {
        'pushkey': const.NOTIFY['PUSH_KEY'],
        'text': append_str,
    }
    # 这里为了避免证书验证，使用http而非https
    requests.get(url="http://api2.pushdeer.com/message/push", params=params)

def push_pushPlus(weibos:List,token):
    interested_key = ['screen_name','text','created_at']
    interested_weibos = [{key: weibo[key] for key in interested_key} for weibo in weibos]
    # print(interested_weibos)

    push = {"token": token,
            "content": interested_weibos,
            "template": "json"
            }

    response = requests.post(url="http://www.pushplus.plus/send/", json=push)
    print(response)

