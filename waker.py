import urllib.request

sleeping_beauties = ['https://compreqs.herokuapp.com/']

for beauty in sleeping_beauties:
    try:
        urllib.request.urlopen(beauty).close()
    except:
        pass
