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
## forループ
- 降順 :  
`range(start, end, step)`
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
https://qiita.com/_-_-_-_-_/items/89e966df1c1764f70690  

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
