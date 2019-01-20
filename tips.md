# Tips

## 入力
- 数字  
`x = int(input())`

- スペース挟んで入力  
`x, y, z = input().split()`

- 数値  
`list = list(map(int, input().split()))`  
`x, y, z = map(int, input().split(' '))`

- 改行ありの入力  
`[input for _ in range(n)]`

### 標準入力について
- `input()`より`sys.stdin.readline()`の方が10倍以上速いそう
    - https://www.kumilog.net/entry/python-speed-comp  

```
import sys
input = sys.stdin.readline
x = int(input())
```

## 出力
-  スペース挟んで出力  
``" ".join([Array])``

- 改行なしの出力  
`print("hello", end="")`  
`p = sys.stdout.write` `p(***)`

- p = sys.stdout.write  
`p("HELLO")`

## 数字
- 無限大
    - float型の無限大  
    `float('inf')`  
    `sys.maxsize`
    - Python3は，int型に上限はない

## 三項演算子
- `(変数) = (条件がTrueのときの値) if (条件) else (条件がFalseのときの値)`

## forループ
- 降順 :  
`range(start, end, step)`

## 配列
- n個の要素を持つ配列がほしいとき  
`[0 for i in range(n)]`

- 長さ  
`len(list)`

- インデクスをゲットする  
`list.index(x)`

## コピー
- オブジェクトのコピー（☓参照）  
`from copy import deepcopy`  
`from copy import copy`

## 判定
- 変数が数字かどうか判定  
`isdigit()`

## データ構造
- スタック  
https://github.com/maro525/aizu-online-judge/blob/master/alds1_3_b.py

- 連結リスト  
http://www.geocities.jp/m_hiroi/light/python05.html#chap11

- 配列によるリングバッファ  
https://github.com/maro525/aizu-online-judge/blob/master/alds1_3_b.py

## アルゴリズム
- 速い線形探索   
https://scrapbox.io/tech-hdmr/%E7%B7%9A%E5%BD%A2%E6%8E%A2%E7%B4%A2  
https://github.com/maro525/aizu-online-judge/blob/master/alds1_4_a.py

- 二分探索
https://github.com/maro525/aizu-online-judge/blob/master/alds1_4_b.py  
    - 二分探索する公式のPythonライブラリ  
https://qiita.com/_-_-_-_-_/items/89e966df1c1764f70690  

- 分割統治法
    - 最大値問題  
    https://scrapbox.io/tech-hdmr/%E5%88%86%E5%89%B2%E7%B5%B1%E6%B2%BB%E6%B3%95%E3%81%A7%E6%9C%80%E5%A4%A7%E5%80%A4%E5%95%8F%E9%A1%8C%E3%82%92%E8%A7%A3%E3%81%8F%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0

## ソート
### Python標準
- `sorted(list)`
- `list.sort()`
- 降順のソート  
`sorted(list, reverse=True)`

### ソートアルゴリズム
- マージソート  
https://github.com/maro525/aizu-online-judge/blob/master/alds1_5_b.py
- 計数ソート
https://github.com/maro525/aizu-online-judge/blob/master/alds1_6_a.py
- バブルソート
- クイックソート  
https://github.com/maro525/aizu-online-judge/blob/master/alds1_6_c.py


## 参考
- 【Pythonチュートリアル】データ構造 - Qiita  
https://qiita.com/Tocyuki/items/c45dda6007bfb7e9292f
- アルゴリズムとデータ構造 - Qiita  
https://qiita.com/cabernet_rock/items/cdd12b07d213b67d0530
- Python 競技プログラミング　チートシート自分用 - Qiita  
https://qiita.com/hasekura/items/65d5eb18e9b6f50b6d19
- 競技プログラミングを Python 3 で解く - Qiita  
https://qiita.com/skcvim/items/9eed47f5483679fa66b1
- Pythonで使う競技プログラミング用チートシート - Qiita  
https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
- トップページ | Programming Place Plus　アルゴリズムとデータ構造編  
https://programming-place.net/ProgrammingPlacePlus/algorithm/index.html
