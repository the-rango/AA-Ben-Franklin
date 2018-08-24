import urllib.request
from datetime import datetime

now_time = datetime.now().time()
print(now_time)
if True:#(now_time > datetime.strptime('15:00', '%H:%M').time() and now_time < datetime.strptime('23:59', '%H:%M').time()) or now_time < datetime.strptime('5:00', '%H:%M').time():
    try:
        data = urllib.request.urlopen('https://antalmanac.herokuapp.com/')
        data.read()
        data.close()
    except:
        pass
    try:
        data = urllib.request.urlopen('http://summer18.herokuapp.com/')
        data.read()
        data.close()
    except:
        pass
    try:
        data = urllib.request.urlopen('https://websocserver.herokuapp.com/')
        data.read()
        data.close()
    except:
        pass
    try:
        data = urllib.request.urlopen('https://reactant.herokuapp.com/')
        data.read()
        data.close()
    except:
        pass
    try:
        data = urllib.request.urlopen('https://aareact.herokuapp.com/')
        data.read()
        data.close()
    except:
        pass
    try:
        data = urllib.request.urlopen('https://antal.herokuapp.com/')
        data.read()
        data.close()
    except:
        pass
    
    print('woke')
else:
    print ('aint time yet')
