"""
test.py テスト用　pythonファイル　
2019/08/24
    1. xml使用テスト 2019/08/24
        20190824.xml
"""
#--1--
import xml.etree.ElementTree as ET


#--1--
"""
ET.fromstring   <- XML形式のデータの読み込み関数
ET.parse        <- XMLファイルを解析
tree.getroot()  <- XMLファイルを配列として取得
"""
#  root = ET.fromstring(sports_xml)
test1_pass = "D:\\_user_template_\\Documents\\PG\\BOT\\guild_bot\\testCD\\test資産\\20190824.xml"
tree = ET.parse(test1_pass)
print(tree.getroot())   #オブジェクト形式を参照
root = tree.getroot()
for name in root.iter('name'):
    print(name.text)
print(root[0].text)
print(root[1].attrib)
