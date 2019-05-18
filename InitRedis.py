import os
from urllib.parse import urlparse
import SOCSpider
import redis

r = redis.from_url(os.environ.get('REDISCLOUD_URL'))

########## Only if one existed before ##########
# r.flushall()

print('*****Doggo\'s doing its thing*****')
master_dict = SOCSpider.getAllInfo(SOCSpider.getURL(SOCSpider.getDepts()))
for code, data in master_dict.items():
    print(code,end=' ')
    ########## Change Qtr ##########
    r.set('f'+code, ([data[0]], [data[1]], [data[2]], [data[3]], [data[4]]))
print('done')
