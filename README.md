# MusicPowerTools
|Symbol|Statement|
|---|---|
|:x:|Not Supported But On List|
|🔘|Not Fully Supported / Testing|
|:white_check_mark:|Supported|

## Install dependencies
`pip3 install mutagen`

## FileType Support
|Filetype|music-tag|Mp3tag|MusicPowerToys|
|---|---|---|---|
|aac (ID3 Variant)|:white_check_mark:|:white_check_mark:|🔘|
|aif / aiff (ID3 Variant)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|dsf (ID3 Variant)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|flac (FLAC)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|m4a (MP4)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|mp3 (ID3)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|ogg (Vorbis Comment)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|opus (Vorbis Comment)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|wav (ID3 Variant)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|wv (APEv2)|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|mp4 (MP4)|:x:|:white_check_mark:|:white_check_mark:|
|m4b (MP4)|:x:|:white_check_mark:|:white_check_mark:|
|m4v (MP4)|:x:|:white_check_mark:|:white_check_mark:|
|mpc (APEv2)|:x:|:white_check_mark:|:white_check_mark:|
|ape (APEv2)|:x:|:white_check_mark:|:white_check_mark:|

## Tags Support
|FileType|TITLE|ALBUM|ARTIST|YEAR|TRACK|GENRE|COMMENT|ALBUMARTIST|COMPOSER|DISCNUMBER|LYRICS|
|---|---|---|---|---|---|---|---|---|---|---|---|
|aac|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|
|aif|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|aif / aiff|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|dsf|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|flac|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|m4a|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|mp3|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|ogg|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|opus|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|wav|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|wv|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|mp4|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|m4b|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|m4v|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|mpc|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|ape|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|

## Class
`class AUDIO`  
Directly access audio files.
```Python
au = AUDIO(Path) #Instantiation
au.ARTIST = ["A", "B"] #Modify tag values Directly with a list, string, and int
print(au.TITLE)
```

<!-- `class EAUDIO`  
Subclass of `AUDIO` -->