import taglib
import os
import re
# file_path = r'\\ds920\music\Avicii\Avicii - Feeling Good - Feeling Good.flac'
#file_path = r'\\ds920\music\Lifeformed - Fastfall\Lifeformed - Fastfall - 9-bit Expedition.mp3'


def sed(file_path):
    song = taglib.File(file_path)
    lrcpth = os.path.splitext(file_path)[0]+'.lrc'
    if(os.path.exists(lrcpth)):
        with open(lrcpth) as lrc:
            LYRIC = lrc.readlines()
            if(LYRIC):
                song.tags['LYRICS'] = ''.join(LYRIC)
                print("LRC ADDED")
    if 'GENRE' in song.tags.keys():
        if re.match('[0-9]+_[0-9]+', song.tags['GENRE'][0], flags=0):
            del song.tags['GENRE']
            print('GENRE DELED')
    song.save()
    song.close()


for root, dirs, files in os.walk("C:\\Users\\23660\\Desktop\\李玉刚 - 清明上河图 (伴奏)(bq)\\"):
    for name in files:
        if not name.endswith(".lrc"):
            print(os.path.join(root, name))
            try:
                sed(os.path.join(root, name))
            except:
                pass
# sed(file_path)
