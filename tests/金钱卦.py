import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《增删卜易》占卦法假设例，秦慎安校勘本PDF第22–24页记六次背数1、2、3、0、3、2及水火既济 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=23

    def test_占卦法既济例(self):
        输出 = 运行("金钱卦.py", "1\n1 2 3 0 3 2\n")
        self.assertIn("本卦：䷾ 水火既济", 输出)
        self.assertIn("动爻：三爻、四爻、五爻", 输出)
        self.assertIn("初爻：1背，7，单（少阳） ⚊", 输出)
        self.assertIn("二爻：2背，8，拆（少阴） ⚋", 输出)
        self.assertIn("三爻：3背，9，重（老阳） ⚊ ○", 输出)
        self.assertIn("四爻：0背，6，交（老阴） ⚋ ×", 输出)
        self.assertIn("五爻：3背，9，重（老阳） ⚊ ○", 输出)
        self.assertIn("上爻：2背，8，拆（少阴） ⚋", 输出)

    # 《增删卜易》占卦法再排一卦假设例，秦慎安校勘本PDF第24页记六次背数2、3、2、1、0、1及火水未济 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=24

    def test_占卦法未济例(self):
        输出 = 运行("金钱卦.py", "1\n2 3 2 1 0 1\n")
        self.assertIn("本卦：䷿ 火水未济", 输出)
        self.assertIn("动爻：二爻、五爻", 输出)
        self.assertIn("初爻：2背，8，拆（少阴） ⚋", 输出)
        self.assertIn("二爻：3背，9，重（老阳） ⚊ ○", 输出)
        self.assertIn("三爻：2背，8，拆（少阴） ⚋", 输出)
        self.assertIn("四爻：1背，7，单（少阳） ⚊", 输出)
        self.assertIn("五爻：0背，6，交（老阴） ⚋ ×", 输出)
        self.assertIn("上爻：1背，7，单（少阳） ⚊", 输出)

    # 《增删卜易》用神章乾卦假设例，秦慎安校勘本PDF第38页原六爻皆静，背数依爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=38

    def test_用神章乾卦例(self):
        输出 = 运行("金钱卦.py", "1\n1 1 1 1 1 1\n")
        self.assertIn("本卦：䷀ 乾为天", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》第9章“辰月戊申日占父近病”，秦慎安校勘本PDF第50–51页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=50

    def test_辰月戊申占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 1\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)

    # 《增删卜易》元神忌神衰旺章第十“酉月辛卯日占谒贵求财”，秦慎安校勘本PDF第52页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=52

    def test_酉月辛卯占谒贵求财(self):
        输出 = 运行("金钱卦.py", "1\n3 1 2 1 3 2\n")
        self.assertIn("本卦：䷹ 兑为泽", 输出)
        self.assertIn("动爻：初爻、五爻", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)

    # 《增删卜易》第10章“巳月乙未日自占病”，秦慎安校勘本PDF第54页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=54

    def test_巳月乙未自占病(self):
        输出 = 运行("金钱卦.py", "1\n2 1 1 1 3 0\n")
        self.assertIn("本卦：䷛ 泽风大过", 输出)
        self.assertIn("动爻：五爻、上爻", 输出)
        self.assertIn("变卦：䷱ 火风鼎", 输出)

    # 《增删卜易》第11章“卯月己卯日弟占兄重罪”，秦慎安校勘本PDF第54–55页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=54

    def test_卯月己卯占兄重罪(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 0 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 输出)
        self.assertIn("动爻：四爻", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)

    # 《增删卜易》第12章“卯月戊寅日占父官事”，秦慎安校勘本PDF第55页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=55

    def test_卯月戊寅占父官事(self):
        输出 = 运行("金钱卦.py", "1\n0 2 0 1 1 0\n")
        self.assertIn("本卦：䷬ 泽地萃", 输出)
        self.assertIn("动爻：初爻、三爻、上爻", 输出)
        self.assertIn("变卦：䷌ 天火同人", 输出)

    # 《增删卜易》第12章“同日妹占兄官事”，秦慎安校勘本PDF第55–56页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=56

    def test_卯月戊寅妹占兄官事(self):
        输出 = 运行("金钱卦.py", "1\n2 0 2 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 输出)
        self.assertIn("动爻：二爻", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)

    # 《增删卜易》第13章“辰月丙申占弟痘症”，秦慎安校勘本PDF第57页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=57

    def test_辰月丙申占弟痘症(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 1 2\n")
        self.assertIn("本卦：䷾ 水火既济", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)

    # 《增删卜易》第14章“假令春天寅卯月占得坤卦”假设例，秦慎安校勘本PDF第57页；背数依原静爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=57

    def test_春天寅卯月坤卦例(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》第14章“假令寅月占得兑卦变归妹”假设例，秦慎安校勘本PDF第58页；背数依原五爻动爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=58

    def test_寅月兑之归妹例(self):
        输出 = 运行("金钱卦.py", "1\n1 1 2 1 3 2\n")
        self.assertIn("本卦：䷹ 兑为泽", 输出)
        self.assertIn("动爻：五爻", 输出)
        self.assertIn("变卦：䷵ 雷泽归妹", 输出)

    # 《增删卜易》第15章“假令子月卯日占得坤卦变火地晋”假设例，秦慎安校勘本PDF第58–59页；背数依原四、上爻动爻画换算 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=58

    def test_子月卯日坤之晋例(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 0 2 0\n")
        self.assertIn("本卦：䷁ 坤为地", 输出)
        self.assertIn("动爻：四爻、上爻", 输出)
        self.assertIn("变卦：䷢ 火地晋", 输出)

    # 《增删卜易》第16章“寅月庚戌占求财”，秦慎安校勘本PDF第62页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=62

    def test_寅月庚戌占求财(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 2 1\n")
        self.assertIn("本卦：䷍ 火天大有", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《增删卜易》第16章“酉月丙寅占谒贵”，秦慎安校勘本PDF第62页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=62

    def test_酉月丙寅占谒贵(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 2 2 1\n")
        self.assertIn("本卦：䷑ 山风蛊", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷃ 山水蒙", 钱卦)

    # 《增删卜易》第16章“寅月丙申占升迁”，秦慎安校勘本PDF第63页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=63

    def test_寅月丙申占升迁(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 3 2 2 1\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷚ 山雷颐", 钱卦)

    # 《增删卜易》第16章“午月丁未占弟被讼”，秦慎安校勘本PDF第64页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=64

    def test_午月丁未占弟被讼(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 0 1 3 2\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：三爻、五爻", 钱卦)
        self.assertIn("变卦：䷟ 雷风恒", 钱卦)

    # 《增删卜易》第16章“寅月辛酉占开铺”，秦慎安校勘本PDF第65页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=65

    def test_寅月辛酉占开铺(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 1 2 2 3\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：初爻、上爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)

    # 《增删卜易》第16章“午月戊辰占妹临产”，秦慎安校勘本PDF第66页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=66

    def test_午月戊辰占妹临产(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 2 1\n")
        self.assertIn("本卦：䷢ 火地晋", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《增删卜易》第17章“申月戊午自占病”，秦慎安校勘本PDF第68页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=68

    def test_申月戊午自占病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 1 1 1 1\n")
        self.assertIn("本卦：䷠ 天山遁", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷫ 天风姤", 钱卦)

    # 《增删卜易》第17章“巳月丁亥占仆归期”，秦慎安校勘本PDF第68页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=68

    def test_巳月丁亥占仆归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 3 1 1 0\n")
        self.assertIn("本卦：䷪ 泽天夬", 钱卦)
        self.assertIn("动爻：三爻、上爻", 钱卦)
        self.assertIn("变卦：䷉ 天泽履", 钱卦)

    # 《增删卜易》第十八章戊子占生产，秦慎安校勘本PDF第72页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=72

    def test_戊子日占生产(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 0 1\n")
        self.assertIn("本卦：䷖ 山地剥", 输出)
        self.assertIn("动爻：五爻", 输出)
        self.assertIn("变卦：䷓ 风地观", 输出)

    # 《增删卜易》第18章“申月甲辰日占兄病”，秦慎安校勘本PDF第72–73页原载屯之震与土申两动，背数据本变换算；五爻动符与变栏不合 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=73

    def test_申月甲辰占兄病(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 0 3 2\n")
        self.assertIn("本卦：䷂ 水雷屯", 输出)
        self.assertIn("动爻：四爻、五爻", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)

    # 《增删卜易》第19章“申月丙子日占得出行”，秦慎安校勘本PDF第75页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=75

    def test_申月丙子占出门(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 0 2 2\n")
        self.assertIn("本卦：䷣ 地火明夷", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷽ 雷山小过", 钱卦)

    # 《增删卜易》第19章“未月丁巳日占已悔婚还可成否”，秦慎安校勘本PDF第75–76页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=75

    def test_未月丁巳占悔婚(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 2 1\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)

    # 《增删卜易》第19章“卯月甲寅日占风水”，秦慎安校勘本PDF第77页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=77

    def test_卯月甲寅占风水(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 2 3 1 2\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)

    # 《增删卜易》第19章“卯月丁巳日上下两村因争用水殴打”，秦慎安校勘本PDF第79页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=79

    def test_卯月丁巳争田水(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 3 3 2 3\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻、三爻、四爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)

    # 《增删卜易》第20章“巳月戊戌日占财”，秦慎安校勘本PDF第80–81页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=80

    def test_巳月戊戌占财(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 2 1 1\n")
        self.assertIn("本卦：䷩ 风雷益", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》第20章“午月丙辰日占出外贸易财喜”，秦慎安校勘本PDF第81页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=81

    def test_午月丙辰经商(self):
        输出 = 运行("金钱卦.py", "1\n2 3 3 1 2 2\n")
        self.assertIn("本卦：䷟ 雷风恒", 输出)
        self.assertIn("动爻：二爻、三爻", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)

    # 《增删卜易》第20章“酉月乙未日占子久出不归”，秦慎安校勘本PDF第81–82页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=81

    def test_酉月乙未占子(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》第20章“巳月甲寅日占延师训子”，秦慎安校勘本PDF第82页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=82

    def test_巳月甲寅严师训子(self):
        输出 = 运行("金钱卦.py", "1\n0 0 0 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 输出)
        self.assertIn("动爻：初爻、二爻、三爻", 输出)
        self.assertIn("变卦：䷀ 乾为天", 输出)

    # 《增删卜易》第20章“申月乙卯日父子七人”，秦慎安校勘本PDF第82–83页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=82

    def test_申月乙卯父子七人(self):
        输出 = 运行("金钱卦.py", "1\n2 3 3 2 3 3\n")
        self.assertIn("本卦：䷸ 巽为风", 输出)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 输出)
        self.assertIn("变卦：䷁ 坤为地", 输出)

    # 《增删卜易》第21章“寅月庚申占子痘症”，秦慎安校勘本PDF第83页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=83

    def test_寅月庚申占子痘症(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 3 1\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)

    # 《增删卜易》第22章“寅月己未占女痘”，秦慎安校勘本PDF第84页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=84

    def test_寅月己未占女痘(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷆ 地水师", 钱卦)

    # 《增删卜易》第23章“丑月丁酉占父出外”，秦慎安校勘本PDF第85页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=85

    def test_丑月丁酉占父出外(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 2 2 1 3\n")
        self.assertIn("本卦：䷺ 风水涣", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷜ 坎为水", 钱卦)

    # 《增删卜易》第24章“卯月辛巳代占长辈功名”，秦慎安校勘本PDF第87页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=87

    def test_卯月辛巳代占长辈功名(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 1 0 1 1\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)

    # 《增删卜易》第24章“午月丙寅占主病”，秦慎安校勘本PDF第87页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=87

    def test_午月丙寅占主病(self):
        钱卦 = 运行("金钱卦.py", "1\n3 0 3 3 0 3\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷜ 坎为水", 钱卦)

    # 《卜筮正宗》十八问答所记伏神、暗动、月破、应期等未在当前脚本输出，只重放明爻主变与纳甲 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf

    # 《卜筮正宗》卷十三十八问答第一问，光绪十五年重刻本第六册PDF第4页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=4

    def test_申月戊子占坟地(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 1\n")
        self.assertIn("本卦：䷖ 山地剥", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第5页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=5

    def test_卯月癸亥占家宅人口(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 0 1 0\n")
        self.assertIn("本卦：䷄ 水天需", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第6页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=6

    def test_卯月乙未占卖货(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 1 2 1 1\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第7页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=7

    def test_酉月丙寅占何日雨(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 2 2 2\n")
        self.assertIn("本卦：䷭ 地风升", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷆ 地水师", 钱卦)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第8页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=8

    def test_卯月乙酉占索房价(self):
        钱卦 = 运行("金钱卦.py", "1\n2 3 2 2 3 2\n")
        self.assertIn("本卦：䷜ 坎为水", 钱卦)
        self.assertIn("动爻：二爻、五爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第9页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=9

    def test_申月戊辰占具题(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 2 2 2 0\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：初爻、二爻、上爻", 钱卦)
        self.assertIn("变卦：䷨ 山泽损", 钱卦)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第9页；背数依原爻画换算，未记年份 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=9

    def test_丁巳占虑大计(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 1 3 2 3\n")
        self.assertIn("本卦：䷷ 火山旅", 钱卦)
        self.assertIn("动爻：初爻、四爻、上爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第10页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=10

    def test_申月戊辰妻占夫近病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 3 1\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第10页；第三问卯月甲寅占风水困之节，与现有《增删卜易》卯月甲寅占风水为同案。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=10

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第11页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=11

    def test_丑月戊子自占近病(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 3 1\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：初爻、五爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第11页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=11

    def test_寅月乙丑子占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 2 2 2\n")
        self.assertIn("本卦：䷭ 地风升", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷆ 地水师", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第12页；第四问卯月丁巳两村争戽水，与已核《增删卜易》卯月丁巳争田水同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=12

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第13页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=13

    def test_巳月丁酉递呈谋补缺(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 3\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷄ 水天需", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第13页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=13

    def test_寅月丙辰占选期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 1\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14

    def test_辰月丁亥占辨复(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 0 1 1 2\n")
        self.assertIn("本卦：䷬ 泽地萃", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14

    def test_丑月己卯占父急病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 3 1 3 3 1\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：二爻、四爻、五爻", 钱卦)
        self.assertIn("变卦：䷕ 山火贲", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14

    def test_丑月戊午占姑病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 3 2 3\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15

    def test_未月戊申占子归期(self):
        钱卦 = 运行("金钱卦.py", "1\n3 1 0 1 2 1\n")
        self.assertIn("本卦：䷥ 火泽睽", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷱ 火风鼎", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15

    def test_巳月丙申占父归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 0 0 1\n")
        self.assertIn("本卦：䷙ 山天大畜", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15

    def test_丑月戊辰占防参劾(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 3 2 1 0\n")
        self.assertIn("本卦：䷯ 水风井", 钱卦)
        self.assertIn("动爻：初爻、三爻、上爻", 钱卦)
        self.assertIn("变卦：䷼ 风泽中孚", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第16页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=16

    def test_寅月戊午占地造葬(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 0 1\n")
        self.assertIn("本卦：䷚ 山雷颐", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷘ 天雷无妄", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第16页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=16

    def test_巳月甲辰占雨止(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 3 1 2 1\n")
        self.assertIn("本卦：䷱ 火风鼎", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷥ 火泽睽", 钱卦)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第17页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=17

    def test_酉月辛卯妻去摇会(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 3 2 0\n")
        self.assertIn("本卦：䷟ 雷风恒", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷑ 山风蛊", 钱卦)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18

    def test_卯月壬申占随官上任(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 0 2 1 2\n")
        self.assertIn("本卦：䷇ 水地比", 钱卦)
        self.assertIn("动爻：二爻、三爻", 钱卦)
        self.assertIn("变卦：䷯ 水风井", 钱卦)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18

    def test_卯月乙亥占升选(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 2 2 0 0\n")
        self.assertIn("本卦：䷒ 地泽临", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷼ 风泽中孚", 钱卦)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18

    def test_未月丁巳占嫂复病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 3\n")
        self.assertIn("本卦：䷖ 山地剥", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第19页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=19

    def test_巳月戊申往前处脱货(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 0 1 1\n")
        self.assertIn("本卦：䷈ 风天小畜", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第19页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=19

    def test_卯月戊子占坟地(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 2 3 3\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷭ 地风升", 钱卦)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第20页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=20

    def test_申月乙卯避兵(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 0 1 3 3\n")
        self.assertIn("本卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷡ 雷天大壮", 钱卦)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第21页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=21

    def test_申月甲午占父在任(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 3 3\n")
        self.assertIn("本卦：䷫ 天风姤", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷟ 雷风恒", 钱卦)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第21页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=21

    def test_寅月乙卯客外占家中(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 0 1 1 1\n")
        self.assertIn("本卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("动爻：二爻、三爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第22页；第七问巳月戊戌求财益卦，与已核《增删卜易》巳月戊戌占财同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=22

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第22页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=22

    def test_寅月乙卯占妻在家(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 0 0\n")
        self.assertIn("本卦：䷏ 雷地豫", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷋ 天地否", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23

    def test_亥月甲子占仆归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 2\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23

    def test_申月丁卯见贵求财(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 1\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23

    def test_子月癸酉自占婚(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 2 0\n")
        self.assertIn("本卦：䷟ 雷风恒", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷱ 火风鼎", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24

    def test_午月癸丑占妻病愈期(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 3 1 2\n")
        self.assertIn("本卦：䷬ 泽地萃", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷇ 水地比", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24

    def test_寅月庚戌占子病愈期(self):
        钱卦 = 运行("金钱卦.py", "1\n0 3 3 1 1 1\n")
        self.assertIn("本卦：䷫ 天风姤", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻", 钱卦)
        self.assertIn("变卦：䷘ 天雷无妄", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24

    def test_未月庚子占求财到手(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 1 1\n")
        self.assertIn("本卦：䷈ 风天小畜", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25

    def test_酉月庚辰占岳母近病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 0 2 2 2\n")
        self.assertIn("本卦：䷆ 地水师", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷭ 地风升", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25

    def test_酉月壬辰占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 1 2\n")
        self.assertIn("本卦：䷛ 泽风大过", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25

    def test_子月乙巳占弟尸首(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 2 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第26页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=26

    def test_丑月甲午占父近病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 2 0\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷔ 火雷噬嗑", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27

    def test_未月戊戌因大旱占雨(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 1 1\n")
        self.assertIn("本卦：䷓ 风地观", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27

    def test_未月戊戌占交疏人来期(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 2 1 2\n")
        self.assertIn("本卦：䷦ 水山蹇", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27

    def test_未月甲辰占大雨(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 1 1 0 2\n")
        self.assertIn("本卦：䷽ 雷山小过", 钱卦)
        self.assertIn("动爻：初爻、五爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第28页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=28

    def test_戌月丁卯占讼事(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 2 2\n")
        self.assertIn("本卦：䷊ 地天泰", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第29页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=29

    def test_亥月己丑占将来有官否(self):
        钱卦 = 运行("金钱卦.py", "1\n3 1 2 1 1 0\n")
        self.assertIn("本卦：䷹ 兑为泽", 钱卦)
        self.assertIn("动爻：初爻、上爻", 钱卦)
        self.assertIn("变卦：䷅ 天水讼", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第29页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=29

    def test_辰月戊子占父归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 1 3\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷪ 泽天夬", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第30页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=30

    def test_午月癸卯占后运功名(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 3 2 0 1\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：三爻、五爻", 钱卦)
        self.assertIn("变卦：䷓ 风地观", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第30页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=30

    def test_寅月甲午占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 3 2 2 1\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：二爻、三爻", 钱卦)
        self.assertIn("变卦：䷃ 山水蒙", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第31页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=31

    def test_丑月庚申占坟地风水(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 1 1 2\n")
        self.assertIn("本卦：䷞ 泽山咸", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第31页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=31

    def test_申月辛卯占买宅(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 1 1 1 2\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷪ 泽天夬", 钱卦)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第32页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=32

    def test_卯月壬辰占候文书(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 2 2 1\n")
        self.assertIn("本卦：䷕ 山火贲", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第32页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=32

    def test_辰月丁巳占逃仆(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 2 1 2\n")
        self.assertIn("本卦：䷦ 水山蹇", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33

    def test_酉月丙辰占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 2 2 2\n")
        self.assertIn("本卦：䷭ 地风升", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33

    def test_卯月丙辰占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 2 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33

    def test_辰月庚申占蚕桑叶贵贱(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 2 1 2\n")
        self.assertIn("本卦：䷾ 水火既济", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第34页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=34

    def test_寅月戊辰占病有何鬼神(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 1 1\n")
        self.assertIn("本卦：䷈ 风天小畜", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第36页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=36

    def test_申月癸卯占乡试(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 0 2\n")
        self.assertIn("本卦：䷟ 雷风恒", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷛ 泽风大过", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第36页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=36

    def test_酉月庚戌占生子年(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 2 2 1 2\n")
        self.assertIn("本卦：䷂ 水雷屯", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第37页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=37

    def test_卯月乙丑自占求婚(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 2 3 0 3\n")
        self.assertIn("本卦：䷔ 火雷噬嗑", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷇ 水地比", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第37页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=37

    def test_酉月甲辰因参论占自陈(self):
        钱卦 = 运行("金钱卦.py", "1\n0 3 0 2 2 2\n")
        self.assertIn("本卦：䷆ 地水师", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第38页；第十一问午月丙辰出外贸易恒之豫，与已核《增删卜易》午月丙辰经商同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第38页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    def test_未月丁卯占出仕功名(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 3\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第38页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    def test_戌月甲辰占借银(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第39页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=39

    def test_寅月戊戌占失银物(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 0 1 1\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：三爻、四爻", 钱卦)
        self.assertIn("变卦：䷅ 天水讼", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40

    def test_辰月丁酉自占婚姻(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40

    def test_卯月乙卯占谋望求财(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 1 2\n")
        self.assertIn("本卦：䷛ 泽风大过", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40

    def test_午月辛亥占师近病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 2 2 1 2\n")
        self.assertIn("本卦：䷻ 水泽节", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第41页；第十一问未月丁巳悔婚离之旅，与已核《增删卜易》未月丁巳悔婚同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=41

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第41页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=41

    def test_寅月戊辰占兄近病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 2 1\n")
        self.assertIn("本卦：䷢ 火地晋", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第42页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=42

    def test_巳月戊寅占何日得财(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 2 3\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷶ 雷火丰", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第42页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=42

    def test_午月己卯占妻病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 0 1 2 2\n")
        self.assertIn("本卦：䷲ 震为雷", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷶ 雷火丰", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43

    def test_寅月戊子占生产(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 0 1\n")
        self.assertIn("本卦：䷖ 山地剥", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷓ 风地观", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43

    def test_子月辛未占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 3 2 1 1\n")
        self.assertIn("本卦：䷴ 风山渐", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻", 钱卦)
        self.assertIn("变卦：䷼ 风泽中孚", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43

    def test_辰月甲寅占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 3 2\n")
        self.assertIn("本卦：䷂ 水雷屯", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷲ 震为雷", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第44页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=44

    def test_申月丙辰占弟病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 3 2\n")
        self.assertIn("本卦：䷾ 水火既济", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷶ 雷火丰", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第45页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=45

    def test_申月癸丑占子在楚生理(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 2 2 2 1\n")
        self.assertIn("本卦：䷨ 山泽损", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第45页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=45

    def test_叔占侄在外平安(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 3 3 1\n")
        self.assertIn("本卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷚ 山雷颐", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46

    def test_亥月丙寅嫂占姑病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 3 1 2\n")
        self.assertIn("本卦：䷞ 泽山咸", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷦ 水山蹇", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46

    def test_卯月乙未姑占弟妇怀孕(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 2 3 1 2\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷜ 坎为水", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46

    def test_丁卯占劾奏他人(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 1 2 1\n")
        self.assertIn("本卦：䷷ 火山旅", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第47页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=47

    def test_未月戊申因误军粮被参(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 2 0\n")
        self.assertIn("本卦：䷶ 雷火丰", 钱卦)
        self.assertIn("动爻：初爻、上爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第47页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=47

    def test_卯月壬寅占坟地(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 3 1 2\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷾ 水火既济", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第48页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=48

    def test_酉月壬子占侄被害(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 2 2\n")
        self.assertIn("本卦：䷡ 雷天大壮", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷊ 地天泰", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第48页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=48

    def test_巳月丁酉占文书到期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 1 1\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49

    def test_午月丙子占开店(self):
        钱卦 = 运行("金钱卦.py", "1\n3 1 1 3 0 0\n")
        self.assertIn("本卦：䷡ 雷天大壮", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷸ 巽为风", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49

    def test_申月乙卯因子被拿占讼(self):
        钱卦 = 运行("金钱卦.py", "1\n2 3 3 2 3 3\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49

    def test_未月乙亥往买卖求利(self):
        钱卦 = 运行("金钱卦.py", "1\n1 3 2 1 3 2\n")
        self.assertIn("本卦：䷹ 兑为泽", 钱卦)
        self.assertIn("动爻：二爻、五爻", 钱卦)
        self.assertIn("变卦：䷲ 震为雷", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第50页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=50

    def test_子月己巳占赌钱(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第50页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=50

    def test_辰月庚午占会(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 0 1 1\n")
        self.assertIn("本卦：䷓ 风地观", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷋ 天地否", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51

    def test_寅月甲午占子久病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 2 2\n")
        self.assertIn("本卦：䷡ 雷天大壮", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51

    def test_卯月甲午占起去寄信(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51

    def test_巳月甲戌同乡占借贷(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 2 0 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷏ 雷地豫", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第52页；第十三问巳月甲寅延师训子否之乾，与已核《增删卜易》巳月甲寅严师训子同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=52

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53

    def test_寅月庚申占侄孙病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 3 1\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53

    def test_辰月戊午占夫病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 3 3 2 1\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：三爻、四爻", 钱卦)
        self.assertIn("变卦：䷚ 山雷颐", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53

    def test_亥月戊戌占妻近病(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 1 0 3 1\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻", 钱卦)
        self.assertIn("变卦：䷍ 火天大有", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第54页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=54

    def test_戌月庚子占冬生意(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 2 0 1\n")
        self.assertIn("本卦：䷕ 山火贲", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷤ 风火家人", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第54页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=54

    def test_午月丙午占自去请父回(self):
        钱卦 = 运行("金钱卦.py", "1\n1 3 1 1 2 1\n")
        self.assertIn("本卦：䷍ 火天大有", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第55页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=55

    def test_再占请父回(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 3 1 2\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷾ 水火既济", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第55页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=55

    def test_申月辛卯占子嗣(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 2 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56

    def test_午月甲申占雨久伤麦(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 3\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56

    def test_申月甲午开煤窑占见煤时(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 3 2 1 1\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷩ 风雷益", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56

    def test_寅月庚戌占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 3 0 3 0 3\n")
        self.assertIn("本卦：䷿ 火水未济", 钱卦)
        self.assertIn("动爻：二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷦ 水山蹇", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第57页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=57

    def test_寅月甲辰占父远出归期(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 3 1 3 3\n")
        self.assertIn("本卦：䷠ 天山遁", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷵ 雷泽归妹", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第57至58页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=57

    def test_午月庚辰占仆近出归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 2 1\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第58页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=58

    def test_辰月己卯占今日还银(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第58至59页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=58

    def test_子月壬申占父在乱军(self):
        钱卦 = 运行("金钱卦.py", "1\n3 3 3 0 0 3\n")
        self.assertIn("本卦：䷙ 山天大畜", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷬ 泽地萃", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第59页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=59

    def test_辰月甲子造坟葬亲(self):
        钱卦 = 运行("金钱卦.py", "1\n3 3 3 3 3 3\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第60页；第十七问未月庚子占求财小畜卦，与第七问同案重见，已按首次出现顺序列测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第60页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60

    def test_未月甲午占自升迁(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 2 2 0 0\n")
        self.assertIn("本卦：䷆ 地水师", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷺ 风水涣", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第60页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60

    def test_亥月丙午占子脱难(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 2 1 2 2\n")
        self.assertIn("本卦：䷏ 雷地豫", 钱卦)
        self.assertIn("动爻：初爻、二爻", 钱卦)
        self.assertIn("变卦：䷵ 雷泽归妹", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第61页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=61

    def test_未月丁丑占子久出归期(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 1 3 0 3\n")
        self.assertIn("本卦：䷱ 火风鼎", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷄ 水天需", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第61页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=61

    def test_寅月癸亥占子嗣(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 0 2 2 0\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：三爻、上爻", 钱卦)
        self.assertIn("变卦：䷳ 艮为山", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第62页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=62

    def test_酉月戊申占伯父归期(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 3 2 1\n")
        self.assertIn("本卦：䷷ 火山旅", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷳ 艮为山", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第62页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=62

    def test_申月乙亥占家宅(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 3 2 1 2\n")
        self.assertIn("本卦：䷯ 水风井", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第63页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=63

    def test_未月癸亥占流年(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 2 2 1\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第63页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=63

    def test_子月乙酉占现任吉凶(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 1 2\n")
        self.assertIn("本卦：䷄ 水天需", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第64页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=64

    def test_午月辛丑因母病问流年(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 1 1\n")
        self.assertIn("本卦：䷩ 风雷益", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷘ 天雷无妄", 钱卦)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第64页；背数依原本变卦换算，缺唯一纪年 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=64

    def test_午月辛酉父为十二岁子占功名(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 0 1 1 0\n")
        self.assertIn("本卦：䷬ 泽地萃", 钱卦)
        self.assertIn("动爻：三爻、上爻", 钱卦)
        self.assertIn("变卦：䷠ 天山遁", 钱卦)

    # 《祛疑说·易占说》国图藏刻本PDF第1～2页载面背及木丸规则，未记六次钱数和所得卦 https://upload.wikimedia.org/wikipedia/commons/5/53/NCL-07324_%E7%A5%9B%E7%96%91%E8%AA%AA.pdf#page=1
