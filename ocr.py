from PIL import Image
import sys

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


txt = tool.image_to_string(#ここでOCRの対象や言語、オプションを指定する
    Image.open("testdata/itoh.jpg"),
    lang='jpn',
    builder=pyocr.builders.TextBuilder()
    )
print(txt)
