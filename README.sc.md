# MusicPowerTools
## 一个简易的音频元数据编辑器。
* **支持 9 种（共 10 种）[music-tag](https://github.com/KristoforMaynard/music-tag) 支持的格式！**
* **支持 15 种（共 28 种）[Mp3tag](https://www.mp3tag.de) 支持的格式！**
* **基于 [mutagen](https://github.com/quodlibet/mutagen) 开发。**

[English](https://github.com/hexin-lin-1024/MusicPowerToys/blob/main/README.md) | [简体中文](https://github.com/hexin-lin-1024/MusicPowerToys/blob/main/README.sc.md)
## 安装依赖
`pip3 install mutagen`

## 支持的文件格式
|符号|说明|
|---|---|
|:x:|不支持但在计划清单上|
|🔘|尚未完全支持 / 测试中|
|:white_check_mark:|支持|

|文件格式|music-tag|Mp3tag|MusicPowerToys|
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

## 支持的标签
|符号|说明|
|---|---|
|:x:|不支持但在计划清单上|
|🔘|尚未完全支持 / 测试中|
|:white_check_mark:|支持|

|标签格式|TITLE|ALBUM|ARTIST|YEAR|TRACK|GENRE|COMMENT|ALBUMARTIST|COMPOSER|DISCNUMBER|LYRICS|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID3 / ID3 Variant|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|🔘|
|APEv2|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|Vorbis Comment|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|FLAC|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|

* 支持列表的标签

|符号|说明|
|---|---|
|:x:|不支持|
|🔘|非原生支持 / 开发中|
|:white_check_mark:|支持|

|元数据类型|TITLE|ALBUM|ARTIST|YEAR|TRACK|GENRE|COMMENT|ALBUMARTIST|COMPOSER|DISCNUMBER|LYRICS|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID3 / ID3 Variant|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|🔘|
|APEv2|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|🔘|
|Vorbis Comment|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|FLAC|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|

# 文档
## AUDIO.py
### `class AUDIO`
* 每个在上述表格中提到的标签都是 `AUDIO` 类可写的属性。
* 修改这些属性即可修改元数据的值。

构造方法
|参数|功能|
|---|---|
|path|指定路径|

使用例:
```Python
au = AUDIO(path) #实例化
au.ARTIST = ["A", "B"] #使用整形、字符串或者列表修改标签
print(au.TITLE)
```

### `class EAUDIO`
* `EAUDIO` 是 `AUDIO` 的一个子类。

构造方法
|参数|功能|
|---|---|
|path|指定路径|
|delimiter（接受列表）|一个会在 `FORMAT()` 函数中使用的分隔符列表|
|CAPARTIST = True（默认值）|决定是否在 `FORMAT()` 函数中将每个艺术家的名称标题化（大写每个单词的首字母）|

`EAUDIO` 几乎与 `AUDIO` 类相同，但是 `EAUDIO` 提供更多接口并且添加了一些属性类型的限制。  
 `EAUDIO` 中仅三个属性接受列表：

|接受列表的标签类型|
|---|
|ARTIST|
|ALBUMARTIST|
|COMPOSER|

如果不支持列表的标签类型被赋列表类型的值，程序将抛出 `ValueError()` 异常。

此外，`EAUDIO` 类提供额外接口。

|接口|参数|功能|
|---|---|---|
|FORMAT|ARTIST = True（默认值，程序会尝试处理 ARTIST 标签字段），ALBUMARTIST = True，COMPOSER = True|自动分割用连接符连接的 ARTIST 字段|
|ADDLYRICS|FO（接受类文件对象）或 String（接受字符串）|为音频添加歌词|
