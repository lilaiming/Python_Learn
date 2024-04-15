# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com


import requests

headers = {
    'Host': 'www.amazon.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Sec-GPC': '1',
    'Alt-Used': 'www.amazon.com',
    'Connection': 'keep-alive',
    'Cookie': 'session-id=135-4107951-7751067; session-id-time=2082787201l; sp-cdn="L5Z9:HK"; skin=noskin; csm-hit=tb:8XS5VYGY159WMERE84JR+s-M3GWD931TCZGBC2DG1YC|1713163735858&t:1713163735858&adb:adblk_no; ubid-main=133-3731748-1656911; sst-main=Sst1|PQFD87u4oe7mP2PavKSnWDFmB1Gzn1R3BTooXdtOc-QApxKazjfRKmvyQcMUwUlDb8Rrm_bxgkKWIiuoowycbdbWN77iRCILPIfx5lzIjEbJ97jqcoR0JyzXJ1pq7HtIzKYmdrQfmkU-zHshGCBcylhEqYEL6Ufe9LXV4REpBmBECsrHIcYu0rvWxe4wK35A4MN7mO1xWF6o2mMX9CEHA_pbKgeVohZL4d4oX2YYEeXwPZnyudwA6s90yA70_Wvgk7kl; session-token=ZCitp5AxCZ5jL2nJunxJ35y5b3NQ3us9hyXrB2v6KUIN2rShaslw7Xxf7A7kqS9xFckOlQZ/WHjCcaO7kmu8Qpy07sb6fJQYSzAfm2uAiB1QOItD95eVKf4KYoFGmA26Y3NsU37p9QswgWlPIgyhrVRoCtIP8iAJqV/4NWFB2Y/oAXztmassjw1tVAhhzxvotXeyN7FMAZDisCYbOWgFXwJ3fqfxWUZR3+m/qWZhYUzUMKezqhxXQlrjNX94WbrdGKJY9BejcBZlqw+SZi/EqosJlrKGEyfKLb9NkIrWa84RQXrvzd+34wUhPLTTDmV9hhX/eIvrXh41CtxCAPLZqrIMpldtht6g; i18n-prefs=USD; lc-main=en_US',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

url = "https://www.amazon.com/s?k=iphone"

response = requests.get(url=url, headers=headers)

print(response.status_code)



