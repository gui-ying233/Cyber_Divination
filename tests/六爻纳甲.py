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

    # 《高島易斷》1901增补本下经贞原影第95–96页，大浦难船案记筮得涣之讼、六四；爻值依原卦和动爻换算 https://dl.ndl.go.jp/pid/760555/1/95

    def test_高岛占大浦难船(self):
        输出 = 运行("六爻纳甲.py", "8 7 8 6 7 7\n\n")
        self.assertIn("主卦：䷺ 风水涣", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)
        self.assertRegex(输出, r"(?m)^四爻 .*⚋ ×")
        self.assertEqual([行[0] for 行 in 输出.splitlines() if "○" in 行 or "×" in 行], ["四"])

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
