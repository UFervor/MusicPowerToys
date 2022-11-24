import taglib,os,re
file_path = r'\\ds920\music\Avicii\Avicii - Feeling Good - Feeling Good.flac'
#file_path = r'\\ds920\music\Lifeformed - Fastfall\Lifeformed - Fastfall - 9-bit Expedition.mp3'
def sed(file_path):
    song = taglib.File(file_path)
    lrcpth = os.path.splitext(file_path)[0]+'.lrc'
    if(os.path.exists(lrcpth)):
        with open(lrcpth) as lrc:
            LYRIC=lrc.readlines()
            if(LYRIC):
                song.tags['LYRICS']=''.join(LYRIC)
                print("LRC ADDED")
    if 'GENRE' in song.tags.keys():
        if re.match('[0-9]+_[0-9]+',song.tags['GENRE'][0], flags=0):
            del song.tags['GENRE']
            print('GENRE DELED')
    song.save()
    song.close()

for root,dirs,files in os.walk('\\\\ds920\\music\\'):
    for name in files:
        if name.endswith(".flac") or name.endswith(".mp3") or name.endswith(".aif"):
            print(os.path.join(root, name))
            sed(os.path.join(root, name))
            
# sed(file_path)