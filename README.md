# 概要
OCR機能を利用し、広告から値段と商品名を取り出す。

1. tesseractのインストール
2. 日本語辞書の追加
3. pyocrインストール
4. 使い方

## tesseractのインストール
`brew install tesseract`

## 日本語辞書の追加
`curl -L -o /usr/local/share/tessdata/jpn.traineddata 'https://github.com/tesseract-ocr/tessdata/raw/master/jpn.traineddata'`

## pyocrインストール
`pip install pyocr`

## pyocrの使い方
1. https://github.com/openpaperwork/pyocr
2. http://teru0rc4.hatenablog.com/entry/2017/08/09/230046
上記二つのサイトが非常にわかりやすいです。

## 参考
- http://teru0rc4.hatenablog.com/entry/2017/08/09/230046
- http://nfnoface.hatenablog.com/entry/2016/11/06/115000
- https://github.com/openpaperwork/pyocr

## 問題点
- まだ精度が悪い(入力がtestdata/itoh.png)
- 数値が読み込まれていない
- 余分な文字列も出力される
- 画質の悪い画像(testdata/seiyu.png)では出力がなくなる

## 今後
- 文字を正確に読み込むこと(testdata/itoh.jpg)
- 数値が読み込むこと
- 画質の悪い画像(testdata/seiyu.png)から情報を取得する
- 大きな画像から商品ごとに切り抜き
