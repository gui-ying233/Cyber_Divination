import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《梅花易数》序“投瓦枕”，枕中字只记某年某月日某时，未载实际年月日时及起卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_1_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=15 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=3

    # 《梅花易数》序“秀士家白金”，陶家传书后断床西北壁中白金，未载问占年月日时、起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_1_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=16 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=3

    # 《梅花易数》序“置椅仙人坐破”，椅底只记某年月日当为仙人坐破，未载实际年月日时、起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_1_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=16 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=4

    # 《梅花易数》卷1“观梅占”，按原载辰5、十二月12、十七日17、申9起卦，革初变咸。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=22 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=23

    def test_观梅(self):
        输出 = 运行("梅花易数.py", "5 12 17 9\n")
        self.assertIn("䷰ 泽火革\n\t变卦为：䷞ 泽山咸", 输出)

    # 《梅花易数》卷1“牡丹占”，按原载巳6、三月3、十六日16、卯4起卦，姤五变鼎。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=24 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=24

    def test_牡丹(self):
        输出 = 运行("梅花易数.py", "6 3 16 4\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷱ 火风鼎", 输出)

    # 《梅花易数》卷1“邻夜扣门借物占”，文明书局24～25页与旧本均载一、五声，酉时十数只加入动爻，姤四变巽。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=25 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=24

    def test_邻夜扣门借物(self):
        输出 = 运行("梅花易数.py", "1 5 10\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷸ 巽为风", 输出)

    # 《梅花易数》卷1“今日动静如何”，文明书局25～26页与旧本均载八、五数，升初变泰。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=27 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=25

    def test_今日动静如何(self):
        输出 = 运行("梅花易数.py", "8 5\n")
        self.assertIn("䷭ 地风升\n\t变卦为：䷊ 地天泰", 输出)

    # 《梅花易数》卷1“西林寺牌额占”，两本均载七、八数剥变艮，添林字两钩后七、十数损变中孚；新本十五除六余三却写第二爻变艮，与旧本六三及所载变卦矛盾，按旧本原数保留。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=28 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=26

    def test_西林寺牌额(self):
        初占 = 运行("梅花易数.py", "7 8\n")
        改额 = 运行("梅花易数.py", "7 10\n")
        self.assertIn("䷖ 山地剥\n\t变卦为：䷳ 艮为山", 初占)
        self.assertIn("䷨ 山泽损\n\t变卦为：䷼ 风泽中孚", 改额)

    # 《梅花易数》卷1“老人有忧色占”，两本均载乾一、巽五、卯时四，姤九四变巽。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=29 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=27

    def test_老人有忧色(self):
        输出 = 运行("梅花易数.py", "1 5 4\n")
        self.assertIn("䷫ 天风姤\n\t变卦为：䷸ 巽为风", 输出)

    # 《梅花易数》卷1“少年有喜色占”，两本均载艮七、离三、午时七，贲五变家人。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=31 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=28

    def test_少年有喜色(self):
        输出 = 运行("梅花易数.py", "7 3 7\n")
        self.assertIn("䷕ 山火贲\n\t变卦为：䷤ 风火家人", 输出)

    # 《梅花易数》卷1“牛哀鸣占”，两本均载坤八、坎六、午时七，师三变升。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=32 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=28

    def test_牛哀鸣(self):
        输出 = 运行("梅花易数.py", "8 6 7\n")
        self.assertIn("䷆ 地水师\n\t变卦为：䷭ 地风升", 输出)

    # 《梅花易数》卷1“鸡悲鸣占”，两本均载巽五、乾一、卯时四，小畜四变乾。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=33 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=29

    def test_鸡悲鸣(self):
        输出 = 运行("梅花易数.py", "5 1 4\n")
        self.assertIn("䷈ 风天小畜\n\t变卦为：䷀ 乾为天", 输出)

    # 《梅花易数》卷1“枯枝坠地占”，两本均载离三、兑二、辰时五，睽四变损。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=34 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=29

    def test_枯枝坠地(self):
        输出 = 运行("梅花易数.py", "3 2 5\n")
        self.assertIn("䷥ 火泽睽\n\t变卦为：䷨ 山泽损", 输出)

    # 《梅花易数》卷1“风觉占南来风”，只以南来风断家人，未载时数或动爻、变卦。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=35 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=30

    # 《梅花易数》卷1“鸟占一至三只”，只以只数取乾、兑、离，未载完整方位、时数或本变卦。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=37 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=31

    # 《梅花易数》卷1“听声音占”，只载一声乾、二声兑及鼓木震等取象，未载一例完整上卦、下卦、时数和本变卦。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=38 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=31

    # 《梅花易数》卷1“形物占验色占”，只载圆乾、方坤、刚兑、柔巽等形色取象，未载一例完整时数及本变卦。 https://jsg.aks.ac.kr/data/serviceFiles/pdf/K3-430_001.pdf#page=39 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=32

    # 《梅花易数》卷2“乾上坤下占病”，初爻动，下卦坤变震；按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=23 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=73

    def test_乾坤占病初爻(self):
        输出 = 运行("梅花易数.py", "1 8 / 1\n")
        self.assertRegex(输出, r"变卦为：[^\n]* 天雷")

    # 《梅花易数》卷2“乾上坤下占病”，二爻动，下卦坤变坎；按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=23 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=73

    def test_乾坤占病二爻(self):
        输出 = 运行("梅花易数.py", "1 8 / 2\n")
        self.assertRegex(输出, r"变卦为：[^\n]* 天水")

    # 《梅花易数》卷2“乾上坤下占病”，三爻动，下卦坤变艮；按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=23 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=73

    def test_乾坤占病三爻(self):
        输出 = 运行("梅花易数.py", "1 8 / 3\n")
        self.assertRegex(输出, r"变卦为：[^\n]* 天山")

    # 《梅花易数》卷2“乾上坤下占病”，四爻动，上卦乾变巽；按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=23 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=73

    def test_乾坤占病四爻(self):
        输出 = 运行("梅花易数.py", "1 8 / 4\n")
        self.assertRegex(输出, r"变卦为：[^\n]* 风地")

    # 《梅花易数》卷2“乾上坤下占病”，五爻动，上卦乾变离；按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=23 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=73

    def test_乾坤占病五爻(self):
        输出 = 运行("梅花易数.py", "1 8 / 5\n")
        self.assertRegex(输出, r"变卦为：[^\n]* 火地")

    # 《梅花易数》卷2“乾上坤下占病”，上爻动，上卦乾变兑；按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=23 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=73

    def test_乾坤占病上爻(self):
        输出 = 运行("梅花易数.py", "1 8 / 6\n")
        self.assertRegex(输出, r"变卦为：[^\n]* 泽地")

    # 《梅花易数》卷2“起卦加数例王姓屋宅”，两本均载寅3、十二月12、初一1、午7、王4，原合数20、27，丰三变震。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=54 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=95

    def test_王姓屋宅(self):
        输出 = 运行("梅花易数.py", "3 12 1 7 4\n")
        self.assertIn("䷶ 雷火丰\n\t变卦为：䷲ 震为雷", 输出)

    # 《梅花易数》卷2“起卦加数例田姓屋宅”，两本均载寅3、十二月12、初一1、午7、田6，原合数22、29，井五变升。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=54 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=95

    def test_田姓屋宅(self):
        输出 = 运行("梅花易数.py", "3 12 1 7 6\n")
        self.assertIn("䷯ 水风井\n\t变卦为：䷭ 地风升", 输出)

    # 《梅花易数》卷2“起卦加数例韩姓屋宅”，两本均载寅3、十二月12、初一1、午7、韩21，原合数37、44，益二变中孚。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=54 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=95

    def test_韩姓屋宅(self):
        输出 = 运行("梅花易数.py", "3 12 1 7 21\n")
        self.assertIn("䷩ 风雷益\n\t变卦为：䷼ 风泽中孚", 输出)

    # 《梅花易数》卷3“变卦式泽火革变咸”，两本均载上兑下离、离初爻阳动变艮，按原卦象与动爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=61 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=105

    def test_泽火革变咸(self):
        输出 = 运行("梅花易数.py", "2 3 / 1\n")
        self.assertIn("䷰ 泽火革\n\t变卦为：䷞ 泽山咸", 输出)

    # 《梅花易数》卷3“变卦式地雷复变临”，两本均载复变临图，未明记动爻；由本变卦唯一反推二爻动。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=62 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=105
    # def test_地雷复变临(self):
    #     输出 = 运行("梅花易数.py", "8 4 / 2\n")
    #     self.assertIn("䷗ 地雷复\n\t变卦为：䷒ 地泽临", 输出)

    # 《梅花易数》卷3“变卦式天泽履变乾”，两本均载履变乾图，未明记动爻；由本变卦唯一反推三爻动。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=62 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=106
    # def test_天泽履变乾(self):
    #     输出 = 运行("梅花易数.py", "1 2 / 3\n")
    #     self.assertIn("䷉ 天泽履\n\t变卦为：䷀ 乾为天", 输出)

    # 《梅花易数》卷3“变卦式泽火革变噬嗑”，两本题名由革变噬嗑须三、五、上爻同变，未载对应多爻取法。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=62 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=106

    # 《梅花易数》卷3“变卦式归妹变睽”，两本题名由归妹变睽唯一反推上爻动，原文却写四爻变卦成艮，与题名不合。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=62 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=106
    # def test_归妹变睽(self):
    #     输出 = 运行("梅花易数.py", "4 2 / 6\n")
    #     self.assertIn("䷵ 雷泽归妹\n\t变卦为：䷥ 火泽睽", 输出)

    # 《梅花易数》卷3“变卦式泽天夬变兑”，两本均载夬变兑图，未明记动爻；由本变卦唯一反推三爻动。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=63 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=106
    # def test_泽天夬变兑(self):
    #     输出 = 运行("梅花易数.py", "2 1 / 3\n")
    #     self.assertIn("䷪ 泽天夬\n\t变卦为：䷹ 兑为泽", 输出)

    # 《梅花易数》卷3“变卦式泽火革变咸”，两本重述革初爻变咸及破磁碟物断，本变卦回放合并第105页同图演例。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=63 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=107

    # 《梅花易数》卷3“天水讼变兑求财”，两本图载上乾变兑、下坎不变，未明记动爻；据图唯一反推上爻动。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=64 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=107
    # def test_天水讼变兑求财(self):
    #     输出 = 运行("梅花易数.py", "1 6 / 6\n")
    #     self.assertIn("䷅ 天水讼", 输出)
    #     self.assertRegex(输出, r"变卦为：[^\n]* 泽水")

    # 《梅花易数》卷3“假如天地否与泽火革”，仅以乾一坤八、兑二离三说明卦数，未给具体起卦原数、动爻或变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=74 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=116

    # 《梅花易数》卷3“观物乾初二三爻”，只载乾三爻卦初变巽、二变离、三变兑及物断，未给完整上下卦组合。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=88 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=126

    # 《梅花易数》卷3“观物用易笼盛草根”，原记泰初爻变升，按原卦象与初爻回放。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=89 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=127

    def test_笼盛草根(self):
        输出 = 运行("梅花易数.py", "8 1 / 1\n")
        self.assertIn("䷊ 地天泰\n\t变卦为：䷭ 地风升", 输出)

    # 《梅花易数》卷3“观物用易钟覆破玉环”，原记鼎变恒，未明记动爻；由本变卦唯一反推上爻动。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=89 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=127
    # def test_钟覆破玉环(self):
    #     输出 = 运行("梅花易数.py", "3 5 / 6\n")
    #     self.assertIn("䷱ 火风鼎\n\t变卦为：䷟ 雷风恒", 输出)

    # 《梅花易数》卷3“猜手中物”，乾圆白、坎黑近水、艮瓦石、震巽竹木等均为卦象与物类判断，未有独立完整起卦取数及本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_2_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=89 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=128

    # 《梅花易数》卷4“梦腹上生松”，仅以松为十八公断幽州刺史，未载梅花起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=14 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=154

    # 《梅花易数》卷4“黄头小人”，仅以黄头小人合恭的字理解释，未载梅花起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=14 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=154

    # 《梅花易数》卷4“十四心口在天上”，以十四心合德、口在天上合吴等字理解释，未载梅花起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=14 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=154

    # 《梅花易数》卷4“入女安乐与君王五月”，以人女为吉造、两角女子为安乐、君王一止之月为正月等字理解释，未载梅花起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=14 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=154

    # 《梅花易数》卷4“字画经验”，以数、家、刑、砚、典及后页各字的字形取象，未载用于本变卦计算的完整取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=16 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=155

    # 《梅花易数》卷4“象人天字”，天字分别对秀才、官员、庶人释未与来等字理；未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=27 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=164

    # 《梅花易数》卷4“立字遇雨与言字遇犬”，立加雨为泣、言见犬为狱，据此外应断病讼，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=28 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=165

    # 《梅花易数》卷4“牛字春夏秋冬”，按牛劳苦及季节释春夏劳苦秋冬安逸，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=29 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=166

    # 《梅花易数》卷4“楼字问行人”，楼取重屋而拆千里尸至，以此断行人死外，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=29 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=166

    # 《梅花易数》卷4“官员尹字与君字”，尹添口为君、君无口为尹，以此断禄位，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=29 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=166

    # 《梅花易数》卷4“诸字减两旁”，诸中言写得好则减两部而言吉，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=30 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=167

    # 《梅花易数》卷4“吉字上土与常字变宀”，按书写上土及常头写作宀断病，未载用于本变卦计算的起卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=30 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=167

    # 《梅花易数》卷4“宀家头破与山缺笔”，按宀缺笔为破家宅、山缺笔为悬针山断凶，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=30 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=167

    # 《梅花易数》卷4“幸字行人日期”，幸字取六七日或六十一日等字形拆解日期，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=31 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=168

    # 《梅花易数》卷4“谋字求谋”，谋字写相粘取二十四五前成，以隔字体释之，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=33 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=170

    # 《梅花易数》卷4“喜庆星反体”，喜含舌脚、庆含忧脚、日在星上等字理，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=35 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=172

    # 《梅花易数》卷4“玄黄笔法歌偏旁演例”，就走之、子系、阝邑旁和点画等字形断事，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=38 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=175

    # 《梅花易数》卷4“玄黄笔法歌续例”，就之、弓、完、山、呂等字形断事，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=39 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=176

    # 《梅花易数》卷4“玄黄笔法歌户礼元骨身”，就户礼元骨身等字形断事，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=39 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=177

    # 《梅花易数》卷4“假如车字与幸字”，以车直笔强健为甲木、幸上一立下一短为乙木，输出五行归属，未载本变卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=45 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=182

    # 《梅花易数》卷4“假如虚字与从字”，虚撇长取丙火、从撇短取丁火，输出五行归属，未载本变卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=46 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=183

    # 《梅花易数》卷4“假如聿字与求字”，聿第一画长及末后一画长按阳土、求点可作己土论，输出五行归属，未载本变卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=47 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=185

    # 《梅花易数》卷4“假如喜字与抓字”，喜两口取庚申阳金、抓挑捺取辛酉阴金，输出五行归属，未载本变卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=49 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=186

    # 《梅花易数》卷4“假如文字月字景字”，文点在上为癸水、月腹点为子水、景中点为亥水下点为壬水，输出五行归属，未载本变卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=51 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=187

    # 《梅花易数》卷5“比例歌斗字”，以斗为事不差，无心书鬼为状元家，功名第二与为政按字理判断，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=59 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=197

    # 《梅花易数》卷5“比例歌死字”，以死字登科作探花按字理判断，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=59 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=197

    # 《梅花易数》卷5“比例歌才字”，辰时书才、正午书言、水旁书牛分别按字理判断，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=60 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=197

    # 《梅花易数》卷5“比例歌进字与申字”，进书八土能成照、申更不乱推联捷、数进三一为贡等按字理判断，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=60 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=198

    # 《梅花易数》卷5“比例歌读字与余字”，二人同到读书余释徐问，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=60 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=198

    # 《梅花易数》卷5“比例歌失字与执字”，失执金判铁，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=60 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=198

    # 《梅花易数》卷5“赤黑二马入河”，只载演得离卦，以火未然烟先发断黑马先起；未载起卦取数、动爻或变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=61 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=198

    # 《梅花易数》卷5“断扇占”，只载扇面落地，子断骨肉分离、淳风断穿衣见父脱衣见夫；未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=61 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=198

    # 《梅花易数》卷5“买香占”，按原载酉10、八月8、二十五日25、午7起卦，原合数43、50，睽二变噬嗑。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=61 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=199

    def test_买香(self):
        输出 = 运行("梅花易数.py", "10 8 25 7\n")
        self.assertIn("䷥ 火泽睽\n\t变卦为：䷔ 火雷噬嗑", 输出)

    # 《梅花易数》卷5“谢石相高宗二字”，二字添土为王，另问字按两君形象识主上，未载用于梅花本变卦计算的起卦取数。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=62 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=200

    # 《梅花易数》卷5“谢石相春字”，高宗写春，以秦头太重压日无光解释，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=63 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=200

    # 《梅花易数》卷5“谢石女子相谢皮仙字”，谢释寸言中立身、皮逢石为破、人在山旁为仙，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=63 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=200

    # 《梅花易数》卷5“张乘槎相来远楼”，来远楼初揭匾，以丰字、山为墓、二手为手上树、豆为祭器等字理断王恩死，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=63 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=200

    # 《梅花易数》卷5“延槎相德字”，德字以双立人为行人、十四为归期、一心为必来，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=64 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=201

    # 《梅花易数》卷5“裴晋公征吴元济石字”，鸡未肥、酒未熟释无肉为己、无水为酉，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=64 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=201

    # 《梅花易数》卷5“广明元年黄氏谶字”，左足踏日右足踏月合黄姓造谶，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=64 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=201

    # 《梅花易数》卷5“太平与国相字”，太平拆一人六十，以此断太宗六十寿，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=65 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=201

    # 《梅花易数》卷5“周侍翰桃符联语”，门无公事年俸卒于官、家有阴功子孙多等按联语前三字相之，未载梅花起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=65 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=201

    # 《梅花易数》卷5“相字寿数法”，列两笔、有撇无撇、常变、无勾添九、无直减十等寿数规则，未载一例具体完整字形、命属与最终寿数，亦不输出本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=78 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=214

    # 《梅花易数》卷5“占字笔数管岁法”，列十笔以上笔管六岁、十笔以下管九岁、五笔内管十六年及十五二笔折一，未载一例具体笔形及最终寿数，亦不输出本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=84 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=218

    # 《梅花易数》卷5“假如子字求子蓄女字婚姻”，按日建、笔画单双与子字或蓄女字字义断求子和婚姻，未载起卦取数、本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=85 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=219

    # 《梅花易数》卷5“假如青龙白虎父母子孙”，依功名、庶人、占墓、游子不同问事释六神与用神组合，未载具体字形、起卦取数或本变卦。 https://commons.wikimedia.org/wiki/File:CNTS-00047981941_3_新刻增定邵康節先生梅花觀梅折字數全集._卷1-5-_邵雍(宋)_著.pdf?page=91 https://upload.wikimedia.org/wikipedia/commons/a/af/NLC416-12jh005426-44577_%E6%A2%85%E8%8A%B1%E6%98%93%E6%95%B8.pdf#page=224
