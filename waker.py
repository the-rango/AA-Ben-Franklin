import urllib.request

sleeping_beauties = ['https://the-antalmanac.herokuapp.com/',
                     'https://gentle-inlet-23513.herokuapp.com/']

for beauty in sleeping_beauties:
    try:
        urllib.request.urlopen(beauty).close()
    except:
        pass
