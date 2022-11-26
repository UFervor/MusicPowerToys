from mutagen.id3 import ID3, TIT2, TPE1, TALB
from mutagen.flac import FLAC
import mutagen
import os
import shutil


class Audio:
    def __init__(self, path, delimiter):
        self.path = os.path.abspath(path)
        self.delimiter = delimiter

    @property
    def Title(self):
        title = ''
        try:
            file = mutagen.File(self.path)
            title = file.tags["TIT2"].text[0]
        except:
            try:
                tags = mutagen.File(self.path).tags
                for i in tags:
                    if i[0].upper() == 'TITLE':
                        title = i[1]
                        break
            except:
                pass
        return title

    @property
    def Album(self):
        album = ''
        try:
            file = mutagen.File(self.path)
            album = file.tags["TALB"].text[0]
        except:
            try:
                tags = mutagen.File(self.path).tags
                for i in tags:
                    if i[0].upper() == 'ALBUM':
                        album = i[1]
                        break
            except:
                pass
        return album

    @property
    def Artist(self):
        artist = []
        try:
            file = mutagen.File(self.path)
            artist = file.tags["TPE1"].text
        except:
            try:
                tags = mutagen.File(self.path).tags
                for i in tags:
                    if i[0].upper() == 'ARTIST':
                        artist.append(i[1])
            except:
                pass
        for i in self.delimiter:
            fin = []
            for j in artist:
                tmp = j.split(i)
                while '' in tmp:
                    tmp.remove('')
                for j in range(0, len(tmp)):
                    tmp[j] = tmp[j].strip()
                fin += tmp
            artist = fin
        return artist


class AudioTool:
    def __init__(self, base, suffix=["mp3", "flac", "aif"], delimiter=['&', '/', 'ft.', 'feat.', '\\\\']):
        self.base = base.strip(["/", "\\"])
        self.suffix = suffix
        self.delimiter = delimiter

    def fjoin(self, dir, name):
        return self.base + dir + "\\" + name

    def sed(self, au):
        album = au.Album
        title = au.Title

        try:
            audio = FLAC(au.path)
            audio['ARTIST'] = '\\\\'.join(au.Artist)
            audio.save()
        except:
            tags = ID3(au.path)
            tags['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
                encoding=3,
                text='\\\\'.join(au.Artist)
            )
            tags.save(au.path)
        fname = ''

        try:
            fname += ', '.join(au.Artist)
        except:
            pass
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
        fname += os.path.splitext(au.path)[-1]
        fname = fname.replace('/', '／').replace(':',
                                                '：').replace("\"", '\'').replace('*', '＊')

        if dirname not in os.listdir():
            try:
                os.mkdir(dirname)
                # print('Successfully Made Dir:' + dirname)
            except Exception as e:
                print('Unexpected Error Occurred While Making Dir: ' + dirname)
                print(e)

        try:
            os.rename(au.path, fname)
            # print('Successfully Renamed '+ src +' as '+ fname)
        except Exception as e:
            print('Unexpected Error Occurred While Renaming File: ' + au.path)
            print(e)

        try:
            shutil.move(fname, self.fjoin(dirname, fname))
            # print('Successfully Moved Song: '+ src)
            if os.path.exists(lrcname):
                shutil.move(lrcname, self.fjoin(dirname, lrcname))
                # print('Successfully Moved Lrc: '+ lrcname)
        except Exception as e:
            print('Unexpected Error Occurred While Moiving File: ' + au.path)
            print(e)

        def start(self):
            for root, ds, fs in os.walk(self.base):
                for f in fs:
                    if f[f.rfind(".") + 1:] in self.suffix:
                        fullname = os.path.join(root, f)
                        self.sed(fullname)
