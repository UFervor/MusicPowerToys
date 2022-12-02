import os
import importlib
import mutagen
from mutagen.id3 import TIT2, TPE1, TALB, TDRC, TRCK, TCON, COMM, TPE2, TCOM, TPOS, TXXX, USLT


class AUDIO:
    # List Supported：True
    # String：Char
    # No List Supported：False
    MAP = {
        "ape": "APEv2",
        "wv": "APEv2",
        "mpc": "APEv2",
        "m4a": "MP4",
        "m4b": "MP4",
        "m4v": "MP4",
        "mp4": "MP4",
        "mp3": "ID3",
        "dsf": "ID3",
        "aac": "ID3",
        "wav": "ID3",
        "aiff": "ID3",
        "aif": "ID3",
        "flac": "FLAC",
        "opus": "Vorbis Comment",
        "ogg": "Vorbis Comment"
    }
    Config = {
        "APEv2": {
            'TITLE': ('TITLE', "\x00", ("str")),
            'ARTIST': ('ARTIST', "\x00", ("str")),
            'ALBUM': ('ALBUM', "\x00", ("str")),
            'YEAR': ('YEAR', "\x00", ("str")),
            'TRACK': ('TRACK', "\x00", ("str")),
            'GENRE': ('GENRE', "\x00", ("str")),
            'COMMENT': ('COMMENT', "\x00", ("str")),
            'ALBUMARTIST': ('ALBUMARTIST', "\x00", ("str")),
            'COMPOSER': ('COMPOSER', "\x00", ("str")),
            'DISCNUMBER': ('DISCNUMBER', "\x00", ("str")),
            'LYRICS': ('LYRICS', "\x00", ("str")),
            'ID3': False
        },
        "MP4": {
            'TITLE': ('©nam', True, ("str")),
            'ARTIST': ('©ART', True, ("str")),
            'ALBUM': ('©alb', True, ("str")),
            'YEAR': ('©day', True, ("str")),
            'TRACK': ('----:com.apple.iTunes:track', False, ("str")),
            'GENRE': ('----:com.apple.iTunes:GENRE', True, ("str")),
            'COMMENT': ('©cmt', True, ("str")),
            'ALBUMARTIST': ('aART', True, ("str")),
            'COMPOSER': ('©wrt', True, ("str")),
            'DISCNUMBER': ('----:com.apple.iTunes:disc', False, ("str")),
            'LYRICS': ('©lyr', True, ("str")),
            'ID3': False
        },
        "ID3": {
            'TITLE': ('TIT2', True, ("str")),
            'ARTIST': ('TPE1', True, ("str")),
            'ALBUM': ('TALB', True, ("str")),
            'YEAR': ('TDRC', True, ("str")),
            'TRACK': ('TRCK', True, ("str")),
            'GENRE': ('TCON', True, ("str")),
            'COMMENT': ('TXXX:COMMENT', True, ("str")),
            'ALBUMARTIST': ('TPE2', True, ("str")),
            'COMPOSER': ('TCOM', True, ("str")),
            'DISCNUMBER': ('TPOS', True, ("str")),
            'LYRICS': ('TXXX:LYRICS', True, ("str")),
            'ID3': True
        },
        "FLAC": {
            'TITLE': ('TITLE', True, ("str")),
            'ARTIST': ('ARTIST', True, ("str")),
            'ALBUM': ('ALBUM', True, ("str")),
            'YEAR': ('DATE', True, ("str")),
            'TRACK': ('TRACKNUMBER', True, ("str")),
            'GENRE': ('GENRE', True, ("str")),
            'COMMENT': ('COMMENT', True, ("str")),
            'ALBUMARTIST': ('ALBUMARTIST', True, ("str")),
            'COMPOSER': ('COMPOSER', True, ("str")),
            'DISCNUMBER': ('DISCNUMBER', True, ("str")),
            'LYRICS': ('LYRICS', True, ("str")),
            'ID3': False
        },
        "Vorbis Comment": {
            'TITLE': ('TITLE', True, ("str")),
            'ARTIST': ('ARTIST', True, ("str")),
            'ALBUM': ('ALBUM', True, ("str")),
            'YEAR': ('DATE', True, ("str")),
            'TRACK': ('TRACKNUMBER', True, ("str")),
            'GENRE': ('GENRE', True, ("str")),
            'COMMENT': ('COMMENT', True, ("str")),
            'ALBUMARTIST': ('ALBUMARTIST', True, ("str")),
            'COMPOSER': ('COMPOSER', True, ("str")),
            'DISCNUMBER': ('DISCNUMBER', True, ("str")),
            'LYRICS': ('LYRICS', True, ("str")),
            'ID3': False
        }
    }
    ID3D = {
        'TITLE': TIT2,
        'ARTIST': TPE1,
        'ALBUM': TALB,
        'YEAR': TDRC,
        'TRACK': TRCK,
        'GENRE': TCON,
        'COMMENT': TXXX,
        'ALBUMARTIST': TPE2,
        'COMPOSER': TCOM,
        'DISCNUMBER': TPOS,
        'LYRICS': TXXX
    }

    def __init__(self, path):
        self.Path = path
        self.Audio = mutagen.File(path)
        self.FileType = path[path.rfind(".") + 1:].lower()
        try:
            self.Config = self.Config[self.MAP[self.FileType]]
        except:
            raise ValueError(
                "Filetype " + self.Audio.mime[0].split("/")[1] + " not supported")

    def importID3(self, Type):
        if Type == "wav":
            Type = "wave"
        elif Type == "aif":
            Type = "aiff"
        ID3M = importlib.import_module("mutagen." + Type.lower())
        return getattr(ID3M, Type.upper())

    def __generalgetter__(self, TAG):
        C = self.Config[TAG]
        if self.Config["ID3"]:
            return self.__id3getter__(TAG)
        if isinstance(self.Audio[C[0]], mutagen.id3.TextFrame):
            return self.Audio[C[0]].text
        if C[1] == False or C[1] == True:
            return self.Audio[C[0]]
        else:
            return str(self.Audio[C[0]]).split(C[1])

    def __generalsetter__(self, TAG, Value):
        if self.Config["ID3"]:
            return self.__id3setter__(TAG, Value)
        C = self.Config[TAG]
        if isinstance(Value, list):
            if C[1] == False:
                raise ValueError("List is unacceptable.")
            else:
                for i in Value:
                    if not (type(i).__name__ in C[2]):
                        raise ValueError(
                            type(i).__name__.title() + " is unacceptable.")
        elif type(Value).__name__ in C[2]:
            pass
        else:
            raise ValueError(type(Value).__name__.title() +
                             " is unacceptable.")
        try:
            self.Audio[C[0]] = Value
            self.Audio.save()
        except Exception as e:
            if "TypeError: can't concat str to bytes" in repr(e):
                if isinstance(Value, list):
                    for i in Value:
                        self.Audio[C[0]] = [i.encode() for i in Value]
                        self.Audio.save()
                elif isinstance(Value, str):
                    self.Audio[C[0]] = Value.encode()
                    self.Audio.save()
            elif "not a Frame instance" in repr(e):
                self.Audio[C[0]] = mutagen.id3.TextFrame(
                    encoding=3,
                    text=Value
                )
                self.Audio.save()
            else:
                raise RuntimeError("Unexpected Error")

    def __id3getter__(self, TAG):
        C = self.Config[TAG]
        ID3C = self.importID3(self.FileType)
        ID3 = ID3C(self.Path)
        return ID3[C[0]].text

    def __id3setter__(self, TAG, Value):
        C = self.Config[TAG]
        ID3C = self.importID3(self.FileType)
        ID3 = ID3C(self.Path)
        if TAG == "COMMENT":
            ID3.tags.setall('COMM', [])
            ID3[C[0]] = COMM(
                encoding=3,
                text=Value
            )
        if C[0].startswith("TXXX"):
            ID3.tags.setall(C[0], [])
            ID3[C[0]] = TXXX(
                encoding=3,
                text=Value,
                desc=TAG
            )
        else:
            ID3.tags.setall(C[0], [])
            ID3[C[0]] = self.ID3D[TAG](
                encoding=3,
                text=Value
            )
        ID3.save()

    @property
    def TITLE(self):
        try:
            return self.__generalgetter__("TITLE")
        except:
            return ""

    @TITLE.setter
    def TITLE(self, Value):
        self.__generalsetter__("TITLE", Value)

    @property
    def ALBUM(self):
        try:
            return self.__generalgetter__("ALBUM")
        except:
            return ""

    @ALBUM.setter
    def ALBUM(self, Value):
        self.__generalsetter__("ALBUM", Value)

    @property
    def ARTIST(self):
        try:
            return self.__generalgetter__("ARTIST")
        except:
            return ""

    @ARTIST.setter
    def ARTIST(self, Value):
        self.__generalsetter__("ARTIST", Value)

    @property
    def YEAR(self):
        try:
            return self.__generalgetter__("YEAR")
        except:
            return ""

    @YEAR.setter
    def YEAR(self, Value):
        self.__generalsetter__("YEAR", Value)

    @property
    def TRACK(self):
        try:
            return self.__generalgetter__("TRACK")
        except:
            return ""

    @TRACK.setter
    def TRACK(self, Value):
        self.__generalsetter__("TRACK", Value)

    @property
    def GENRE(self):
        try:
            return self.__generalgetter__("GENRE")
        except:
            return ""

    @GENRE.setter
    def GENRE(self, Value):
        self.__generalsetter__("GENRE", Value)

    @property
    def COMMENT(self):
        try:
            return self.__generalgetter__("COMMENT")
        except:
            return ""

    @COMMENT.setter
    def COMMENT(self, Value):
        self.__generalsetter__("COMMENT", Value)

    @property
    def ALBUMARTIST(self):
        try:
            return self.__generalgetter__("ALBUMARTIST")
        except:
            return ""

    @ALBUMARTIST.setter
    def ALBUMARTIST(self, Value):
        self.__generalsetter__("ALBUMARTIST", Value)

    @property
    def COMPOSER(self):
        try:
            return self.__generalgetter__("COMPOSER")
        except:
            return ""

    @COMPOSER.setter
    def COMPOSER(self, Value):
        self.__generalsetter__("COMPOSER", Value)

    @property
    def DISCNUMBER(self):
        try:
            return self.__generalgetter__("DISCNUMBER")
        except:
            return ""

    @DISCNUMBER.setter
    def DISCNUMBER(self, Value):
        self.__generalsetter__("DISCNUMBER", Value)

    @property
    def LYRICS(self):
        try:
            return self.__generalgetter__("LYRICS")
        except:
            return ""

    @LYRICS.setter
    def LYRICS(self, Value):
        self.__generalsetter__("LYRICS", Value)

    @property
    def DICT(self):
        r = {}
        for i in ['TITLE', 'ARTIST', 'ALBUM', 'YEAR', 'TRACK', 'GENRE', 'COMMENT', 'ALBUMARTIST', 'COMPOSER', 'DISCNUMBER']:
            try:
                r[i] = getattr(self, i)
            except Exception as e:
                pass
        return r

    # @DICT.setter
    # def DICT(self, Value):
    #     for i in Value.keys():
    #         getattr(self, i) = Value[i]


