import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《左传》庄公二十二年陈侯筮敬仲，宋刊注疏第五册第25–28页记观之否、六四变；爻值依原卦和动爻换算 https://upload.wikimedia.org/wikipedia/commons/a/a9/NLC892-412004000069-405179_附釋音春秋左傳注疏_六十卷_劉叔剛宋刻本_第5冊.pdf#page=25

    def test_陈侯筮敬仲(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 6 7 7\n\n")
        self.assertIn("主卦：䷓ 风地观", 输出)
        self.assertIn("变卦：䷋ 天地否", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《左传》闵公元年毕万筮仕于晋，宋刊注疏第六册第4–5页记屯之比、初九变；爻值依原卦和动爻换算 https://upload.wikimedia.org/wikipedia/commons/0/0b/NLC892-412004000069-405185_附釋音春秋左傳注疏_六十卷_劉叔剛宋刻本_第6冊.pdf#page=4

    def test_毕万筮仕于晋(self):
        输出 = 运行("六爻纳甲.py", "9 8 8 8 7 8\n\n")
        self.assertIn("主卦：䷂ 水雷屯", 输出)
        self.assertIn("变卦：䷇ 水地比", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《周易筮述》卷八京都1793本第263幅，英宗北狩问筮得乾之复，独初爻不变；爻值依原卦和动爻换算 http://kanji.zinbun.kyoto-u.ac.jp/db-machine/toho/L/A0290263.jpg

    def test_英宗北狩问筮(self):
        输出 = 运行("六爻纳甲.py", "7 9 9 9 9 9\n\n")
        self.assertIn("主卦：䷀ 乾为天", 输出)
        self.assertIn("变卦：䷗ 地雷复", 输出)
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上", "五", "四", "三", "二"])
        self.assertNotIn("×", 输出)

    # 《周易筮述》卷八第264幅原记元仁宗筮遇乾三爻变之睽，乾至睽实际第三、第五两爻变化 http://kanji.zinbun.kyoto-u.ac.jp/db-machine/toho/L/A0290264.jpg

    # 《周易筮述》卷八京都1793本第264幅，托赵辅和筮父病遇乾四爻变之晋；爻值依原卦和动爻换算 http://kanji.zinbun.kyoto-u.ac.jp/db-machine/toho/L/A0290264.jpg

    def test_赵辅和代占父病(self):
        输出 = 运行("六爻纳甲.py", "9 9 9 7 9 7\n\n")
        self.assertIn("主卦：䷀ 乾为天", 输出)
        self.assertIn("变卦：䷢ 火地晋", 输出)
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五", "三", "二", "初"])
        self.assertNotIn("×", 输出)

    # 《高島易斷》1901增补本下经贞原影第7幅，缙绅某占气运得革之夬、六二；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/7

    def test_高岛占缙绅气运六二(self):
        输出 = 运行("六爻纳甲.py", "7 6 7 7 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 输出)
        self.assertIn("变卦：䷪ 泽天夬", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第8幅，友人某占气运得革之既济、九四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/8

    def test_高岛占友人气运九四(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 9 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 输出)
        self.assertIn("变卦：䷾ 水火既济", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第9幅，明治28年2月5日占北洋舰队得革之既济、九四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/9

    def test_高岛占北洋舰队(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 9 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 输出)
        self.assertIn("变卦：䷾ 水火既济", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第10幅，某诸侯派庶子问国政得革之丰、九五；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/10

    def test_高岛占诸侯国政(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 7 9 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 输出)
        self.assertIn("变卦：䷶ 雷火丰", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第11幅，缙绅某占气运得革之同人、上六；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/11

    def test_高岛占缙绅气运上六(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 7 7 6\n\n")
        self.assertIn("主卦：䷰ 泽火革", 输出)
        self.assertIn("变卦：䷌ 天火同人", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第15幅（原叶14），缙绅占夫人病得鼎之大有，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/15

    def test_高岛缙绅占夫人病(self):
        输出 = 运行("六爻纳甲.py", "6 7 7 7 8 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷍ 火天大有", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第16幅（原叶15），明治十三年占大阪两氏被疑拘留得鼎之旅，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/16

    def test_高岛明治十三年占大阪两氏被疑拘留(self):
        输出 = 运行("六爻纳甲.py", "8 9 7 7 8 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷷ 火山旅", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第16幅（原叶15），友人占说亲女子姿容得鼎之旅，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/16

    def test_高岛友人占说亲女子姿容(self):
        输出 = 运行("六爻纳甲.py", "8 9 7 7 8 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷷ 火山旅", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第17幅（原叶16），明治三十一年占英德交际得鼎之旅，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/17

    def test_高岛明治三十一年占英德交际(self):
        输出 = 运行("六爻纳甲.py", "8 9 7 7 8 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷷ 火山旅", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第18幅（原叶17），明治二十年占某公朝运得鼎之未济，原文明确引九三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/18

    def test_高岛明治二十年占某公朝运(self):
        输出 = 运行("六爻纳甲.py", "8 7 9 7 8 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷿ 火水未济", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第19幅（原叶18），明治十五年七月占朝鲜内变仅记筮得鼎之象及九四论，未明确本次动爻和变卦，不能确定完整六爻输入。 https://dl.ndl.go.jp/pid/760555/1/19

    # 《高島易斷》1901增补本下经贞原影第20幅（原叶19），商人占气运得鼎之姤，原文明确引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/20

    def test_高岛商人占气运(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 7 6 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷫ 天风姤", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第20幅（原叶19），明治三十一年占改进党气运得鼎之姤，原文明确引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/20

    def test_高岛明治三十一年占改进党气运(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 7 6 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷫ 天风姤", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第21幅（原叶20），缙绅占气运上九得鼎之恒，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/21

    def test_高岛缙绅占气运上九(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 7 8 9\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 输出)
        self.assertIn("变卦：䷟ 雷风恒", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第25幅（原叶24），友人占气运初九得震之豫，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/25

    def test_高岛友人占气运初九(self):
        输出 = 运行("六爻纳甲.py", "9 8 8 7 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第25幅（原叶24），占米价初九得震之豫，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/25

    def test_高岛占米价初九(self):
        输出 = 运行("六爻纳甲.py", "9 8 8 7 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第26幅（原叶25），金田孝占运气得震之归妹，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/26

    def test_高岛金田孝占运气(self):
        输出 = 运行("六爻纳甲.py", "7 6 8 7 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷵ 雷泽归妹", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第26幅（原叶25），华族隐居君占切要之事得震之归妹，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/26

    def test_高岛华族隐居君占切要之事(self):
        输出 = 运行("六爻纳甲.py", "7 6 8 7 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷵ 雷泽归妹", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第27幅（原叶26），明治二十五年占制造社运得震之丰，原文明确引六三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/27

    def test_高岛明治二十五年占制造社运(self):
        输出 = 运行("六爻纳甲.py", "7 8 6 7 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷶ 雷火丰", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第28幅（原叶27），友人占气运九四得震之复，原文明确引九四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/28

    def test_高岛友人占气运九四(self):
        输出 = 运行("六爻纳甲.py", "7 8 8 9 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷗ 地雷复", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第29幅（原叶28），友人占气运六五得震之随，原文明确引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/29

    def test_高岛友人占气运六五(self):
        输出 = 运行("六爻纳甲.py", "7 8 8 7 6 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷐ 泽雷随", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第30幅（原叶29），明治十八年占亲妹行踪得震之噬嗑，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/30

    def test_高岛明治十八年占亲妹行踪(self):
        输出 = 运行("六爻纳甲.py", "7 8 8 7 8 6\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷔ 火雷噬嗑", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第30幅（原叶29），明治二十八年占我国与朝鲜交际得震之噬嗑，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/30

    def test_高岛明治二十八年占我国与朝鲜交际(self):
        输出 = 运行("六爻纳甲.py", "7 8 8 7 8 6\n\n")
        self.assertIn("主卦：䷲ 震为雷", 输出)
        self.assertIn("变卦：䷔ 火雷噬嗑", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第34幅（原叶33），明治二十四年占某大臣气运得艮之贲，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/34

    def test_高岛明治二十四年占某大臣气运(self):
        输出 = 运行("六爻纳甲.py", "6 8 7 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertIn("变卦：䷕ 山火贲", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第35幅（原叶34），石坂占矿山得艮之蛊，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/35

    def test_高岛石坂占矿山(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertIn("变卦：䷑ 山风蛊", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第35–36幅（原叶34–35），明治二十七年冬至占战后形势得艮之蛊，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/35

    def test_高岛明治二十七年冬至占战后形势(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertIn("变卦：䷑ 山风蛊", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第37幅（原叶36），占某贵显气运九三得艮之剥，原文明确引九三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/37

    def test_高岛占某贵显气运九三(self):
        输出 = 运行("六爻纳甲.py", "8 8 9 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertIn("变卦：䷖ 山地剥", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第37幅（原叶36），明治二十年占某贵显气运得艮之旅，原文明确引六四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/37

    def test_高岛明治二十年占某贵显气运(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 6 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertIn("变卦：䷷ 火山旅", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第38幅（原叶37），明治二十三年十二月占众议院回述得艮之渐，回述只载本卦和变卦，六五仅由两卦唯一反推，未载本次明确动爻，保留完整注释测试；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/38

    # def test_高岛明治二十三年十二月占众议院回述(self):
    #     输出 = 运行("六爻纳甲.py", "8 8 7 8 6 7\n\n")
    #     self.assertIn("主卦：䷳ 艮为山", 输出)
    #     self.assertIn("变卦：䷴ 风山渐", 输出)
    #     self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
    #     self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第38–39幅（原叶37–38），明治二十四年十一月占众议院得艮五爻；本次未记变卦名，只核本卦和原载动爻，原文明确“得艮五爻”并引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/38

    def test_高岛明治二十四年十一月占众议院(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 8 6 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第39幅（原叶38），明治二十七年三月占某贵显气运得艮之谦，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/39

    def test_高岛明治二十七年三月占某贵显气运(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 8 8 9\n\n")
        self.assertIn("主卦：䷳ 艮为山", 输出)
        self.assertIn("变卦：䷎ 地山谦", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第43幅（原叶42），友人占事业成否得渐之家人，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/43

    def test_高岛友人占事业成否(self):
        输出 = 运行("六爻纳甲.py", "6 8 7 8 7 7\n\n")
        self.assertIn("主卦：䷴ 风山渐", 输出)
        self.assertIn("变卦：䷤ 风火家人", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第44幅（原叶43），明治十三年占某贵显气运得渐之巽，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/44

    def test_高岛明治十三年占某贵显气运(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 8 7 7\n\n")
        self.assertIn("主卦：䷴ 风山渐", 输出)
        self.assertIn("变卦：䷸ 巽为风", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第44幅（原叶43），明治三十二年占北海道厅气运得渐之巽，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/44

    def test_高岛明治三十二年占北海道厅气运(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 8 7 7\n\n")
        self.assertIn("主卦：䷴ 风山渐", 输出)
        self.assertIn("变卦：䷸ 巽为风", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第45幅（原叶44），自占气运艮之渐回述得艮之渐，回述只载本卦和变卦，六五仅由两卦唯一反推，未载本次明确动爻，保留完整注释测试；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/45

    # def test_高岛自占气运艮之渐回述(self):
    #     输出 = 运行("六爻纳甲.py", "8 8 7 8 6 7\n\n")
    #     self.assertIn("主卦：䷳ 艮为山", 输出)
    #     self.assertIn("变卦：䷴ 风山渐", 输出)
    #     self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
    #     self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第45幅（原叶44），狱中自占罪案得渐之观，原文明确引九三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/45

    def test_高岛狱中自占罪案(self):
        输出 = 运行("六爻纳甲.py", "8 8 9 8 7 7\n\n")
        self.assertIn("主卦：䷴ 风山渐", 输出)
        self.assertIn("变卦：䷓ 风地观", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第46幅（原叶45），原大垣藩主户田太君病仅载筮得渐及归魂、三年推期，未载实际动爻或变卦；“自四至上三爻”用于推年数，不能据此确定六爻输入。 https://dl.ndl.go.jp/pid/760555/1/46

    # 《高島易斷》1901增补本下经贞原影第47幅（原叶46），商人占气运九五得渐之艮，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/47

    def test_高岛商人占气运九五(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 8 9 7\n\n")
        self.assertIn("主卦：䷴ 风山渐", 输出)
        self.assertIn("变卦：䷳ 艮为山", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第47–48幅（原叶46–47），明治十九年尾藤占气运得渐之蹇，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/47

    def test_高岛明治十九年尾藤占气运(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 8 7 9\n\n")
        self.assertIn("主卦：䷴ 风山渐", 输出)
        self.assertIn("变卦：䷦ 水山蹇", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第51幅（原叶50），明治十六年藤野正启占运气得归妹之解，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/51

    def test_高岛明治十六年藤野正启占运气(self):
        输出 = 运行("六爻纳甲.py", "9 7 8 7 8 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第51幅（原叶50），某官员占气运初九得归妹之解，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/51

    def test_高岛某官员占气运初九(self):
        输出 = 运行("六爻纳甲.py", "9 7 8 7 8 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第52幅（原叶51），华族占潮花寿命得归妹之震，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/52

    def test_高岛华族占潮花寿命(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 7 8 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第52幅（原叶51），明治三十一年占台湾总督府气运得归妹之震，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/52

    def test_高岛明治三十一年占台湾总督府气运(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 7 8 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第53幅（原叶52），某县人占求官成否得归妹之大壮，原文明确引六三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/53

    def test_高岛某县人占求官成否(self):
        输出 = 运行("六爻纳甲.py", "7 7 6 7 8 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷡ 雷天大壮", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第54幅（原叶53），商人占货物卖买时机得归妹之临，原文明确引九四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/54

    def test_高岛商人占货物卖买时机(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 9 8 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷒ 地泽临", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第55幅（原叶54），友人占某氏赴任得归妹之兑，原文明确引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/55

    def test_高岛友人占某氏赴任(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 7 6 8\n\n")
        self.assertIn("主卦：䷵ 雷泽归妹", 输出)
        self.assertIn("变卦：䷹ 兑为泽", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第56幅（原叶55），友人与友人谋合业原记归妹之兑并引上六；归妹变兑须六五动，上六动则为睽，原载本变卦与爻辞矛盾。 https://dl.ndl.go.jp/pid/760555/1/56

    # 《高島易斷》1901增补本下经贞原影第60幅（原叶59），明治三十一年占英佛两国交际得丰之小过，原文明记初九；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/60

    def test_高岛丰明治三十一年占英佛两国交际(self):
        输出 = 运行("六爻纳甲.py", "9 8 7 7 8 8\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("变卦：䷽ 雷山小过", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第61幅（原叶60），明治三十一年占自由党气运得丰之大壮，原文明记六二；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/61

    def test_高岛丰明治三十一年占自由党气运(self):
        输出 = 运行("六爻纳甲.py", "7 6 7 7 8 8\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("变卦：䷡ 雷天大壮", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第62幅（原叶61），友人加入某会社得丰之震，原文明记九三；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/62

    def test_高岛丰友人加入某会社(self):
        输出 = 运行("六爻纳甲.py", "7 8 9 7 8 8\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第63幅（原叶62），豪家支配人占运气得丰之明夷，原文明记九四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/63

    def test_高岛丰豪家支配人占运气(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 9 8 8\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("变卦：䷣ 地火明夷", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第64幅（原叶63），亲友某当翁占气运得丰之革，原文明记六五；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/64

    def test_高岛丰亲友某当翁占气运(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 7 6 8\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("变卦：䷰ 泽火革", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第65幅（原叶64），明治十五年请减洋银取引所税得丰之离，原文明记上六；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/65

    def test_高岛丰明治十五年请减洋银取引所税(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 7 8 6\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("变卦：䷝ 离为火", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第68幅（原叶67），友人占气运初六得旅之离，原文明记初六；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/68

    def test_高岛旅友人占气运初六(self):
        输出 = 运行("六爻纳甲.py", "6 8 7 7 8 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 输出)
        self.assertIn("变卦：䷝ 离为火", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第69幅（原叶68），明治十七年九州某石灰坑业得旅之鼎，原文明记六二；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/69

    def test_高岛旅明治十七年九州某石灰坑业(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 7 8 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 输出)
        self.assertIn("变卦：䷱ 火风鼎", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第69–70幅（原叶68–69），明治十八年云照师占宗教得旅之晋，原文明记得旅三爻；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/69

    def test_高岛旅明治十八年云照师占宗教(self):
        输出 = 运行("六爻纳甲.py", "8 8 9 7 8 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 输出)
        self.assertIn("变卦：䷢ 火地晋", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第70–71幅（原叶69–70），明治十八年某贵显受外国公使命得旅之艮，原文明记九四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/70

    def test_高岛旅明治十八年某贵显受外国公使命(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 9 8 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 输出)
        self.assertIn("变卦：䷳ 艮为山", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第71幅（原叶70），明治二十四年某贵显占气运得旅之遯，原文明记六五；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/71

    def test_高岛旅明治二十四年某贵显占气运(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 7 6 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 输出)
        self.assertIn("变卦：䷠ 天山遁", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第72–73幅（原叶71–72），明治二十四年五月占大津事变得旅之小过，原文明记上九；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/72

    def test_高岛旅明治二十四年五月占大津事变(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 7 8 9\n\n")
        self.assertIn("主卦：䷷ 火山旅", 输出)
        self.assertIn("变卦：䷽ 雷山小过", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第77幅（原叶76），友人占气运初六得巽之小畜，原文明记初六；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/77

    def test_高岛巽友人占气运初六(self):
        输出 = 运行("六爻纳甲.py", "6 7 7 8 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷈ 风天小畜", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第77–78幅（原叶76–77），某缙绅占方今时势得巽之渐，原文明记九二；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/77

    def test_高岛巽某缙绅占方今时势(self):
        输出 = 运行("六爻纳甲.py", "8 9 7 8 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷴ 风山渐", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第78幅（原叶77），友人占气运九三得巽之涣，原文明记九三；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/78

    def test_高岛巽友人占气运九三(self):
        输出 = 运行("六爻纳甲.py", "8 7 9 8 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷺ 风水涣", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第78–79幅（原叶77–78），明治三十年占贵族院气运得巽之涣，原文明记九三；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/78

    def test_高岛巽明治三十年占贵族院气运(self):
        输出 = 运行("六爻纳甲.py", "8 7 9 8 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷺ 风水涣", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第79幅（原叶78），横滨商人占谋事得失得巽之姤，原文明记六四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/79

    def test_高岛巽横滨商人占谋事得失(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 6 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷫ 天风姤", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第80幅（原叶79），明治二十四年某贵显占气运得巽之蛊，原文明记九五；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/80

    def test_高岛巽明治二十四年某贵显占气运(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 8 9 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷑ 山风蛊", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第81幅（原叶80），明治二十四年占国运治乱得巽之井，原文明记上九；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/81

    def test_高岛巽明治二十四年占国运治乱(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 8 7 9\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷯ 水风井", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第85幅（原叶84），友人占谋事成否得兑之困，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/85

    def test_高岛兑友人占谋事成否(self):
        输出 = 运行("六爻纳甲.py", "9 7 8 7 7 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷮ 泽水困", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第86幅（原叶85），友人占气运九二得兑之随，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/86

    def test_高岛兑友人占气运九二(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 7 7 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷐ 泽雷随", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第86幅（原叶85），明治二十八年占我国与美国交际得兑之随，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/86

    def test_高岛兑明治二十八年占我国与美国交际(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 7 7 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷐ 泽雷随", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第87幅（原叶86），明治二十四年代占某氏气运得兑之夬，原文明确引六三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/87

    def test_高岛兑明治二十四年代占某氏气运(self):
        输出 = 运行("六爻纳甲.py", "7 7 6 7 7 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷪ 泽天夬", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第88幅（原叶87），某氏占缙绅运气得兑之节，原文明确引九四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/88

    def test_高岛兑某氏占缙绅运气(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 9 7 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷻ 水泽节", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第88–89幅（原叶87–88），明治二十二年友人占气运九五得兑之归妹，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/88

    def test_高岛兑明治二十二年友人占气运九五(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 7 9 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷵ 雷泽归妹", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第89幅（原叶88），明治二十二年占贵显气运得兑之履，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/89

    def test_高岛兑明治二十二年占贵显气运(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 7 7 6\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷉ 天泽履", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第93幅（原叶92），友人占气运初六得涣之中孚，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/93

    def test_高岛涣友人占气运初六(self):
        输出 = 运行("六爻纳甲.py", "6 7 8 8 7 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷼ 风泽中孚", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第94幅（原叶93），友人占抵押债务处置得涣之观，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/94

    def test_高岛涣友人占抵押债务处置(self):
        输出 = 运行("六爻纳甲.py", "8 9 8 8 7 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷓ 风地观", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第95幅（原叶94），友人占气运六三得涣之巽，原文明确引六三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/95

    def test_高岛涣友人占气运六三(self):
        输出 = 运行("六爻纳甲.py", "8 7 6 8 7 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷸ 巽为风", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第95–96页，大浦难船案记筮得涣之讼、六四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/95

    def test_高岛占大浦难船(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 6 7 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第96–97幅（原叶95–96），明治二十七年朴泳孝占朝鲜治乱得涣之蒙，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/96

    def test_高岛涣明治二十七年朴泳孝占朝鲜治乱(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 8 9 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷃ 山水蒙", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第97幅（原叶96），明治二十七年山田德明问朝鲜开战得涣之蒙，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/97

    def test_高岛涣明治二十七年山田德明问朝鲜开战(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 8 9 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷃ 山水蒙", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第98幅（原叶97），友人占气运上九得涣之坎，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/98

    def test_高岛涣友人占气运上九(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 8 7 9\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷜ 坎为水", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第98–99幅（原叶97–98），明治三十一年占英国与露国交际得涣之坎，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/98

    def test_高岛涣明治三十一年占英国与露国交际(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 8 7 9\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷜ 坎为水", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第102幅（原叶101），友人占家宅得节之坎，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/102

    def test_高岛节友人占家宅(self):
        输出 = 运行("六爻纳甲.py", "9 7 8 8 7 8\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷜ 坎为水", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第103–104幅（原叶102–103），警吏代占旧藩士债务得节之屯，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/103

    def test_高岛节警吏代占旧藩士债务(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 8 7 8\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷂ 水雷屯", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第104–105幅（原叶103–104），明治二十年占旧大垣藩主渡海平安得节之需，原文明确引六三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/104

    def test_高岛节明治二十年占旧大垣藩主渡海平安(self):
        输出 = 运行("六爻纳甲.py", "7 7 6 8 7 8\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷄ 水天需", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第105–106幅（原叶104–105），官吏占官位升迁得节之兑，原文明确引六四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/105

    def test_高岛节官吏占官位升迁(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 6 7 8\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷹ 兑为泽", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第106幅（原叶105），商人占商业盈亏得节之临，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/106

    def test_高岛节商人占商业盈亏(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 8 9 8\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷒ 地泽临", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第107幅（原叶106），商友占股票涨跌得节之中孚，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/107

    def test_高岛节商友占股票涨跌(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 8 7 6\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷼ 风泽中孚", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第107幅（原叶106），明治三十一年占北海道厅政治得节之中孚，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/107

    def test_高岛节明治三十一年占北海道厅政治(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 8 7 6\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷼ 风泽中孚", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第107–108幅（原叶106–107），明治三十一年占外交形势得节之中孚，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/107

    def test_高岛节明治三十一年占外交形势(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 8 7 6\n\n")
        self.assertIn("主卦：䷻ 水泽节", 输出)
        self.assertIn("变卦：䷼ 风泽中孚", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第111幅（原叶110），友人占商业得中孚之涣，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/111

    def test_高岛中孚友人占商业(self):
        输出 = 运行("六爻纳甲.py", "9 7 8 8 7 7\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷺ 风水涣", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第112幅（原叶111），占贵显续弦得中孚之益，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/112

    def test_高岛中孚占贵显续弦(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 8 7 7\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷩ 风雷益", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第112幅（原叶111），中孚续弦案再占媒人得兑之随，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/112

    def test_高岛中孚续弦案再占媒人(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 7 7 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷐ 泽雷随", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第112–113幅（原叶111–112），中孚续弦案复占前约得履之睽，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/112

    def test_高岛中孚续弦案复占前约(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 7 9 7\n\n")
        self.assertIn("主卦：䷉ 天泽履", 输出)
        self.assertIn("变卦：䷥ 火泽睽", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第113幅（原叶112），明治三十年占我国与美国交际得中孚之益，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/113

    def test_高岛中孚明治三十年占我国与美国交际(self):
        输出 = 运行("六爻纳甲.py", "7 9 8 8 7 7\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷩ 风雷益", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第113–114幅（原叶112–113），县职友人占降级得中孚之小畜，原文明确引六三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/113

    def test_高岛中孚县职友人占降级(self):
        输出 = 运行("六爻纳甲.py", "7 7 6 8 7 7\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷈ 风天小畜", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第114–115幅（原叶113–114），缙绅占谋事得中孚之履，原文明确引六四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/114

    def test_高岛中孚缙绅占谋事(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 6 7 7\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷉ 天泽履", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第115幅（原叶114），缙绅占婚姻得中孚之损，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/115

    def test_高岛中孚缙绅占婚姻(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 8 9 7\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷨ 山泽损", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第116幅（原叶115），自称天爵大神者占运气得中孚之节，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/116

    def test_高岛中孚自称天爵大神者占运气(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 8 7 9\n\n")
        self.assertIn("主卦：䷼ 风泽中孚", 输出)
        self.assertIn("变卦：䷻ 水泽节", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第120–121幅（原叶119–120），友人占谋事成否得小过之丰，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/120

    def test_高岛小过友人占谋事成否(self):
        输出 = 运行("六爻纳甲.py", "6 8 7 7 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷶ 雷火丰", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第121幅（原叶120），明治二十七年冬至占次年露国交际得小过之丰，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/121

    def test_高岛小过明治二十七年冬至占次年露国交际(self):
        输出 = 运行("六爻纳甲.py", "6 8 7 7 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷶ 雷火丰", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第122幅（原叶121），明治十八年占角堂俳谐得小过之恒，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/122

    def test_高岛小过明治十八年占角堂俳谐(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 7 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷟ 雷风恒", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第122幅（原叶121），明治二十九年朴泳孝占归国行止得小过之恒，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/122

    def test_高岛小过明治二十九年朴泳孝占归国行止(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 7 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷟ 雷风恒", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第122幅（原叶121），明治三十年占我国与英国交际得小过之恒，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/122

    def test_高岛小过明治三十年占我国与英国交际(self):
        输出 = 运行("六爻纳甲.py", "8 6 7 7 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷟ 雷风恒", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第123幅（原叶122），佐田金作占寻失童得小过之豫，原文明确引九三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/123

    def test_高岛小过佐田金作占寻失童(self):
        输出 = 运行("六爻纳甲.py", "8 8 9 7 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第124幅（原叶123），友人占借贷钱财得小过之谦，原文明确引九四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/124

    def test_高岛小过友人占借贷钱财(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 9 8 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷎ 地山谦", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第125幅（原叶124），明治三十年占陆军省气运得小过之咸，原文明确引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/125

    def test_高岛小过明治三十年占陆军省气运(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 7 6 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷞ 泽山咸", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第126幅（原叶125），友人占子病得小过之旅，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/126

    def test_高岛小过友人占子病(self):
        输出 = 运行("六爻纳甲.py", "8 8 7 7 8 6\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 输出)
        self.assertIn("变卦：䷷ 火山旅", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第129幅（原叶128），明治二十一年缙绅占气运得既济之蹇，原文明确引初九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/129

    def test_高岛既济明治二十一年缙绅占气运(self):
        输出 = 运行("六爻纳甲.py", "9 8 7 8 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷦ 水山蹇", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第130幅（原叶129），占贵显勋章得既济之需，原文明确引六二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/130

    def test_高岛既济占贵显勋章(self):
        输出 = 运行("六爻纳甲.py", "7 6 7 8 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷄ 水天需", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第131幅（原叶130），商人占谋事成否得既济之屯，原文明确引九三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/131

    def test_高岛既济商人占谋事成否(self):
        输出 = 运行("六爻纳甲.py", "7 8 9 8 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷂ 水雷屯", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第131–132幅（原叶130–131），明治三十年杉浦重刚问足尾铁毒得既济之屯，原文明确引九三爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/131

    def test_高岛既济明治三十年杉浦重刚问足尾铁毒(self):
        输出 = 运行("六爻纳甲.py", "7 8 9 8 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷂ 水雷屯", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三"])

    # 《高島易斷》1901增补本下经贞原影第132–133幅（原叶131–132），西村舍三占治水处置得既济之革，原文明确引六四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/132

    def test_高岛既济西村舍三占治水处置(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 6 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷰ 泽火革", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第133幅（原叶132），占阪田春雄归期得既济之革，原文明确引六四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/133

    def test_高岛既济占阪田春雄归期(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 6 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷰ 泽火革", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第134幅（原叶133），明治元年占橘屋材木价得既济之明夷，原文明确引九五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/134

    def test_高岛既济明治元年占橘屋材木价(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 8 9 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷣ 地火明夷", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第135幅（原叶134），友人占行运得既济之家人，原文明确引上六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/135

    def test_高岛既济友人占行运(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 8 7 6\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertIn("变卦：䷤ 风火家人", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《高島易斷》1901增补本下经贞原影第138–139幅（原叶137–138），友人占制造物品生业得未济之睽，原文明确引初六爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/138

    def test_高岛未济友人占制造物品生业(self):
        输出 = 运行("六爻纳甲.py", "6 7 8 7 8 7\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertIn("变卦：䷥ 火泽睽", 输出)
        self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《高島易斷》1901增补本下经贞原影第139–140幅（原叶138–139），明治八年九月占朝鲜兴问罪之师得未济之晋，原文明确引九二爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/139

    def test_高岛未济明治八年九月占朝鲜兴问罪之师(self):
        输出 = 运行("六爻纳甲.py", "8 9 8 7 8 7\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertIn("变卦：䷢ 火地晋", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["二"])

    # 《高島易斷》1901增补本下经贞原影第140–141幅（原叶139–140），三十年占众议院气运记未济之鼎，却将“未济征凶利涉大川”爻辞题为九三；未济第三爻为阴爻，未济之鼎也只变第三爻，原书九三题名与卦画相矛盾。 https://dl.ndl.go.jp/pid/760555/1/140

    # 《高島易斷》1901增补本下经贞原影第141幅（原叶140），友人占气运九四得未济之蒙，原文明确引九四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/141

    def test_高岛未济友人占气运九四(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 9 8 7\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertIn("变卦：䷃ 山水蒙", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第141–142幅（原叶140–141），明治二十七年冬至占次年圣运得未济之蒙，原文明确引九四爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/141

    def test_高岛未济明治二十七年冬至占次年圣运(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 9 8 7\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertIn("变卦：䷃ 山水蒙", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《高島易斷》1901增补本下经贞原影第142幅（原叶141），缙绅占官阶升迁得未济之讼，原文明确引六五爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/142

    def test_高岛未济缙绅占官阶升迁(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 7 6 7\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《高島易斷》1901增补本下经贞原影第143幅（原叶142），明治二十八年七月二十七日占新闻号外得未济之解，原文明确引上九爻辞；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/143

    def test_高岛未济明治二十八年七月二十七日占新闻号外(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 7 8 9\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《易林补遗》卷1“易林总断”演例，明刻本PDF第50页载未月壬戌日父占子病得乾卦安静；爻值依原卦换算 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=50

    def test_易林未月壬戌父占子病(self):
        输出 = 运行("六爻纳甲.py", "7 7 7 7 7 7\n\n")
        self.assertIn("主卦：䷀ 乾为天", 输出)
        self.assertIn("变卦：䷀ 乾为天（乾宫），无动爻", 输出)

    # 《易林补遗》卷1“易林总断”演例，明刻本PDF第50页载秋月甲申日求财得睽之归妹，未明记动爻；依本变卦唯一反推上爻阳动 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=50

    # def test_易林秋月甲申求财(self):
    #     输出 = 运行("六爻纳甲.py", "7 7 8 7 8 9\n\n")
    #     self.assertIn("主卦：䷥ 火泽睽", 输出)
    #     self.assertIn("变卦：䷵ 雷泽归妹", 输出)
    #     self.assertRegex(输出, r"(?m)^上爻 .*⚊ ○")
    #     self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《易林补遗》卷1“易林总断”演例，明刻本PDF第51页载甲辰旬丁未日得兑之艮，未明记动爻；依本变卦唯一反推六爻全动 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=51

    # def test_易林丁未兑之艮(self):
    #     输出 = 运行("六爻纳甲.py", "9 9 6 9 9 6\n\n")
    #     self.assertIn("主卦：䷹ 兑为泽", 输出)
    #     self.assertIn("变卦：䷳ 艮为山", 输出)
    #     self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上", "五", "四", "三", "二", "初"])

    # 《易林补遗》卷1“易林总断”演例，明刻本PDF第51页载七月丙辰日占长子病得恒九四动之升、内卦不动；爻值依原卦和动爻换算 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=51

    def test_易林七月丙辰占长子病(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 9 8 8\n\n")
        self.assertIn("主卦：䷟ 雷风恒", 输出)
        self.assertIn("变卦：䷭ 地风升", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

    # 《易林补遗》元集卷1“易林总断章第一”假设例，明刻本PDF第56页原叶八载戌月丁亥日巳时求财得蒙卦安静，金财伏于四爻土下；爻值依原静卦换算，不虚补占年 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=56

    def test_易林戌月丁亥蒙静求财(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 8 8 7\n\n")
        self.assertIn("主卦：䷃ 山水蒙", 输出)
        self.assertIn("无动爻", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*[辰戌丑未] ⚋")

    # 《易林补遗》元集卷1“易林总断章第一”，明刻本PDF第56页原叶八载丁酉日妻占远路行夫得旅卦，未明记动静，不能补作静卦输入 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=56

    # 《易林补遗》元集卷3“六亲寿命章第八”假设例，明刻本PDF第94页原叶九载丙辰年七月己丑日子占父寿得革卦安静；爻值依原静卦换算，不虚补公历占年 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=94

    def test_易林丙辰子占父寿革静(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 7 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 输出)
        self.assertIn("无动爻", 输出)
        self.assertNotIn("○", 输出)
        self.assertNotIn("×", 输出)

    # 《易林补遗》元集卷3“六亲寿命章第八”假设例，明刻本PDF第94页原叶九载戊辰年六月戊戌日夫占妻寿得丰卦安静；爻值依原静卦换算，不虚补公历占年 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=94

    def test_易林戊辰夫占妻寿丰静(self):
        输出 = 运行("六爻纳甲.py", "7 8 7 7 8 8\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 输出)
        self.assertIn("无动爻", 输出)
        self.assertNotIn("○", 输出)
        self.assertNotIn("×", 输出)

    # 《易林补遗》利集卷7“何处得病章第六十六”，明刻本PDF第152页原叶五记家人卦三爻伏官鬼辛酉金、飞神己亥水，未明记动静；程序不列伏神，且不能补作静卦输入 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=152

    # 《易林补遗》利集卷7“疾病吉凶章第六十九”假设例，明刻本PDF第160页版心叶号有遮损载三月甲子日妻占夫病得观之益，未明记动爻；依本变卦唯一反推初爻阴动，不虚补占年 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=160

    # def test_易林三月甲子妻占夫病(self):
    #     输出 = 运行("六爻纳甲.py", "6 8 8 8 7 7\n\n")
    #     self.assertIn("主卦：䷓ 风地观", 输出)
    #     self.assertIn("变卦：䷩ 风雷益", 输出)
    #     self.assertRegex(输出, r"(?m)^初爻 .*⚋ ×")
    #     self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["初"])

    # 《易林补遗》利集卷7“疾病吉凶章第六十九”假设例，明刻本PDF第160页版心叶号有遮损载十月戊辰日弟占兄病得剥、初二三爻皆动，申金兄弟伏在世爻子水之下；只核原载世爻子水，不虚补占年 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=160

    def test_易林十月戊辰弟占兄病(self):
        输出 = 运行("六爻纳甲.py", "6 6 6 8 8 7\n\n")
        self.assertIn("主卦：䷖ 山地剥", 输出)
        self.assertRegex(输出, r"(?m)^五爻 .*子 .*世$")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["三", "二", "初"])

    # 《易林补遗》利集卷7“疾病吉凶章第六十九”假设例，明刻本PDF第160页版心叶号有遮损载五月甲午旬癸卯日父占子病得萃、上六父动化进气；只核原载父母爻变进气，未变戌对应进土，不虚补占年 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=160

    def test_易林五月癸卯父占子病(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 7 7 6\n\n")
        self.assertIn("主卦：䷬ 泽地萃", 输出)
        self.assertRegex(输出, r"(?m)^上爻 父母 .未 ⚋ × .*→ 父母 .戌$")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上"])

    # 《易林补遗》贞集卷11“离枷出狱章第一百二十七”假设例，明刻本PDF第223页原叶五载戌日占风地观、二爻巳火官爻，未明记动静；不能补作静卦输入 https://commons.wikimedia.org/wiki/File:NCL-06549_易林補遺.pdf?page=223

    # 《增删卜易》占卦法假设例，秦慎安校勘本PDF第22–24页记六次背数1、2、3、0、3、2及水火既济；爻值依占卦法换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=23

    def test_占卦法既济例(self):
        输出 = 运行("六爻纳甲.py", "7 8 9 6 9 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 输出)
        self.assertRegex(输出, r"(?m)^三爻 .*⚊ ○")
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertRegex(输出, r"(?m)^五爻 .*⚊ ○")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五", "四", "三"])

    # 《增删卜易》占卦法再排一卦假设例，秦慎安校勘本PDF第24页记六次背数2、3、2、1、0、1及火水未济；爻值依占卦法换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=24

    def test_占卦法未济例(self):
        输出 = 运行("六爻纳甲.py", "8 9 8 7 6 7\n\n")
        self.assertIn("主卦：䷿ 火水未济", 输出)
        self.assertRegex(输出, r"(?m)^二爻 .*⚊ ○")
        self.assertRegex(输出, r"(?m)^五爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五", "二"])

    # 《增删卜易》用神章乾卦假设例，秦慎安校勘本PDF第38页原六爻皆静，爻值依爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=38

    def test_用神章乾卦例(self):
        输出 = 运行("六爻纳甲.py", "7 7 7 7 7 7\n\n")
        self.assertIn("主卦：䷀ 乾为天（乾宫，属金，世6应3）", 输出)
        self.assertIn("变卦：䷀ 乾为天（乾宫），无动爻", 输出)
        self.assertRegex(输出, r"(?m)^上爻 父母 .戌 ⚊ +世$")
        self.assertRegex(输出, r"(?m)^五爻 兄弟 .申 ⚊")
        self.assertRegex(输出, r"(?m)^四爻 官鬼 .午 ⚊")
        self.assertRegex(输出, r"(?m)^三爻 父母 .辰 ⚊ +应$")
        self.assertRegex(输出, r"(?m)^二爻 妻财 .寅 ⚊")
        self.assertRegex(输出, r"(?m)^初爻 子孙 .子 ⚊")

    # 《增删卜易》第9章“辰月戊申日占父近病”，秦慎安校勘本PDF第50–51页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=50

    def test_辰月戊申占父病(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 7\n\n")
        self.assertIn("主卦：䷀ 乾为天（乾宫，属金，世6应3）", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 辛未", 纳甲)

    # 《增删卜易》第10章“酉月辛卯日占谒贵求财”，秦慎安校勘本PDF第52页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=52

    def test_酉月辛卯占谒贵求财(self):
        输出 = 运行("六爻纳甲.py", "9 7 8 7 9 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)
        self.assertRegex(输出, r"(?m)^五爻 兄弟 .酉 ⚊ ○ +→ 兄弟 .申$")
        self.assertRegex(输出, r"(?m)^初爻 官鬼 .巳 ⚊ ○ +→ 妻财 .寅$")

    # 《增删卜易》第10章“巳月乙未日自占病”，秦慎安校勘本PDF第54页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=54

    def test_巳月乙未自占病(self):
        输出 = 运行("六爻纳甲.py", "8 7 7 7 9 6\n\n")
        self.assertIn("主卦：䷛ 泽风大过", 输出)
        self.assertIn("变卦：䷱ 火风鼎", 输出)
        self.assertRegex(输出, r"(?m)^上爻 妻财 .未 ⚋ × +→ 子孙 .巳$")
        self.assertRegex(输出, r"(?m)^五爻 官鬼 .酉 ⚊ ○ +→ 妻财 .未$")

    # 《增删卜易》第11章“卯月己卯日弟占兄已得重罪，母叩阍能救否”，秦慎安校勘本PDF第54～55页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=55

    def test_卯月己卯占兄重罪(self):
        输出 = 运行("六爻纳甲.py", "7 8 8 6 8 8\n\n")
        self.assertIn("主卦：䷗ 地雷复", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)
        self.assertRegex(输出, r"(?m)^四爻 兄弟 .丑 ⚋ × .*→ 父母 .午$")

    # 《增删卜易》第12章“卯月戊寅日占父官事已拟重罪”，秦慎安校勘本PDF第55页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=55

    def test_卯月戊寅占父官事(self):
        输出 = 运行("六爻纳甲.py", "6 8 6 7 7 6\n\n")
        self.assertIn("主卦：䷬ 泽地萃", 输出)
        self.assertIn("变卦：䷌ 天火同人", 输出)
        self.assertRegex(输出, r"(?m)^上爻 父母 .未 ⚋ × +→ 父母 .戌$")
        self.assertRegex(输出, r"(?m)^三爻 妻财 .卯 ⚋ × +→ 子孙 .亥$")
        self.assertRegex(输出, r"(?m)^初爻 父母 .未 ⚋ × +→ 妻财 .卯$")

    # 《增删卜易》第12章“同日妹占兄官事同此一案亦拟重罪”，秦慎安校勘本PDF第56页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=56

    def test_卯月戊寅妹占兄官事(self):
        输出 = 运行("六爻纳甲.py", "8 6 8 7 7 7\n\n")
        self.assertIn("主卦：䷋ 天地否", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)
        self.assertRegex(输出, r"(?m)^二爻 官鬼 .巳 ⚋ ×")

    # 《增删卜易》第13章“辰月丙申占弟痘症”，秦慎安校勘本PDF第57页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=57

    def test_辰月丙申占弟痘症(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济（坎宫，属水，世3应6）", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("四爻 父母 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁亥", 纳甲)

    # 《增删卜易》第14章“假令春天寅卯月占得坤卦”假设例，秦慎安校勘本PDF第57页；爻值依原静爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=57

    def test_春天寅卯月坤卦例(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷁ 坤为地（坤宫，属土，世6应3）", 输出)
        self.assertIn("变卦：䷁ 坤为地（坤宫），无动爻", 输出)
        self.assertRegex(输出, r"(?m)^上爻 子孙 .酉 ⚋ +世$")
        self.assertRegex(输出, r"(?m)^五爻 妻财 .亥 ⚋")
        self.assertRegex(输出, r"(?m)^四爻 兄弟 .丑 ⚋")
        self.assertRegex(输出, r"(?m)^三爻 官鬼 .卯 ⚋ +应$")
        self.assertRegex(输出, r"(?m)^二爻 父母 .巳 ⚋")
        self.assertRegex(输出, r"(?m)^初爻 兄弟 .未 ⚋")

    # 《增删卜易》第14章“假令寅月占得兑卦变归妹”假设例，秦慎安校勘本PDF第58页；爻值依原五爻动爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=58

    def test_寅月兑之归妹例(self):
        输出 = 运行("六爻纳甲.py", "7 7 8 7 9 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽（兑宫，属金，世6应3）", 输出)
        self.assertIn("变卦：䷵ 雷泽归妹", 输出)
        self.assertRegex(输出, r"(?m)^五爻 兄弟 .酉 ⚊ ○ +→ 兄弟 .申$")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["五"])

    # 《增删卜易》第15章“假令子月卯日占得坤卦变火地晋”假设例，秦慎安校勘本PDF第58–59页；爻值依原四、上爻动爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=58

    def test_子月卯日坤之晋例(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 6 8 6\n\n")
        self.assertIn("主卦：䷁ 坤为地（坤宫，属土，世6应3）", 输出)
        self.assertIn("变卦：䷢ 火地晋", 输出)
        self.assertRegex(输出, r"(?m)^上爻 子孙 .酉 ⚋ × 世 → 父母 .巳$")
        self.assertRegex(输出, r"(?m)^四爻 兄弟 .丑 ⚋ × +→ 子孙 .酉$")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上", "四"])

    # 《增删卜易》第16章“寅月庚戌占求财”，秦慎安校勘本PDF第62页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=62

    def test_寅月庚戌占求财(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 8 7\n\n")
        self.assertIn("主卦：䷍ 火天大有（乾宫，属金，世3应6）", 纳甲)
        self.assertIn("变卦：䷍ 火天大有", 纳甲)
        self.assertIn("二爻 妻财 甲寅", 纳甲)
        self.assertIn("三爻 父母 甲辰", 纳甲)

    # 《增删卜易》第16章“酉月丙寅占谒贵”，秦慎安校勘本PDF第62页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=62

    def test_酉月丙寅占谒贵(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 9 8 8 7\n\n")
        self.assertIn("主卦：䷑ 山风蛊（巽宫，属木，世3应6）", 纳甲)
        self.assertIn("变卦：䷃ 山水蒙", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)

    # 《增删卜易》第16章“寅月丙申占升迁”，秦慎安校勘本PDF第63页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=63

    def test_寅月丙申占升迁(self):
        纳甲 = 运行("六爻纳甲.py", "6 8 9 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山（艮宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷚ 山雷颐", 纳甲)
        self.assertIn("初爻 兄弟 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 庚子", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚辰", 纳甲)

    # 《增删卜易》第16章“午月丁未占弟被讼”，秦慎安校勘本PDF第64页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=64

    def test_午月丁未占弟被讼(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 6 7 9 8\n\n")
        self.assertIn("主卦：䷮ 泽水困（兑宫，属金，世1应4）", 纳甲)
        self.assertIn("变卦：䷟ 雷风恒", 纳甲)
        self.assertIn("三爻 官鬼 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 辛酉", 纳甲)
        self.assertIn("五爻 兄弟 丁酉 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)

    # 《增删卜易》第16章“寅月辛酉占开铺”，秦慎安校勘本PDF第65页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=65

    def test_寅月辛酉占开铺(self):
        纳甲 = 运行("六爻纳甲.py", "6 8 7 8 8 9\n\n")
        self.assertIn("主卦：䷳ 艮为山（艮宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("上爻 官鬼 丙寅 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸酉", 纳甲)
        self.assertIn("初爻 兄弟 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己卯", 纳甲)

    # 《增删卜易》第16章“午月戊辰占妹临产”，秦慎安校勘本PDF第66页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=66

    def test_午月戊辰占妹临产(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 8 7\n\n")
        self.assertIn("主卦：䷢ 火地晋（乾宫，属金，世4应1）", 纳甲)
        self.assertIn("变卦：䷢ 火地晋", 纳甲)
        self.assertIn("四爻 兄弟 己酉", 纳甲)
        self.assertIn("二爻 官鬼 乙巳", 纳甲)

    # 《增删卜易》第17章“申月戊午自占病”，秦慎安校勘本PDF第68页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=68

    def test_申月戊午自占病(self):
        纳甲 = 运行("六爻纳甲.py", "8 6 7 7 7 7\n\n")
        self.assertIn("主卦：䷠ 天山遁（乾宫，属金，世2应5）", 纳甲)
        self.assertIn("变卦：䷫ 天风姤", 纳甲)
        self.assertIn("二爻 官鬼 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 辛亥", 纳甲)

    # 《增删卜易》第17章“巳月丁亥占仆归期”，秦慎安校勘本PDF第68页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=68

    def test_巳月丁亥占仆归期(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 9 7 7 6\n\n")
        self.assertIn("主卦：䷪ 泽天夬（坤宫，属土，世5应2）", 纳甲)
        self.assertIn("变卦：䷉ 天泽履", 纳甲)
        self.assertIn("三爻 兄弟 甲辰 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 丁丑", 纳甲)
        self.assertIn("上爻 兄弟 丁未 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 壬戌", 纳甲)

    # 《增删卜易》第18章“戊子日占生产”，秦慎安校勘本PDF第72页载剥之观及子水化巳火，爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=72

    def test_戊子日占生产(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 8 6 7\n\n")
        self.assertIn("主卦：䷖ 山地剥", 输出)
        self.assertIn("变卦：䷓ 风地观", 输出)
        self.assertRegex(输出, r"(?m)^五爻 子孙 .子 ⚋ × 世 → 官鬼 .巳$")

    # 《增删卜易》第18章“申月甲辰日占兄病”，秦慎安校勘本PDF第72～73页题屯之震、文言土申两动，图却四爻未标动、五爻标×而变午火；按本变卦唯一反推四阴五阳两动 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=73

    # def test_申月甲辰占兄病(self):
    #     输出 = 运行("六爻纳甲.py", "7 8 8 6 9 8\n\n")
    #     self.assertIn("主卦：䷂ 水雷屯", 输出)
    #     self.assertIn("变卦：䷲ 震为雷", 输出)
    #     self.assertRegex(输出, r"(?m)^五爻 父母 .申 ⚊ ○ +→ 妻财 .午$")
    #     self.assertRegex(输出, r"(?m)^四爻 官鬼 .辰 ⚋ × +→ 兄弟 .子$")

    # 《增删卜易》第19章“申月丙子日占得出行”，秦慎安校勘本PDF第75页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=75

    def test_申月丙子占出门(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 7 6 8 8\n\n")
        self.assertIn("主卦：䷣ 地火明夷（坎宫，属水，世4应1）", 纳甲)
        self.assertIn("变卦：䷽ 雷山小过", 纳甲)

    # 《增删卜易》第19章“未月丁巳日占已悔婚还可成否”，秦慎安校勘本PDF第75–76页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=75

    def test_未月丁巳占悔婚(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 8 7\n\n")
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)

    # 《增删卜易》第19章“卯月甲寅日占风水”，秦慎安校勘本PDF第77页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=77

    def test_卯月甲寅占风水(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 8 9 7 8\n\n")
        self.assertIn("主卦：䷮ 泽水困（兑宫，属金，世1应4）", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)

    # 《增删卜易》第19章“卯月丁巳日上下两村因争用水殴打”，秦慎安校勘本PDF第79页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=79

    def test_卯月丁巳争田水(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 9 9 8 9\n\n")
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)

    # 《增删卜易》第20章“巳月戊戌日占财”，秦慎安校勘本PDF第80～81页载风雷益静卦，爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=81

    def test_巳月戊戌占财(self):
        输出 = 运行("六爻纳甲.py", "7 8 8 8 7 7\n\n")
        self.assertIn("主卦：䷩ 风雷益", 输出)
        self.assertIn("变卦：䷩ 风雷益（巽宫），无动爻", 输出)
        self.assertRegex(输出, r"(?m)^三爻 妻财 .辰 ⚋ +世$")

    # 《增删卜易》第20章“午月丙辰日占出外贸易财喜”，秦慎安校勘本PDF第81页载恒之豫，爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=81

    def test_午月丙辰经商(self):
        输出 = 运行("六爻纳甲.py", "8 9 9 7 8 8\n\n")
        self.assertIn("主卦：䷟ 雷风恒", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)
        self.assertRegex(输出, r"(?m)^三爻 官鬼 .酉 ⚊ ○ 世 → 兄弟 .卯$")
        self.assertRegex(输出, r"(?m)^二爻 父母 .亥 ⚊ ○ +→ 子孙 .巳$")

    # 《增删卜易》第20章“酉月乙未日占子久出不归生死何如”，秦慎安校勘本PDF第81～82页载坤卦，爻值依原静爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=81

    def test_酉月乙未占子(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷁ 坤为地", 输出)
        self.assertIn("变卦：䷁ 坤为地（坤宫），无动爻", 输出)
        self.assertRegex(输出, r"(?m)^上爻 子孙 .酉 ⚋ +世$")

    # 《增删卜易》第20章“巳月甲寅日占延师训子”，秦慎安校勘本PDF第82页载否之乾，爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=82

    def test_巳月甲寅严师训子(self):
        输出 = 运行("六爻纳甲.py", "6 6 6 7 7 7\n\n")
        self.assertIn("主卦：䷋ 天地否", 输出)
        self.assertIn("变卦：䷀ 乾为天", 输出)
        self.assertRegex(输出, r"(?m)^三爻 妻财 .卯 ⚋ × 世 → 父母 .辰$")
        self.assertRegex(输出, r"(?m)^二爻 官鬼 .巳 ⚋ × +→ 妻财 .寅$")
        self.assertRegex(输出, r"(?m)^初爻 父母 .未 ⚋ × +→ 子孙 .子$")

    # 《增删卜易》第20章“申月乙卯日父子七人俱蒙拿问”，秦慎安校勘本PDF第82～83页载巽之坤，爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=83

    def test_申月乙卯父子七人(self):
        输出 = 运行("六爻纳甲.py", "8 9 9 8 9 9\n\n")
        self.assertIn("主卦：䷸ 巽为风", 输出)
        self.assertIn("变卦：䷁ 坤为地", 输出)
        self.assertRegex(输出, r"(?m)^上爻 兄弟 .卯 ⚊ ○ 世 → 官鬼 .酉$")
        self.assertRegex(输出, r"(?m)^五爻 子孙 .巳 ⚊ ○ +→ 父母 .亥$")
        self.assertRegex(输出, r"(?m)^三爻 官鬼 .酉 ⚊ ○ 应 → 兄弟 .卯$")
        self.assertRegex(输出, r"(?m)^二爻 父母 .亥 ⚊ ○ +→ 子孙 .巳$")

    # 《增删卜易》第21章“寅月庚申占子痘症”，秦慎安校勘本PDF第83页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=83

    def test_寅月庚申占子痘症(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 9 7\n\n")
        self.assertIn("主卦：䷤ 风火家人（巽宫，属木，世2应5）", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己酉", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 己未", 纳甲)

    # 《增删卜易》第22章“寅月己未占女痘”，秦慎安校勘本PDF第84页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=84

    def test_寅月己未占女痘(self):
        纳甲 = 运行("六爻纳甲.py", "8 6 8 8 8 8\n\n")
        self.assertIn("主卦：䷁ 坤为地（坤宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷆ 地水师", 纳甲)
        self.assertIn("二爻 父母 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 戊辰", 纳甲)

    # 《增删卜易》第23章“丑月丁酉占父出外”，秦慎安校勘本PDF第85页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=85

    def test_丑月丁酉占父出外(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 8 8 7 9\n\n")
        self.assertIn("主卦：䷺ 风水涣（离宫，属火，世5应2）", 纳甲)
        self.assertIn("变卦：䷜ 坎为水", 纳甲)
        self.assertIn("上爻 父母 辛卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊子", 纳甲)

    # 《增删卜易》第24章“卯月辛巳代占长辈功名”，秦慎安校勘本PDF第87页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=87

    def test_卯月辛巳代占长辈功名(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 7 6 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风（巽宫，属木，世6应3）", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 甲子", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)

    # 《增删卜易》第24章“午月丙寅占主病”，秦慎安校勘本PDF第87页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=87

    def test_午月丙寅占主病(self):
        纳甲 = 运行("六爻纳甲.py", "9 6 9 9 6 9\n\n")
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷜ 坎为水", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊子", 纳甲)
        self.assertIn("二爻 子孙 己丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 戊辰", 纳甲)

    # 《卜筮正宗》卷3“辟易林补遗终身大小限之谬”，光绪十五年重刻本第二册PDF第24～26页载戊辰年辰月丙辰日自占终身成败旅之蛊，未排爻画；依本变卦唯一反推二阴四阳动 https://commons.wikimedia.org/wiki/File:NCPSSD-70017387_卜筮正宗十四卷_第二册.pdf?page=25

    # def test_自占终身成败(self):
    #     输出 = 运行("六爻纳甲.py", "8 6 7 9 8 7\n\n")
    #     self.assertIn("主卦：䷷ 火山旅", 输出)
    #     self.assertIn("变卦：䷑ 山风蛊", 输出)
    #     self.assertRegex(输出, r"(?m)^四爻 妻财 .酉 ⚊ ○ +(?:应 +)?→ 子孙 .戌$")
    #     self.assertRegex(输出, r"(?m)^二爻 兄弟 .午 ⚋ × +→ 官鬼 .亥$")

    # 《卜筮正宗》卷3“辟易林补遗婚姻嫁娶之谬”，光绪十五年重刻本第二册PDF第29页左叶载午建乙卯日女择婿得否卦安静、世阴应阳；爻值依原卦换算，未载年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017387_卜筮正宗十四卷_第二册.pdf?page=29

    def test_卜筮正宗午月乙卯女择婿(self):
        输出 = 运行("六爻纳甲.py", "8 8 8 7 7 7\n\n")
        self.assertIn("主卦：䷋ 天地否", 输出)
        self.assertIn("无动爻", 输出)
        self.assertRegex(输出, r"(?m)^三爻 妻财 乙卯 ⚋ +世$")
        self.assertRegex(输出, r"(?m)^上爻 .*⚊ +应$")

    # 《卜筮正宗》卷3“辟易林补遗婚姻嫁娶之谬”，光绪十五年重刻本第二册PDF第29页左叶载申月甲午日女择婿得复之睽，未明记动爻；依本变卦唯一反推二、四、上爻阴动，未载年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017387_卜筮正宗十四卷_第二册.pdf?page=29

    # def test_卜筮正宗申月甲午女择婿(self):
    #     输出 = 运行("六爻纳甲.py", "7 6 8 6 8 6\n\n")
    #     self.assertIn("主卦：䷗ 地雷复", 输出)
    #     self.assertIn("变卦：䷥ 火泽睽", 输出)
    #     self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["上", "四", "二"])

    # 《卜筮正宗》十八问答所记伏神、暗动、月破、应期等未在当前脚本输出，只重放明爻主变与纳甲 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf

    # 《卜筮正宗》卷十三十八问答第一问，光绪十五年重刻本第六册PDF第4页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=4

    def test_申月戊子占坟地(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 7\n\n")
        self.assertIn("主卦：䷖ 山地剥（乾宫，属金，世5应2）", 纳甲)
        self.assertIn("变卦：䷖ 山地剥", 纳甲)
        self.assertIn("五爻 子孙 丙子", 纳甲)
        self.assertIn("上爻 妻财 丙寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第5页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=5

    def test_卯月癸亥占家宅人口(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 6 7 6\n\n")
        self.assertIn("主卦：䷄ 水天需（坤宫，属土，世4应1）", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("四爻 子孙 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬午", 纳甲)
        self.assertIn("上爻 妻财 戊子 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 壬戌", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第6页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=6

    def test_卯月乙未占卖货(self):
        纳甲 = 运行("六爻纳甲.py", "7 6 7 8 7 7\n\n")
        self.assertIn("主卦：䷤ 风火家人（巽宫，属木，世2应5）", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("二爻 妻财 己丑 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 甲寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第7页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=7

    def test_酉月丙寅占何日雨(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 9 8 8 8\n\n")
        self.assertIn("主卦：䷭ 地风升（震宫，属木，世4应1）", 纳甲)
        self.assertIn("变卦：䷆ 地水师", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第8页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=8

    def test_卯月乙酉占索房价(self):
        纳甲 = 运行("六爻纳甲.py", "8 9 8 8 9 8\n\n")
        self.assertIn("主卦：䷜ 坎为水（坎宫，属水，世6应3）", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("二爻 官鬼 戊辰 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 乙巳", 纳甲)
        self.assertIn("五爻 官鬼 戊戌 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第9页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=9

    def test_申月戊辰占具题(self):
        纳甲 = 运行("六爻纳甲.py", "6 6 8 8 8 6\n\n")
        self.assertIn("主卦：䷁ 坤为地（坤宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷨ 山泽损", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丙寅", 纳甲)
        self.assertIn("二爻 父母 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第9页；爻值依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=9

    def test_丁巳占虑大计(self):
        纳甲 = 运行("六爻纳甲.py", "6 8 7 9 8 9\n\n")
        self.assertIn("主卦：䷷ 火山旅（离宫，属火，世1应4）", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 癸酉", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸丑", 纳甲)
        self.assertIn("初爻 子孙 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 己卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第10页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=10

    def test_申月戊辰妻占夫近病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 9 7\n\n")
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("五爻 妻财 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 己未", 纳甲)
        self.assertIn("四爻 兄弟 壬午", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第10页；第三问卯月甲寅占风水困之节，与现有《增删卜易》卯月甲寅占风水为同案。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=10

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第11页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=11

    def test_丑月戊子自占近病(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 9 7\n\n")
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)
        self.assertIn("五爻 妻财 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 己未", 纳甲)
        self.assertIn("初爻 父母 己卯 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙辰", 纳甲)

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第11页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=11

    def test_寅月乙丑子占父病(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 9 8 8 8\n\n")
        self.assertIn("主卦：䷭ 地风升", 纳甲)
        self.assertIn("变卦：䷆ 地水师", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)
        self.assertIn("二爻 父母 辛亥", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第12页；第四问卯月丁巳两村争戽水，与已核《增删卜易》卯月丁巳争田水同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=12

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第13页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=13

    def test_巳月丁酉递呈谋补缺(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 9\n\n")
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷄ 水天需", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊子", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第13页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=13

    def test_寅月丙辰占选期(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 7\n\n")
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 辛未", 纳甲)
        self.assertIn("二爻 妻财 甲寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14

    def test_辰月丁亥占辨复(self):
        纳甲 = 运行("六爻纳甲.py", "6 8 6 7 7 8\n\n")
        self.assertIn("主卦：䷬ 泽地萃", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("三爻 妻财 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己亥", 纳甲)
        self.assertIn("初爻 父母 乙未 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 己卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14

    def test_丑月己卯占父急病(self):
        纳甲 = 运行("六爻纳甲.py", "7 9 7 9 9 7\n\n")
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷕ 山火贲", 纳甲)
        self.assertIn("五爻 兄弟 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙子", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丙戌", 纳甲)
        self.assertIn("二爻 妻财 甲寅 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 己丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14

    def test_丑月戊午占姑病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 9 8 9\n\n")
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 癸酉", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15

    def test_未月戊申占子归期(self):
        纳甲 = 运行("六爻纳甲.py", "9 7 6 7 8 7\n\n")
        self.assertIn("主卦：䷥ 火泽睽", 纳甲)
        self.assertIn("变卦：䷱ 火风鼎", 纳甲)
        self.assertIn("三爻 兄弟 丁丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 辛酉", 纳甲)
        self.assertIn("初爻 父母 丁巳 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 辛丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15

    def test_巳月丙申占父归期(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 6 6 7\n\n")
        self.assertIn("主卦：䷙ 山天大畜", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("五爻 妻财 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬申", 纳甲)
        self.assertIn("四爻 兄弟 丙戌 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15

    def test_丑月戊辰占防参劾(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 9 8 7 6\n\n")
        self.assertIn("主卦：䷯ 水风井", 纳甲)
        self.assertIn("变卦：䷼ 风泽中孚", 纳甲)
        self.assertIn("上爻 父母 戊子 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 辛卯", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丁丑", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁巳", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第16页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=16

    def test_寅月戊午占地造葬(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 6 7\n\n")
        self.assertIn("主卦：䷚ 山雷颐", 纳甲)
        self.assertIn("变卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("五爻 父母 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 壬申", 纳甲)
        self.assertIn("四爻 妻财 丙戌 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第16页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=16

    def test_巳月甲辰占雨止(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 9 7 8 7\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 纳甲)
        self.assertIn("变卦：䷥ 火泽睽", 纳甲)
        self.assertIn("三爻 妻财 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丁丑", 纳甲)
        self.assertIn("初爻 子孙 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁巳", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第17页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=17

    def test_酉月辛卯妻去摇会(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 9 8 6\n\n")
        self.assertIn("主卦：䷟ 雷风恒", 纳甲)
        self.assertIn("变卦：䷑ 山风蛊", 纳甲)
        self.assertIn("上爻 妻财 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丙寅", 纳甲)
        self.assertIn("四爻 子孙 庚午 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丙戌", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18

    def test_卯月壬申占随官上任(self):
        纳甲 = 运行("六爻纳甲.py", "8 6 6 8 7 8\n\n")
        self.assertIn("主卦：䷇ 水地比", 纳甲)
        self.assertIn("变卦：䷯ 水风井", 纳甲)
        self.assertIn("三爻 官鬼 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 辛酉", 纳甲)
        self.assertIn("二爻 父母 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 辛亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18

    def test_卯月乙亥占升选(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 8 8 6 6\n\n")
        self.assertIn("主卦：䷒ 地泽临", 纳甲)
        self.assertIn("变卦：䷼ 风泽中孚", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 辛卯", 纳甲)
        self.assertIn("五爻 妻财 癸亥 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18

    def test_未月丁巳占嫂复病(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 9\n\n")
        self.assertIn("主卦：䷖ 山地剥", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("上爻 妻财 丙寅 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸酉", 纳甲)
        self.assertIn("五爻 子孙 丙子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第19页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=19

    def test_巳月戊申往前处脱货(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 6 7 7\n\n")
        self.assertIn("主卦：䷈ 风天小畜", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)
        self.assertIn("上爻 兄弟 辛卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第19页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=19

    def test_卯月戊子占坟地(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 8 9 9\n\n")
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷭ 地风升", 纳甲)
        self.assertIn("上爻 兄弟 辛卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 癸酉", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 癸亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第20页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=20

    def test_申月乙卯避兵(self):
        纳甲 = 运行("六爻纳甲.py", "7 6 6 7 9 9\n\n")
        self.assertIn("主卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("变卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("上爻 妻财 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚戌", 纳甲)
        self.assertIn("五爻 官鬼 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 庚申", 纳甲)
        self.assertIn("三爻 妻财 庚辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 甲辰", 纳甲)
        self.assertIn("二爻 兄弟 庚寅 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 甲寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第21页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=21

    def test_申月甲午占父在任(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 9 9\n\n")
        self.assertIn("主卦：䷫ 天风姤", 纳甲)
        self.assertIn("变卦：䷟ 雷风恒", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚戌", 纳甲)
        self.assertIn("五爻 兄弟 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第21页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=21

    def test_寅月乙卯客外占家中(self):
        纳甲 = 运行("六爻纳甲.py", "7 6 6 7 7 7\n\n")
        self.assertIn("主卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("三爻 妻财 庚辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 甲辰", 纳甲)
        self.assertIn("二爻 兄弟 庚寅 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 甲寅", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第22页；第七问巳月戊戌求财益卦，与已核《增删卜易》巳月戊戌占财同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=22

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第22页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=22

    def test_寅月乙卯占妻在家(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 6 6\n\n")
        self.assertIn("主卦：䷏ 雷地豫", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("上爻 妻财 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 壬戌", 纳甲)
        self.assertIn("五爻 官鬼 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 壬申", 纳甲)
        self.assertIn("四爻 子孙 庚午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23

    def test_亥月甲子占仆归期(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("四爻 兄弟 丁亥", 纳甲)
        self.assertIn("上爻 官鬼 丁未", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23

    def test_申月丁卯见贵求财(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 7\n\n")
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷌ 天火同人", 纳甲)
        self.assertIn("三爻 官鬼 己亥", 纳甲)
        self.assertIn("五爻 妻财 壬申", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23

    def test_子月癸酉自占婚(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 8 6\n\n")
        self.assertIn("主卦：䷟ 雷风恒", 纳甲)
        self.assertIn("变卦：䷱ 火风鼎", 纳甲)
        self.assertIn("上爻 妻财 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己巳", 纳甲)
        self.assertIn("三爻 官鬼 辛酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24

    def test_午月癸丑占妻病愈期(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 9 7 8\n\n")
        self.assertIn("主卦：䷬ 泽地萃", 纳甲)
        self.assertIn("变卦：䷇ 水地比", 纳甲)
        self.assertIn("四爻 子孙 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)
        self.assertIn("三爻 妻财 乙卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24

    def test_寅月庚戌占子病愈期(self):
        纳甲 = 运行("六爻纳甲.py", "6 9 9 7 7 7\n\n")
        self.assertIn("主卦：䷫ 天风姤", 纳甲)
        self.assertIn("变卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("三爻 兄弟 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚辰", 纳甲)
        self.assertIn("二爻 子孙 辛亥 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚寅", 纳甲)
        self.assertIn("初爻 父母 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 庚子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24

    def test_未月庚子占求财到手(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 7 7\n\n")
        self.assertIn("主卦：䷈ 风天小畜", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("三爻 妻财 甲辰", 纳甲)
        self.assertIn("四爻 妻财 辛未", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25

    def test_酉月庚辰占岳母近病(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 6 8 8 8\n\n")
        self.assertIn("主卦：䷆ 地水师", 纳甲)
        self.assertIn("变卦：䷭ 地风升", 纳甲)
        self.assertIn("三爻 妻财 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛酉", 纳甲)
        self.assertIn("上爻 父母 癸酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25

    def test_酉月壬辰占子病(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 7 8\n\n")
        self.assertIn("主卦：䷛ 泽风大过", 纳甲)
        self.assertIn("变卦：䷛ 泽风大过", 纳甲)
        self.assertIn("四爻 父母 丁亥", 纳甲)
        self.assertIn("三爻 官鬼 辛酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25

    def test_子月乙巳占弟尸首(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷗ 地雷复", 纳甲)
        self.assertIn("上爻 子孙 癸酉", 纳甲)
        self.assertIn("四爻 兄弟 癸丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第26页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=26

    def test_丑月甲午占父近病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 8 6\n\n")
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷔ 火雷噬嗑", 纳甲)
        self.assertIn("初爻 妻财 庚子", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 己巳", 纳甲)
        self.assertIn("四爻 兄弟 癸丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27

    def test_未月戊戌因大旱占雨(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 7 7\n\n")
        self.assertIn("主卦：䷓ 风地观", 纳甲)
        self.assertIn("变卦：䷓ 风地观", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27

    def test_未月戊戌占交疏人来期(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 8 7 8\n\n")
        self.assertIn("主卦：䷦ 水山蹇", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("四爻 兄弟 戊申", 纳甲)
        self.assertIn("五爻 父母 戊戌", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27

    def test_未月甲辰占大雨(self):
        纳甲 = 运行("六爻纳甲.py", "6 8 7 7 6 8\n\n")
        self.assertIn("主卦：䷽ 雷山小过", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("五爻 兄弟 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁酉", 纳甲)
        self.assertIn("初爻 父母 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 己卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第28页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=28

    def test_戌月丁卯占讼事(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 8 8\n\n")
        self.assertIn("主卦：䷊ 地天泰", 纳甲)
        self.assertIn("变卦：䷊ 地天泰", 纳甲)
        self.assertIn("三爻 兄弟 甲辰", 纳甲)
        self.assertIn("上爻 子孙 癸酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第29页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=29

    def test_亥月己丑占将来有官否(self):
        纳甲 = 运行("六爻纳甲.py", "9 7 8 7 7 6\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 纳甲)
        self.assertIn("变卦：䷅ 天水讼", 纳甲)
        self.assertIn("上爻 父母 丁未 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬戌", 纳甲)
        self.assertIn("初爻 官鬼 丁巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 戊寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第29页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=29

    def test_辰月戊子占父归期(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 7 9\n\n")
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷪ 泽天夬", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丁未", 纳甲)
        self.assertIn("初爻 子孙 甲子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第30页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=30

    def test_午月癸卯占后运功名(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 9 8 6 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 纳甲)
        self.assertIn("变卦：䷓ 风地观", 纳甲)
        self.assertIn("五爻 妻财 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 乙卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第30页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=30

    def test_寅月甲午占子病(self):
        纳甲 = 运行("六爻纳甲.py", "8 6 9 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 纳甲)
        self.assertIn("变卦：䷃ 山水蒙", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊午", 纳甲)
        self.assertIn("二爻 父母 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 戊辰", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第31页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=31

    def test_丑月庚申占坟地风水(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 7 7 8\n\n")
        self.assertIn("主卦：䷞ 泽山咸", 纳甲)
        self.assertIn("变卦：䷞ 泽山咸", 纳甲)
        self.assertIn("三爻 兄弟 丙申", 纳甲)
        self.assertIn("上爻 父母 丁未", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第31页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=31

    def test_申月辛卯占买宅(self):
        纳甲 = 运行("六爻纳甲.py", "7 6 7 7 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷪ 泽天夬", 纳甲)
        self.assertIn("二爻 官鬼 己丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 甲寅", 纳甲)
        self.assertIn("三爻 兄弟 己亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第32页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=32

    def test_卯月壬辰占候文书(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 8 8 7\n\n")
        self.assertIn("主卦：䷕ 山火贲", 纳甲)
        self.assertIn("变卦：䷕ 山火贲", 纳甲)
        self.assertIn("二爻 兄弟 己丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第32页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=32

    def test_辰月丁巳占逃仆(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 8 7 8\n\n")
        self.assertIn("主卦：䷦ 水山蹇", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("二爻 官鬼 丙午", 纳甲)
        self.assertIn("初爻 父母 丙辰", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33

    def test_酉月丙辰占子病(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 8 8 8\n\n")
        self.assertIn("主卦：䷭ 地风升", 纳甲)
        self.assertIn("变卦：䷭ 地风升", 纳甲)
        self.assertIn("二爻 父母 辛亥", 纳甲)
        self.assertIn("五爻 父母 癸亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33

    def test_卯月丙辰占父病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷗ 地雷复", 纳甲)
        self.assertIn("二爻 官鬼 庚寅", 纳甲)
        self.assertIn("四爻 兄弟 癸丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33

    def test_辰月庚申占蚕桑叶贵贱(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 8 7 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 纳甲)
        self.assertIn("变卦：䷾ 水火既济", 纳甲)
        self.assertIn("三爻 兄弟 己亥", 纳甲)
        self.assertIn("上爻 兄弟 戊子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第34页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=34

    def test_寅月戊辰占病有何鬼神(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 7 7\n\n")
        self.assertIn("主卦：䷈ 风天小畜", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("三爻 妻财 甲辰", 纳甲)
        self.assertIn("四爻 妻财 辛未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第36页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=36

    def test_申月癸卯占乡试(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 6 8\n\n")
        self.assertIn("主卦：䷟ 雷风恒", 纳甲)
        self.assertIn("变卦：䷛ 泽风大过", 纳甲)
        self.assertIn("五爻 官鬼 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁酉", 纳甲)
        self.assertIn("三爻 官鬼 辛酉", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第36页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=36

    def test_酉月庚戌占生子年(self):
        纳甲 = 运行("六爻纳甲.py", "7 6 8 8 7 8\n\n")
        self.assertIn("主卦：䷂ 水雷屯", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)
        self.assertIn("二爻 子孙 庚寅 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁卯", 纳甲)
        self.assertIn("五爻 官鬼 戊戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第37页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=37

    def test_卯月乙丑自占求婚(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 8 9 6 9\n\n")
        self.assertIn("主卦：䷔ 火雷噬嗑", 纳甲)
        self.assertIn("变卦：䷇ 水地比", 纳甲)
        self.assertIn("上爻 子孙 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊子", 纳甲)
        self.assertIn("五爻 妻财 己未 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 戊戌", 纳甲)
        self.assertIn("四爻 官鬼 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊申", 纳甲)
        self.assertIn("初爻 父母 庚子 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 乙未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第37页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=37

    def test_酉月甲辰因参论占自陈(self):
        纳甲 = 运行("六爻纳甲.py", "6 9 6 8 8 8\n\n")
        self.assertIn("主卦：䷆ 地水师", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("三爻 妻财 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 己亥", 纳甲)
        self.assertIn("二爻 官鬼 戊辰 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 己丑", 纳甲)
        self.assertIn("初爻 子孙 戊寅 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己卯", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第38页；第十一问午月丙辰出外贸易恒之豫，与已核《增删卜易》午月丙辰经商同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第38页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    def test_未月丁卯占出仕功名(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 9\n\n")
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("上爻 子孙 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丁未", 纳甲)
        self.assertIn("三爻 官鬼 己亥", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第38页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    def test_戌月甲辰占借银(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("五爻 妻财 癸亥", 纳甲)
        self.assertIn("初爻 兄弟 乙未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第39页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=39

    def test_寅月戊戌占失银物(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 9 6 7 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷅ 天水讼", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40

    def test_辰月丁酉自占婚姻(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 7 7\n\n")
        self.assertIn("主卦：䷋ 天地否", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("三爻 妻财 乙卯", 纳甲)
        self.assertIn("上爻 父母 壬戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40

    def test_卯月乙卯占谋望求财(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 7 8\n\n")
        self.assertIn("主卦：䷛ 泽风大过", 纳甲)
        self.assertIn("变卦：䷛ 泽风大过", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40

    def test_午月辛亥占师近病(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 8 8 7 8\n\n")
        self.assertIn("主卦：䷻ 水泽节", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)
        self.assertIn("四爻 父母 戊申", 纳甲)
        self.assertIn("初爻 妻财 丁巳", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第41页；第十一问未月丁巳悔婚离之旅，与已核《增删卜易》未月丁巳悔婚同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=41

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第41页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=41

    def test_寅月戊辰占兄近病(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 8 7\n\n")
        self.assertIn("主卦：䷢ 火地晋", 纳甲)
        self.assertIn("变卦：䷢ 火地晋", 纳甲)
        self.assertIn("四爻 兄弟 己酉", 纳甲)
        self.assertIn("上爻 官鬼 己巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第42页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=42

    def test_巳月戊寅占何日得财(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 8 9\n\n")
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷶ 雷火丰", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 庚戌", 纳甲)
        self.assertIn("四爻 妻财 己酉", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第42页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=42

    def test_午月己卯占妻病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 6 7 8 8\n\n")
        self.assertIn("主卦：䷲ 震为雷", 纳甲)
        self.assertIn("变卦：䷶ 雷火丰", 纳甲)
        self.assertIn("三爻 妻财 庚辰 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 己亥", 纳甲)
        self.assertIn("上爻 妻财 庚戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43

    def test_寅月戊子占生产(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 6 7\n\n")
        self.assertIn("主卦：䷖ 山地剥", 纳甲)
        self.assertIn("变卦：䷓ 风地观", 纳甲)
        self.assertIn("五爻 子孙 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 辛巳", 纳甲)
        self.assertIn("上爻 妻财 丙寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43

    def test_子月辛未占子病(self):
        纳甲 = 运行("六爻纳甲.py", "6 6 9 8 7 7\n\n")
        self.assertIn("主卦：䷴ 风山渐", 纳甲)
        self.assertIn("变卦：䷼ 风泽中孚", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 丁丑", 纳甲)
        self.assertIn("二爻 父母 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁卯", 纳甲)
        self.assertIn("初爻 兄弟 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 丁巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43

    def test_辰月甲寅占父病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 9 8\n\n")
        self.assertIn("主卦：䷂ 水雷屯", 纳甲)
        self.assertIn("变卦：䷲ 震为雷", 纳甲)
        self.assertIn("五爻 官鬼 戊戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚申", 纳甲)
        self.assertIn("四爻 父母 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 庚午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第44页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=44

    def test_申月丙辰占弟病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 9 8\n\n")
        self.assertIn("主卦：䷾ 水火既济", 纳甲)
        self.assertIn("变卦：䷶ 雷火丰", 纳甲)
        self.assertIn("五爻 官鬼 戊戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚申", 纳甲)
        self.assertIn("四爻 父母 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 庚午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第45页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=45

    def test_申月癸丑占子在楚生理(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 8 8 8 7\n\n")
        self.assertIn("主卦：䷨ 山泽损", 纳甲)
        self.assertIn("变卦：䷨ 山泽损", 纳甲)
        self.assertIn("四爻 兄弟 丙戌", 纳甲)
        self.assertIn("上爻 官鬼 丙寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第45页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=45

    def test_叔占侄在外平安(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 9 9 7\n\n")
        self.assertIn("主卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("变卦：䷚ 山雷颐", 纳甲)
        self.assertIn("五爻 官鬼 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丙子", 纳甲)
        self.assertIn("四爻 子孙 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丙戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46

    def test_亥月丙寅嫂占姑病(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 9 7 8\n\n")
        self.assertIn("主卦：䷞ 泽山咸", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("四爻 子孙 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)
        self.assertIn("初爻 父母 丙辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46

    def test_卯月乙未姑占弟妇怀孕(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 8 9 7 8\n\n")
        self.assertIn("主卦：䷮ 泽水困", 纳甲)
        self.assertIn("变卦：䷜ 坎为水", 纳甲)
        self.assertIn("四爻 子孙 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)
        self.assertIn("上爻 父母 丁未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46

    def test_丁卯占劾奏他人(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 7 8 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)
        self.assertIn("三爻 妻财 丙申", 纳甲)
        self.assertIn("上爻 兄弟 己巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第47页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=47

    def test_未月戊申因误军粮被参(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 8 6\n\n")
        self.assertIn("主卦：䷶ 雷火丰", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)
        self.assertIn("上爻 官鬼 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 己巳", 纳甲)
        self.assertIn("初爻 子孙 己卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 丙辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第47页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=47

    def test_卯月壬寅占坟地(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 9 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷾ 水火既济", 纳甲)
        self.assertIn("四爻 兄弟 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊申", 纳甲)
        self.assertIn("三爻 兄弟 己亥", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第48页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=48

    def test_酉月壬子占侄被害(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 8 8\n\n")
        self.assertIn("主卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("变卦：䷊ 地天泰", 纳甲)
        self.assertIn("四爻 父母 庚午 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸丑", 纳甲)
        self.assertIn("上爻 兄弟 庚戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第48页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=48

    def test_巳月丁酉占文书到期(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 7 7\n\n")
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("上爻 父母 壬戌", 纳甲)
        self.assertIn("三爻 父母 甲辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49

    def test_午月丙子占开店(self):
        纳甲 = 运行("六爻纳甲.py", "9 7 7 9 6 6\n\n")
        self.assertIn("主卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("变卦：䷸ 巽为风", 纳甲)
        self.assertIn("上爻 兄弟 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 辛卯", 纳甲)
        self.assertIn("五爻 子孙 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)
        self.assertIn("四爻 父母 庚午 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 辛未", 纳甲)
        self.assertIn("初爻 妻财 甲子 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 辛丑", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49

    def test_申月乙卯因子被拿占讼(self):
        纳甲 = 运行("六爻纳甲.py", "8 9 9 8 9 9\n\n")
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("上爻 兄弟 辛卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 癸酉", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 癸亥", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 乙卯", 纳甲)
        self.assertIn("二爻 父母 辛亥 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 乙巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49

    def test_未月乙亥往买卖求利(self):
        纳甲 = 运行("六爻纳甲.py", "7 9 8 7 9 8\n\n")
        self.assertIn("主卦：䷹ 兑为泽", 纳甲)
        self.assertIn("变卦：䷲ 震为雷", 纳甲)
        self.assertIn("五爻 兄弟 丁酉 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)
        self.assertIn("二爻 妻财 丁卯 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第50页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=50

    def test_子月己巳占赌钱(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("五爻 妻财 癸亥", 纳甲)
        self.assertIn("三爻 官鬼 乙卯", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第50页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=50

    def test_辰月庚午占会(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 6 7 7\n\n")
        self.assertIn("主卦：䷓ 风地观", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("四爻 父母 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 壬午", 纳甲)
        self.assertIn("五爻 官鬼 辛巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51

    def test_寅月甲午占子久病(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 8 8\n\n")
        self.assertIn("主卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("变卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("五爻 子孙 庚申", 纳甲)
        self.assertIn("四爻 父母 庚午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51

    def test_卯月甲午占起去寄信(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 7 7\n\n")
        self.assertIn("主卦：䷋ 天地否", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("三爻 妻财 乙卯", 纳甲)
        self.assertIn("四爻 官鬼 壬午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51

    def test_巳月甲戌同乡占借贷(self):
        纳甲 = 运行("六爻纳甲.py", "9 8 8 6 8 8\n\n")
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷏ 雷地豫", 纳甲)
        self.assertIn("四爻 兄弟 癸丑 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 庚午", 纳甲)
        self.assertIn("初爻 妻财 庚子 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 乙未", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第52页；第十三问巳月甲寅延师训子否之乾，与已核《增删卜易》巳月甲寅严师训子同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=52

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53

    def test_寅月庚申占侄孙病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 9 7\n\n")
        self.assertIn("主卦：䷤ 风火家人", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 己未", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己酉", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53

    def test_辰月戊午占夫病(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 9 9 8 7\n\n")
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷚ 山雷颐", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙戌", 纳甲)
        self.assertIn("三爻 官鬼 己亥 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 庚辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53

    def test_亥月戊戌占妻近病(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 7 6 9 7\n\n")
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷍ 火天大有", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 己未", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己酉", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 甲子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第54页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=54

    def test_戌月庚子占冬生意(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 8 6 7\n\n")
        self.assertIn("主卦：䷕ 山火贲", 纳甲)
        self.assertIn("变卦：䷤ 风火家人", 纳甲)
        self.assertIn("五爻 妻财 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)
        self.assertIn("上爻 官鬼 丙寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第54页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=54

    def test_午月丙午占自去请父回(self):
        纳甲 = 运行("六爻纳甲.py", "7 9 7 7 8 7\n\n")
        self.assertIn("主卦：䷍ 火天大有", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("二爻 妻财 甲寅 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 己丑", 纳甲)
        self.assertIn("三爻 父母 甲辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第55页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=55

    def test_再占请父回(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 9 7 8\n\n")
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷾ 水火既济", 纳甲)
        self.assertIn("四爻 兄弟 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊申", 纳甲)
        self.assertIn("上爻 官鬼 丁未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第55页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=55

    def test_申月辛卯占子嗣(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷗ 地雷复", 纳甲)
        self.assertIn("上爻 子孙 癸酉", 纳甲)
        self.assertIn("初爻 妻财 庚子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56

    def test_午月甲申占雨久伤麦(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 9\n\n")
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("上爻 子孙 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丁未", 纳甲)
        self.assertIn("四爻 兄弟 壬午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56

    def test_申月甲午开煤窑占见煤时(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 9 8 7 7\n\n")
        self.assertIn("主卦：䷤ 风火家人", 纳甲)
        self.assertIn("变卦：䷩ 风雷益", 纳甲)
        self.assertIn("三爻 父母 己亥 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚辰", 纳甲)
        self.assertIn("四爻 妻财 辛未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56

    def test_寅月庚戌占父病(self):
        纳甲 = 运行("六爻纳甲.py", "8 9 6 9 6 9\n\n")
        self.assertIn("主卦：䷿ 火水未济", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊子", 纳甲)
        self.assertIn("五爻 子孙 己未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 戊戌", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 戊申", 纳甲)
        self.assertIn("三爻 兄弟 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 丙申", 纳甲)
        self.assertIn("二爻 子孙 戊辰 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 丙午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第57页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=57

    def test_寅月甲辰占父远出归期(self):
        纳甲 = 运行("六爻纳甲.py", "6 6 9 7 9 9\n\n")
        self.assertIn("主卦：䷠ 天山遁", 纳甲)
        self.assertIn("变卦：䷵ 雷泽归妹", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚戌", 纳甲)
        self.assertIn("五爻 兄弟 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)
        self.assertIn("三爻 兄弟 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丁丑", 纳甲)
        self.assertIn("二爻 官鬼 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 丁卯", 纳甲)
        self.assertIn("初爻 父母 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第57至58页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=57

    def test_午月庚辰占仆近出归期(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 8 7\n\n")
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("四爻 妻财 己酉", 纳甲)
        self.assertIn("二爻 子孙 己丑", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第58页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=58

    def test_辰月己卯占今日还银(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("五爻 妻财 癸亥", 纳甲)
        self.assertIn("初爻 兄弟 乙未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第58至59页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=58

    def test_子月壬申占父在乱军(self):
        纳甲 = 运行("六爻纳甲.py", "9 9 9 6 6 9\n\n")
        self.assertIn("主卦：䷙ 山天大畜", 纳甲)
        self.assertIn("变卦：䷬ 泽地萃", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第59页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=59

    def test_辰月甲子造坟葬亲(self):
        纳甲 = 运行("六爻纳甲.py", "9 9 9 9 9 9\n\n")
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸酉", 纳甲)
        self.assertIn("五爻 兄弟 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸亥", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 癸丑", 纳甲)
        self.assertIn("三爻 父母 甲辰 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 乙卯", 纳甲)
        self.assertIn("二爻 妻财 甲寅 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 乙巳", 纳甲)
        self.assertIn("初爻 子孙 甲子 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 乙未", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第60页；第十七问未月庚子占求财小畜卦，与第七问同案重见，已按首次出现顺序列测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第60页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60

    def test_未月甲午占自升迁(self):
        纳甲 = 运行("六爻纳甲.py", "8 7 8 8 6 6\n\n")
        self.assertIn("主卦：䷆ 地水师", 纳甲)
        self.assertIn("变卦：䷺ 风水涣", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第60页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60

    def test_亥月丙午占子脱难(self):
        纳甲 = 运行("六爻纳甲.py", "6 6 8 7 8 8\n\n")
        self.assertIn("主卦：䷏ 雷地豫", 纳甲)
        self.assertIn("变卦：䷵ 雷泽归妹", 纳甲)
        self.assertIn("二爻 子孙 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁卯", 纳甲)
        self.assertIn("初爻 妻财 乙未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁巳", 纳甲)
        self.assertIn("三爻 兄弟 乙卯", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第61页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=61

    def test_未月丁丑占子久出归期(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 7 9 6 9\n\n")
        self.assertIn("主卦：䷱ 火风鼎", 纳甲)
        self.assertIn("变卦：䷄ 水天需", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊子", 纳甲)
        self.assertIn("五爻 子孙 己未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 戊戌", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 戊申", 纳甲)
        self.assertIn("初爻 子孙 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 甲子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第61页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=61

    def test_寅月癸亥占子嗣(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 6 8 8 6\n\n")
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷳ 艮为山", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丙寅", 纳甲)
        self.assertIn("三爻 官鬼 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丙申", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第62页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=62

    def test_酉月戊申占伯父归期(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 9 8 7\n\n")
        self.assertIn("主卦：䷷ 火山旅", 纳甲)
        self.assertIn("变卦：䷳ 艮为山", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙戌", 纳甲)
        self.assertIn("上爻 兄弟 己巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第62页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=62

    def test_申月乙亥占家宅(self):
        纳甲 = 运行("六爻纳甲.py", "6 7 9 8 7 8\n\n")
        self.assertIn("主卦：䷯ 水风井", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)
        self.assertIn("五爻 妻财 戊戌", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁巳", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丁丑", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第63页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=63

    def test_未月癸亥占流年(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 7 8 8 7\n\n")
        self.assertIn("主卦：䷳ 艮为山", 纳甲)
        self.assertIn("变卦：䷳ 艮为山", 纳甲)
        self.assertIn("上爻 官鬼 丙寅", 纳甲)
        self.assertIn("三爻 子孙 丙申", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第63页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=63

    def test_子月乙酉占现任吉凶(self):
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 7 8\n\n")
        self.assertIn("主卦：䷄ 水天需", 纳甲)
        self.assertIn("变卦：䷄ 水天需", 纳甲)
        self.assertIn("四爻 子孙 戊申", 纳甲)
        self.assertIn("初爻 妻财 甲子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第64页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=64

    def test_午月辛丑因母病问流年(self):
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 7 7\n\n")
        self.assertIn("主卦：䷩ 风雷益", 纳甲)
        self.assertIn("变卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)
        self.assertIn("三爻 妻财 庚辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第64页；爻值依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=64

    def test_午月辛酉父为十二岁子占功名(self):
        纳甲 = 运行("六爻纳甲.py", "8 8 6 7 7 6\n\n")
        self.assertIn("主卦：䷬ 泽地萃", 纳甲)
        self.assertIn("变卦：䷠ 天山遁", 纳甲)
        self.assertIn("上爻 父母 丁未 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬戌", 纳甲)
        self.assertIn("三爻 妻财 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丙申", 纳甲)

    # 《升庵先生文集》卷七十五“六神”仅论起例，未载实占；万历刻本第7页为戊己共起勾陈、壬起螣蛇 https://upload.wikimedia.org/wikipedia/commons/9/98/Harvard_drs_51546102_%E5%8D%87%E8%8F%B4%E5%85%88%E7%94%9F%E6%96%87%E9%9B%86_v.22.pdf#page=7
