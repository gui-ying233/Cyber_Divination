import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《梅花易数》卷一“观梅占”仅记辰年，缺具体纪年 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=22

    # 《梅花易数》卷一“牡丹占”仅记巳年，缺具体纪年 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=24

    # 《梅花易数》卷一“邻夜扣门借物占”，酉时十数只加入动爻 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=25

    def test_邻夜扣门借物(self):
        输出 = 运行("梅花易数.py", "1 5 10\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷸ 巽为风", 输出)

    # 《梅花易数》“今日动静如何”，韩国藏书阁K3-430写本26～28页原载八、五数，升初爻变泰 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=27

    def test_今日动静如何(self):
        输出 = 运行("梅花易数.py", "8 5\n")
        self.assertIn("䷭ 地风升\n\t变卦为：䷊ 地天泰", 输出)

    # 《梅花易数》“西林寺额占”，韩国藏书阁K3-430写本28～29页原载七、八数剥变艮，添林字二画为损变中孚 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=28

    def test_西林寺牌额(self):
        初占 = 运行("梅花易数.py", "7 8\n")
        改额 = 运行("梅花易数.py", "7 10\n")
        self.assertIn("䷖ 山地剥\n\t变卦为：䷳ 艮为山", 初占)
        self.assertIn("䷨ 山泽损\n\t变卦为：䷼ 风泽中孚", 改额)

    # 《梅花易数》卷一“老人有忧色占”，原记姤九四变，可确定之卦为巽 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=29

    def test_老人有忧色(self):
        输出 = 运行("梅花易数.py", "1 5 4\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷸ 巽为风", 输出)

    # 《梅花易数》卷一“少年有喜色占” https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=31

    def test_少年有喜色(self):
        输出 = 运行("梅花易数.py", "7 3 7\n")
        self.assertIn("䷕ 山火贲\n\t变卦为：䷤ 风火家人", 输出)

    # 《梅花易数》卷一“牛哀鸣占” https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=32

    def test_牛哀鸣(self):
        输出 = 运行("梅花易数.py", "8 6 7\n")
        self.assertIn("䷆ 地水师\n\t变卦为：䷭ 地风升", 输出)

    # 《梅花易数》卷一“鸡悲鸣占” https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=33

    def test_鸡悲鸣(self):
        输出 = 运行("梅花易数.py", "5 1 4\n")
        self.assertIn("䷈ 风天小畜\n\t变卦为：䷀ 乾为天", 输出)

    # 《梅花易数》卷一“枯枝坠地占” https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=34

    def test_枯枝坠地(self):
        输出 = 运行("梅花易数.py", "3 2 5\n")
        self.assertIn("䷥ 火泽睽\n\t变卦为：䷨ 山泽损", 输出)

    # 《梅花易数》卷二起卦加数及屋宅占，韩国国立中央图书馆CNTS-00047981941第2册54～57页原载王4、田6、韩21姓数加入年月日时，当前公历起卦未收姓数 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=54

    # 《梅花易数》卷三观物用易例，韩国国立中央图书馆CNTS-00047981941第2册89页笼盛草根仅记泰初变升，钟覆破玉环仅记鼎变恒，未载起卦取数 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=89
