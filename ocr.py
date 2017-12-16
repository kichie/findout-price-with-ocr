from PIL import Image
import sys
import matplotlib.pyplot as plt


import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools)==0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

#使用するOCRツールの名前が出る、買いたい場合は一個前の参照先を変えること
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages() #使用できる言語の確認
print("Available langages: %s" % ",".join(langs))

lang = langs[2]
print("Will use lang '%s'" % (lang))#使用する言語について

img = Image.open("testdata/itoh.jpg")
gray = img.convert("L")                     # グレイスケールに変換
gray = gray.point(lambda x: 0 if x < 200 else x)   # 値が230以下は0になる
# gray.show()


txt = tool.image_to_string(#ここでOCRの対象や言語、オプションを指定する
    gray,
    lang='jpn',
    builder=pyocr.builders.TextBuilder()
    )
print(txt)
