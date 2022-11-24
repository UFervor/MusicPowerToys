from mutagen.id3 import ID3, TIT2, TPE1,TALB
from mutagen.flac import FLAC
import mutagen
import os,shutil
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.mp3') or f.endswith('.flac') or f.endswith('.aif'):
                fullname = os.path.join(root, f)
                yield fullname
base = str(input("请输入路径："))
os.chdir(base)
def get_title(i):
    title = ''
    try:
        file = mutagen.File(os.path.abspath(i))
        title = file.tags["TIT2"].text[0]
    except:
        try:
            tags = mutagen.File(os.path.abspath(i)).tags
            for i in tags:
                if i[0].upper()=='TITLE':
                    title=i[1]
                    break
        except:
            pass
    return title

def get_album(i):
    album = ''
    try:
        file = mutagen.File(os.path.abspath(i))
        album = file.tags["TALB"].text[0]
    except:
        try:
            tags = mutagen.File(os.path.abspath(i)).tags
            for i in tags:
                if i[0].upper()=='ALBUM':
                    album=i[1]
                    break
        except:
            pass
    return album

def get_artist(i):
    artist = []
    try:
        file = mutagen.File(os.path.abspath(i))
        artist = file.tags["TPE1"].text
    except:
        try:
            tags = mutagen.File(os.path.abspath(i)).tags
            for i in tags:
                if i[0].upper()=='ARTIST':
                    artist.append(i[1])
        except:
            pass
    return artist

def smart_sep(artist):
    sc = ['&','/','ft.','feat.','\\\\']
    for i in sc:
        artist = sep(artist,i)
    return artist
        
def sep(artist,str):
    fin = []
    for i in artist:
        tmp = i.split(str)
        while '' in tmp:
            tmp.remove('')
        ran = len(tmp)
        for i in range(0,ran):
            tmp[i] = tmp[i].strip()
        fin += tmp
    return fin

def sfa(path, artist):
    audio = FLAC(path)
    audio['ARTIST'] = artist
    audio.save()

def sfi(path, artist):
    tags = ID3(path)
    tags['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
        encoding=3,
        text=artist
    )
    tags.save(path)

def mv(q):
    src = q
    album = get_album(src)
    title = get_title(src)
    try:
        sfa(src,'\\\\'.join(smart_sep(get_artist(i))))
    except:
        sfi(src,'\\\\'.join(smart_sep(get_artist(i))))
    fname = ''

    try:
        fname += ', '.join(smart_sep(get_artist(i)))
    except:pass
    if album != '':
        if fname != '':
            fname += ' - ' + album
        else:
            fname += album
    
    dirname = fname
    if title != '':
        if fname != '':
            fname += ' - ' + title
        else:
            fname += title
    lrcname = fname + '.lrc'
    fname += os.path.splitext(src)[-1]
    fname = fname.replace('/','／').replace(':','：').replace(r'"','\'').replace('*','＊')

    if dirname not in os.listdir():
        try:
            os.mkdir(dirname)
            # print('Successfully Made Dir:' + dirname)
        except Exception as e:
            print('Unexpected Error Occurred While Making Dir: ' + dirname)
            print(e)
            
    try:
        os.rename(src,fname)
        # print('Successfully Renamed '+ src +' as '+ fname)
    except Exception as e:
        print('Unexpected Error Occurred While Renaming File: ' + src)
        print(e)
    
    try:
        shutil.move(fname,base+dirname+'\\'+fname)
        # print('Successfully Moved Song: '+ src)
        if os.path.exists(lrcname):
            shutil.move(lrcname,base+dirname+'\\'+lrcname)
            # print('Successfully Moved Lrc: '+ lrcname)
    except Exception as e:
        print('Unexpected Error Occurred While Moiving File: ' + src)
        print(e)

for i in findAllFile(base):
    mv(i)