class EAUDIO(AUDIO):
    def __init__(self, path, delimiter, CAPARTIST=False):
        super().__init__(path)
        self.delimiter = delimiter
        self.dir = os.path.dirname(path)
        self.CAPARTIST = CAPARTIST

    def FORMAT(self, ARTIST=True, ALBUMARTIST=True, COMPOSER=True):
        if ARTIST:
            self.ARTIST = self.SEP(self.ARTIST)
        if ALBUMARTIST:
            self.ALBUMARTIST = self.SEP(self.ALBUMARTIST)
        if COMPOSER:
            self.COMPOSER = self.SEP(self.COMPOSER)

    def SEP(self, Values):
        r = Values
        for i in self.delimiter:
            fin = []
            for j in r:
                tmp = list(filter(None, j.split(i)))
                tmp = [i.strip() for i in tmp]
                fin += tmp
            r = fin
        if self.CAPARTIST:
            for i in r:
                i = i.title()
        return r

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
        return super().ARTIST

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
        return super().ALBUMARTIST

    @ALBUMARTIST.setter
    def ALBUMARTIST(self, Value):
        self.__generalsetter__("ALBUMARTIST", Value)

    @property
    def COMPOSER(self):
        return super().COMPOSER

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
    def LYRICS(self):
        return super().LYRICS[0]

    @LYRICS.setter
    def LYRICS(self, Value):
        self.__generalsetter__("LYRICS", Value)

    def ADDLYRICS(self, FO=None, String=None):
        if String:
            pass
        elif FO:
            String = FO.read()
        else:
            raise ValueError("No args are provided to attach lyrics")
        self.LYRICS = String

    @property
    def FileName(self):
        return " - ".join(list(filter(None, [', '.join(self.ARTIST), self.ALBUM, self.TITLE])))
