# Tips

## 入力
- 数字
`x = int(input())`
- スペース挟んで入力
`x, y, z = input().split()`
- 数値
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

## forループ

- 降順 :
`range(start, end, step)``

## コピー

- オブジェクトのコピー（☓参照）
`from copy import deepcopy`
`from copy import copy`

## 判定

- 変数が数字かどうか判定
`isdigit()`
