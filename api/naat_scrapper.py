from bs4 import BeautifulSoup
# from bs4 import 
import requests
import audioread
import pathlib



def SearchNaats(name=None,url=None):
    query = str(name)
    query = query.replace(' ','+')
    if url is not None:
        r = requests.get(url=url)
    else:
        r = requests.get(url=f'https://thenaatsharif.com/?s={query}')
    html = r.content
    # print(html)
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find_all('article')
    page_div = str(soup.find_all('div',{'class':'nav-links'}))


    naats = []
    for link in links:
        anchors = link.find_all('a')
        link = link.find('a')
        title = anchors[0].getText()
        l = str(anchors[1].get('href'))
        audio = l.replace('download','downloads').replace('index.php?track=','')
        half = audio.replace('https://files.thenaatsharif.com/downloads/','')
        artist = half[:half.find('/')].replace('-',' ').capitalize()
        naat = {
            'title':title,
            'audio':audio,
            'naat_khwan': artist
        }
        naats.append(naat)
    return naats,page_div
    

def get_naat_khwans(url=None):
    if url is None:
        r = requests.get(url='https://thenaatsharif.com/naat-khawans/')
        html = r.content
        soup = BeautifulSoup(html,'html.parser')
        elem = soup.find_all('li',{'class':'cat-item'})
        naat_khwans = []
        for i in elem:
            # print(i)
            anchor = i.find('a')
     
            naat_khwan = {
                'link' : anchor.get('href'),
                'name' : anchor.getText()
            }
            naat_khwans.append(naat_khwan) 
        return naat_khwans
      
    naat,page_div = SearchNaats(url=url)
    return naat,page_div


def GetAudio(url):
    try: 
        r = requests.get(url=url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        # down_a = soup.find('a',{'class':'download-page-link'})
        # down_link = down_a.get('href')
        # print(down_link)
        audio = soup.find('audio')
        source = audio.get('src')
        t = soup.find('h1',{'class':'entry-title'})
        artist = str(url).replace('https://thenaatsharif.com/','')
        artist = artist[:artist.find('/')]
        # s = Search(str(t.getText()).lower()+artist)
        # print(str(t.getText()).lower()+artist)
        # v = str(s.results[0])
        # vid = v[41:].replace('>','')
        # img_url = f'https://img.youtube.com/vi/{vid}/hqdefault.jpg'
        return {'source':source} 
    except:
        return {'source':'None'}

def GetLyrics(url):
    r = requests.get(url)
    html  = r.content
    soup = BeautifulSoup(html, 'html.parser')
    lyrics = soup.find('div',{'class':'lyrics_container'}).children
    innerhtml = ''
    for i in lyrics:
        innerhtml = innerhtml + str(i)
    return innerhtml

def YtSrapper(url):
    r = requests.get(url=url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    audio = soup.find('audio')
    source = audio.get('src')
    t = soup.find('h1',{'class':'entry-title'})
    title = t.getText()
    nr = requests.get(url='https://www.google.com/search?rlz=1C1RXQR_enIN965IN965&sxsrf=AJOqlzVl07Lky1g4Am18_f8UnSvmXPbVRA:1677374754524&q=sar+e+la+makan+se+talab+hafiz-ahmed-raza-qadri&tbm=isch&sa=X&ved=2ahUKEwi47pfzg7L9AhX-XmwGHZldCigQ0pQJegQIDhAB&biw=1450&bih=667&dpr=1.32')
    html2 = nr.content
    soup2 = BeautifulSoup(html2,'html.parser')
    a = soup2.find_all('h3')
  