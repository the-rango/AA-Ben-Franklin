import os
import SOCSpider
import redis

r = redis.from_url(os.environ.get('REDISCLOUD_URL'))

print('=====================================')
print('doggos is working on it right now')
master_dict = SOCSpider.getAllInfo(SOCSpider.getURL(SOCSpider.getDepts()))
print('got it!')
print('=====================================')

for code, data in master_dict.items():
    print(code,end=' ')
    try:
        ########## Change Qtr ##########
        cap, enr, req, wl, res = eval(r.get('f'+code))
    except:
        continue
    cap.append(data[0])
    enr.append(data[1])
    req.append(data[2])
    wl.append(data[3])
    res.append(data[4])
    ########## Change Qtr ##########
    r.set('f'+code, (cap, enr, req, wl, res))
print('done')
