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
    # 《玉匣记》“李淳风六壬时课”的三月初五辰时明称“假如”，是起例而非实占，不作历史测试 https://zh.wikisource.org/wiki/玉匣記#雜占篇_李淳風六壬時課

    # 《多能鄙事》卷八“小六壬课时”列月日起时规则及正月初一示例，未记具体实占，暂不补造历史案例 https://www.shidianguji.com/zh/book/CADAL02097181/chapter/1lco8m1j7ucyw

    # 朱熹《周易本义·筮仪》记揲蓍操作，未记可重放的十八次实际分策；不能仅凭历史所得卦检验随机揲蓍过程 https://www.eee-learning.com/book/juicy-ritual

    # 郭雍《郭氏传家易说》卷七列一挂再扐及爻数，未记十八次实占分策，不能构造随机种子冒充古占 https://zh.wikisource.org/wiki/郭氏傳家易說_(四庫全書本)/卷07

    # 《梅花易数》卷一“观梅占”仅记辰年，缺具体纪年，不能唯一换算公历输入 https://zh.wikisource.org/wiki/梅花易數/卷一#觀梅占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=22

    # 《梅花易数》卷一“牡丹占”仅记巳年，缺具体纪年，不能唯一换算公历输入 https://zh.wikisource.org/wiki/梅花易數/卷一#牡丹占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=24

    # 《梅花易数》卷一“邻夜扣门借物占”，酉时十数只加入动爻 https://zh.wikisource.org/wiki/梅花易數/卷一#鄰夜扣門借物占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=25
    def test_邻夜扣门借物(self):
        输出 = 运行("梅花易数.py", "1 5 10\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷸ 巽为风", 输出)

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

    # 《梅花易数》卷一“老人有忧色占”，原记姤九四变，可确定之卦为巽 https://zh.wikisource.org/wiki/梅花易數/卷一#老人有憂色占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=29
    def test_老人有忧色(self):
        输出 = 运行("梅花易数.py", "1 5 4\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷸ 巽为风", 输出)

    # 《梅花易数》卷一“少年有喜色占” https://zh.wikisource.org/wiki/梅花易數/卷一#少年有喜色占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=31
    def test_少年有喜色(self):
        输出 = 运行("梅花易数.py", "7 3 7\n")
        self.assertIn("䷕ 山火贲\n\t变卦为：䷤ 风火家人", 输出)

    # 《梅花易数》卷一“牛哀鸣占” https://zh.wikisource.org/wiki/梅花易數/卷一#牛哀鳴占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=32
    def test_牛哀鸣(self):
        输出 = 运行("梅花易数.py", "8 6 7\n")
        self.assertIn("䷆ 地水师\n\t变卦为：䷭ 地风升", 输出)

    # 《梅花易数》卷一“鸡悲鸣占” https://zh.wikisource.org/wiki/梅花易數/卷一#雞悲鳴占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=33
    def test_鸡悲鸣(self):
        输出 = 运行("梅花易数.py", "5 1 4\n")
        self.assertIn("䷈ 风天小畜\n\t变卦为：䷀ 乾为天", 输出)

    # 《梅花易数》卷一“枯枝坠地占” https://zh.wikisource.org/wiki/梅花易數/卷一#枯枝墜地占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=34
    def test_枯枝坠地(self):
        输出 = 运行("梅花易数.py", "3 2 5\n")
        self.assertIn("䷥ 火泽睽\n\t变卦为：䷨ 山泽损", 输出)

    # 《梅花易数》卷二王、田、韩三姓起屋占以姓氏笔画加入年月日时，当前公历起卦未收姓数，暂不混用两数法 https://zh.wikisource.org/wiki/梅花易數/卷二

    # 《梅花易数》卷三笼盛草根、钟覆破玉环只载所成卦及变卦，缺起卦所取数，不能重放梅花取数过程 https://zh.wikisource.org/wiki/梅花易數/卷三

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

    # 《增删卜易》第十章“酉月辛亥日占求财” https://zh.wikisource.org/wiki/增刪卜易/10
    def test_酉月辛亥占求财(self):
        输出 = 运行("金钱卦.py", "1\n3 1 2 1 3 2\n")
        self.assertIn("本卦：䷹ 兑为泽", 输出)
        self.assertIn("动爻：初爻、五爻", 输出)
        self.assertIn("变卦：䷧ 雷水解", 输出)

    # 《增删卜易》第十章“巳月乙未日自占病” https://zh.wikisource.org/wiki/增刪卜易/10
    def test_巳月乙未自占病(self):
        输出 = 运行("金钱卦.py", "1\n2 1 1 1 3 0\n")
        self.assertIn("本卦：䷛ 泽风大过", 输出)
        self.assertIn("动爻：五爻、上爻", 输出)
        self.assertIn("变卦：䷱ 火风鼎", 输出)

    # 《增删卜易》第十一章“卯月己卯日弟占兄重罪” https://zh.wikisource.org/wiki/增刪卜易/11
    def test_卯月己卯占兄重罪(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 0 2 2\n")
        self.assertIn("本卦：䷗ 地雷复", 输出)
        self.assertIn("动爻：四爻", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)

    # 《增删卜易》第十二章“卯月戊寅日占父官事” https://zh.wikisource.org/wiki/增刪卜易/12
    def test_卯月戊寅占父官事(self):
        输出 = 运行("金钱卦.py", "1\n0 2 0 1 1 0\n")
        self.assertIn("本卦：䷬ 泽地萃", 输出)
        self.assertIn("动爻：初爻、三爻、上爻", 输出)
        self.assertIn("变卦：䷌ 天火同人", 输出)

    # 《增删卜易》第十二章“卯月戊寅日妹占兄官事” https://zh.wikisource.org/wiki/增刪卜易/12
    def test_卯月戊寅妹占兄官事(self):
        输出 = 运行("金钱卦.py", "1\n2 0 2 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 输出)
        self.assertIn("动爻：二爻", 输出)
        self.assertIn("变卦：䷅ 天水讼", 输出)

    # 《增删卜易》第13章“辰月丙申占弟痘症”，秦慎安校勘本PDF第57页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=57
    def test_辰月丙申占弟痘症(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 7 8\n\n")
        self.assertIn("本卦：䷾ 水火既济", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)
        self.assertIn("主卦：䷾ 水火既济（坎宫，属水，世3应6）", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("四爻 父母 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁亥", 纳甲)

    # 《增删卜易》第十四、十五章以“假令”讲解例式，未记具体实占，不作为历史案例 https://zh.wikisource.org/wiki/增刪卜易/14 https://zh.wikisource.org/wiki/增刪卜易/15

    # 《增删卜易》第16章“寅月庚戌占求财”，秦慎安校勘本PDF第62页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=62
    def test_寅月庚戌占求财(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 8 7\n\n")
        self.assertIn("本卦：䷍ 火天大有", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷍ 火天大有（乾宫，属金，世3应6）", 纳甲)
        self.assertIn("变卦：䷍ 火天大有", 纳甲)
        self.assertIn("二爻 妻财 甲寅", 纳甲)
        self.assertIn("三爻 父母 甲辰", 纳甲)

    # 《增删卜易》第16章“酉月丙寅占谒贵”，秦慎安校勘本PDF第62页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=62
    def test_酉月丙寅占谒贵(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 9 8 8 7\n\n")
        self.assertIn("本卦：䷑ 山风蛊", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷃ 山水蒙", 钱卦)
        self.assertIn("主卦：䷑ 山风蛊（巽宫，属木，世3应6）", 纳甲)
        self.assertIn("变卦：䷃ 山水蒙", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)

    # 《增删卜易》第16章“寅月丙申占升迁”，秦慎安校勘本PDF第63页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=63
    def test_寅月丙申占升迁(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 3 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "6 8 9 8 8 7\n\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷚ 山雷颐", 钱卦)
        self.assertIn("主卦：䷳ 艮为山（艮宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷚ 山雷颐", 纳甲)
        self.assertIn("初爻 兄弟 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 庚子", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚辰", 纳甲)

    # 《增删卜易》第16章“午月丁未占弟被讼”，秦慎安校勘本PDF第64页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=64
    def test_午月丁未占弟被讼(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 0 1 3 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 6 7 9 8\n\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：三爻、五爻", 钱卦)
        self.assertIn("变卦：䷟ 雷风恒", 钱卦)
        self.assertIn("主卦：䷮ 泽水困（兑宫，属金，世1应4）", 纳甲)
        self.assertIn("变卦：䷟ 雷风恒", 纳甲)
        self.assertIn("三爻 官鬼 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 辛酉", 纳甲)
        self.assertIn("五爻 兄弟 丁酉 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)

    # 《增删卜易》第16章“寅月辛酉占开铺”，秦慎安校勘本PDF第65页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=65
    def test_寅月辛酉占开铺(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 1 2 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "6 8 7 8 8 9\n\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：初爻、上爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)
        self.assertIn("主卦：䷳ 艮为山（艮宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("上爻 官鬼 丙寅 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸酉", 纳甲)
        self.assertIn("初爻 兄弟 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己卯", 纳甲)

    # 《增删卜易》第16章“午月戊辰占妹临产”，秦慎安校勘本PDF第66页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=66
    def test_午月戊辰占妹临产(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 8 7\n\n")
        self.assertIn("本卦：䷢ 火地晋", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷢ 火地晋（乾宫，属金，世4应1）", 纳甲)
        self.assertIn("变卦：䷢ 火地晋", 纳甲)
        self.assertIn("四爻 兄弟 己酉", 纳甲)
        self.assertIn("二爻 官鬼 乙巳", 纳甲)

    # 《增删卜易》第17章“申月戊午自占病”，秦慎安校勘本PDF第68页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=68
    def test_申月戊午自占病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 1 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 6 7 7 7 7\n\n")
        self.assertIn("本卦：䷠ 天山遁", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷫ 天风姤", 钱卦)
        self.assertIn("主卦：䷠ 天山遁（乾宫，属金，世2应5）", 纳甲)
        self.assertIn("变卦：䷫ 天风姤", 纳甲)
        self.assertIn("二爻 官鬼 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 辛亥", 纳甲)

    # 《增删卜易》第17章“巳月丁亥占仆归期”，秦慎安校勘本PDF第68页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=68
    def test_巳月丁亥占仆归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 3 1 1 0\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 9 7 7 6\n\n")
        self.assertIn("本卦：䷪ 泽天夬", 钱卦)
        self.assertIn("动爻：三爻、上爻", 钱卦)
        self.assertIn("变卦：䷉ 天泽履", 钱卦)
        self.assertIn("主卦：䷪ 泽天夬（坤宫，属土，世5应2）", 纳甲)
        self.assertIn("变卦：䷉ 天泽履", 纳甲)
        self.assertIn("三爻 兄弟 甲辰 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 丁丑", 纳甲)
        self.assertIn("上爻 兄弟 丁未 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 壬戌", 纳甲)

    # 《增删卜易》第十八章戊子占生产，扫描初爻勾陈、二爻螣蛇，录文互倒；无占年不伪造日期校六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=72 https://zh.wikisource.org/wiki/增刪卜易/18
    def test_戊子日占生产(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 0 1\n")
        self.assertIn("本卦：䷖ 山地剥", 输出)
        self.assertIn("动爻：五爻", 输出)
        self.assertIn("变卦：䷓ 风地观", 输出)

    # 《增删卜易》第十八章“申月甲辰日占兄病” https://zh.wikisource.org/wiki/增刪卜易/18
    def test_申月甲辰占兄病(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 0 3 2\n")
        self.assertIn("本卦：䷂ 水雷屯", 输出)
        self.assertIn("动爻：四爻、五爻", 输出)
        self.assertIn("变卦：䷲ 震为雷", 输出)

    # 《增删卜易》第十九章“申月丙子日占出门” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_申月丙子占出门(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 0 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 7 6 8 8\n\n")
        self.assertIn("本卦：䷣ 地火明夷", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷽ 雷山小过", 钱卦)
        self.assertIn("主卦：䷣ 地火明夷（坎宫，属水，世4应1）", 纳甲)
        self.assertIn("变卦：䷽ 雷山小过", 纳甲)

    # 《增删卜易》第十九章“未月丁巳日占悔婚” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_未月丁巳占悔婚(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 8 7\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)

    # 《增删卜易》第十九章“卯月甲寅日占风水” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_卯月甲寅占风水(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 2 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 8 9 7 8\n\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)
        self.assertIn("主卦：䷮ 泽水困（兑宫，属金，世1应4）", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)

    # 《增删卜易》第十九章“卯月丁巳日争田水” https://zh.wikisource.org/wiki/增刪卜易/19
    def test_卯月丁巳争田水(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 3 3 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 9 9 8 9\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻、三爻、四爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)

    # 《增删卜易》第二十章“巳月戊戌日占财” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_巳月戊戌占财(self):
        输出 = 运行("金钱卦.py", "1\n1 2 2 2 1 1\n")
        self.assertIn("本卦：䷩ 风雷益", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》第二十章“午月丙辰日经商” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_午月丙辰经商(self):
        输出 = 运行("金钱卦.py", "1\n2 3 3 1 2 2\n")
        self.assertIn("本卦：䷟ 雷风恒", 输出)
        self.assertIn("动爻：二爻、三爻", 输出)
        self.assertIn("变卦：䷏ 雷地豫", 输出)

    # 《增删卜易》第二十章“酉月乙未日占子” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_酉月乙未占子(self):
        输出 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        self.assertIn("本卦：䷁ 坤为地", 输出)
        self.assertIn("动爻：无", 输出)
        self.assertIn("变卦：无（静卦）", 输出)

    # 《增删卜易》第二十章“巳月甲寅日严师训子” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_巳月甲寅严师训子(self):
        输出 = 运行("金钱卦.py", "1\n0 0 0 1 1 1\n")
        self.assertIn("本卦：䷋ 天地否", 输出)
        self.assertIn("动爻：初爻、二爻、三爻", 输出)
        self.assertIn("变卦：䷀ 乾为天", 输出)

    # 《增删卜易》第二十章“申月己卯日父子七人” https://zh.wikisource.org/wiki/增刪卜易/20
    def test_申月己卯父子七人(self):
        输出 = 运行("金钱卦.py", "1\n2 3 3 2 3 3\n")
        self.assertIn("本卦：䷸ 巽为风", 输出)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 输出)
        self.assertIn("变卦：䷁ 坤为地", 输出)

    # 《增删卜易》第21章“寅月庚申占子痘症”，秦慎安校勘本PDF第83页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=83
    def test_寅月庚申占子痘症(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 9 7\n\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)
        self.assertIn("主卦：䷤ 风火家人（巽宫，属木，世2应5）", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己酉", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 己未", 纳甲)

    # 《增删卜易》第22章“寅月己未占女痘”，秦慎安校勘本PDF第84页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=84
    def test_寅月己未占女痘(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 6 8 8 8 8\n\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷆ 地水师", 钱卦)
        self.assertIn("主卦：䷁ 坤为地（坤宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷆ 地水师", 纳甲)
        self.assertIn("二爻 父母 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 戊辰", 纳甲)

    # 《增删卜易》第23章“丑月丁酉占父出外”，秦慎安校勘本PDF第85页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=85
    def test_丑月丁酉占父出外(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 2 2 1 3\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 8 8 7 9\n\n")
        self.assertIn("本卦：䷺ 风水涣", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷜ 坎为水", 钱卦)
        self.assertIn("主卦：䷺ 风水涣（离宫，属火，世5应2）", 纳甲)
        self.assertIn("变卦：䷜ 坎为水", 纳甲)
        self.assertIn("上爻 父母 辛卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊子", 纳甲)

    # 《增删卜易》第24章“卯月辛巳代占长辈功名”，秦慎安校勘本PDF第87页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=87
    def test_卯月辛巳代占长辈功名(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 1 0 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 7 6 7 7\n\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)
        self.assertIn("主卦：䷸ 巽为风（巽宫，属木，世6应3）", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 甲子", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)

    # 《增删卜易》第24章“午月丙寅占主病”，秦慎安校勘本PDF第87页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NLC416-12jh005345-45344_增刪卜易.pdf?page=87
    def test_午月丙寅占主病(self):
        钱卦 = 运行("金钱卦.py", "1\n3 0 3 3 0 3\n")
        纳甲 = 运行("六爻纳甲.py", "9 6 9 9 6 9\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷜ 坎为水", 钱卦)
        self.assertIn("主卦：䷝ 离为火（离宫，属火，世6应3）", 纳甲)
        self.assertIn("变卦：䷜ 坎为水", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 戊子", 纳甲)
        self.assertIn("二爻 子孙 己丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 戊辰", 纳甲)

    # 《卜筮正宗》十八问答所记伏神、暗动、月破、应期等未在当前脚本输出，只重放明爻主变与纳甲，不据占断文字造程序预期 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf

    # 《卜筮正宗》卷十三十八问答第一问，光绪十五年重刻本第六册PDF第4页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=4
    def test_申月戊子占坟地(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 7\n\n")
        self.assertIn("本卦：䷖ 山地剥", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷖ 山地剥（乾宫，属金，世5应2）", 纳甲)
        self.assertIn("变卦：䷖ 山地剥", 纳甲)
        self.assertIn("五爻 子孙 丙子", 纳甲)
        self.assertIn("上爻 妻财 丙寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第5页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=5
    def test_卯月癸亥占家宅人口(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 0 1 0\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 6 7 6\n\n")
        self.assertIn("本卦：䷄ 水天需", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)
        self.assertIn("主卦：䷄ 水天需（坤宫，属土，世4应1）", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("四爻 子孙 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬午", 纳甲)
        self.assertIn("上爻 妻财 戊子 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 壬戌", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第6页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=6
    def test_卯月乙未占卖货(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 1 2 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 6 7 8 7 7\n\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)
        self.assertIn("主卦：䷤ 风火家人（巽宫，属木，世2应5）", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("二爻 妻财 己丑 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 甲寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第7页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=7
    def test_酉月丙寅占何日雨(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 9 8 8 8\n\n")
        self.assertIn("本卦：䷭ 地风升", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷆ 地水师", 钱卦)
        self.assertIn("主卦：䷭ 地风升（震宫，属木，世4应1）", 纳甲)
        self.assertIn("变卦：䷆ 地水师", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第8页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=8
    def test_卯月乙酉占索房价(self):
        钱卦 = 运行("金钱卦.py", "1\n2 3 2 2 3 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 9 8 8 9 8\n\n")
        self.assertIn("本卦：䷜ 坎为水", 钱卦)
        self.assertIn("动爻：二爻、五爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)
        self.assertIn("主卦：䷜ 坎为水（坎宫，属水，世6应3）", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("二爻 官鬼 戊辰 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 乙巳", 纳甲)
        self.assertIn("五爻 官鬼 戊戌 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第9页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=9
    def test_申月戊辰占具题(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 2 2 2 0\n")
        纳甲 = 运行("六爻纳甲.py", "6 6 8 8 8 6\n\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：初爻、二爻、上爻", 钱卦)
        self.assertIn("变卦：䷨ 山泽损", 钱卦)
        self.assertIn("主卦：䷁ 坤为地（坤宫，属土，世6应3）", 纳甲)
        self.assertIn("变卦：䷨ 山泽损", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丙寅", 纳甲)
        self.assertIn("二爻 父母 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第二问，光绪十五年重刻本第六册PDF第9页；背数依原爻画换算，未记年份不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=9
    def test_丁巳占虑大计(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 1 3 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "6 8 7 9 8 9\n\n")
        self.assertIn("本卦：䷷ 火山旅", 钱卦)
        self.assertIn("动爻：初爻、四爻、上爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)
        self.assertIn("主卦：䷷ 火山旅（离宫，属火，世1应4）", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 癸酉", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸丑", 纳甲)
        self.assertIn("初爻 子孙 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 己卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第10页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=10
    def test_申月戊辰妻占夫近病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 9 7\n\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("五爻 妻财 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 己未", 纳甲)
        self.assertIn("四爻 兄弟 壬午", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第10页；第三问卯月甲寅占风水困之节，与现有《增删卜易》卯月甲寅占风水为同案，保留已核测试，不重复。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=10

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第11页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=11
    def test_丑月戊子自占近病(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 9 7\n\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：初爻、五爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)
        self.assertIn("五爻 妻财 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 己未", 纳甲)
        self.assertIn("初爻 父母 己卯 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙辰", 纳甲)

    # 《卜筮正宗》卷十三十八问答第三问，光绪十五年重刻本第六册PDF第11页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=11
    def test_寅月乙丑子占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 9 8 8 8\n\n")
        self.assertIn("本卦：䷭ 地风升", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷆ 地水师", 钱卦)
        self.assertIn("主卦：䷭ 地风升", 纳甲)
        self.assertIn("变卦：䷆ 地水师", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)
        self.assertIn("二爻 父母 辛亥", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第12页；第四问卯月丁巳两村争戽水，与已核《增删卜易》卯月丁巳争田水同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=12

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第13页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=13
    def test_巳月丁酉递呈谋补缺(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 9\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷄ 水天需", 钱卦)
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷄ 水天需", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊子", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第13页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=13
    def test_寅月丙辰占选期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 7\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 辛未", 纳甲)
        self.assertIn("二爻 妻财 甲寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14
    def test_辰月丁亥占辨复(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 0 1 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 8 6 7 7 8\n\n")
        self.assertIn("本卦：䷬ 泽地萃", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)
        self.assertIn("主卦：䷬ 泽地萃", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("三爻 妻财 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己亥", 纳甲)
        self.assertIn("初爻 父母 乙未 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 己卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14
    def test_丑月己卯占父急病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 3 1 3 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 9 7 9 9 7\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：二爻、四爻、五爻", 钱卦)
        self.assertIn("变卦：䷕ 山火贲", 钱卦)
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷕ 山火贲", 纳甲)
        self.assertIn("五爻 兄弟 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙子", 纳甲)
        self.assertIn("四爻 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丙戌", 纳甲)
        self.assertIn("二爻 妻财 甲寅 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 己丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第14页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=14
    def test_丑月戊午占姑病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 3 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 9 8 9\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 癸酉", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 癸丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15
    def test_未月戊申占子归期(self):
        钱卦 = 运行("金钱卦.py", "1\n3 1 0 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "9 7 6 7 8 7\n\n")
        self.assertIn("本卦：䷥ 火泽睽", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷱ 火风鼎", 钱卦)
        self.assertIn("主卦：䷥ 火泽睽", 纳甲)
        self.assertIn("变卦：䷱ 火风鼎", 纳甲)
        self.assertIn("三爻 兄弟 丁丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 辛酉", 纳甲)
        self.assertIn("初爻 父母 丁巳 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 辛丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15
    def test_巳月丙申占父归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 0 0 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 6 6 7\n\n")
        self.assertIn("本卦：䷙ 山天大畜", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)
        self.assertIn("主卦：䷙ 山天大畜", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("五爻 妻财 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬申", 纳甲)
        self.assertIn("四爻 兄弟 丙戌 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第15页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=15
    def test_丑月戊辰占防参劾(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 3 2 1 0\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 9 8 7 6\n\n")
        self.assertIn("本卦：䷯ 水风井", 钱卦)
        self.assertIn("动爻：初爻、三爻、上爻", 钱卦)
        self.assertIn("变卦：䷼ 风泽中孚", 钱卦)
        self.assertIn("主卦：䷯ 水风井", 纳甲)
        self.assertIn("变卦：䷼ 风泽中孚", 纳甲)
        self.assertIn("上爻 父母 戊子 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 辛卯", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丁丑", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁巳", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第16页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=16
    def test_寅月戊午占地造葬(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 0 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 6 7\n\n")
        self.assertIn("本卦：䷚ 山雷颐", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("主卦：䷚ 山雷颐", 纳甲)
        self.assertIn("变卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("五爻 父母 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 壬申", 纳甲)
        self.assertIn("四爻 妻财 丙戌 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第16页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=16
    def test_巳月甲辰占雨止(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 3 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 9 7 8 7\n\n")
        self.assertIn("本卦：䷱ 火风鼎", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷥ 火泽睽", 钱卦)
        self.assertIn("主卦：䷱ 火风鼎", 纳甲)
        self.assertIn("变卦：䷥ 火泽睽", 纳甲)
        self.assertIn("三爻 妻财 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丁丑", 纳甲)
        self.assertIn("初爻 子孙 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁巳", 纳甲)

    # 《卜筮正宗》卷十三十八问答第四问，光绪十五年重刻本第六册PDF第17页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=17
    def test_酉月辛卯妻去摇会(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 3 2 0\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 9 8 6\n\n")
        self.assertIn("本卦：䷟ 雷风恒", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷑ 山风蛊", 钱卦)
        self.assertIn("主卦：䷟ 雷风恒", 纳甲)
        self.assertIn("变卦：䷑ 山风蛊", 纳甲)
        self.assertIn("上爻 妻财 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丙寅", 纳甲)
        self.assertIn("四爻 子孙 庚午 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丙戌", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18
    def test_卯月壬申占随官上任(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 0 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 6 6 8 7 8\n\n")
        self.assertIn("本卦：䷇ 水地比", 钱卦)
        self.assertIn("动爻：二爻、三爻", 钱卦)
        self.assertIn("变卦：䷯ 水风井", 钱卦)
        self.assertIn("主卦：䷇ 水地比", 纳甲)
        self.assertIn("变卦：䷯ 水风井", 纳甲)
        self.assertIn("三爻 官鬼 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 辛酉", 纳甲)
        self.assertIn("二爻 父母 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 辛亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18
    def test_卯月乙亥占升选(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 2 2 0 0\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 8 8 6 6\n\n")
        self.assertIn("本卦：䷒ 地泽临", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷼ 风泽中孚", 钱卦)
        self.assertIn("主卦：䷒ 地泽临", 纳甲)
        self.assertIn("变卦：䷼ 风泽中孚", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 辛卯", 纳甲)
        self.assertIn("五爻 妻财 癸亥 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第18页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=18
    def test_未月丁巳占嫂复病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 9\n\n")
        self.assertIn("本卦：䷖ 山地剥", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)
        self.assertIn("主卦：䷖ 山地剥", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("上爻 妻财 丙寅 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸酉", 纳甲)
        self.assertIn("五爻 子孙 丙子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第19页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=19
    def test_巳月戊申往前处脱货(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 0 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 6 7 7\n\n")
        self.assertIn("本卦：䷈ 风天小畜", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)
        self.assertIn("主卦：䷈ 风天小畜", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)
        self.assertIn("上爻 兄弟 辛卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第五问，光绪十五年重刻本第六册PDF第19页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=19
    def test_卯月戊子占坟地(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 2 3 3\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 8 9 9\n\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷭ 地风升", 钱卦)
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷭ 地风升", 纳甲)
        self.assertIn("上爻 兄弟 辛卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 癸酉", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 癸亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第20页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=20
    def test_申月乙卯避兵(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 0 1 3 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 6 6 7 9 9\n\n")
        self.assertIn("本卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷡ 雷天大壮", 钱卦)
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

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第21页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=21
    def test_申月甲午占父在任(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 3 3\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 9 9\n\n")
        self.assertIn("本卦：䷫ 天风姤", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷟ 雷风恒", 钱卦)
        self.assertIn("主卦：䷫ 天风姤", 纳甲)
        self.assertIn("变卦：䷟ 雷风恒", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚戌", 纳甲)
        self.assertIn("五爻 兄弟 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第21页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=21
    def test_寅月乙卯客外占家中(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 0 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 6 6 7 7 7\n\n")
        self.assertIn("本卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("动爻：二爻、三爻", 钱卦)
        self.assertIn("变卦：䷀ 乾为天", 钱卦)
        self.assertIn("主卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("三爻 妻财 庚辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 甲辰", 纳甲)
        self.assertIn("二爻 兄弟 庚寅 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 甲寅", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第22页；第七问巳月戊戌求财益卦，与已核《增删卜易》巳月戊戌占财同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=22

    # 《卜筮正宗》卷十三十八问答第六问，光绪十五年重刻本第六册PDF第22页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=22
    def test_寅月乙卯占妻在家(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 0 0\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 6 6\n\n")
        self.assertIn("本卦：䷏ 雷地豫", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷋ 天地否", 钱卦)
        self.assertIn("主卦：䷏ 雷地豫", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("上爻 妻财 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 壬戌", 纳甲)
        self.assertIn("五爻 官鬼 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 壬申", 纳甲)
        self.assertIn("四爻 子孙 庚午", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23
    def test_亥月甲子占仆归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 8\n\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("四爻 兄弟 丁亥", 纳甲)
        self.assertIn("上爻 官鬼 丁未", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23
    def test_申月丁卯见贵求财(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 7\n\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷌ 天火同人", 纳甲)
        self.assertIn("三爻 官鬼 己亥", 纳甲)
        self.assertIn("五爻 妻财 壬申", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第23页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=23
    def test_子月癸酉自占婚(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 2 0\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 8 6\n\n")
        self.assertIn("本卦：䷟ 雷风恒", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷱ 火风鼎", 钱卦)
        self.assertIn("主卦：䷟ 雷风恒", 纳甲)
        self.assertIn("变卦：䷱ 火风鼎", 纳甲)
        self.assertIn("上爻 妻财 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己巳", 纳甲)
        self.assertIn("三爻 官鬼 辛酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24
    def test_午月癸丑占妻病愈期(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 9 7 8\n\n")
        self.assertIn("本卦：䷬ 泽地萃", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷇ 水地比", 钱卦)
        self.assertIn("主卦：䷬ 泽地萃", 纳甲)
        self.assertIn("变卦：䷇ 水地比", 纳甲)
        self.assertIn("四爻 子孙 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)
        self.assertIn("三爻 妻财 乙卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24
    def test_寅月庚戌占子病愈期(self):
        钱卦 = 运行("金钱卦.py", "1\n0 3 3 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "6 9 9 7 7 7\n\n")
        self.assertIn("本卦：䷫ 天风姤", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻", 钱卦)
        self.assertIn("变卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("主卦：䷫ 天风姤", 纳甲)
        self.assertIn("变卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("三爻 兄弟 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚辰", 纳甲)
        self.assertIn("二爻 子孙 辛亥 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚寅", 纳甲)
        self.assertIn("初爻 父母 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 庚子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第24页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=24
    def test_未月庚子占求财到手(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 7 7\n\n")
        self.assertIn("本卦：䷈ 风天小畜", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷈ 风天小畜", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("三爻 妻财 甲辰", 纳甲)
        self.assertIn("四爻 妻财 辛未", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25
    def test_酉月庚辰占岳母近病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 0 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 6 8 8 8\n\n")
        self.assertIn("本卦：䷆ 地水师", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷭ 地风升", 钱卦)
        self.assertIn("主卦：䷆ 地水师", 纳甲)
        self.assertIn("变卦：䷭ 地风升", 纳甲)
        self.assertIn("三爻 妻财 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛酉", 纳甲)
        self.assertIn("上爻 父母 癸酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25
    def test_酉月壬辰占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 7 8\n\n")
        self.assertIn("本卦：䷛ 泽风大过", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷛ 泽风大过", 纳甲)
        self.assertIn("变卦：䷛ 泽风大过", 纳甲)
        self.assertIn("四爻 父母 丁亥", 纳甲)
        self.assertIn("三爻 官鬼 辛酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第25页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=25
    def test_子月乙巳占弟尸首(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 8 8 8\n\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷗ 地雷复", 纳甲)
        self.assertIn("上爻 子孙 癸酉", 纳甲)
        self.assertIn("四爻 兄弟 癸丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第26页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=26
    def test_丑月甲午占父近病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 2 0\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 8 6\n\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：四爻、上爻", 钱卦)
        self.assertIn("变卦：䷔ 火雷噬嗑", 钱卦)
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷔ 火雷噬嗑", 纳甲)
        self.assertIn("初爻 妻财 庚子", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 己巳", 纳甲)
        self.assertIn("四爻 兄弟 癸丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27
    def test_未月戊戌因大旱占雨(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 7 7\n\n")
        self.assertIn("本卦：䷓ 风地观", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷓ 风地观", 纳甲)
        self.assertIn("变卦：䷓ 风地观", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27
    def test_未月戊戌占交疏人来期(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 8 7 8\n\n")
        self.assertIn("本卦：䷦ 水山蹇", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷦ 水山蹇", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("四爻 兄弟 戊申", 纳甲)
        self.assertIn("五爻 父母 戊戌", 纳甲)

    # 《卜筮正宗》卷十三十八问答第七问，光绪十五年重刻本第六册PDF第27页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=27
    def test_未月甲辰占大雨(self):
        钱卦 = 运行("金钱卦.py", "1\n0 2 1 1 0 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 8 7 7 6 8\n\n")
        self.assertIn("本卦：䷽ 雷山小过", 钱卦)
        self.assertIn("动爻：初爻、五爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)
        self.assertIn("主卦：䷽ 雷山小过", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("五爻 兄弟 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁酉", 纳甲)
        self.assertIn("初爻 父母 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 己卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第28页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=28
    def test_戌月丁卯占讼事(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 8 8\n\n")
        self.assertIn("本卦：䷊ 地天泰", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷊ 地天泰", 纳甲)
        self.assertIn("变卦：䷊ 地天泰", 纳甲)
        self.assertIn("三爻 兄弟 甲辰", 纳甲)
        self.assertIn("上爻 子孙 癸酉", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第29页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=29
    def test_亥月己丑占将来有官否(self):
        钱卦 = 运行("金钱卦.py", "1\n3 1 2 1 1 0\n")
        纳甲 = 运行("六爻纳甲.py", "9 7 8 7 7 6\n\n")
        self.assertIn("本卦：䷹ 兑为泽", 钱卦)
        self.assertIn("动爻：初爻、上爻", 钱卦)
        self.assertIn("变卦：䷅ 天水讼", 钱卦)
        self.assertIn("主卦：䷹ 兑为泽", 纳甲)
        self.assertIn("变卦：䷅ 天水讼", 纳甲)
        self.assertIn("上爻 父母 丁未 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬戌", 纳甲)
        self.assertIn("初爻 官鬼 丁巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 戊寅", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第29页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=29
    def test_辰月戊子占父归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 1 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 7 9\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷪ 泽天夬", 钱卦)
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷪ 泽天夬", 纳甲)
        self.assertIn("上爻 父母 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丁未", 纳甲)
        self.assertIn("初爻 子孙 甲子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第30页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=30
    def test_午月癸卯占后运功名(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 3 2 0 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 9 8 6 7\n\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：三爻、五爻", 钱卦)
        self.assertIn("变卦：䷓ 风地观", 钱卦)
        self.assertIn("主卦：䷳ 艮为山", 纳甲)
        self.assertIn("变卦：䷓ 风地观", 纳甲)
        self.assertIn("五爻 妻财 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 乙卯", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第30页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=30
    def test_寅月甲午占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 0 3 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 6 9 8 8 7\n\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：二爻、三爻", 钱卦)
        self.assertIn("变卦：䷃ 山水蒙", 钱卦)
        self.assertIn("主卦：䷳ 艮为山", 纳甲)
        self.assertIn("变卦：䷃ 山水蒙", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊午", 纳甲)
        self.assertIn("二爻 父母 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 戊辰", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第31页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=31
    def test_丑月庚申占坟地风水(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 1 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 7 7 8\n\n")
        self.assertIn("本卦：䷞ 泽山咸", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷞ 泽山咸", 纳甲)
        self.assertIn("变卦：䷞ 泽山咸", 纳甲)
        self.assertIn("三爻 兄弟 丙申", 纳甲)
        self.assertIn("上爻 父母 丁未", 纳甲)

    # 《卜筮正宗》卷十三十八问答第八问，光绪十五年重刻本第六册PDF第31页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=31
    def test_申月辛卯占买宅(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 1 1 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 6 7 7 7 8\n\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷪ 泽天夬", 钱卦)
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷪ 泽天夬", 纳甲)
        self.assertIn("二爻 官鬼 己丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 甲寅", 纳甲)
        self.assertIn("三爻 兄弟 己亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第32页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=32
    def test_卯月壬辰占候文书(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 8 8 7\n\n")
        self.assertIn("本卦：䷕ 山火贲", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷕ 山火贲", 纳甲)
        self.assertIn("变卦：䷕ 山火贲", 纳甲)
        self.assertIn("二爻 兄弟 己丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第32页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=32
    def test_辰月丁巳占逃仆(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 8 7 8\n\n")
        self.assertIn("本卦：䷦ 水山蹇", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷦ 水山蹇", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("二爻 官鬼 丙午", 纳甲)
        self.assertIn("初爻 父母 丙辰", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33
    def test_酉月丙辰占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 8 8 8\n\n")
        self.assertIn("本卦：䷭ 地风升", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷭ 地风升", 纳甲)
        self.assertIn("变卦：䷭ 地风升", 纳甲)
        self.assertIn("二爻 父母 辛亥", 纳甲)
        self.assertIn("五爻 父母 癸亥", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33
    def test_卯月丙辰占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 8 8 8\n\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷗ 地雷复", 纳甲)
        self.assertIn("二爻 官鬼 庚寅", 纳甲)
        self.assertIn("四爻 兄弟 癸丑", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第33页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=33
    def test_辰月庚申占蚕桑叶贵贱(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 8 7 8\n\n")
        self.assertIn("本卦：䷾ 水火既济", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷾ 水火既济", 纳甲)
        self.assertIn("变卦：䷾ 水火既济", 纳甲)
        self.assertIn("三爻 兄弟 己亥", 纳甲)
        self.assertIn("上爻 兄弟 戊子", 纳甲)

    # 《卜筮正宗》卷十三十八问答第九问，光绪十五年重刻本第六册PDF第34页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=34
    def test_寅月戊辰占病有何鬼神(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 7 7\n\n")
        self.assertIn("本卦：䷈ 风天小畜", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷈ 风天小畜", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("三爻 妻财 甲辰", 纳甲)
        self.assertIn("四爻 妻财 辛未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第36页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=36
    def test_申月癸卯占乡试(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 0 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 6 8\n\n")
        self.assertIn("本卦：䷟ 雷风恒", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷛ 泽风大过", 钱卦)
        self.assertIn("主卦：䷟ 雷风恒", 纳甲)
        self.assertIn("变卦：䷛ 泽风大过", 纳甲)
        self.assertIn("五爻 官鬼 庚申 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁酉", 纳甲)
        self.assertIn("三爻 官鬼 辛酉", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第36页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=36
    def test_酉月庚戌占生子年(self):
        钱卦 = 运行("金钱卦.py", "1\n1 0 2 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 6 8 8 7 8\n\n")
        self.assertIn("本卦：䷂ 水雷屯", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)
        self.assertIn("主卦：䷂ 水雷屯", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)
        self.assertIn("二爻 子孙 庚寅 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁卯", 纳甲)
        self.assertIn("五爻 官鬼 戊戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第37页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=37
    def test_卯月乙丑自占求婚(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 2 3 0 3\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 8 9 6 9\n\n")
        self.assertIn("本卦：䷔ 火雷噬嗑", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷇ 水地比", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第37页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=37
    def test_酉月甲辰因参论占自陈(self):
        钱卦 = 运行("金钱卦.py", "1\n0 3 0 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 9 6 8 8 8\n\n")
        self.assertIn("本卦：䷆ 地水师", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻", 钱卦)
        self.assertIn("变卦：䷣ 地火明夷", 钱卦)
        self.assertIn("主卦：䷆ 地水师", 纳甲)
        self.assertIn("变卦：䷣ 地火明夷", 纳甲)
        self.assertIn("三爻 妻财 戊午 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 己亥", 纳甲)
        self.assertIn("二爻 官鬼 戊辰 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 己丑", 纳甲)
        self.assertIn("初爻 子孙 戊寅 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 己卯", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第38页；第十一问午月丙辰出外贸易恒之豫，与已核《增删卜易》午月丙辰经商同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38

    # 《卜筮正宗》卷十四十八问答第十问，光绪十五年重刻本第六册PDF第38页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38
    def test_未月丁卯占出仕功名(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 9\n\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("上爻 子孙 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丁未", 纳甲)
        self.assertIn("三爻 官鬼 己亥", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第38页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=38
    def test_戌月甲辰占借银(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("五爻 妻财 癸亥", 纳甲)
        self.assertIn("初爻 兄弟 乙未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第39页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=39
    def test_寅月戊戌占失银物(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 3 0 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 9 6 7 7\n\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：三爻、四爻", 钱卦)
        self.assertIn("变卦：䷅ 天水讼", 钱卦)
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷅ 天水讼", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 戊午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40
    def test_辰月丁酉自占婚姻(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 7 7\n\n")
        self.assertIn("本卦：䷋ 天地否", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷋ 天地否", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("三爻 妻财 乙卯", 纳甲)
        self.assertIn("上爻 父母 壬戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40
    def test_卯月乙卯占谋望求财(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 1 1 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 7 7 7 8\n\n")
        self.assertIn("本卦：䷛ 泽风大过", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷛ 泽风大过", 纳甲)
        self.assertIn("变卦：䷛ 泽风大过", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第40页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=40
    def test_午月辛亥占师近病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 2 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 8 8 7 8\n\n")
        self.assertIn("本卦：䷻ 水泽节", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷻ 水泽节", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)
        self.assertIn("四爻 父母 戊申", 纳甲)
        self.assertIn("初爻 妻财 丁巳", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第41页；第十一问未月丁巳悔婚离之旅，与已核《增删卜易》未月丁巳悔婚同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=41

    # 《卜筮正宗》卷十四十八问答第十一问，光绪十五年重刻本第六册PDF第41页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=41
    def test_寅月戊辰占兄近病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 8 7\n\n")
        self.assertIn("本卦：䷢ 火地晋", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷢ 火地晋", 纳甲)
        self.assertIn("变卦：䷢ 火地晋", 纳甲)
        self.assertIn("四爻 兄弟 己酉", 纳甲)
        self.assertIn("上爻 官鬼 己巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第42页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=42
    def test_巳月戊寅占何日得财(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 2 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 8 9\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷶ 雷火丰", 钱卦)
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷶ 雷火丰", 纳甲)
        self.assertIn("上爻 兄弟 己巳 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 庚戌", 纳甲)
        self.assertIn("四爻 妻财 己酉", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第42页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=42
    def test_午月己卯占妻病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 0 1 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 6 7 8 8\n\n")
        self.assertIn("本卦：䷲ 震为雷", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷶ 雷火丰", 钱卦)
        self.assertIn("主卦：䷲ 震为雷", 纳甲)
        self.assertIn("变卦：䷶ 雷火丰", 纳甲)
        self.assertIn("三爻 妻财 庚辰 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 己亥", 纳甲)
        self.assertIn("上爻 妻财 庚戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43
    def test_寅月戊子占生产(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 0 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 6 7\n\n")
        self.assertIn("本卦：䷖ 山地剥", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷓ 风地观", 钱卦)
        self.assertIn("主卦：䷖ 山地剥", 纳甲)
        self.assertIn("变卦：䷓ 风地观", 纳甲)
        self.assertIn("五爻 子孙 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 辛巳", 纳甲)
        self.assertIn("上爻 妻财 丙寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43
    def test_子月辛未占子病(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 3 2 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "6 6 9 8 7 7\n\n")
        self.assertIn("本卦：䷴ 风山渐", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻", 钱卦)
        self.assertIn("变卦：䷼ 风泽中孚", 钱卦)
        self.assertIn("主卦：䷴ 风山渐", 纳甲)
        self.assertIn("变卦：䷼ 风泽中孚", 纳甲)
        self.assertIn("三爻 子孙 丙申 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 丁丑", 纳甲)
        self.assertIn("二爻 父母 丙午 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丁卯", 纳甲)
        self.assertIn("初爻 兄弟 丙辰 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 丁巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第43页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=43
    def test_辰月甲寅占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 3 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 9 8\n\n")
        self.assertIn("本卦：䷂ 水雷屯", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷲ 震为雷", 钱卦)
        self.assertIn("主卦：䷂ 水雷屯", 纳甲)
        self.assertIn("变卦：䷲ 震为雷", 纳甲)
        self.assertIn("五爻 官鬼 戊戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚申", 纳甲)
        self.assertIn("四爻 父母 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 庚午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第44页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=44
    def test_申月丙辰占弟病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 3 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 9 8\n\n")
        self.assertIn("本卦：䷾ 水火既济", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷶ 雷火丰", 钱卦)
        self.assertIn("主卦：䷾ 水火既济", 纳甲)
        self.assertIn("变卦：䷶ 雷火丰", 纳甲)
        self.assertIn("五爻 官鬼 戊戌 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 庚申", 纳甲)
        self.assertIn("四爻 父母 戊申 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 庚午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第45页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=45
    def test_申月癸丑占子在楚生理(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 2 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 8 8 8 7\n\n")
        self.assertIn("本卦：䷨ 山泽损", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷨ 山泽损", 纳甲)
        self.assertIn("变卦：䷨ 山泽损", 纳甲)
        self.assertIn("四爻 兄弟 丙戌", 纳甲)
        self.assertIn("上爻 官鬼 丙寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第45页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=45
    def test_叔占侄在外平安(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 3 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 9 9 7\n\n")
        self.assertIn("本卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷚ 山雷颐", 钱卦)
        self.assertIn("主卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("变卦：䷚ 山雷颐", 纳甲)
        self.assertIn("五爻 官鬼 壬申 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 丙子", 纳甲)
        self.assertIn("四爻 子孙 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丙戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46
    def test_亥月丙寅嫂占姑病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 9 7 8\n\n")
        self.assertIn("本卦：䷞ 泽山咸", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷦ 水山蹇", 钱卦)
        self.assertIn("主卦：䷞ 泽山咸", 纳甲)
        self.assertIn("变卦：䷦ 水山蹇", 纳甲)
        self.assertIn("四爻 子孙 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)
        self.assertIn("初爻 父母 丙辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46
    def test_卯月乙未姑占弟妇怀孕(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 2 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 8 9 7 8\n\n")
        self.assertIn("本卦：䷮ 泽水困", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷜ 坎为水", 钱卦)
        self.assertIn("主卦：䷮ 泽水困", 纳甲)
        self.assertIn("变卦：䷜ 坎为水", 纳甲)
        self.assertIn("四爻 子孙 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 戊申", 纳甲)
        self.assertIn("上爻 父母 丁未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第46页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=46
    def test_丁卯占劾奏他人(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 7 8 7\n\n")
        self.assertIn("本卦：䷷ 火山旅", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷷ 火山旅", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)
        self.assertIn("三爻 妻财 丙申", 纳甲)
        self.assertIn("上爻 兄弟 己巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第47页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=47
    def test_未月戊申因误军粮被参(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 1 1 2 0\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 7 7 8 6\n\n")
        self.assertIn("本卦：䷶ 雷火丰", 钱卦)
        self.assertIn("动爻：初爻、上爻", 钱卦)
        self.assertIn("变卦：䷷ 火山旅", 钱卦)
        self.assertIn("主卦：䷶ 雷火丰", 纳甲)
        self.assertIn("变卦：䷷ 火山旅", 纳甲)
        self.assertIn("上爻 官鬼 庚戌 ⚋ ×", 纳甲)
        self.assertIn("→ 妻财 己巳", 纳甲)
        self.assertIn("初爻 子孙 己卯 ⚊ ○", 纳甲)
        self.assertIn("→ 官鬼 丙辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十二问，光绪十五年重刻本第六册PDF第47页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=47
    def test_卯月壬寅占坟地(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 9 7 8\n\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷾ 水火既济", 钱卦)
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷾ 水火既济", 纳甲)
        self.assertIn("四爻 兄弟 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊申", 纳甲)
        self.assertIn("三爻 兄弟 己亥", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第48页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=48
    def test_酉月壬子占侄被害(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 8 8\n\n")
        self.assertIn("本卦：䷡ 雷天大壮", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷊ 地天泰", 钱卦)
        self.assertIn("主卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("变卦：䷊ 地天泰", 纳甲)
        self.assertIn("四爻 父母 庚午 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 癸丑", 纳甲)
        self.assertIn("上爻 兄弟 庚戌", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第48页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=48
    def test_巳月丁酉占文书到期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 7 7\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷀ 乾为天", 纳甲)
        self.assertIn("变卦：䷀ 乾为天", 纳甲)
        self.assertIn("上爻 父母 壬戌", 纳甲)
        self.assertIn("三爻 父母 甲辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49
    def test_午月丙子占开店(self):
        钱卦 = 运行("金钱卦.py", "1\n3 1 1 3 0 0\n")
        纳甲 = 运行("六爻纳甲.py", "9 7 7 9 6 6\n\n")
        self.assertIn("本卦：䷡ 雷天大壮", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷸ 巽为风", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49
    def test_申月乙卯因子被拿占讼(self):
        钱卦 = 运行("金钱卦.py", "1\n2 3 3 2 3 3\n")
        纳甲 = 运行("六爻纳甲.py", "8 9 9 8 9 9\n\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：二爻、三爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第49页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=49
    def test_未月乙亥往买卖求利(self):
        钱卦 = 运行("金钱卦.py", "1\n1 3 2 1 3 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 9 8 7 9 8\n\n")
        self.assertIn("本卦：䷹ 兑为泽", 钱卦)
        self.assertIn("动爻：二爻、五爻", 钱卦)
        self.assertIn("变卦：䷲ 震为雷", 钱卦)
        self.assertIn("主卦：䷹ 兑为泽", 纳甲)
        self.assertIn("变卦：䷲ 震为雷", 纳甲)
        self.assertIn("五爻 兄弟 丁酉 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 庚申", 纳甲)
        self.assertIn("二爻 妻财 丁卯 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第50页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=50
    def test_子月己巳占赌钱(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("五爻 妻财 癸亥", 纳甲)
        self.assertIn("三爻 官鬼 乙卯", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第50页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=50
    def test_辰月庚午占会(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 0 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 6 7 7\n\n")
        self.assertIn("本卦：䷓ 风地观", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷋ 天地否", 钱卦)
        self.assertIn("主卦：䷓ 风地观", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("四爻 父母 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 壬午", 纳甲)
        self.assertIn("五爻 官鬼 辛巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51
    def test_寅月甲午占子久病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 1 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 7 8 8\n\n")
        self.assertIn("本卦：䷡ 雷天大壮", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("变卦：䷡ 雷天大壮", 纳甲)
        self.assertIn("五爻 子孙 庚申", 纳甲)
        self.assertIn("四爻 父母 庚午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51
    def test_卯月甲午占起去寄信(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 1 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 7 7 7\n\n")
        self.assertIn("本卦：䷋ 天地否", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷋ 天地否", 纳甲)
        self.assertIn("变卦：䷋ 天地否", 纳甲)
        self.assertIn("三爻 妻财 乙卯", 纳甲)
        self.assertIn("四爻 官鬼 壬午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十三问，光绪十五年重刻本第六册PDF第51页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=51
    def test_巳月甲戌同乡占借贷(self):
        钱卦 = 运行("金钱卦.py", "1\n3 2 2 0 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "9 8 8 6 8 8\n\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：初爻、四爻", 钱卦)
        self.assertIn("变卦：䷏ 雷地豫", 钱卦)
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷏ 雷地豫", 纳甲)
        self.assertIn("四爻 兄弟 癸丑 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 庚午", 纳甲)
        self.assertIn("初爻 妻财 庚子 ⚊ ○", 纳甲)
        self.assertIn("→ 兄弟 乙未", 纳甲)

    # 《卜筮正宗》光绪十五年重刻本第六册PDF第52页；第十三问巳月甲寅延师训子否之乾，与已核《增删卜易》巳月甲寅严师训子同案，不重复测试。 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=52

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53
    def test_寅月庚申占侄孙病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 0 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 6 9 7\n\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：四爻、五爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)
        self.assertIn("主卦：䷤ 风火家人", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 己未", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己酉", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53
    def test_辰月戊午占夫病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 3 3 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 9 9 8 7\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：三爻、四爻", 钱卦)
        self.assertIn("变卦：䷚ 山雷颐", 钱卦)
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷚ 山雷颐", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙戌", 纳甲)
        self.assertIn("三爻 官鬼 己亥 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 庚辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第53页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=53
    def test_亥月戊戌占妻近病(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 1 0 3 1\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 7 6 9 7\n\n")
        self.assertIn("本卦：䷸ 巽为风", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻", 钱卦)
        self.assertIn("变卦：䷍ 火天大有", 钱卦)
        self.assertIn("主卦：䷸ 巽为风", 纳甲)
        self.assertIn("变卦：䷍ 火天大有", 纳甲)
        self.assertIn("五爻 子孙 辛巳 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 己未", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 己酉", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 甲子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十四问，光绪十五年重刻本第六册PDF第54页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=54
    def test_戌月庚子占冬生意(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 2 0 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 8 6 7\n\n")
        self.assertIn("本卦：䷕ 山火贲", 钱卦)
        self.assertIn("动爻：五爻", 钱卦)
        self.assertIn("变卦：䷤ 风火家人", 钱卦)
        self.assertIn("主卦：䷕ 山火贲", 纳甲)
        self.assertIn("变卦：䷤ 风火家人", 纳甲)
        self.assertIn("五爻 妻财 丙子 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 辛巳", 纳甲)
        self.assertIn("上爻 官鬼 丙寅", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第54页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=54
    def test_午月丙午占自去请父回(self):
        钱卦 = 运行("金钱卦.py", "1\n1 3 1 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 9 7 7 8 7\n\n")
        self.assertIn("本卦：䷍ 火天大有", 钱卦)
        self.assertIn("动爻：二爻", 钱卦)
        self.assertIn("变卦：䷝ 离为火", 钱卦)
        self.assertIn("主卦：䷍ 火天大有", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("二爻 妻财 甲寅 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 己丑", 纳甲)
        self.assertIn("三爻 父母 甲辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第55页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=55
    def test_再占请父回(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 3 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 9 7 8\n\n")
        self.assertIn("本卦：䷰ 泽火革", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷾ 水火既济", 钱卦)
        self.assertIn("主卦：䷰ 泽火革", 纳甲)
        self.assertIn("变卦：䷾ 水火既济", 纳甲)
        self.assertIn("四爻 兄弟 丁亥 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 戊申", 纳甲)
        self.assertIn("上爻 官鬼 丁未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第55页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=55
    def test_申月辛卯占子嗣(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 8 8 8\n\n")
        self.assertIn("本卦：䷗ 地雷复", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷗ 地雷复", 纳甲)
        self.assertIn("变卦：䷗ 地雷复", 纳甲)
        self.assertIn("上爻 子孙 癸酉", 纳甲)
        self.assertIn("初爻 妻财 庚子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56
    def test_午月甲申占雨久伤麦(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 1 3\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 7 9\n\n")
        self.assertIn("本卦：䷌ 天火同人", 钱卦)
        self.assertIn("动爻：上爻", 钱卦)
        self.assertIn("变卦：䷰ 泽火革", 钱卦)
        self.assertIn("主卦：䷌ 天火同人", 纳甲)
        self.assertIn("变卦：䷰ 泽火革", 纳甲)
        self.assertIn("上爻 子孙 壬戌 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丁未", 纳甲)
        self.assertIn("四爻 兄弟 壬午", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56
    def test_申月甲午开煤窑占见煤时(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 3 2 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 9 8 7 7\n\n")
        self.assertIn("本卦：䷤ 风火家人", 钱卦)
        self.assertIn("动爻：三爻", 钱卦)
        self.assertIn("变卦：䷩ 风雷益", 钱卦)
        self.assertIn("主卦：䷤ 风火家人", 纳甲)
        self.assertIn("变卦：䷩ 风雷益", 纳甲)
        self.assertIn("三爻 父母 己亥 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 庚辰", 纳甲)
        self.assertIn("四爻 妻财 辛未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第56页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=56
    def test_寅月庚戌占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n2 3 0 3 0 3\n")
        纳甲 = 运行("六爻纳甲.py", "8 9 6 9 6 9\n\n")
        self.assertIn("本卦：䷿ 火水未济", 钱卦)
        self.assertIn("动爻：二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷦ 水山蹇", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十五问，光绪十五年重刻本第六册PDF第57页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=57
    def test_寅月甲辰占父远出归期(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 3 1 3 3\n")
        纳甲 = 运行("六爻纳甲.py", "6 6 9 7 9 9\n\n")
        self.assertIn("本卦：䷠ 天山遁", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷵ 雷泽归妹", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第57至58页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=57
    def test_午月庚辰占仆近出归期(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 1 1 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 7 7 8 7\n\n")
        self.assertIn("本卦：䷝ 离为火", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷝ 离为火", 纳甲)
        self.assertIn("变卦：䷝ 离为火", 纳甲)
        self.assertIn("四爻 妻财 己酉", 纳甲)
        self.assertIn("二爻 子孙 己丑", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第58页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=58
    def test_辰月己卯占今日还银(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 2 2 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 8 8 8 8\n\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷁ 坤为地", 纳甲)
        self.assertIn("五爻 妻财 癸亥", 纳甲)
        self.assertIn("初爻 兄弟 乙未", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第58至59页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=58
    def test_子月壬申占父在乱军(self):
        钱卦 = 运行("金钱卦.py", "1\n3 3 3 0 0 3\n")
        纳甲 = 运行("六爻纳甲.py", "9 9 9 6 6 9\n\n")
        self.assertIn("本卦：䷙ 山天大畜", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷬ 泽地萃", 钱卦)
        self.assertIn("主卦：䷙ 山天大畜", 纳甲)
        self.assertIn("变卦：䷬ 泽地萃", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十六问，光绪十五年重刻本第六册PDF第59页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=59
    def test_辰月甲子造坟葬亲(self):
        钱卦 = 运行("金钱卦.py", "1\n3 3 3 3 3 3\n")
        纳甲 = 运行("六爻纳甲.py", "9 9 9 9 9 9\n\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：初爻、二爻、三爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷁ 坤为地", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第60页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60
    def test_未月甲午占自升迁(self):
        钱卦 = 运行("金钱卦.py", "1\n2 1 2 2 0 0\n")
        纳甲 = 运行("六爻纳甲.py", "8 7 8 8 6 6\n\n")
        self.assertIn("本卦：䷆ 地水师", 钱卦)
        self.assertIn("动爻：五爻、上爻", 钱卦)
        self.assertIn("变卦：䷺ 风水涣", 钱卦)
        self.assertIn("主卦：䷆ 地水师", 纳甲)
        self.assertIn("变卦：䷺ 风水涣", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第60页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=60
    def test_亥月丙午占子脱难(self):
        钱卦 = 运行("金钱卦.py", "1\n0 0 2 1 2 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 6 8 7 8 8\n\n")
        self.assertIn("本卦：䷏ 雷地豫", 钱卦)
        self.assertIn("动爻：初爻、二爻", 钱卦)
        self.assertIn("变卦：䷵ 雷泽归妹", 钱卦)
        self.assertIn("主卦：䷏ 雷地豫", 纳甲)
        self.assertIn("变卦：䷵ 雷泽归妹", 纳甲)
        self.assertIn("二爻 子孙 乙巳 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丁卯", 纳甲)
        self.assertIn("初爻 妻财 乙未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁巳", 纳甲)
        self.assertIn("三爻 兄弟 乙卯", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第61页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=61
    def test_未月丁丑占子久出归期(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 1 3 0 3\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 7 9 6 9\n\n")
        self.assertIn("本卦：䷱ 火风鼎", 钱卦)
        self.assertIn("动爻：初爻、四爻、五爻、上爻", 钱卦)
        self.assertIn("变卦：䷄ 水天需", 钱卦)
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

    # 《卜筮正宗》卷十四十八问答第十七问，光绪十五年重刻本第六册PDF第61页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=61
    def test_寅月癸亥占子嗣(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 0 2 2 0\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 6 8 8 6\n\n")
        self.assertIn("本卦：䷁ 坤为地", 钱卦)
        self.assertIn("动爻：三爻、上爻", 钱卦)
        self.assertIn("变卦：䷳ 艮为山", 钱卦)
        self.assertIn("主卦：䷁ 坤为地", 纳甲)
        self.assertIn("变卦：䷳ 艮为山", 纳甲)
        self.assertIn("上爻 子孙 癸酉 ⚋ ×", 纳甲)
        self.assertIn("→ 官鬼 丙寅", 纳甲)
        self.assertIn("三爻 官鬼 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丙申", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第62页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=62
    def test_酉月戊申占伯父归期(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 3 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 9 8 7\n\n")
        self.assertIn("本卦：䷷ 火山旅", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷳ 艮为山", 钱卦)
        self.assertIn("主卦：䷷ 火山旅", 纳甲)
        self.assertIn("变卦：䷳ 艮为山", 纳甲)
        self.assertIn("四爻 妻财 己酉 ⚊ ○", 纳甲)
        self.assertIn("→ 子孙 丙戌", 纳甲)
        self.assertIn("上爻 兄弟 己巳", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第62页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=62
    def test_申月乙亥占家宅(self):
        钱卦 = 运行("金钱卦.py", "1\n0 1 3 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "6 7 9 8 7 8\n\n")
        self.assertIn("本卦：䷯ 水风井", 钱卦)
        self.assertIn("动爻：初爻、三爻", 钱卦)
        self.assertIn("变卦：䷻ 水泽节", 钱卦)
        self.assertIn("主卦：䷯ 水风井", 纳甲)
        self.assertIn("变卦：䷻ 水泽节", 纳甲)
        self.assertIn("五爻 妻财 戊戌", 纳甲)
        self.assertIn("初爻 妻财 辛丑 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 丁巳", 纳甲)
        self.assertIn("三爻 官鬼 辛酉 ⚊ ○", 纳甲)
        self.assertIn("→ 妻财 丁丑", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第63页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=63
    def test_未月癸亥占流年(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 1 2 2 1\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 7 8 8 7\n\n")
        self.assertIn("本卦：䷳ 艮为山", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷳ 艮为山", 纳甲)
        self.assertIn("变卦：䷳ 艮为山", 纳甲)
        self.assertIn("上爻 官鬼 丙寅", 纳甲)
        self.assertIn("三爻 子孙 丙申", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第63页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=63
    def test_子月乙酉占现任吉凶(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 2 1 2\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 8 7 8\n\n")
        self.assertIn("本卦：䷄ 水天需", 钱卦)
        self.assertIn("动爻：无", 钱卦)
        self.assertIn("变卦：无（静卦）", 钱卦)
        self.assertIn("主卦：䷄ 水天需", 纳甲)
        self.assertIn("变卦：䷄ 水天需", 纳甲)
        self.assertIn("四爻 子孙 戊申", 纳甲)
        self.assertIn("初爻 妻财 甲子", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第64页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=64
    def test_午月辛丑因母病问流年(self):
        钱卦 = 运行("金钱卦.py", "1\n1 2 2 0 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 8 8 6 7 7\n\n")
        self.assertIn("本卦：䷩ 风雷益", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷘ 天雷无妄", 钱卦)
        self.assertIn("主卦：䷩ 风雷益", 纳甲)
        self.assertIn("变卦：䷘ 天雷无妄", 纳甲)
        self.assertIn("四爻 妻财 辛未 ⚋ ×", 纳甲)
        self.assertIn("→ 子孙 壬午", 纳甲)
        self.assertIn("三爻 妻财 庚辰", 纳甲)

    # 《卜筮正宗》卷十四十八问答第十八问，光绪十五年重刻本第六册PDF第64页；爻数、背数依原本变卦换算，缺唯一纪年不排六神 https://commons.wikimedia.org/wiki/File:NCPSSD-70017391_卜筮正宗十四卷_第六册.pdf?page=64
    def test_午月辛酉父为十二岁子占功名(self):
        钱卦 = 运行("金钱卦.py", "1\n2 2 0 1 1 0\n")
        纳甲 = 运行("六爻纳甲.py", "8 8 6 7 7 6\n\n")
        self.assertIn("本卦：䷬ 泽地萃", 钱卦)
        self.assertIn("动爻：三爻、上爻", 钱卦)
        self.assertIn("变卦：䷠ 天山遁", 钱卦)
        self.assertIn("主卦：䷬ 泽地萃", 纳甲)
        self.assertIn("变卦：䷠ 天山遁", 纳甲)
        self.assertIn("上爻 父母 丁未 ⚋ ×", 纳甲)
        self.assertIn("→ 父母 壬戌", 纳甲)
        self.assertIn("三爻 妻财 乙卯 ⚋ ×", 纳甲)
        self.assertIn("→ 兄弟 丙申", 纳甲)

    # 《祛疑说·易占说》只记投钱规则和制器法，未记六次实掷钱数及所得实占卦，反旧法暂无可复现历史案例 https://zh.wikisource.org/zh-hans/祛疑説#易占說

    # 《升庵先生文集》卷七十五“六神”仅论起例，未载实占；万历刻本第7页为戊己共起勾陈、壬起螣蛇，录文己误为巳 https://upload.wikimedia.org/wikipedia/commons/9/98/Harvard_drs_51546102_%E5%8D%87%E8%8F%B4%E5%85%88%E7%94%9F%E6%96%87%E9%9B%86_v.22.pdf#page=7

    # 《太乙金钥匙》本卷成化乙巳年积10155402，仅记纪年，以1485年中代表该岁检验积年，不指占日 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkvlnkx7u
    def test_成化乙巳太乙积年(self):
        输出 = 运行("太乙.py", "1\n1485 07 01\n")
        self.assertIn("岁计：积10155402", 输出)

    # 《太乙金钥匙》本卷临津问道起兵例明称“似如”，卦运、大游、小游等亦不属当前四计输出，不能混作已实现的实占 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkvlnkx7u

    # 《太乙金钥匙》续集嘉靖四十年辛酉岁计，只载占年，以该年九月朔代表，不指实际占日 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8
    def test_嘉靖四十年太乙岁计(self):
        输出 = 运行("太乙.py", "1\n1561 10 19\n")
        self.assertIn("第4纪，庚子元第22局", 输出)
        self.assertIn("太乙：巽9宫", 输出)
        self.assertIn("文昌：阴德（乾），计神：巳，始击：天道（未）", 输出)
        self.assertIn("主算：16，主大将：6宫，主参将：8宫", 输出)
        self.assertIn("客算：30，客大将：3宫，客参将：9宫", 输出)

    # 《太乙金钥匙》续集辛酉岁戊戌月计，未记占日，以该月九月朔为日期输入代表 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8
    def test_嘉靖四十年太乙月计(self):
        输出 = 运行("太乙.py", "2\n1561 10 19 12\n")
        self.assertIn("第6纪，壬子元第47局", 输出)
        self.assertIn("太乙：巽9宫", 输出)
        self.assertIn("文昌：高丛（卯），计神：辰，始击：阳德（丑）", 输出)
        self.assertIn("主算：4，主大将：4宫，主参将：2宫", 输出)
        self.assertIn("客算：8，客大将：8宫，客参将：4宫", 输出)

    # 《太乙金钥匙》续集辛酉十一月二十一丁未日计，对应公历1562-01-06，非岁计、月计同一天 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8
    def test_嘉靖四十年太乙日计(self):
        输出 = 运行("太乙.py", "3\n1\n1562 01 06 12\n")
        self.assertIn("甲子元第44局", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：阳德（丑），计神：未，始击：大武（坤）", 输出)
        self.assertIn("主算：33，主大将：3宫，主参将：9宫", 输出)
        self.assertIn("客算：14，客大将：4宫，客参将：2宫", 输出)

    # 《太乙金钥匙》续集辛酉十二月二十二丁丑日庚戌时计，对应公历1562-02-05戌时 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8
    def test_嘉靖四十年太乙时计(self):
        输出 = 运行("太乙.py", "4\n1562 02 05 20\n")
        self.assertIn("第3纪，戊子元第23局", 输出)
        self.assertIn("太乙：巽9宫", 输出)
        self.assertIn("文昌：阴德（乾），计神：辰，始击：武德（申）", 输出)
        self.assertIn("主算：16，主大将：6宫，主参将：8宫", 输出)
        self.assertIn("客算：23，客大将：3宫，客参将：9宫", 输出)

    # 《太乙金钥匙》续集末另用193万上元；明抄影像52、53亦记23257410周余30及707887076余56，实余330、356，且古日锚点差2，待另本校勘 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8

    # 《太乙金钥匙》岁计未明确换岁时刻，月计仅载天地二正次序；现公历年及大雪换月口径在岁界处尚缺历史例验证 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8

    # 《太乙金镜式经》卷一四库第七叶下确记月法2447，与朔策、小余、日法推数未合，非此录文OCR独误，暂不按此改动日计锚点 https://www.shidianguji.com/zh/book/SK1615/chapter/1l9lir71os7ce

    # 《太乙金镜式经》卷一梁天监三年六月八日积707501061、太乙八宫和德；四库影像第八叶上核字，儒略7月5日即本脚本公历7月7日 https://www.shidianguji.com/zh/book/SK1615/chapter/1l9lir71os7ce https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷01
    def test_梁天监三年太乙日计(self):
        输出 = 运行("太乙.py", "3\n2\n504 07 07\n")
        self.assertIn("庚子元第45局", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：和德（艮）", 输出)

    # 《太乙金镜式经》卷一开元十八年含元殿问答未给占时课盘，十月五日庚申例明称“假”，不作具日实占 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷01

    # 《太乙金镜式经》卷二帝王纪年及卷三阴阳七十二局是立成表，非记录实占，不任取公历日冒充古案 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷02 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷03

    # 《太乙金镜式经》卷三阳39主25、阳50主6，四库扫描111、112页同，按投算起例应35、16；表数与起例异，待另本校勘 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=111

    # 《太乙金镜式经》卷三阴11客36、阴15客29、阴25主21、阴26主31、阴27主39，四库扫描117至119页同；与起例推数不合，非现代OCR独误，不据此替换已核规则 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=117

    # 《太乙金镜式经》卷三阴37客目大威、阴43大武38、阴44太簇31，四库扫描120、121页同；按计神加和德应大武25、大神1、大武38，立成表与起例口径待校 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=120

    # 《太乙金镜式经》卷三阴46客算一、阴70主算三十二，四库扫描121、124页明确如此，电子表误录二、二十二，代码按原起例相符 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=121

    # 《太乙金镜式经》卷四三门、主客、出师等是术式条文及假令，不是具年实占记录 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷04

    # 《太乙金镜式经》卷五基福、大游、小游不属当前四计模块，所载纪年不能以普通岁计充替 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷05

    # 《太乙金镜式经》卷六将兵课式以“假令”设例，未记具体实占年日，不作历史测试 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷06

    # 《太乙金镜式经》卷七景祐元年积10154950，比本脚本金钥匙岁计少1，算内外或上元版本未明，暂不混用 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷07

    # 《太乙金镜式经》卷七十精、阳九百六及卷八分野未实现，卷九、十“假令”课式亦非具年实占，不能混作已支持算法测试 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷07 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷08 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷09 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷10

    # 《六壬断案》元集天时第1案韩太守祈雪原记十一月初四己卯寅将，但该日为戊申丑将；十月初四可复盘，月份待校 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集天时第2案只记十二月戊申日子将申时，未记占年，无法唯一换算公历日期 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集宅墓第1案张九翁占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_张九翁占宅(self):
        输出 = 运行("大六壬.py", "1128 10 11 13\n1\n1\n")
        self.assertIn("庚寅日，天罡辰将加未时", 输出)
        self.assertIn("初传：巳 勾陈 官鬼", 输出)
        self.assertIn("中传：寅 螣蛇 妻财", 输出)
        self.assertIn("末传：亥 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第2案叶助教占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_叶助教占宅(self):
        输出 = 运行("大六壬.py", "1128 02 15 13\n1\n1\n")
        self.assertIn("辛卯日，神后子将加未时", 输出)
        self.assertIn("初传：卯 玄武 妻财", 输出)
        self.assertIn("中传：申 朱雀 兄弟", 输出)
        self.assertIn("末传：丑 白虎 父母", 输出)

    # 《六壬断案》元集宅墓第3案邵三翁占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_邵三翁占宅(self):
        输出 = 运行("大六壬.py", "1128 10 02 21\n1\n1\n")
        self.assertIn("辛巳日，天罡辰将加亥时", 输出)
        self.assertIn("初传：卯 天后 妻财", 输出)
        self.assertIn("中传：申 天空 兄弟", 输出)
        self.assertIn("末传：丑 螣蛇 父母", 输出)

    # 《六壬断案》元集宅墓第4案邵秀才己酉乙巳日不在戌将期，历日待校；录文先干不重位取辰卯寅，现可选重复课法2保留该取法 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集宅墓第5案邵巡检占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_邵巡检占宅(self):
        输出 = 运行("大六壬.py", "1128 08 02 03\n1\n1\n")
        self.assertIn("庚辰日，胜光午将加寅时", 输出)
        self.assertIn("初传：辰 玄武 父母", 输出)
        self.assertIn("中传：申 螣蛇 兄弟", 输出)
        self.assertIn("末传：子 青龙 子孙", 输出)

    # 《六壬断案》元集宅墓第6案任三翁占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_任三翁占宅(self):
        输出 = 运行("大六壬.py", "1128 12 22 15\n1\n1\n")
        self.assertIn("壬寅日，大吉丑将加申时", 输出)
        self.assertIn("初传：子 白虎 兄弟", 输出)
        self.assertIn("中传：巳 贵人 妻财", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)

    # 《六壬断案》元集宅墓第7案邵伯达占宅基 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_邵伯达占宅基(self):
        输出 = 运行("大六壬.py", "1129 12 05 17\n1\n1\n")
        self.assertIn("庚寅日，功曹寅将加酉时", 输出)
        self.assertIn("初传：子 青龙 子孙", 输出)
        self.assertIn("中传：巳 太阴 官鬼", 输出)
        self.assertIn("末传：戌 六合 父母", 输出)

    # 《六壬断案》元集宅墓第8案童保仪，据孟子翔引录本第93页的六月初四丁巳；另本作初七，与纪日不合 https://files.yijingyixue.com/documents/MZX020_4eef2264aa.pdf#page=93 https://tianyugong.com/liurenduanan/
    def test_童保仪占宅(self):
        输出 = 运行("大六壬.py", "1128 07 10 17\n1\n1\n")
        self.assertIn("丁巳日，小吉未将加酉时", 输出)
        self.assertIn("初传：丑 勾陈 子孙", 输出)
        self.assertIn("中传：亥 朱雀 官鬼", 输出)
        self.assertIn("末传：酉 贵人 妻财", 输出)

    # 《六壬断案》元集宅墓第9案郑宣义未直记占年，1128年可由后续年份反推但仍属推测，暂不固定公历输入 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集宅墓第10案王德卿占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_王德卿占宅(self):
        输出 = 运行("大六壬.py", "1128 11 02 05\n1\n1\n")
        self.assertIn("壬子日，太冲卯将加卯时", 输出)
        self.assertIn("初传：亥 天空 兄弟", 输出)
        self.assertIn("中传：子 青龙 兄弟", 输出)
        self.assertIn("末传：卯 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第11案童得松占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_童得松占宅(self):
        输出 = 运行("大六壬.py", "1129 07 10 01\n1\n1\n")
        self.assertIn("壬戌日，小吉未将加丑时", 输出)
        self.assertIn("初传：巳 太阴 妻财", 输出)
        self.assertIn("中传：亥 勾陈 兄弟", 输出)
        self.assertIn("末传：巳 太阴 妻财", 输出)

    # 《六壬断案》元集宅墓第12案徐八公据夜贵版和“卯子息爻乘夜贵”断语核对；另本天将作昼贵，儒略历七月九日为本脚本公历七月十六日 https://shuyuan.zhiming.life/read/大六壬断案(亨集)/9 https://tianyugong.com/liurenduanan/
    def test_徐八公占宅(self):
        for 昼夜法 in ("1", "3"):
            输出 = 运行("大六壬.py", f"1128 07 16 17\n1\n{昼夜法}\n")
            self.assertIn("癸亥日，小吉未将加酉时，夜贵卯", 输出)
            self.assertIn("初传：未 太常 官鬼", 输出)
            self.assertIn("中传：巳 太阴 妻财", 输出)
            self.assertIn("末传：卯 贵人 子孙", 输出)
        输出 = 运行("大六壬.py", "1128 07 16 17\n1\n2\n")
        self.assertIn("癸亥日，小吉未将加酉时", 输出)
        self.assertIn("昼贵巳", 输出)
        self.assertIn("初传：未 太阴 官鬼", 输出)
        self.assertIn("中传：巳 贵人 妻财", 输出)
        self.assertIn("末传：卯 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第13案刘将仕，所引页误重第14案课图，依卷一异本辰申子三传核对 https://tianyugong.com/liurenduanan/ https://libokang.com/guji/liuren/六壬断案/
    def test_刘将仕占宅(self):
        输出 = 运行("大六壬.py", "1129 06 26 05\n1\n1\n")
        self.assertIn("戊申日，小吉未将加卯时", 输出)
        self.assertIn("初传：辰 玄武 兄弟", 输出)
        self.assertIn("中传：申 青龙 子孙", 输出)
        self.assertIn("末传：子 螣蛇 妻财", 输出)

    # 《六壬断案》元集宅墓第14案何丞务，己酉年戊子日戌将唯一对应1129-04-07，可复盘但农历和通常节月均未解释原记“二月”，仅存待校例 https://shuyuan.zhiming.life/read/大六壬断案(亨集)/10
    # def test_何丞务占宅(self):
    #     输出 = 运行("大六壬.py", "1129 04 07 09\n1\n1\n")
    #     self.assertIn("戊子日，河魁戌将加巳时", 输出)
    #     self.assertIn("初传：巳 太常 父母", 输出)
    #     self.assertIn("中传：戌 六合 兄弟", 输出)
    #     self.assertIn("末传：卯 太阴 官鬼", 输出)

    # 《六壬断案》元集宅墓第15案任太公占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_任太公占宅(self):
        输出 = 运行("大六壬.py", "1128 02 10 07\n1\n1\n")
        self.assertIn("丙戌日，神后子将加辰时", 输出)
        self.assertIn("初传：酉 太阴 妻财", 输出)
        self.assertIn("中传：巳 天空 兄弟", 输出)
        self.assertIn("末传：丑 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第16案王解元占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_王解元占宅(self):
        输出 = 运行("大六壬.py", "1129 04 12 13\n1\n1\n")
        self.assertIn("癸巳日，河魁戌将加未时", 输出)
        self.assertIn("初传：申 六合 父母", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：寅 玄武 子孙", 输出)

    # 《六壬断案》元集宅墓第17案何宣义占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_何宣义占宅(self):
        输出 = 运行("大六壬.py", "1129 04 12 17\n1\n1\n")
        self.assertIn("癸巳日，河魁戌将加酉时", 输出)
        self.assertIn("初传：未 勾陈 官鬼", 输出)
        self.assertIn("中传：申 青龙 父母", 输出)
        self.assertIn("末传：酉 天空 父母", 输出)

    # 《六壬断案》元集宅墓第18案林丞务，辰时尚未交立秋，仍为六月节月；末传据六合本，另录作勾陈 https://shuyuan.zhiming.life/read/大六壬断案(亨集)/10 https://tianyugong.com/liurenduanan/
    def test_林丞务占宅(self):
        输出 = 运行("大六壬.py", "1129 08 08 07\n1\n1\n")
        self.assertIn("辛卯日，胜光午将加辰时", 输出)
        self.assertIn("初传：巳 天后 官鬼", 输出)
        self.assertIn("中传：未 螣蛇 父母", 输出)
        self.assertIn("末传：酉 六合 兄弟", 输出)

    # 《六壬断案》元集宅墓第19案冯修职占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_冯修职占宅(self):
        输出 = 运行("大六壬.py", "1128 06 08 05\n1\n1\n")
        self.assertIn("乙酉日，传送申将加卯时", 输出)
        self.assertIn("初传：未 青龙 妻财", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：巳 白虎 子孙", 输出)

    # 《六壬断案》元集宅墓第20案叶油饼店主占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_叶油饼店主占宅(self):
        输出 = 运行("大六壬.py", "1128 07 21 17\n1\n1\n")
        self.assertIn("戊辰日，小吉未将加酉时", 输出)
        self.assertIn("初传：丑 天空 兄弟", 输出)
        self.assertIn("中传：亥 太常 妻财", 输出)
        self.assertIn("末传：酉 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第21案童秀才，所引页未记占时，可由戌将和乙上丑唯一反推丑时；另录已有丑时，仍依要求仅存注释例 https://tianyugong.com/liurenduanan/ https://gushu.net.cn/guji/易藏/术数/六壬断案-3.html
    # def test_童秀才占宅(self):
    #     输出 = 运行("大六壬.py", "1128 04 19 02\n1\n1\n")
    #     self.assertIn("乙未日，河魁戌将加丑时", 输出)
    #     self.assertIn("初传：丑 青龙 妻财", 输出)
    #     self.assertIn("中传：戌 朱雀 妻财", 输出)
    #     self.assertIn("末传：未 天后 妻财", 输出)

    # 《六壬断案》元集宅墓第22案何七秀才占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_何七秀才占宅(self):
        输出 = 运行("大六壬.py", "1128 03 19 11\n1\n1\n")
        self.assertIn("甲子日，登明亥将加午时", 输出)
        self.assertIn("初传：子 螣蛇 父母", 输出)
        self.assertIn("中传：巳 太常 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》元集宅墓第23案某占家宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_某占家宅(self):
        输出 = 运行("大六壬.py", "1128 10 05 21\n1\n1\n")
        self.assertIn("甲申日，天罡辰将加亥时", 输出)
        self.assertIn("初传：子 青龙 父母", 输出)
        self.assertIn("中传：巳 太阴 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》元集宅墓第24案郁氏女，完整录文为申将戌时，简录作申时；丙辰年五月初八与丁亥纪日仍不合，暂不能定公历输入 https://gushu.net.cn/guji/易藏/术数/六壬断案-3.html https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集宅墓第25案邵三公占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_邵三公占宅(self):
        输出 = 运行("大六壬.py", "1129 01 31 00\n1\n1\n")
        self.assertIn("壬午日，神后子将加子时", 输出)
        self.assertIn("初传：亥 太常 兄弟", 输出)
        self.assertIn("中传：午 六合 妻财", 输出)
        self.assertIn("末传：子 玄武 兄弟", 输出)

    # 《六壬断案》元集宅墓第26案江文老只记七月十五丁酉日，未载占年，无法唯一定位公历日期 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集宅墓第27案徐大夫占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1128
    def test_徐大夫占宅(self):
        输出 = 运行("大六壬.py", "1128 02 10 13\n1\n1\n")
        self.assertIn("丙戌日，神后子将加未时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：丑 太阴 子孙", 输出)
        self.assertIn("末传：午 青龙 兄弟", 输出)

    # 《六壬断案》元集宅墓第28案郭德占家宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_郭德占家宅(self):
        输出 = 运行("大六壬.py", "1129 07 02 11\n1\n1\n")
        self.assertIn("甲寅日，小吉未将加午时", 输出)
        self.assertIn("初传：辰 六合 妻财", 输出)
        self.assertIn("中传：巳 勾陈 子孙", 输出)
        self.assertIn("末传：午 青龙 子孙", 输出)

    # 《六壬断案》元集宅墓第29案叶助教占家宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_叶助教占家宅(self):
        输出 = 运行("大六壬.py", "1129 03 03 11\n1\n1\n")
        self.assertIn("癸丑日，登明亥将加午时", 输出)
        self.assertIn("初传：午 螣蛇 妻财", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：辰 天后 官鬼", 输出)

    # 《六壬断案》元集宅墓第30案童三十四公占宅 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_童三十四公占宅(self):
        输出 = 运行("大六壬.py", "1129 08 25 05\n1\n1\n")
        self.assertIn("戊申日，太乙巳将加卯时", 输出)
        self.assertIn("初传：子 天后 妻财", 输出)
        self.assertIn("中传：寅 螣蛇 官鬼", 输出)
        self.assertIn("末传：辰 六合 兄弟", 输出)

    # 《六壬断案》元集汪四六公案，所引页误作壬辰，依课图午支及异本壬午日核对 https://tianyugong.com/liurenduanan/ https://shuyuan.zhiming.life/read/大六壬断案(亨集)/12
    def test_汪四六公占宅(self):
        输出 = 运行("大六壬.py", "1129 09 28 15\n1\n1\n")
        self.assertIn("壬午日，天罡辰将加申时", 输出)
        self.assertIn("初传：戌 白虎 官鬼", 输出)
        self.assertIn("中传：午 天后 妻财", 输出)
        self.assertIn("末传：寅 六合 子孙", 输出)

    # 《六壬断案》元集伊伯廷案写己酉年丙午日卯将，但1129年丙午日均不在卯将期间；1128年有同盘，年号待校 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集某占家宅仅记正月丁卯日，未记占年，不能唯一换算公历日期 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集“时生己酉年四十三岁二月朔占”未明记占年和占日干支，无法唯一定位 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集某占宅仅记癸酉日巳将申时，未记占年，不能唯一换算公历日期 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集另一某占家宅仅记正月己巳日午将酉时，未记占年，不能唯一换算公历日期 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集郑三公案己酉年正月二十三壬寅日应在雨水后用亥将，原文却作子将，待校 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集徐承务案原记己酉九月癸卯辰将；可复盘日期属闰八月，且卯时天将起例不合，待校 https://tianyugong.com/liurenduanan/

    # 《六壬断案》元集刘秘教占宅，六月初一戊申日与第13案同日，课图可独立复盘 https://tianyugong.com/liurenduanan/ https://hhl.cnkgraph.com/Calendar/1129
    def test_刘秘教占宅(self):
        输出 = 运行("大六壬.py", "1129 06 26 17\n1\n1\n")
        self.assertIn("戊申日，小吉未将加酉时", 输出)
        self.assertIn("初传：丑 天空 兄弟", 输出)
        self.assertIn("中传：亥 太常 妻财", 输出)
        self.assertIn("末传：酉 太阴 子孙", 输出)

    # 《六壬断案》元集郭仲起案写己酉年六月甲寅日寅将，但该月甲寅日应未将，年或月将待校 https://tianyugong.com/liurenduanan/

    # 《景祐六壬神定经》起贵条文未记具年实占；王仁俊《神定经纂》稿本第23页录乙己，另电子本乙巳与日干不合，未据摘抄本判定原十卷录入层次 https://upload.wikimedia.org/wikipedia/commons/a/ad/NLC892-411999030028-142313_%E6%AD%A3%E5%AD%B8%E5%A0%82%E9%9B%9C%E8%91%97_%E7%AC%AC18%E5%86%8A.pdf#page=23

    # 《六壬大全》涉害篇以“如”举缺占年的起例，不能任补公历年作实占测试 https://www.shidianguji.com/zh/book/SK1599/chapter/1m1g2evjvmoez

    # 《六壬大全》卷五元首范蠡占郑妃生产，缺占年且有四月丁丑、辛巳异文，不能唯一还原日期 https://zh.wikisource.org/wiki/六壬大全_(四庫全書本)/卷05

    # 《六壬大全》卷五重审李司马占，只记乙亥日辰时酉将，未记占年，不能唯一还原日期 https://zh.wikisource.org/wiki/六壬大全_(四庫全書本)/卷05

    # 《御定六壬直指》卷上起例及七百二十立式不是实占，所引指南等占验须回原案核对；贵表及昼夜界已核故宫本第8页 https://upload.wikimedia.org/wikipedia/commons/d/dd/GGZBCK417_%E5%BE%A1%E5%AE%9A%E5%85%AD%E5%A3%AC%E7%9B%B4%E6%8C%87.pdf#page=8

    # 《御定六壬直指》辛卯第一课明确卯子午，并注毕法用卯子卯；这是伏吟互刑异法，非录入错误，具年傅姓案另见指南 https://upload.wikimedia.org/wikipedia/commons/d/dd/GGZBCK417_%E5%BE%A1%E5%AE%9A%E5%85%AD%E5%A3%AC%E7%9B%B4%E6%8C%87.pdf#page=227

    # 《六壬指南》迟父师祈雨，1925年国图扫描第127页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=127
    def test_迟父师祈雨(self):
        输出 = 运行("大六壬.py", "1638 04 19 01\n1\n1\n")
        self.assertIn("己巳日，河魁戌将加丑时", 输出)
        self.assertIn("初传：寅 天空 官鬼", 输出)
        self.assertIn("中传：亥 六合 妻财", 输出)
        self.assertIn("末传：申 贵人 子孙", 输出)

    # 《六壬指南》曾刑长垣雪后问雪，1925年国图扫描第128页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=128
    def test_曾刑长垣雪后问雪(self):
        输出 = 运行("大六壬.py", "1638 01 17 05\n1\n1\n")
        self.assertIn("丁酉日，大吉丑将加卯时", 输出)
        self.assertIn("初传：丑 朱雀 子孙", 输出)
        self.assertIn("中传：巳 天空 兄弟", 输出)
        self.assertIn("末传：巳 天空 兄弟", 输出)

    # 《六壬指南》施指挥守岁问雪，1925年国图扫描第128页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=128
    def test_施指挥守岁问雪(self):
        输出 = 运行("大六壬.py", "1645 01 27 17\n1\n1\n")
        self.assertIn("甲申日，神后子将加酉时", 输出)
        self.assertIn("初传：申 螣蛇 官鬼", 输出)
        self.assertIn("中传：亥 勾陈 父母", 输出)
        self.assertIn("末传：寅 白虎 兄弟", 输出)

    # 《六壬指南》庚寅五月问雨，1925年国图扫描第129页；原刻五月，现代录文误作正月 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=129
    def test_庚寅五月问雨(self):
        输出 = 运行("大六壬.py", "1650 06 20 13\n1\n1\n")
        self.assertIn("甲戌日，传送申将加未时", 输出)
        self.assertIn("初传：辰 六合 妻财", 输出)
        self.assertIn("中传：巳 勾陈 子孙", 输出)
        self.assertIn("末传：午 青龙 子孙", 输出)

    # 《六壬指南》庚寅闻鸠鸣，1925年国图扫描第130页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=130
    def test_庚寅闻鸠鸣(self):
        输出 = 运行("大六壬.py", "1650 05 31 05\n1\n1\n")
        self.assertIn("甲寅日，传送申将加卯时", 输出)
        self.assertIn("初传：子 螣蛇 父母", 输出)
        self.assertIn("中传：巳 太常 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬指南》甲申日晕，1925年国图扫描第130页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=130
    def test_甲申日晕(self):
        输出 = 运行("大六壬.py", "1644 06 06 11\n1\n1\n")
        self.assertIn("己丑日，传送申将加午时", 输出)
        self.assertIn("初传：卯 玄武 官鬼", 输出)
        self.assertIn("中传：巳 白虎 父母", 输出)
        self.assertIn("末传：未 青龙 兄弟", 输出)

    # 《六壬指南》刘二兄占风水，1925年国图扫描第131页；原刻寅时用昼贵；该年乙酉未将唯一，属芒种至小暑的五月节月 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=131
    def test_刘二兄占风水(self):
        输出 = 运行("大六壬.py", "1650 07 01 03\n1\n2\n")
        self.assertIn("乙酉日，小吉未将加寅时", 输出)
        self.assertIn("初传：未 青龙 妻财", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：巳 白虎 子孙", 输出)

    # 《六壬指南》李庚续弦，1925年国图扫描第133页；原刻己丑五月癸酉酉时、课图申将；1649年该月癸酉为6月24日，酉时两小时均已交夏至用未将，纪月或月将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=133

    # 《六壬指南》东宫田妃六甲，1925年国图扫描第133页；原刻丁丑十月癸丑酉时，图作返吟卯将；1637年该月癸丑为12月4日，酉时均为寅将，课图与历日口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=133

    # 《六壬指南》江右傅姓六甲，1925年国图扫描第134页；原刻庚辰三月辛卯戌时、伏吟戌将；1640年该月辛卯为4月30日，戌时均为酉将，课图与历日口径待校，原图三传卯子卯为循环刑法，可选伏吟法2，历日仍待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=134

    # 《六壬指南》冯尔忠占六甲，1925年国图扫描第135页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=135
    def test_冯尔忠占六甲(self):
        输出 = 运行("大六壬.py", "1637 05 10 18\n1\n1\n")
        self.assertIn("乙酉日，从魁酉将加酉时", 输出)
        self.assertIn("初传：辰 勾陈 妻财", 输出)
        self.assertIn("中传：酉 天后 官鬼", 输出)
        self.assertIn("末传：卯 青龙 兄弟", 输出)

    # 《六壬指南》孙石渠代占生育，1925年国图扫描第135页；课图在第136页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=135
    def test_孙石渠代占生育(self):
        输出 = 运行("大六壬.py", "1649 03 24 22\n1\n1\n")
        self.assertIn("辛丑日，河魁戌将加亥时", 输出)
        self.assertIn("初传：子 太阴 子孙", 输出)
        self.assertIn("中传：亥 玄武 子孙", 输出)
        self.assertIn("末传：戌 太常 父母", 输出)

    # 《六壬指南》戴羲宇占来意，1925年国图扫描第136页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=136
    def test_戴羲宇占来意(self):
        输出 = 运行("大六壬.py", "1624 06 05 11\n1\n1\n")
        self.assertIn("癸卯日，传送申将加午时", 输出)
        self.assertIn("初传：未 朱雀 官鬼", 输出)
        self.assertIn("中传：酉 勾陈 父母", 输出)
        self.assertIn("末传：亥 天空 兄弟", 输出)

    # 《六壬指南》但陵景占府院试，1925年国图扫描第137页；原刻寅时用昼贵；该年甲申巳将唯一，属立秋至白露的七月节月 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=137
    def test_但陵景占府院试(self):
        输出 = 运行("大六壬.py", "1650 08 29 03\n1\n2\n")
        self.assertIn("甲申日，太乙巳将加寅时", 输出)
        self.assertIn("初传：申 青龙 官鬼", 输出)
        self.assertIn("中传：亥 朱雀 父母", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)

    # 《六壬指南》陆夺翼占考试，1925年国图扫描第138页；原刻壬午，现代录误作壬子；原图丑时用昼贵 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=138
    def test_陆夺翼占考试(self):
        输出 = 运行("大六壬.py", "1642 06 14 02\n1\n2\n")
        self.assertIn("丙戌日，传送申将加丑时", 输出)
        self.assertIn("初传：子 螣蛇 官鬼", 输出)
        self.assertIn("中传：未 太常 子孙", 输出)
        self.assertIn("末传：寅 六合 父母", 输出)

    # 《六壬指南》宗开先占乡试，1925年国图扫描第139页；原刻寅时用昼贵、涉害先取孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=139
    def test_宗开先占乡试(self):
        输出 = 运行("大六壬.py", "1633 08 05 03\n1\n2\n2\n")
        self.assertIn("辛卯日，胜光午将加寅时", 输出)
        self.assertIn("初传：未 螣蛇 父母", 输出)
        self.assertIn("中传：亥 青龙 子孙", 输出)
        self.assertIn("末传：卯 玄武 妻财", 输出)

    # 《六壬指南》孙兴功辰时占乡试，1925年国图扫描第140页；原刻辰时图用夜贵，现代编辑改昼贵后天将不同 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=140
    def test_孙兴功辰时占乡试(self):
        输出 = 运行("大六壬.py", "1648 10 10 08\n1\n3\n")
        self.assertIn("丙辰日，天罡辰将加辰时", 输出)
        self.assertIn("初传：巳 勾陈 兄弟", 输出)
        self.assertIn("中传：申 螣蛇 妻财", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)

    # 《六壬指南》孙兴功酉时占乡试，1925年国图扫描第140页；原刻同日辰将加酉、四课偏移七位，却写三传子未寅；依四课下贼比用为午丑申，原断初太岁空战亦指子，不能把两套课式当同一实占 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=140

    # 《六壬指南》何伴鹤代占兄弟乡试，1925年国图扫描第140页；原刻丁卯八月乙巳申时，课图反推辰将；1627年该月乙巳为9月20日，申时均尚为巳将，纪月或月将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=140

    # 《六壬指南》张盛美门生会试，1925年国图扫描第141页；原刻丁丑正月己巳巳时并明写子将；1637年该月己巳为2月23日，巳时均已交雨水用亥将，纪日或月将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=141

    # 《六壬指南》王继廉代占会试，1925年国图扫描第142页；原刻甲戌二月戊辰辰时、返吟戌将；1634年该月戊辰为3月10日，辰时均尚为亥将，纪日或月将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=142

    # 《六壬指南》宫子玄占会试，1925年国图扫描第142页；课图在第143页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=142
    def test_宫子玄占会试(self):
        输出 = 运行("大六壬.py", "1643 03 20 06\n1\n1\n")
        self.assertIn("乙丑日，登明亥将加卯时", 输出)
        self.assertIn("初传：巳 青龙 子孙", 输出)
        self.assertIn("中传：丑 螣蛇 妻财", 输出)
        self.assertIn("末传：酉 玄武 官鬼", 输出)

    # 《六壬指南》孙大宜占会试，1925年国图扫描第143页；原刻丁丑二月癸未午时，课图反推戌将；1637年该月癸未为3月9日，午时均尚为亥将，纪日或月将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=143

    # 《六壬指南》陈公明占会试，1925年国图扫描第144页；原刻戊辰八月甲戌亥时，课图反推未将；1628年八月无甲戌，且该年甲戌均不在未将交接范围，纪月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=144

    # 《六壬指南》刘若宜占会试，1925年国图扫描第144页；原刻丁丑二月乙未戌时，课图反推亥将；1637年该月乙未为3月21日，戌时均已交春分用戌将，尚不能据图改日，气法口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=144

    # 《六壬指南》吴克孝占会试，1925年国图扫描第145页；原刻同为丁丑二月乙未巳时、返吟亥将；1637年3月21日巳时均已交春分用戌将，气法口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=145

    # 《六壬指南》王旋官代占升迁，1925年国图扫描第146页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=146
    def test_王旋官代占升迁(self):
        输出 = 运行("大六壬.py", "1631 04 11 14\n1\n1\n")
        self.assertIn("甲申日，河魁戌将加未时", 输出)
        self.assertIn("初传：申 青龙 官鬼", 输出)
        self.assertIn("中传：亥 朱雀 父母", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)

    # 《六壬指南》蔡熙阳占杨司马罢官，1925年国图扫描第147页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=147
    def test_蔡熙阳占杨司马罢官(self):
        输出 = 运行("大六壬.py", "1637 08 21 09\n1\n1\n")
        self.assertIn("戊辰日，胜光午将加巳时", 输出)
        self.assertIn("初传：寅 螣蛇 官鬼", 输出)
        self.assertIn("中传：午 青龙 父母", 输出)
        self.assertIn("末传：午 青龙 父母", 输出)

    # 《六壬指南》汪仙民邵无奇占马康庄入相，1925年国图扫描第147页；原刻戊辰十二月庚寅辰时、图反推寅将；1628年该月庚寅为12月28日，辰时均为丑将，日将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=147

    # 《六壬指南》杨方壶占仕途，1925年国图扫描第148页；原刻丁卯，现代录误作丁丑 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=148
    def test_杨方壶占仕途(self):
        输出 = 运行("大六壬.py", "1627 12 08 09\n1\n1\n")
        self.assertIn("甲子日，功曹寅将加巳时", 输出)
        self.assertIn("初传：午 青龙 子孙", 输出)
        self.assertIn("中传：卯 朱雀 兄弟", 输出)
        self.assertIn("末传：子 天后 父母", 输出)

    # 《六壬指南》迟王入觐代占王射斗，1925年国图扫描第149页；原纪庚午十二月，公历已为1631年 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=149
    def test_迟王入觐代占王射斗(self):
        输出 = 运行("大六壬.py", "1631 01 04 19\n1\n1\n")
        self.assertIn("丁未日，大吉丑将加戌时", 输出)
        self.assertIn("初传：亥 太阴 官鬼", 输出)
        self.assertIn("中传：戌 天后 子孙", 输出)
        self.assertIn("末传：戌 天后 子孙", 输出)

    # 《六壬指南》阮实夫代占温首揆，1925年国图扫描第150页；原刻丁丑四月丙申酉时伏吟；1637年该月丙申为5月21日，酉时均已交小满用申将，不能复现酉将伏吟，气法口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=150

    # 《六壬指南》陆金吾占陈东明出师，1925年国图扫描第150页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=150
    def test_陆金吾占陈东明出师(self):
        输出 = 运行("大六壬.py", "1636 03 12 05\n1\n1\n")
        self.assertIn("辛巳日，登明亥将加卯时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：寅 勾陈 妻财", 输出)
        self.assertIn("末传：戌 太常 父母", 输出)

    # 《六壬指南》阮胤平占入相，1925年国图扫描第151页；原刻丁丑八月己未辰时、图反推巳将；1637年该月己未为10月11日，辰时均为辰将，年日将不能兼合，口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=151

    # 《六壬指南》仇庸足占功名，1925年国图扫描第152页；原刻辛未四月己未辰时、图反推申将；1631年5月16日辰时均为酉将，与同书宋太斗同日同辰时的酉将课亦不同，课图或纪日待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=152

    # 《六壬指南》陈龙正占钱士升入相，1925年国图扫描第153页；原刻癸酉七月甲寅申时、图反推午将；1633年8月28日申时均已交处暑用巳将，气法或纪日口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=153

    # 《六壬指南》贺中怜代占周首揆，1925年国图扫描第153页；原图返吟涉害取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=153
    def test_贺中怜代占周首揆(self):
        输出 = 运行("大六壬.py", "1633 03 11 09\n1\n1\n2\n")
        self.assertIn("甲子日，登明亥将加巳时", 输出)
        self.assertIn("初传：寅 天后 兄弟", 输出)
        self.assertIn("中传：申 青龙 官鬼", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)

    # 《六壬指南》孙兴功占赵福星升迁，1925年国图扫描第154页；原刻戊子四月丙子辰时、返吟戌将；1648年5月3日辰时均为酉将，年日将不能兼合，口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=154

    # 《六壬指南》阮胤平占李括苍入相，1925年国图扫描第155页；原刻丁丑七月甲戌巳时、图反推午将；1637年8月27日巳时均为巳将，气法或纪日口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=155

    # 《六壬指南》阮胤平占袁郑枚卜，1925年国图扫描第156页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=156
    def test_阮胤平占袁郑枚卜(self):
        输出 = 运行("大六壬.py", "1637 09 18 09\n1\n1\n")
        self.assertIn("丙申日，太乙巳将加巳时", 输出)
        self.assertIn("初传：巳 天空 兄弟", 输出)
        self.assertIn("中传：申 玄武 妻财", 输出)
        self.assertIn("末传：寅 六合 父母", 输出)

    # 《六壬指南》陈公明占黄虎山功名，1925年国图扫描第156页；原刻甲申十月；依年日时及课图卯将唯一反推1644年10月26日，农历与节月均为九月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=156
    # def test_陈公明占黄虎山功名(self):
    #     输出 = 运行("大六壬.py", "1644 10 26 21\n1\n1\n")
    #     self.assertIn("辛亥日，太冲卯将加亥时", 输出)
    #     self.assertIn("初传：未 白虎 父母", 输出)
    #     self.assertIn("中传：亥 六合 子孙", 输出)
    #     self.assertIn("末传：卯 天后 妻财", 输出)

    # 《六壬指南》刘一纯占梁司马冢宰，1925年国图扫描第157页；原刻辛未四月丁酉卯时、图反推戌将；1631年该年丁酉均无相合戌将，纪月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=157

    # 《六壬指南》王昌时占仕途，1925年国图扫描第158页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=158
    def test_王昌时占仕途(self):
        输出 = 运行("大六壬.py", "1638 04 16 05\n1\n1\n")
        self.assertIn("丙寅日，河魁戌将加卯时", 输出)
        self.assertIn("初传：子 螣蛇 官鬼", 输出)
        self.assertIn("中传：未 太常 子孙", 输出)
        self.assertIn("末传：寅 六合 父母", 输出)

    # 《六壬指南》丙午命人随僧索占，1925年国图扫描第159页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=159
    def test_丙午命人随僧索占(self):
        输出 = 运行("大六壬.py", "1642 10 13 13\n1\n1\n")
        self.assertIn("丁亥日，天罡辰将加未时", 输出)
        self.assertIn("初传：巳 天空 兄弟", 输出)
        self.assertIn("中传：寅 六合 父母", 输出)
        self.assertIn("末传：亥 贵人 官鬼", 输出)

    # 《六壬指南》熊潭石聘陈公献，1925年国图扫描第159页；原纪壬午十二月，公历已为1643年 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=159
    def test_熊潭石聘陈公献(self):
        输出 = 运行("大六壬.py", "1643 02 17 13\n1\n1\n")
        self.assertIn("甲午日，神后子将加未时", 输出)
        self.assertIn("初传：子 螣蛇 父母", 输出)
        self.assertIn("中传：巳 太常 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬指南》刘正宗座间索占，1925年国图扫描第160页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=160
    def test_刘正宗座间索占(self):
        输出 = 运行("大六壬.py", "1638 03 22 09\n1\n1\n")
        self.assertIn("辛丑日，河魁戌将加巳时", 输出)
        self.assertIn("初传：卯 玄武 妻财", 输出)
        self.assertIn("中传：申 朱雀 兄弟", 输出)
        self.assertIn("末传：丑 白虎 父母", 输出)

    # 《六壬指南》贺中怜占升迁，1925年国图扫描第161页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=161
    def test_贺中怜占升迁(self):
        输出 = 运行("大六壬.py", "1633 09 05 15\n1\n1\n")
        self.assertIn("壬戌日，太乙巳将加申时", 输出)
        self.assertIn("初传：巳 贵人 妻财", 输出)
        self.assertIn("中传：寅 六合 子孙", 输出)
        self.assertIn("末传：亥 天空 兄弟", 输出)

    # 《六壬指南》司化南占何官，1925年国图扫描第162页；原刻戊子六月乙未未时、图反推亥将；1648年7月21日未时为未将，该年其它乙未未时亦不合亥将，年月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=162

    # 《六壬指南》涂松亭占彭南溟升迁，1925年国图扫描第162页；原刻丁卯正月；依年日时及课图子将唯一反推1628年1月30日，属丁卯十二月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=162
    # def test_涂松亭占彭南溟升迁(self):
    #     输出 = 运行("大六壬.py", "1628 01 30 05\n1\n1\n")
    #     self.assertIn("丁巳日，神后子将加卯时", 输出)
    #     self.assertIn("初传：亥 贵人 官鬼", 输出)
    #     self.assertIn("中传：申 玄武 妻财", 输出)
    #     self.assertIn("末传：巳 天空 兄弟", 输出)

    # 《六壬指南》潘云从占郑潜奄升迁，1925年国图扫描第163页；原刻庚辰正月丁丑卯时，四课反推亥将而三传写寅卯辰；按四课下贼应巳丑酉，与原题从革相合，原图内部亦待校，不能据别盘替换 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=163

    # 《六壬指南》程孝延程翔云占引部来否，1925年国图扫描第164页；原图涉害先取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=164
    def test_程孝延程翔云占引部来否(self):
        输出 = 运行("大六壬.py", "1650 03 21 00\n1\n1\n2\n")
        self.assertIn("癸卯日，河魁戌将加子时", 输出)
        self.assertIn("初传：丑 朱雀 官鬼", 输出)
        self.assertIn("中传：亥 勾陈 兄弟", 输出)
        self.assertIn("末传：酉 天空 父母", 输出)

    # 《六壬指南》宋太斗在仇宅占功名，1925年国图扫描第165页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=165
    def test_宋太斗在仇宅占功名(self):
        输出 = 运行("大六壬.py", "1631 05 16 07\n1\n1\n")
        self.assertIn("己未日，从魁酉将加辰时", 输出)
        self.assertIn("初传：巳 白虎 父母", 输出)
        self.assertIn("中传：戌 朱雀 兄弟", 输出)
        self.assertIn("末传：卯 玄武 官鬼", 输出)

    # 《六壬指南》孙兴功仕扬占功名，1925年国图扫描第165页；原刻辛巳十月己未酉时、图反推寅将；1641年11月19日酉时均尚为卯将；原图末传卯乘太阴亦与贵人序不合，气法及天将待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=165

    # 《六壬指南》胡道台令乔中军索占，1925年国图扫描第166页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=166
    def test_胡道台令乔中军索占(self):
        输出 = 运行("大六壬.py", "1648 08 21 21\n1\n1\n")
        self.assertIn("丙寅日，胜光午将加亥时", 输出)
        self.assertIn("初传：子 六合 官鬼", 输出)
        self.assertIn("中传：未 太阴 子孙", 输出)
        self.assertIn("末传：寅 青龙 父母", 输出)

    # 《六壬指南》蔡熙阳推吴淞总戎，1925年国图扫描第167页；原刻戊寅二月丙午戌时、图反推卯将；1638年该月丙午为3月27日，戌时均为戌将，该年亦无兼合卯将的丙午戌时，年月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=167

    # 《六壬指南》阮胤平推皖抚，1925年国图扫描第167页；原刻戌时图用昼贵 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=167
    def test_阮胤平推皖抚(self):
        输出 = 运行("大六壬.py", "1637 08 12 19\n1\n2\n")
        self.assertIn("己未日，胜光午将加戌时", 输出)
        self.assertIn("初传：卯 六合 官鬼", 输出)
        self.assertIn("中传：亥 天后 妻财", 输出)
        self.assertIn("末传：未 白虎 兄弟", 输出)

    # 《六壬指南》扬州粮厅周公祖索占，1925年国图扫描第168页；农历闰二月而节月三月；原图涉害先取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=168
    def test_扬州粮厅周公祖索占(self):
        输出 = 运行("大六壬.py", "1651 04 15 05\n1\n1\n2\n")
        self.assertIn("癸酉日，河魁戌将加卯时", 输出)
        self.assertIn("初传：卯 朱雀 子孙", 输出)
        self.assertIn("中传：戌 白虎 官鬼", 输出)
        self.assertIn("末传：巳 贵人 妻财", 输出)

    # 《六壬指南》卞圣瑞书房两客索占，1925年国图扫描第169页；原图涉害先取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=169
    def test_卞圣瑞书房两客索占(self):
        输出 = 运行("大六壬.py", "1643 02 22 13\n1\n1\n2\n")
        self.assertIn("己亥日，登明亥将加未时", 输出)
        self.assertIn("初传：未 青龙 兄弟", 输出)
        self.assertIn("中传：亥 螣蛇 妻财", 输出)
        self.assertIn("末传：卯 玄武 官鬼", 输出)

    # 《六壬指南》方潜夫奉诏进京，1925年国图扫描第170页；原刻壬午十月辛未午时、图反推未将；1642年该年辛未午时均不合未将，纪月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=170

    # 《六壬指南》富平朱酉昆入觐考选，1925年国图扫描第171页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=171
    def test_富平朱酉昆入觐考选(self):
        输出 = 运行("大六壬.py", "1630 12 17 13\n1\n1\n")
        self.assertIn("己丑日，功曹寅将加未时", 输出)
        self.assertIn("初传：卯 玄武 官鬼", 输出)
        self.assertIn("中传：戌 朱雀 兄弟", 输出)
        self.assertIn("末传：巳 白虎 父母", 输出)

    # 《六壬指南》程孝延王米山索占，1925年国图扫描第172页；原图涉害先取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=172
    def test_程孝延王米山索占(self):
        输出 = 运行("大六壬.py", "1642 10 25 13\n1\n1\n2\n")
        self.assertIn("己亥日，太冲卯将加未时", 输出)
        self.assertIn("初传：未 白虎 兄弟", 输出)
        self.assertIn("中传：卯 六合 官鬼", 输出)
        self.assertIn("末传：亥 天后 妻财", 输出)

    # 《六壬指南》季大生持进京课，1925年国图扫描第173页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=173
    def test_季大生持进京课(self):
        输出 = 运行("大六壬.py", "1644 03 14 15\n1\n1\n")
        self.assertIn("乙丑日，登明亥将加申时", 输出)
        self.assertIn("初传：未 青龙 妻财", 输出)
        self.assertIn("中传：戌 朱雀 妻财", 输出)
        self.assertIn("末传：丑 天后 妻财", 输出)

    # 《六壬指南》寇道台占仕途，1925年国图扫描第173页；原刻癸酉六月戊寅未时伏吟；1633年7月23日未时已交大暑用午将，该年亦无戊寅未将的时刻，纪日或月将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=173

    # 《六壬指南》江半石占钦差，1925年国图扫描第174页；原刻己巳二月乙巳巳时，课图反推戌将；1629农历年内乙巳巳时均不在戌将，年日将不能兼合，口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=174

    # 《六壬指南》胡尹占巡按差，1925年国图扫描第175页；原刻辛卯二月；依年日时及课图亥将唯一反推1651年3月1日，农历与节月均正月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=175
    # def test_胡尹占巡按差(self):
    #     输出 = 运行("大六壬.py", "1651 03 01 11\n1\n1\n")
    #     self.assertIn("戊子日，登明亥将加午时", 输出)
    #     self.assertIn("初传：巳 太常 父母", 输出)
    #     self.assertIn("中传：戌 六合 兄弟", 输出)
    #     self.assertIn("末传：卯 太阴 官鬼", 输出)

    # 《六壬指南》张维枢占章奏，1925年国图扫描第176页；原刻己巳正月己未午时、四课反推丑将；1629农历年内己未午时均不在丑将，年月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=176

    # 《六壬指南》董兑之代董玄宰辞大宗伯，1925年国图扫描第177页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=177
    def test_董兑之代董玄宰辞大宗伯(self):
        输出 = 运行("大六壬.py", "1633 08 14 19\n1\n1\n")
        self.assertIn("庚子日，胜光午将加戌时", 输出)
        self.assertIn("初传：子 青龙 子孙", 输出)
        self.assertIn("中传：申 螣蛇 兄弟", 输出)
        self.assertIn("末传：辰 玄武 父母", 输出)

    # 《六壬指南》刘退斋占何如人，1925年国图扫描第177页；原刻丁丑八月壬寅卯时、四课反推巳将；1637農历年内壬寅卯时均不在巳将，年月或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=177

    # 《六壬指南》孙鲁山占请告，1925年国图扫描第178页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=178
    def test_孙鲁山占请告(self):
        输出 = 运行("大六壬.py", "1638 04 16 15\n1\n1\n")
        self.assertIn("丙寅日，河魁戌将加申时", 输出)
        self.assertIn("初传：辰 白虎 子孙", 输出)
        self.assertIn("中传：午 青龙 兄弟", 输出)
        self.assertIn("末传：申 六合 妻财", 输出)

    # 《六壬指南》张庠友占赵光汴请缨，1925年国图扫描第179页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=179
    def test_张庠友占赵光汴请缨(self):
        输出 = 运行("大六壬.py", "1637 07 19 15\n1\n1\n")
        self.assertIn("乙未日，小吉未将加申时", 输出)
        self.assertIn("初传：戌 太阴 妻财", 输出)
        self.assertIn("中传：卯 六合 兄弟", 输出)
        self.assertIn("末传：午 天空 子孙", 输出)

    # 《六壬指南》王旋官占上疏，1925年国图扫描第179页；原刻辛未六月；依年日时及课图未将唯一反推1631年6月29日，农历与节月均五月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=179
    # def test_王旋官占上疏(self):
    #     输出 = 运行("大六壬.py", "1631 06 29 05\n1\n1\n2\n")
    #     self.assertIn("癸卯日，小吉未将加卯时", 输出)
    #     self.assertIn("初传：酉 勾陈 父母", 输出)
    #     self.assertIn("中传：丑 太常 官鬼", 输出)
    #     self.assertIn("末传：巳 贵人 妻财", 输出)

    # 《六壬指南》刘退斋请假省亲，1925年国图扫描第180页；原刻丁丑四月丁酉巳时、四课反推酉将；1637农历年内丁酉巳时均不能兼合酉将，日将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=180

    # 《六壬指南》沈云生占回奏，1925年国图扫描第181页；原刻癸酉二月丁丑午时、四课反推亥将；1633农历年内丁丑午时均不能兼合亥将，日将口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=181

    # 《六壬指南》孙三杰代丁科长守科失红本，1925年国图扫描第182页；原刻丁丑十一月丁亥申时、返吟寅将；1637农历年内丁亥申时均不能兼合寅将，气法或纪日待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=182

    # 《六壬指南》李载溪座间索占，1925年国图扫描第182页；原纪戊辰十二月，公历已为1629年 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=182
    def test_李载溪座间索占(self):
        输出 = 运行("大六壬.py", "1629 01 15 15\n1\n1\n")
        self.assertIn("戊申日，大吉丑将加申时", 输出)
        self.assertIn("初传：卯 太阴 官鬼", 输出)
        self.assertIn("中传：申 青龙 子孙", 输出)
        self.assertIn("末传：丑 贵人 兄弟", 输出)

    # 《六壬指南》迟运芝在京偶占，1925年国图扫描第183页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=183
    def test_迟运芝在京偶占(self):
        输出 = 运行("大六壬.py", "1631 05 13 11\n1\n1\n")
        self.assertIn("丙辰日，从魁酉将加午时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：寅 玄武 父母", 输出)

    # 《六壬指南》冯允升被逮求占，1925年国图扫描第184页；原刻丙子三月；依年日时及课图戌将唯一反推1636年3月26日，农历与节月均二月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=184
    # def test_冯允升被逮求占(self):
    #     输出 = 运行("大六壬.py", "1636 03 26 05\n1\n1\n")
    #     self.assertIn("乙未日，河魁戌将加卯时", 输出)
    #     self.assertIn("初传：午 天空 子孙", 输出)
    #     self.assertIn("中传：丑 天后 妻财", 输出)
    #     self.assertIn("末传：申 勾陈 官鬼", 输出)

    # 《六壬指南》陈秋桃占出狱，1925年国图扫描第185页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=185
    def test_陈秋桃占出狱(self):
        输出 = 运行("大六壬.py", "1636 04 09 05\n1\n1\n")
        self.assertIn("己酉日，河魁戌将加卯时", 输出)
        self.assertIn("初传：亥 螣蛇 妻财", 输出)
        self.assertIn("中传：午 天空 父母", 输出)
        self.assertIn("末传：丑 天后 兄弟", 输出)

    # 《六壬指南》埂子街甲午客袖占，1925年国图扫描第185页；原刻壬午七月甲午午时、图反推巳将；1642农历年内甲午午时均不在巳将，纪日或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=185

    # 《六壬指南》周诚生代周首辅占弹劾，1925年国图扫描第186页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=186
    def test_周诚生代周首辅占弹劾(self):
        输出 = 运行("大六壬.py", "1633 05 09 07\n1\n1\n")
        self.assertIn("癸亥日，从魁酉将加辰时", 输出)
        self.assertIn("初传：午 螣蛇 妻财", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：辰 天后 官鬼", 输出)

    # 《六壬指南》戚司宗占重辟，1925年国图扫描第187页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=187
    def test_戚司宗占重辟(self):
        输出 = 运行("大六壬.py", "1636 03 26 05\n1\n1\n")
        self.assertIn("乙未日，河魁戌将加卯时", 输出)
        self.assertIn("初传：午 天空 子孙", 输出)
        self.assertIn("中传：丑 天后 妻财", 输出)
        self.assertIn("末传：申 勾陈 官鬼", 输出)

    # 《六壬指南》宋太斗代占公讼，1925年国图扫描第188页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=188
    def test_宋太斗代占公讼(self):
        输出 = 运行("大六壬.py", "1631 05 15 17\n1\n1\n")
        self.assertIn("戊午日，从魁酉将加酉时", 输出)
        self.assertIn("初传：巳 朱雀 父母", 输出)
        self.assertIn("中传：申 天后 子孙", 输出)
        self.assertIn("末传：寅 青龙 官鬼", 输出)

    # 《六壬指南》吴振缨被逮索占，1925年国图扫描第188页；原刻丙子二月乙酉巳时、图反推戌将；1636农历年内乙酉巳时均不在戌将，气法或纪日口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=188

    # 《六壬指南》盛顺被逮进京，1925年国图扫描第189页；原刻癸未七月丁未未时、图反推辰将；1643农历年内丁未未时均不在辰将，气法或纪日口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=189

    # 《六壬指南》顾友吴子达代占公讼，1925年国图扫描第190页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=190
    def test_顾友吴子达代占公讼(self):
        输出 = 运行("大六壬.py", "1637 06 18 09\n1\n1\n")
        self.assertIn("甲子日，传送申将加巳时", 输出)
        self.assertIn("初传：申 青龙 官鬼", 输出)
        self.assertIn("中传：亥 朱雀 父母", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)

    # 《六壬指南》钱是奄占陈南洲逮问，1925年国图扫描第191页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=191
    def test_钱是奄占陈南洲逮问(self):
        输出 = 运行("大六壬.py", "1637 09 09 07\n1\n1\n")
        self.assertIn("丁亥日，太乙巳将加辰时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：酉 朱雀 妻财", 输出)
        self.assertIn("末传：戌 螣蛇 子孙", 输出)

    # 《六壬指南》谭懋芳李父母被逮，1925年国图扫描第191页；原题丁丑十一月丁亥申时，四课却为癸未辰时；现代录据图改题，按原年及课图日将时唯一反推1638年1月3日，保留待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=191
    # def test_谭懋芳李父母被逮(self):
    #     输出 = 运行("大六壬.py", "1638 01 03 07\n1\n1\n")
    #     self.assertIn("癸未日，大吉丑将加辰时", 输出)
    #     self.assertIn("初传：戌 白虎 官鬼", 输出)
    #     self.assertIn("中传：未 太阴 官鬼", 输出)
    #     self.assertIn("末传：辰 螣蛇 官鬼", 输出)

    # 《六壬指南》熊奋渭代戊寅命人占讼，1925年国图扫描第192页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=192
    def test_熊奋渭代戊寅命人占讼(self):
        输出 = 运行("大六壬.py", "1631 05 20 11\n1\n1\n")
        self.assertIn("癸亥日，从魁酉将加午时", 输出)
        self.assertIn("初传：辰 天后 官鬼", 输出)
        self.assertIn("中传：未 朱雀 官鬼", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)

    # 《六壬指南》王怀荫占失马，1925年国图扫描第193页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=193
    def test_王怀荫占失马(self):
        输出 = 运行("大六壬.py", "1650 11 16 15\n1\n1\n")
        self.assertIn("癸卯日，太冲卯将加申时", 输出)
        self.assertIn("初传：卯 朱雀 子孙", 输出)
        self.assertIn("中传：戌 白虎 官鬼", 输出)
        self.assertIn("末传：巳 贵人 妻财", 输出)

    # 《六壬指南》建龙寺丽天索占，1925年国图扫描第194页；原刻丙寅四月丙寅寅时、图反推酉将；1626农历年内丙寅寅时均不在酉将，气法或纪日口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=194

    # 《六壬指南》张四知占进退行止，1925年国图扫描第194页；课图在第195页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=194
    def test_张四知占进退行止(self):
        输出 = 运行("大六壬.py", "1644 06 12 13\n1\n1\n")
        self.assertIn("乙未日，传送申将加未时", 输出)
        self.assertIn("初传：酉 玄武 官鬼", 输出)
        self.assertIn("中传：戌 太阴 妻财", 输出)
        self.assertIn("末传：亥 天后 父母", 输出)

    # 《六壬指南》田百原为陈公献占搬眷，1925年国图扫描第195页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=195
    def test_田百原为陈公献占搬眷(self):
        输出 = 运行("大六壬.py", "1645 05 06 11\n1\n1\n")
        self.assertIn("癸亥日，从魁酉将加午时", 输出)
        self.assertIn("初传：辰 天后 官鬼", 输出)
        self.assertIn("中传：未 朱雀 官鬼", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)

    # 《六壬指南》弯子街二人占子逃，1925年国图扫描第196页；原刻庚寅四月；依年日时及课图酉将唯一反推1650年5月2日，农历与节月均三月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=196
    # def test_弯子街二人占子逃(self):
    #     输出 = 运行("大六壬.py", "1650 05 02 09\n1\n1\n")
    #     self.assertIn("乙酉日，从魁酉将加巳时", 输出)
    #     self.assertIn("初传：申 勾陈 官鬼", 输出)
    #     self.assertIn("中传：子 贵人 父母", 输出)
    #     self.assertIn("末传：辰 太常 妻财", 输出)

    # 《六壬指南》李六生问燕京安危，1925年国图扫描第197页；按原课图核盘，断语戌发用与图卯不合，叙事日期亦待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=197
    def test_李六生问燕京安危(self):
        输出 = 运行("大六壬.py", "1644 05 08 07\n1\n1\n")
        self.assertIn("庚申日，从魁酉将加辰时", 输出)
        self.assertIn("初传：卯 太阴 妻财", 输出)
        self.assertIn("中传：丑 贵人 父母", 输出)
        self.assertIn("末传：丑 贵人 父母", 输出)

    # 《六壬指南》田百原闻睢州兵变，扫描第197、198页原题戊午日丙申时与图干丙不合；图用子将，按丙午复盘又在雨水后，原题、课图与气法口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=197

    # 《六壬指南》扬州守西门，1925年国图扫描第198页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=198
    def test_扬州守西门(self):
        输出 = 运行("大六壬.py", "1645 05 20 07\n1\n1\n")
        self.assertIn("丁丑日，从魁酉将加辰时", 输出)
        self.assertIn("初传：巳 天空 兄弟", 输出)
        self.assertIn("中传：戌 螣蛇 子孙", 输出)
        self.assertIn("末传：卯 太常 父母", 输出)

    # 《六壬指南》李少文问金兵东下，1925年国图扫描第199页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=199
    def test_李少文问金兵东下(self):
        输出 = 运行("大六壬.py", "1648 03 03 13\n1\n1\n")
        self.assertIn("乙亥日，登明亥将加未时", 输出)
        self.assertIn("初传：未 青龙 妻财", 输出)
        self.assertIn("中传：亥 螣蛇 父母", 输出)
        self.assertIn("末传：卯 玄武 兄弟", 输出)

    # 《六壬指南》王总兵闻大同兵变，扫描第200页原刻五月，另录正月；辛巳亥将唯一对应1649-03-04，但纪月异文待证，仅存注释例 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=200
    # def test_王总兵闻大同兵变(self):
    #     输出 = 运行("大六壬.py", "1649 03 04 05\n1\n1\n")
    #     self.assertIn("辛巳日，登明亥将加卯时", 输出)
    #     self.assertIn("初传：午 贵人 官鬼", 输出)
    #     self.assertIn("中传：寅 勾陈 妻财", 输出)
    #     self.assertIn("末传：戌 太常 父母", 输出)

    # 《六壬指南》武昌城池安危，1925年国图扫描第201页；己丑三月是诸友出示晋戴洋旧课的时间，原占未记具体年日，不能冒作1649年的占局 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=201

    # 《六壬指南》扬城被围，1925年国图扫描第202页；原刻庚申年，另录甲申；按甲申可唯一复盘，纪年异文待校，仅存注释例 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=202
    # def test_扬城被围(self):
    #     输出 = 运行("大六壬.py", "1644 06 17 09\n1\n1\n")
    #     self.assertIn("庚子日，传送申将加巳时", 输出)
    #     self.assertIn("初传：午 白虎 官鬼", 输出)
    #     self.assertIn("中传：酉 勾陈 兄弟", 输出)
    #     self.assertIn("末传：子 螣蛇 子孙", 输出)

    # 《六壬指南》卞孟井问真定安危，1925年国图扫描第202页；只核原课图，原断即此日京陷的纪日待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=202
    def test_卞孟井问真定安危(self):
        输出 = 运行("大六壬.py", "1644 04 24 11\n1\n1\n")
        self.assertIn("丙午日，从魁酉将加午时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：寅 玄武 父母", 输出)

    # 《六壬指南》田百原勤王，1925年国图扫描第203页；辛金寄戌不应抹掉第四课戌土克亥水 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=203
    def test_田百原勤王(self):
        输出 = 运行("大六壬.py", "1645 05 04 15\n1\n1\n1\n")
        self.assertIn("辛酉日，从魁酉将加申时", 输出)
        self.assertIn("初传：亥 白虎 子孙", 输出)
        self.assertIn("中传：子 天空 子孙", 输出)
        self.assertIn("末传：丑 青龙 父母", 输出)

    # 《六壬指南》泽州地方兵警，1925年国图扫描第204页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=204
    def test_泽州地方兵警(self):
        输出 = 运行("大六壬.py", "1649 12 16 19\n1\n1\n")
        self.assertIn("戊辰日，功曹寅将加戌时", 输出)
        self.assertIn("初传：子 青龙 妻财", 输出)
        self.assertIn("中传：辰 玄武 兄弟", 输出)
        self.assertIn("末传：申 螣蛇 子孙", 输出)

    # 《六壬指南》杨九苞舟师来函，1925年国图扫描第205页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=205
    def test_杨九苞舟师来函(self):
        输出 = 运行("大六壬.py", "1645 05 28 07\n1\n1\n")
        self.assertIn("乙酉日，传送申将加辰时", 输出)
        self.assertIn("初传：申 勾陈 官鬼", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：辰 太常 妻财", 输出)

    # 《六壬指南》辛未四月兵警，1925年国图扫描第206页；原图丙子酉将酉时伏吟，1631年丙子均不在酉将期；四月可按节月但月将仍不合，扫描同，口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=206

    # 《六壬指南》程翔云闻兵警，1925年国图扫描第206页；原记正月按立春节月成立，当日农历仍十二月，不按农历月份判错 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=206
    def test_程翔云闻兵警(self):
        输出 = 运行("大六壬.py", "1644 02 05 17\n1\n1\n")
        self.assertIn("丁亥日，神后子将加酉时", 输出)
        self.assertIn("初传：午 六合 兄弟", 输出)
        self.assertIn("中传：戌 天后 子孙", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)

    # 《六壬指南》刘汉式占行人，1925年国图扫描第208页；原记七月，立秋已过而农历为闰六月；涉害先取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=208
    def test_刘汉式占行人(self):
        输出 = 运行("大六壬.py", "1645 08 11 15\n1\n1\n2\n")
        self.assertIn("庚子日，胜光午将加申时", 输出)
        self.assertIn("初传：午 青龙 官鬼", 输出)
        self.assertIn("中传：辰 六合 父母", 输出)
        self.assertIn("末传：寅 螣蛇 妻财", 输出)

    # 《六壬指南》倪子玄占父到京，1925年国图扫描第209页；原刻占父，现代录作占女 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=209
    def test_倪子玄占父到京(self):
        输出 = 运行("大六壬.py", "1628 11 30 09\n1\n1\n")
        self.assertIn("壬戌日，功曹寅将加巳时", 输出)
        self.assertIn("初传：巳 贵人 妻财", 输出)
        self.assertIn("中传：寅 六合 子孙", 输出)
        self.assertIn("末传：亥 天空 兄弟", 输出)

    # 《六壬指南》李梅公占行人，1925年国图扫描第210页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=210
    def test_李梅公占行人(self):
        输出 = 运行("大六壬.py", "1650 08 22 09\n1\n1\n")
        self.assertIn("丁丑日，胜光午将加巳时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：酉 朱雀 妻财", 输出)
        self.assertIn("末传：戌 螣蛇 子孙", 输出)

    # 《六壬指南》庄公远占程翔云到省，1925年国图扫描第210页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=210
    def test_庄公远占程翔云到省(self):
        输出 = 运行("大六壬.py", "1651 10 20 05\n1\n1\n")
        self.assertIn("辛巳日，天罡辰将加卯时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：未 天后 父母", 输出)
        self.assertIn("末传：申 太阴 兄弟", 输出)

    # 《六壬指南》张奉初为观初占病，1925年国图扫描第211页；原刻辛巳九月；依年日时及课图午将唯一反推1641年8月19日，农历与节月均七月，原图丑时用昼贵，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=211
    # def test_张奉初为观初占病(self):
    #     输出 = 运行("大六壬.py", "1641 08 19 01\n1\n2\n")
    #     self.assertIn("丁亥日，胜光午将加丑时", 输出)
    #     self.assertIn("初传：巳 天空 兄弟", 输出)
    #     self.assertIn("中传：戌 螣蛇 子孙", 输出)
    #     self.assertIn("末传：卯 太常 父母", 输出)

    # 《六壬指南》张奉初案后匿名人复占，仅录未亥卯三传及白虎发用，未记占时与完整课图，不能唯一复原 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=211

    # 《六壬指南》张澹宁占病，1925年国图扫描第212页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=212
    def test_张澹宁占病(self):
        输出 = 运行("大六壬.py", "1639 07 23 07\n1\n1\n")
        self.assertIn("己酉日，小吉未将加辰时", 输出)
        self.assertIn("初传：卯 玄武 官鬼", 输出)
        self.assertIn("中传：午 天空 父母", 输出)
        self.assertIn("末传：酉 六合 子孙", 输出)

    # 《六壬指南》卢承山占病，1925年国图扫描第213页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=213
    def test_卢承山占病(self):
        输出 = 运行("大六壬.py", "1645 02 11 09\n1\n1\n")
        self.assertIn("己亥日，神后子将加巳时", 输出)
        self.assertIn("初传：午 天空 父母", 输出)
        self.assertIn("中传：丑 天后 兄弟", 输出)
        self.assertIn("末传：申 勾陈 子孙", 输出)

    # 《六壬指南》楠姓为董晋侯占病，1925年国图扫描第213页；原刻辛卯二月丁未卯时、图反推戌将；1651农历年内丁未卯时均不在戌将，气法或纪日待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=213

    # 《六壬指南》王养吾占妻病，1925年国图扫描第214页；原刻乙丑十月辛亥午时、图反推卯将；1625农历年内辛亥午时均不在卯将，年日将不能兼合，口径待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=214

    # 《六壬指南》刘一纯占病，1925年国图扫描第215页；原刻辛未正月；依年日时及课图亥将唯一反推1631年3月6日，农历与节月均二月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=215
    # def test_刘一纯占病(self):
    #     输出 = 运行("大六壬.py", "1631 03 06 13\n1\n1\n")
    #     self.assertIn("戊申日，登明亥将加未时", 输出)
    #     self.assertIn("初传：辰 玄武 兄弟", 输出)
    #     self.assertIn("中传：申 青龙 子孙", 输出)
    #     self.assertIn("末传：子 螣蛇 妻财", 输出)

    # 《六壬指南》陈惟一占扬州道台病，1925年国图扫描第216页；原刻己丑八月；依年日时及伏吟午将唯一反推1649年7月31日，农历与节月均六月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=216
    # def test_陈惟一占扬州道台病(self):
    #     输出 = 运行("大六壬.py", "1649 07 31 11\n1\n1\n")
    #     self.assertIn("庚戌日，胜光午将加午时", 输出)
    #     self.assertIn("初传：申 白虎 兄弟", 输出)
    #     self.assertIn("中传：寅 螣蛇 妻财", 输出)
    #     self.assertIn("末传：巳 勾陈 官鬼", 输出)

    # 《六壬指南》程孝延代郑姓占病，1925年国图扫描第217页；原刻己丑八月乙未巳时、图反推午将；1649农历年内乙未巳时均不在午将，纪日或课图待校 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=217

    # 《六壬指南》程翔云雪寒占岁，1925年国图扫描第218页；未时尚未交雨水 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=218
    def test_程翔云雪寒占岁(self):
        输出 = 运行("大六壬.py", "1641 02 18 13\n1\n1\n")
        self.assertIn("乙酉日，神后子将加未时", 输出)
        self.assertIn("初传：未 青龙 妻财", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：巳 白虎 子孙", 输出)

    # 《六壬指南》己巳十一月扣门声，1925年国图扫描第219页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=219
    def test_己巳十一月扣门声(self):
        输出 = 运行("大六壬.py", "1629 12 30 19\n1\n1\n")
        self.assertIn("丁酉日，大吉丑将加戌时", 输出)
        self.assertIn("初传：子 玄武 官鬼", 输出)
        self.assertIn("中传：卯 天空 父母", 输出)
        self.assertIn("末传：午 六合 兄弟", 输出)

    # 《六壬指南》敏若夜闻鸦鸣，1925年国图扫描第220页；原刻己丑二月，现代录改三月；依年日时及课图戌将唯一反推1649年4月17日，农历与节月均三月，纪月待证 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=220
    # def test_敏若夜闻鸦鸣(self):
    #     输出 = 运行("大六壬.py", "1649 04 17 21\n1\n1\n")
    #     self.assertIn("乙丑日，河魁戌将加亥时", 输出)
    #     self.assertIn("初传：子 太常 父母", 输出)
    #     self.assertIn("中传：亥 玄武 父母", 输出)
    #     self.assertIn("末传：戌 太阴 妻财", 输出)

    # 《六壬指南》吴三占天宁寺夜惊，1925年国图扫描第220页；原刻江南吴三，现代录作吴一三；课图在第221页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=220
    def test_吴三占天宁寺夜惊(self):
        输出 = 运行("大六壬.py", "1649 07 16 21\n1\n1\n")
        self.assertIn("乙未日，小吉未将加亥时", 输出)
        self.assertIn("初传：卯 白虎 兄弟", 输出)
        self.assertIn("中传：亥 六合 父母", 输出)
        self.assertIn("末传：未 天后 妻财", 输出)

    # 《六壬指南》庄公远占日食，1925年国图扫描第222页；原刻十月辛巳朔，午时图用夜贵 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=222
    def test_庄公远占日食(self):
        输出 = 运行("大六壬.py", "1650 10 25 11\n1\n3\n")
        self.assertIn("辛巳日，太冲卯将加午时", 输出)
        self.assertIn("初传：寅 贵人 妻财", 输出)
        self.assertIn("中传：亥 六合 子孙", 输出)
        self.assertIn("末传：申 天空 兄弟", 输出)

    # 《六壬指南》范玄同射覆石黄，1925年国图扫描第223页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=223
    def test_范玄同射覆石黄(self):
        输出 = 运行("大六壬.py", "1641 09 15 15\n1\n1\n")
        self.assertIn("甲寅日，太乙巳将加申时", 输出)
        self.assertIn("初传：丑 贵人 妻财", 输出)
        self.assertIn("中传：亥 太阴 父母", 输出)
        self.assertIn("末传：亥 太阴 父母", 输出)

    # 《六壬指南》陈开子司化南射覆文书，1925年国图扫描第223页；原刻庚寅五月，现代录改丙寅丑月；图在第224页，用昼贵与地盘孟位涉害，原文另论东方朔本课亥酉未 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=223
    def test_陈开子司化南射覆文书(self):
        输出 = 运行("大六壬.py", "1650 06 30 17\n1\n2\n2\n")
        self.assertIn("甲申日，小吉未将加酉时", 输出)
        self.assertIn("初传：午 青龙 子孙", 输出)
        self.assertIn("中传：辰 六合 妻财", 输出)
        self.assertIn("末传：寅 螣蛇 兄弟", 输出)

    # 现代《六壬指南注解》出行章徐盟鹿庚寅五月庚申丑时案未在1925年国图本卷四占验中定位，原始出处待核，暂不作为该本实占测试 https://shuyuan.zhiming.life/read/六壬指南注解/15
