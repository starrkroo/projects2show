#!/usr/bin/env python3

import vk_api
from datetime import *
from time import sleep

vk_session = vk_api.VkApi('89894715441', 'starrk09095000')
vk_session.auth()

#vk = vk_session.get_api()

def work(item):
  vk_session.method("status.set", {"text": "Until the end of summer there were {}".format(item)})
