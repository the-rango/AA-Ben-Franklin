import urllib.request

sleeping_beauties = ['https://rnh.herokuapp.com/']

for beauty in sleeping_beauties:
    try:
        urllib.request.urlopen(beauty).close()
    except:
        pass
