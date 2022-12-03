# MusicPowerTools
## Simple interface to edit audio file metadata.
* **We now support 9 of 10 formats that music-tag supports!**
* **We now support 15 of 28 formats that Mp3tag supports!**
* **Based on [mutagen](https://github.com/quodlibet/mutagen).**

## Install dependencies
`pip3 install mutagen`

## File Type Support
|Symbol|Statement|
|---|---|
|:x:|Not Supported But On List|
|🔘|Not Fully Supported / Testing|
|:white_check_mark:|Supported|

|File Type|music-tag|Mp3tag|MusicPowerToys|
|---|---|---|---|
|aac (ID3 Variant)|:white_check_mark:|:white_check_mark:|:x:|
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
|Symbol|Statement|
|---|---|
|:x:|Not Supported But On List|
|🔘|Not Fully Supported / Testing|
|:white_check_mark:|Supported|

|Metadata Type|TITLE|ALBUM|ARTIST|YEAR|TRACK|GENRE|COMMENT|ALBUMARTIST|COMPOSER|DISCNUMBER|LYRICS|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID3 / ID3 Variant|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|🔘|
|APEv2|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|Vorbis Comment|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|FLAC|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|

* List Type Support

|Symbol|Statement|
|---|---|
|:x:|Not Supported|
|🔘|Not Originally Supported / Developing|
|:white_check_mark:|Supported|

|Metadata Type|TITLE|ALBUM|ARTIST|YEAR|TRACK|GENRE|COMMENT|ALBUMARTIST|COMPOSER|DISCNUMBER|LYRICS|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID3 / ID3 Variant|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|🔘|
|APEv2|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|
|Vorbis Comment|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|FLAC|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|

# Document
## AUDIO.py
### `class AUDIO`
* Each tag mentioned above in the table is a modifiable property of `AUDIO`.
* You can modify these tags simply by modifying the value of these properties.

Construction method
|Args|Function|
|---|---|
|path|Specify the path|

Usage:
```Python
au = AUDIO(path) #Instantiation
au.ARTIST = ["A", "B"] #Modify tag values Directly with a list, string, or int
print(au.TITLE)
```

### `class EAUDIO`
* `EAUDIO` is a subclass of `AUDIO`.

Construction method
|Args|Function|
|---|---|
|path|Specify the path|
|delimiter (Accept a list)|A list that contains delimiters used in `FORMAT()` function|
|CAPARTIST = True (Default)|Determines whether to title each artist name in `FORMAT()` function|

`EAUDIO` is almost the same as `AUDIO` class, but `EAUDIO` class offer more APIs and has added some restriction to tag values.  
Only three tag types supports list in `EAUDIO`: 

|Tag Types accept a list|
|---|
|ARTIST|
|ALBUMARTIST|
|COMPOSER|

If non-list-supported tag types are assigned with list type values, a `ValueError()` exception will be raised.

Besides, `EAUDIO` class also provides additional APIs.

|APIs|Args|Function|
|---|---|---|
|FORMAT|ARTIST = True (Default, which means the program will try to process the ARTIST Tag Field), ALBUMARTIST = True, COMPOSER = True|Automatically split artist fields joined with a joiner into a list|
|ADDLYRICS|FO(Accepts file-like object) or String(Accepts a string)|Add lyrics to audio|