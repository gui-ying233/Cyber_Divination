import subprocess
import sys
import unittest
from pathlib import Path


目录 = Path(__file__).resolve().parent


def 运行(脚本: str, 输入: str) -> str:
    return subprocess.run(
        [sys.executable, "-S", "-B", str(目录 / 脚本)],
        input=输入,
        text=True,
        capture_output=True,
        check=True,
        cwd=目录,
        timeout=5,
    ).stdout


class 古籍占例(unittest.TestCase):
    # 《梅花易数》卷一“今日动静如何”实占 https://zh.wikisource.org/wiki/梅花易數/卷一#今日動靜如何
    def test_今日动静如何(self):
        输出 = 运行("梅花易数.py", "8 5\n")
        self.assertIn("䷭ 地风升\n\t变卦为：䷊ 地天泰", 输出)

    # 《梅花易数》卷一“西林寺牌额占” https://zh.wikisource.org/wiki/梅花易數/卷一#西林寺牌額占
    def test_西林寺牌额(self):
        初占 = 运行("梅花易数.py", "7 8\n")
        改额 = 运行("梅花易数.py", "7 10\n")
        self.assertIn("䷖ 山地剥\n\t变卦为：䷳ 艮为山", 初占)
        self.assertIn("䷨ 山泽损\n\t变卦为：䷼ 风泽中孚", 改额)

    # 《增删卜易》辰月戊申占父病，原文未记公历年；背数按所载爻画及占卦法换算 https://zh.wikisource.org/wiki/增刪卜易/9 https://www.shidianguji.com/book/XYXZSBY/chapter/1laba3s8ovar2
    def test_辰月戊申占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 7\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)
        self.assertIn("主卦：䷀ 乾为天（乾宫，属金，世6应3）", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 辛未", 纳甲)

    # 《增删卜易》卷十“酉月辛亥日占求财” https://zh.wikisource.org/wiki/增刪卜易/10
    def test_酉月辛亥占求财(self):
        输出 = 运行("金钱卦.py", "1\n3 1 2 1 3 2\n")
        self.assertIn("本卦：䷹ 兑为泽", 输出)
        self.assertIn("动爻：初爻、五爻", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)

    # 《增删卜易》卷十“巳月乙未日自占病” https://zh.wikisource.org/wiki/增刪卜易/10
    def test_巳月乙未自占病(self):
        输出 = 运行("金钱卦.py", "1\n2 1 1 1 3 0\n")
        self.assertIn("本卦：䷛ 泽风大过", 输出)
        self.assertIn("动爻：五爻、上爻", 输出)
        self.assertIn("变卦：䷱ 火风鼎", 输出)

    # 《增删卜易》卷十一“卯月己卯日弟占兄重罪” https://zh.wikisource.org/wiki/增刪卜易/11
    def test_卯月己卯占兄重罪(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 0 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 输出)
        self.assertIn("动爻：四爻", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)

    # 《增删卜易》卷十二“卯月戊寅日占父官事” https://zh.wikisource.org/wiki/增刪卜易/12
    def test_卯月戊寅占父官事(self):
        输出 = 运行("金钱卦.py", "1\n0 2 0 1 1 0\n")
        self.assertIn("本卦：䷬ 泽地萃", 输出)
        self.assertIn("动爻：初爻、三爻、上爻", 输出)
        self.assertIn("变卦：䷌ 天火同人", 输出)

    # 《增删卜易》卷十二“卯月戊寅日妹占兄官事” https://zh.wikisource.org/wiki/增刪卜易/12
    def test_卯月戊寅妹占兄官事(self):
        输出 = 运行("金钱卦.py", "1\n2 0 2 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 输出)
        self.assertIn("动爻：二爻", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)

    # 《增删卜易》卷十八“戊子日占生产” https://zh.wikisource.org/wiki/增刪卜易/18
    def test_戊子日占生产(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 0 1\n")
        self.assertIn("本卦：䷖ 山地剥", 输出)
        self.assertIn("动爻：五爻", 输出)
        self.assertIn("变卦：䷓ 风地观", 输出)

    # 《增删卜易》卷十八“申月甲辰日占兄病” https://zh.wikisource.org/wiki/增刪卜易/18
    def test_申月甲辰占兄病(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 0 3 2\n")
        self.assertIn("本卦：䷂ 水雷屯", 输出)
        self.assertIn("动爻：四爻、五爻", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)

    # 《增删卜易》卷十九“申月丙子日占出门” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_申月丙子占出门(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 0 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 7 6 8 8\n\n")
        self.assertIn("本卦：䷣ 地火明夷", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷽ 雷山小过", 钱卦)
        self.assertIn("主卦：䷣ 地火明夷（坎宫，属水，世4应1）", 纳甲)
        self.assertIn("变卦：䷽ 雷山小过", 纳甲)

    # 《增删卜易》卷十九“未月丁巳日占悔婚” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_未月丁巳占悔婚(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 8 7\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)

    # 《增删卜易》卷十九“卯月甲寅日占风水” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_卯月甲寅占风水(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 2 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 8 9 7 8\n\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)
        self.assertIn("主卦：䷮ 泽水困（兑宫，属金，世1应4）", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)

    # 《增删卜易》卷十九“卯月丁巳日争田水” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_卯月丁巳争田水(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 3 3 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 9 9 8 9\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻、三爻、四爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)

    # 《增删卜易》卷二十“巳月戊戌日占财” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_巳月戊戌占财(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 2 1 1\n")
        self.assertIn("本卦：䷩ 风雷益", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》卷二十“午月丙辰日经商” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_午月丙辰经商(self):
        输出 = 运行("金钱卦.py", "1\n2 3 3 1 2 2\n")
        self.assertIn("本卦：䷟ 雷风恒", 输出)
        self.assertIn("动爻：二爻、三爻", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)

    # 《增删卜易》卷二十“酉月乙未日占子” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_酉月乙未占子(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》卷二十“巳月甲寅日严师训子” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_巳月甲寅严师训子(self):
        输出 = 运行("金钱卦.py", "1\n0 0 0 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 输出)
        self.assertIn("动爻：初爻、二爻、三爻", 输出)
        self.assertIn("变卦：䷀ 乾为天", 输出)

    # 《增删卜易》卷二十“申月己卯日父子七人” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_申月己卯父子七人(self):
        输出 = 运行("金钱卦.py", "1\n2 3 3 2 3 3\n")
        self.assertIn("本卦：䷸ 巽为风", 输出)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 输出)
        self.assertIn("变卦：䷁ 坤为地", 输出)

    # 《太乙金钥匙》续集嘉靖四十年辛酉岁、戊戌月、丁未日、庚戌时占例 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8
    def test_嘉靖四十年太乙四计(self):
        占例 = (
            ("1\n1561 10 19\n", ("庚子元第22局", "巽9宫", "文昌：阴德（乾）", "主算：16", "客算：30")),
            ("2\n1561 10 19 12\n", ("壬子元第47局", "巽9宫", "文昌：高丛（卯）", "主算：4", "客算：8")),
            ("3\n1\n1562 01 06 12\n", ("甲子元第44局", "坎8宫", "文昌：阳德（丑）", "主算：33", "客算：14")),
            ("4\n1562 02 05 20\n", ("戊子元第23局", "巽9宫", "文昌：阴德（乾）", "主算：16", "客算：23")),
        )
        for 输入, 结果 in 占例:
            输出 = 运行("太乙.py", 输入)
            for 字样 in 结果:
                self.assertIn(字样, 输出)

    # 《太乙金镜式经》卷一梁天监三年甲申六月八日积日例 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷01
    def test_梁天监三年太乙日计(self):
        输出 = 运行("太乙.py", "3\n2\n504 07 07\n")
        self.assertIn("庚子元第45局", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：和德（艮）", 输出)

    # 《六壬断案》元集宅墓第1案张九翁占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_张九翁占宅(self):
        输出 = 运行("大六壬.py", "1128 10 11 13\n1\n")
        self.assertIn("庚寅日，天罡辰将加未时", 输出)
        self.assertIn("初传：巳 勾陈 官鬼", 输出)
        self.assertIn("中传：寅 螣蛇 妻财", 输出)
        self.assertIn("末传：亥 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第2案叶助教占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_叶助教占宅(self):
        输出 = 运行("大六壬.py", "1128 02 15 13\n1\n")
        self.assertIn("辛卯日，神后子将加未时", 输出)
        self.assertIn("初传：卯 玄武 妻财", 输出)
        self.assertIn("中传：申 朱雀 兄弟", 输出)
        self.assertIn("末传：丑 白虎 父母", 输出)

    # 《六壬断案》元集宅墓第3案邵三翁占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_邵三翁占宅(self):
        输出 = 运行("大六壬.py", "1128 10 02 21\n1\n")
        self.assertIn("辛巳日，天罡辰将加亥时", 输出)
        self.assertIn("初传：卯 天后 妻财", 输出)
        self.assertIn("中传：申 天空 兄弟", 输出)
        self.assertIn("末传：丑 螣蛇 父母", 输出)

    # 《六壬断案》元集宅墓第5案邵巡检占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_邵巡检占宅(self):
        输出 = 运行("大六壬.py", "1128 08 02 03\n1\n")
        self.assertIn("庚辰日，胜光午将加寅时", 输出)
        self.assertIn("初传：辰 玄武 父母", 输出)
        self.assertIn("中传：申 螣蛇 兄弟", 输出)
        self.assertIn("末传：子 青龙 子孙", 输出)

    # 《六壬断案》元集宅墓第6案任三翁占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_任三翁占宅(self):
        输出 = 运行("大六壬.py", "1128 12 22 15\n1\n")
        self.assertIn("壬寅日，大吉丑将加申时", 输出)
        self.assertIn("初传：子 白虎 兄弟", 输出)
        self.assertIn("中传：巳 贵人 妻财", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)

    # 《六壬断案》元集宅墓第7案邵伯达占宅基 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_邵伯达占宅基(self):
        输出 = 运行("大六壬.py", "1129 12 05 17\n1\n")
        self.assertIn("庚寅日，功曹寅将加酉时", 输出)
        self.assertIn("初传：子 青龙 子孙", 输出)
        self.assertIn("中传：巳 太阴 官鬼", 输出)
        self.assertIn("末传：戌 六合 父母", 输出)

    # 《六壬断案》元集宅墓第10案王德卿占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_王德卿占宅(self):
        输出 = 运行("大六壬.py", "1128 11 02 05\n1\n")
        self.assertIn("壬子日，太冲卯将加卯时", 输出)
        self.assertIn("初传：亥 天空 兄弟", 输出)
        self.assertIn("中传：子 青龙 兄弟", 输出)
        self.assertIn("末传：卯 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第11案童得松占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_童得松占宅(self):
        输出 = 运行("大六壬.py", "1129 07 10 01\n1\n")
        self.assertIn("壬戌日，小吉未将加丑时", 输出)
        self.assertIn("初传：巳 太阴 妻财", 输出)
        self.assertIn("中传：亥 勾陈 兄弟", 输出)
        self.assertIn("末传：巳 太阴 妻财", 输出)

    # 《六壬断案》元集宅墓第15案任太公占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_任太公占宅(self):
        输出 = 运行("大六壬.py", "1128 02 10 07\n1\n")
        self.assertIn("丙戌日，神后子将加辰时", 输出)
        self.assertIn("初传：酉 太阴 妻财", 输出)
        self.assertIn("中传：巳 天空 兄弟", 输出)
        self.assertIn("末传：丑 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第16案王解元占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_王解元占宅(self):
        输出 = 运行("大六壬.py", "1129 04 12 13\n1\n")
        self.assertIn("癸巳日，河魁戌将加未时", 输出)
        self.assertIn("初传：申 六合 父母", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：寅 玄武 子孙", 输出)

    # 《六壬断案》元集宅墓第17案何宣义占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_何宣义占宅(self):
        输出 = 运行("大六壬.py", "1129 04 12 17\n1\n")
        self.assertIn("癸巳日，河魁戌将加酉时", 输出)
        self.assertIn("初传：未 勾陈 官鬼", 输出)
        self.assertIn("中传：申 青龙 父母", 输出)
        self.assertIn("末传：酉 天空 父母", 输出)

    # 《六壬断案》元集宅墓第20案叶油饼店主占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_叶油饼店主占宅(self):
        输出 = 运行("大六壬.py", "1128 07 21 17\n1\n")
        self.assertIn("戊辰日，小吉未将加酉时", 输出)
        self.assertIn("初传：丑 天空 兄弟", 输出)
        self.assertIn("中传：亥 太常 妻财", 输出)
        self.assertIn("末传：酉 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第22案何七秀才占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_何七秀才占宅(self):
        输出 = 运行("大六壬.py", "1128 03 19 11\n1\n")
        self.assertIn("甲子日，登明亥将加午时", 输出)
        self.assertIn("初传：子 螣蛇 父母", 输出)
        self.assertIn("中传：巳 太常 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》元集宅墓第23案某占家宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_某占家宅(self):
        输出 = 运行("大六壬.py", "1128 10 05 21\n1\n")
        self.assertIn("甲申日，天罡辰将加亥时", 输出)
        self.assertIn("初传：子 青龙 父母", 输出)
        self.assertIn("中传：巳 太阴 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》元集宅墓第25案邵三公占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_邵三公占宅(self):
        输出 = 运行("大六壬.py", "1129 01 31 00\n1\n")
        self.assertIn("壬午日，神后子将加子时", 输出)
        self.assertIn("初传：亥 太常 兄弟", 输出)
        self.assertIn("中传：午 六合 妻财", 输出)
        self.assertIn("末传：子 玄武 兄弟", 输出)

    # 《六壬断案》元集宅墓第27案徐大夫占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_徐大夫占宅(self):
        输出 = 运行("大六壬.py", "1128 02 10 13\n1\n")
        self.assertIn("丙戌日，神后子将加未时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：丑 太阴 子孙", 输出)
        self.assertIn("末传：午 青龙 兄弟", 输出)

    # 《六壬断案》元集宅墓第28案郭德占家宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_郭德占家宅(self):
        输出 = 运行("大六壬.py", "1129 07 02 11\n1\n")
        self.assertIn("甲寅日，小吉未将加午时", 输出)
        self.assertIn("初传：辰 六合 妻财", 输出)
        self.assertIn("中传：巳 勾陈 子孙", 输出)
        self.assertIn("末传：午 青龙 子孙", 输出)

    # 《六壬断案》元集宅墓第30案童三十四公占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_童三十四公占宅(self):
        输出 = 运行("大六壬.py", "1129 08 25 05\n1\n")
        self.assertIn("戊申日，太乙巳将加卯时", 输出)
        self.assertIn("初传：子 天后 妻财", 输出)
        self.assertIn("中传：寅 螣蛇 官鬼", 输出)
        self.assertIn("末传：辰 六合 兄弟", 输出)
