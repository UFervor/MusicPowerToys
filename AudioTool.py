from mutagen.id3 import ID3, TIT2, TPE1, TALB
from mutagen.flac import FLAC
import mutagen
import os
import shutil


class Audio:
    def __init__(self, path, delimiter):
        self.path = os.path.abspath(path)
        self.delimiter = delimiter
        self.dir = os.path.dirname(self.path)
        try:
            audio = FLAC(self.path)
            audio['ARTIST'] = self.Artist
            print(audio)
            audio.save()
        except:
            tags = ID3(self.path)
            tags['TPE1'] = TPE1(
                encoding=3,
                text=self.Artist
            )
            tags.save(self.path)

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
        return title.strip()

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
        return album.strip()

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

    @property
    def FileName(self):
        return " - ".join(list(filter(None, [', '.join(self.Artist), self.Album, self.Title])))


class AudioTool:
    def __init__(self, base, suffix=["mp3", "flac", "aif"], delimiter=['/', 'ft.', 'feat.', '\\', '\\\\'], limit=8):
        self.base = base.strip("/\\")
        self.suffix = suffix
        self.delimiter = delimiter
        self.audios = {}
        self.artists = {}
        self.limit = limit

    def fjoin(self, dir, name):
        return self.base + "\\" + dir + "\\" + name

    def sed(self, au):
        dirname = " - ".join(list(filter(None,
                             [', '.join(self.artists[au.Album]), au.Album])))

        fname = au.FileName
        lrcname = fname + '.lrc'
        fname += os.path.splitext(au.path)[-1]
        fname = fname.replace('/', '／').replace(':',
                                                '：').replace("\"", '\'').replace('*', '＊')

        if dirname not in os.listdir():
            try:
                os.mkdir(self.base + "\\" + dirname)
                print('Successfully Made Dir:' + dirname)
            except Exception as e:
                print('Unexpected Error Occurred While Making Dir: ' + dirname)
                print(e)

        try:
            os.rename(au.path, au.dir + "\\" + fname)
            print('Successfully Renamed ' + au.path +
                  ' as ' + au.dir + "\\" + fname)
        except Exception as e:
            print('Unexpected Error Occurred While Renaming File: ' + au.path)
            print(e)

        try:
            shutil.move(au.dir + "\\" + fname, self.fjoin(dirname, fname))
            print('Successfully Moved Song: ' + au.path)
            if os.path.exists(au.dir + "\\" + lrcname):
                shutil.move(au.dir + "\\" + lrcname,
                            self.fjoin(dirname, lrcname))
                print('Successfully Moved Lrc: ' + lrcname)
        except Exception as e:
            print('Unexpected Error Occurred While Moiving File: ' + au.path)
            print(e)

    def start(self):
        for root, dir, fs in os.walk(self.base):
            for f in fs:
                if f[f.rfind(".") + 1:] in self.suffix:
                    tmp = Audio(os.path.join(root, f), self.delimiter)
                    try:
                        self.audios[tmp.Album].append(tmp)
                    except:
                        self.audios[tmp.Album] = []
                        self.audios[tmp.Album].append(tmp)

        for i in self.audios.keys():
            tmp = []
            for j in self.audios[i]:
                tmp.extend(j.Artist)
            tmp = list(set(tmp))

            if len(tmp) <= self.limit:
                self.artists[i] = tmp
            else:
                self.artists[i] = ["Various Artists"]

        for i in self.audios.keys():
            for j in self.audios[i]:
                if j.Album or j.Artist:
                    self.sed(j)
