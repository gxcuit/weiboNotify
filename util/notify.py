import logging
import os
from typing import List

import requests
import const
# from weibo import logger



def push_deer(append_str):
    params = {
        'pushkey': const.NOTIFY['PUSH_KEY'],
        'text': append_str,
    }
    # 这里为了避免证书验证，使用http而非https
    requests.get(url="http://api2.pushdeer.com/message/push", params=params)

def push_pushPlus(weibos:List,token):
    interested_key = ['screen_name','text','created_at']
    # interested_weibos = [{key: weibo[key] for key in interested_key} for weibo in weibos]
    # print(interested_weibos)
    push_weibos = []
    for weibo in weibos:
        # 原创微博
        push_weibo = {key: weibo[key] for key in interested_key}
        # 如果存在转发，将转发微博加上
        if 'retweet' in weibo:
            retweet_weibo = {key: weibo['retweet'][key] for key in interested_key}
            push_weibo['retweet'] = retweet_weibo

        push_weibos.append(push_weibo)

    push = {"token": token,
            "content": push_weibos,
            "template": "json"
            }

    response = requests.post(url="http://www.pushplus.plus/send/", json=push)
    response.encoding='utf-8'
    return response.text

