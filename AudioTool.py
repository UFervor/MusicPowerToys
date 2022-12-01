from AUDIO import AUDIO
import os
import shutil


class EAUDIO(AUDIO):
    def __init__(self, path, delimiter, CAPARTIST=False):
        super().__init__(path)
        self.delimiter = delimiter
        self.dir = os.path.dirname(path)
        self.CAPARTIST = CAPARTIST
        try:
            audio = AUDIO(path)
            audio.ARTIST = self.ARTIST
        except:
            pass

    @property
    def TITLE(self):
        return super().TITLE[0]

    @TITLE.setter
    def TITLE(self, Value):
        self.__generalsetter__("TITLE", Value)

    @property
    def ALBUM(self):
        return super().ALBUM[0]

    @ALBUM.setter
    def ALBUM(self, Value):
        self.__generalsetter__("ALBUM", Value)

    @property
    def ARTIST(self):
        r = super().ARTIST
        for i in self.delimiter:
            fin = []
            for j in r:
                tmp = j.split(i)
                while '' in tmp:
                    tmp.remove('')
                for j in range(0, len(tmp)):
                    tmp[j] = tmp[j].strip()
                fin += tmp
            r = fin
        if self.CAPARTIST:
            for i in r:
                i = i.title()
        return r

    @ARTIST.setter
    def ARTIST(self, Value):
        self.__generalsetter__("ARTIST", Value)

    @property
    def YEAR(self):
        return super().YEAR[0]

    @YEAR.setter
    def YEAR(self, Value):
        self.__generalsetter__("YEAR", Value)

    @property
    def TRACK(self):
        return super().TRACK[0]

    @TRACK.setter
    def TRACK(self, Value):
        self.__generalsetter__("TRACK", Value)

    @property
    def GENRE(self):
        return super().GENRE[0]

    @GENRE.setter
    def GENRE(self, Value):
        self.__generalsetter__("GENRE", Value)

    @property
    def COMMENT(self):
        return super().COMMENT[0]

    @COMMENT.setter
    def COMMENT(self, Value):
        self.__generalsetter__("COMMENT", Value)

    @property
    def ALBUMARTIST(self):
        return super().ALBUMARTIST[0]

    @ALBUMARTIST.setter
    def ALBUMARTIST(self, Value):
        self.__generalsetter__("ALBUMARTIST", Value)

    @property
    def COMPOSER(self):
        return super().COMPOSER[0]

    @COMPOSER.setter
    def COMPOSER(self, Value):
        self.__generalsetter__("COMPOSER", Value)

    @property
    def DISCNUMBER(self):
        return super().DISCNUMBER[0]

    @DISCNUMBER.setter
    def DISCNUMBER(self, Value):
        self.__generalsetter__("DISCNUMBER", Value)

    @property
    def FileName(self):
        return " - ".join(list(filter(None, [', '.join(self.ARTIST), self.ALBUM, self.TITLE])))


class AudioTool:
    def __init__(self, base, suffix=["aac", "aif", "aiff", "dsf", "flac", "m4a", "mp3", "ogg", "opus", "wav", "wv", "m4b", "mpc", "ape"], delimiter=['/', 'ft.', 'feat.', '\\', '\\\\', '、'], limit=8):
        self.base = base.strip("/\\")
        self.suffix = suffix
        self.delimiter = delimiter
        self.audios = {}
        self.artists = {}
        self.limit = limit

    def fjoin(self, dir, name):
        return self.base + "\\" + dir + "\\" + name

    def fstd(self, string):
        return string.replace('/', '／').replace(':',
                                                '：').replace("\"", '\'').replace('*', '＊')

    def sed(self, au):
        dirname = self.fstd(" - ".join(list(filter(None,
                                                   [', '.join(self.artists[au.ALBUM]), au.ALBUM]))))
        fname = au.FileName
        lrcname = fname + '.lrc'
        fname += os.path.splitext(au.Path)[-1]
        fname = self.fstd(fname)

        if dirname not in os.listdir():
            try:
                if not os.path.exists(self.base + "\\" + dirname):
                    os.mkdir(self.base + "\\" + dirname)
                    # print('Successfully Made Dir: ' + dirname)
            except Exception as e:
                print('Unexpected Error Occurred While Making Dir: ' + dirname)
                print(e)

        try:
            os.rename(au.Path, au.dir + "\\" + fname)
            # print('Successfully Renamed ' + au.Path +
            #   ' as ' + au.dir + "\\" + fname)
        except Exception as e:
            print('Unexpected Error Occurred While Renaming File: ' + au.Path)
            print(e)

        try:
            shutil.move(au.dir + "\\" + fname, self.fjoin(dirname, fname))
            # print('Successfully Moved Song: ' + au.Path)
            if os.path.exists(au.dir + "\\" + lrcname):
                shutil.move(au.dir + "\\" + lrcname,
                            self.fjoin(dirname, lrcname))
                # print('Successfully Moved Lrc: ' + lrcname)
        except Exception as e:
            print('Unexpected Error Occurred While Moiving File: ' + au.Path)
            print(e)

    def start(self):
        for root, dir, fs in os.walk(self.base):
            for f in fs:
                if f[f.rfind(".") + 1:] in self.suffix:
                    tmp = EAUDIO(os.path.join(root, f), self.delimiter)
                    try:
                        self.audios[tmp.ALBUM].append(tmp)
                    except:
                        self.audios[tmp.ALBUM] = []
                        self.audios[tmp.ALBUM].append(tmp)

        for i in self.audios.keys():
            tmp = []
            for j in self.audios[i]:
                tmp.extend(j.ARTIST)
            tmp = list(set(tmp))
            tmp.sort()

            if len(tmp) <= self.limit:
                self.artists[i] = tmp
            else:
                self.artists[i] = ["Various Artists"]

        for i in self.audios.keys():
            for j in self.audios[i]:
                if j.ALBUM or j.ARTIST:
                    self.sed(j)
