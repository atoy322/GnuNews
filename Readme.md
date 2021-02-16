# King Gnu news getter
---

これは、[公式サイト](https://kinggnu.jp/news)からKing Gnu の ニュースを取得して一覧表示するプログラムです。

## Requirements
<li>Python 3</li>
<li>requests</li>
<li>colorama</li>

## Usage

```shell
$ git clone https://github.com/atoy322/GnuNews.git
cd GnuNews
```

### in terminal
```shell
$ python3 gnu.py
~ List of news ~
```

##### Screenshot
![screenshot](./screenshot/img.png)

### in python interpreter or .py file
```python
>>> from gnu import GetNews
>>> GetNews()  # return list of news.
```


## License
##### MIT License