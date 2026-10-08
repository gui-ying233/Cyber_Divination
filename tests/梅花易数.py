import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《梅花易数》卷一“观梅占”仅记辰年，缺具体纪年 https://zh.wikisource.org/wiki/梅花易數/卷一#觀梅占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=22

    # 《梅花易数》卷一“牡丹占”仅记巳年，缺具体纪年 https://zh.wikisource.org/wiki/梅花易數/卷一#牡丹占 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=24

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

    # 《梅花易数》卷二王、田、韩三姓起屋占以姓氏笔画加入年月日时，当前公历起卦未收姓数 https://zh.wikisource.org/wiki/梅花易數/卷二

    # 《梅花易数》卷三笼盛草根、钟覆破玉环只载所成卦及变卦，缺起卦所取数 https://zh.wikisource.org/wiki/梅花易數/卷三
