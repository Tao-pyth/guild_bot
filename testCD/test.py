"""
test.py テスト用　pythonファイル　
2019/08/24
    1. xml使用テスト 2019/08/24
        20190824.xml
    2. __name__の挙動　2019/08/24
"""
#--1--
import xml.etree.ElementTree as ET
import test_fanc as T
import sys
sys.path.append("D:\\_user_template_\\Documents\\PG\\BOT\\guild_bot\\sys_fanc")
import LOG_orig


T.test_time(0)
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

T.test_time(1)
T.name()

T.test_time(2)
LOG = LOG_orig.LOG(__file__)
LOG.msg("本日はお日柄もくよくよ")
LOG.msg("本日はお日柄もくよくよ",2)
LOG.msg("本日はお日柄もくよくよ",3)
LOG.msg("本日はお日柄もくよくよ",6)
