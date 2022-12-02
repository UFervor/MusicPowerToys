from AUDIO import EAUDIO
import os
import shutil


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
