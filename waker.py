import urllib.request
from datetime import datetime

sleeping_beauties = ['https://antalmanac.herokuapp.com/',
                     'http://summer18.herokuapp.com/',
                     'https://websocserver.herokuapp.com/',
                     'https://reactant.herokuapp.com/',
                     'https://aareact.herokuapp.com/',
                     'https://antal.herokuapp.com/',
                     'https://gentle-inlet-23513.herokuapp.com/']
                     
now_time = datetime.now().time()
print(now_time)
if True:#(now_time > datetime.strptime('15:00', '%H:%M').time() and now_time < datetime.strptime('23:59', '%H:%M').time()) or now_time < datetime.strptime('5:00', '%H:%M').time():
    for beauty in sleeping_beauties:
        try:
            data = urllib.request.urlopen(beauty)
            data.read()
            data.close()
        except:
            pass
    
    print('woke')
else:
    print ('aint time yet')
