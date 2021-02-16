# King Gnu news getter
---

これは、[公式サイト](https://kinggnu.jp/news)からKing Gnu の ニュースを取得して一覧表示するプログラムです。
King Gnu について ⇒ [https://kinggnu.jp/](https://kinggnu.jp/)

## Requirements
<li>Python 3</li>
<li>requests</li>
<li>colorama</li>
<li>termcolor</li>

## Usage

```shell
$ git clone https://github.com/atoy322/GnuNews.git
cd GnuNews
```

in terminal
```shell
$ python3 gnu.py
~ List of news ~
```

in python interpreter or .py file
```python
>>> from gnu import GetNews
>>> GetNews()  # return list of news.
```

## License
##### MIT License