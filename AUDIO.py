import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3


class AUDIO:
    # 原生列表：True
    # 字符串分割：字符
    # 不支持：False
    Config = {
        "ape": {
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
            'ID3': False
        },
        "wv": {
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
            'ID3': False
        },
        "mpc": {
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
            'ID3': False
        },
        "m4a": {
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
            'ID3': False
        },
        "m4b": {
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
            'ID3': False
        },
        "m4v": {
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
            'ID3': False
        },
        "mp4": {
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
            'ID3': False
        },
        "mp3": {
            'TITLE': ('title', True, ("str")),
            'ARTIST': ('artist', True, ("str")),
            'ALBUM': ('album', True, ("str")),
            'YEAR': ('date', True, ("str")),
            'TRACK': ('tracknumber', True, ("str")),
            'GENRE': ('genre', True, ("str")),
            # 'COMMENT': ('comment', True, ("str")),
            'ALBUMARTIST': ('albumartist', True, ("str")),
            'COMPOSER': ('composer', True, ("str")),
            'DISCNUMBER': ('discnumber', True, ("str")),
            'ID3': True
        },
        "dsf": {
            'TITLE': ('TIT2', True, ("str")),
            'ARTIST': ('TPE1', True, ("str")),
            'ALBUM': ('TALB', True, ("str")),
            'YEAR': ('TDRC', True, ("str")),
            'TRACK': ('TRCK', True, ("str")),
            'GENRE': ('TCON', True, ("str")),
            'COMMENT': ('COMM', True, ("str")),
            'ALBUMARTIST': ('TPE2', True, ("str")),
            'COMPOSER': ('TCOM', True, ("str")),
            'DISCNUMBER': ('TPOS', True, ("str")),
            'ID3': False
        },
        "wav": {
            'TITLE': ('TIT2', True, ("str")),
            'ARTIST': ('TPE1', True, ("str")),
            'ALBUM': ('TALB', True, ("str")),
            'YEAR': ('TDRC', True, ("str")),
            'TRACK': ('TRCK', True, ("str")),
            'GENRE': ('TCON', True, ("str")),
            # 'COMMENT': ('COMM', True, ("str")),
            'ALBUMARTIST': ('TPE2', True, ("str")),
            'COMPOSER': ('TCOM', True, ("str")),
            'DISCNUMBER': ('TPOS', True, ("str")),
            'ID3': False
        },
        "aiff": {
            'TITLE': ('TIT2', True, ("str")),
            'ARTIST': ('TPE1', True, ("str")),
            'ALBUM': ('TALB', True, ("str")),
            'YEAR': ('TDRC', True, ("str")),
            'TRACK': ('TRCK', True, ("str")),
            'GENRE': ('TCON', True, ("str")),
            # 'COMMENT': ('COMM', True, ("str")),
            'ALBUMARTIST': ('TPE2', True, ("str")),
            'COMPOSER': ('TCOM', True, ("str")),
            'DISCNUMBER': ('TPOS', True, ("str")),
            'ID3': False
        },
        "aif": {
            'TITLE': ('title', True, ("str")),
            'ARTIST': ('artist', True, ("str")),
            'ALBUM': ('album', True, ("str")),
            'YEAR': ('date', True, ("str")),
            'TRACK': ('tracknumber', True, ("str")),
            'GENRE': ('genre', True, ("str")),
            # 'COMMENT': ('comment', True, ("str")),
            'ALBUMARTIST': ('albumartist', True, ("str")),
            'COMPOSER': ('composer', True, ("str")),
            'DISCNUMBER': ('discnumber', True, ("str")),
            'ID3': False
        },
        "flac": {
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
            'ID3': False
        },
        "opus": {
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
            'ID3': False
        },
        "ogg": {
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
            'ID3': False
        }
    }

    def __init__(self, path):
        self.Path = path
        self.Audio = mutagen.File(path)
        try:
            self.Config = self.Config[path[path.rfind(".") + 1:].lower()]
        except:
            raise ValueError(
                "Filetype " + self.Audio.mime[0].split("/")[1] + " not supported")

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
        EI = EasyID3(self.Path)
        C = self.Config[TAG]
        return EI[C[0]]

    def __id3setter__(self, TAG, Value):
        if not TAG == "COMMENT":
            EI = EasyID3(self.Path)
            C = self.Config[TAG]
            EI[C[0]] = Value
            EI.save()

    @property
    def TITLE(self):
        try:
            return self.__generalgetter__("TITLE")
        except:
            return None

    @TITLE.setter
    def TITLE(self, Value):
        self.__generalsetter__("TITLE", Value)

    @property
    def ALBUM(self):
        try:
            return self.__generalgetter__("ALBUM")
        except:
            return None

    @ALBUM.setter
    def TITLE(self, Value):
        self.__generalsetter__("ALBUM", Value)

    @property
    def ARTIST(self):
        try:
            return self.__generalgetter__("ARTIST")
        except:
            return None

    @ARTIST.setter
    def ARTIST(self, Value):
        self.__generalsetter__("ARTIST", Value)

    @property
    def YEAR(self):
        try:
            return self.__generalgetter__("YEAR")
        except:
            return None

    @YEAR.setter
    def YEAR(self, Value):
        self.__generalsetter__("YEAR", Value)

    @property
    def TRACK(self):
        try:
            return self.__generalgetter__("TRACK")
        except:
            return None

    @TRACK.setter
    def TRACK(self, Value):
        self.__generalsetter__("TRACK", Value)

    @property
    def GENRE(self):
        try:
            return self.__generalgetter__("GENRE")
        except:
            return None

    @GENRE.setter
    def GENRE(self, Value):
        self.__generalsetter__("GENRE", Value)

    @property
    def COMMENT(self):
        try:
            return self.__generalgetter__("COMMENT")
        except:
            return None

    @COMMENT.setter
    def COMMENT(self, Value):
        self.__generalsetter__("COMMENT", Value)

    @property
    def ALBUMARTIST(self):
        try:
            return self.__generalgetter__("ALBUMARTIST")
        except:
            return None

    @ALBUMARTIST.setter
    def ALBUMARTIST(self, Value):
        self.__generalsetter__("ALBUMARTIST", Value)

    @property
    def COMPOSER(self):
        try:
            return self.__generalgetter__("COMPOSER")
        except:
            return None

    @COMPOSER.setter
    def COMPOSER(self, Value):
        self.__generalsetter__("COMPOSER", Value)

    @property
    def DISCNUMBER(self):
        try:
            return self.__generalgetter__("DISCNUMBER")
        except:
            return None

    @DISCNUMBER.setter
    def DISCNUMBER(self, Value):
        self.__generalsetter__("DISCNUMBER", Value)

    @property
    def DICT(self):
        r = {}
        for i in ['TITLE','ARTIST','ALBUM','YEAR','TRACK','GENRE','COMMENT','ALBUMARTIST','COMPOSER','DISCNUMBER']:
            try:
                r[i]=getattr(self,i)
            except Exception as e:
                pass
        return r
