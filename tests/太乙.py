import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《太乙金钥匙》本卷成化乙巳年积10155402，仅记纪年，以1485年中代表该岁检验积年，不指占日 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkvlnkx7u

    def test_成化乙巳太乙积年(self):
        输出 = 运行("太乙.py", "1\n1485 07 01\n")
        self.assertIn("岁计：积10155402", 输出)

    # 《太乙金钥匙》本卷临津问道假例仅记起兵干支年，破年、破月、破日、破时及卦运、大游、小游不属当前四计输出 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkvlnkx7u

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

    # 《太乙金钥匙》续集末另用193万上元；明抄影像52、53亦记23257410周余30及707887076余56，实余330、356，影像原数的除余有误，古日锚点亦差2 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8

    # 《太乙金钥匙》岁计未明确换岁时刻，月计仅载天地二正次序；现公历年及大雪换月口径在岁界处尚缺历史例验证 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8

    # 《太乙金镜式经》卷一四库第七叶下确记月法2447，与朔策、小余、日法推数未合，该扫描原数与起例推数不合 https://www.shidianguji.com/zh/book/SK1615/chapter/1l9lir71os7ce

    # 《太乙金镜式经》卷一梁天监三年六月八日积707501061、太乙八宫和德；四库影像第八叶上核字，儒略7月5日即本脚本公历7月7日 https://www.shidianguji.com/zh/book/SK1615/chapter/1l9lir71os7ce

    def test_梁天监三年太乙日计(self):
        输出 = 运行("太乙.py", "3\n2\n504 07 07\n")
        self.assertIn("庚子元第45局", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：和德（艮）", 输出)

    # 《太乙金镜式经》卷一开元十八年含元殿问答未给占时课盘，四库扫描第1册48～49页 https://commons.wikimedia.org/wiki/File:SSID-12326977_太乙金鏡式經_1.pdf?page=48

    # 《太乙金镜式经》卷一推太乙当时法，四库扫描第1册56～57页，十月五日庚申、戊寅时假例阴遁27局，以2026-07-15寅时代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326977_太乙金鏡式經_1.pdf?page=56

    def test_太乙当时阴局假例(self):
        输出 = 运行("太乙.py", "4\n2026 07 15 03\n")
        self.assertIn("第6纪，壬子元第27局，阴遁", 输出)
        self.assertIn("太乙：巽9宫", 输出)
        self.assertIn("文昌：大武（坤），计神：午，始击：高丛（卯）", 输出)
        self.assertIn("主算：29，主大将：9宫，主参将：7宫", 输出)
        self.assertIn("客算：4，客大将：4宫，客参将：2宫", 输出)

    # 《太乙金镜式经》卷二帝王纪年、卷三阴阳七十二局立成表，四库扫描第1册84～87、106～125页 https://commons.wikimedia.org/wiki/File:SSID-12326977_太乙金鏡式經_1.pdf?page=84

    # 《太乙金镜式经》卷三阳39主25、阳50主6，四库扫描111、112页同，按投算起例应35、16；该本立成表与起例不合 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=111

    # 《太乙金镜式经》卷三阴11客36、阴15客29、阴25主21、阴26主31、阴27主39，四库扫描117至119页同；与起例推数不合 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=117

    # 《太乙金镜式经》卷三阴37客目大威、阴43大武38、阴44太簇31，四库扫描120、121页同；按计神加和德应大武25、大神1、大武38；该本立成表与起例不合 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=120

    # 《太乙金镜式经》卷三阴46客算一、阴70主算三十二，四库扫描121、124页 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=121

    # 《太乙金镜式经》卷四假令以门、天目地目或主客算为输入，所得三门、胜负、出师向背及阵法不属当前四计输出，四库扫描第1册128～143页 https://commons.wikimedia.org/wiki/File:SSID-12326977_太乙金鏡式經_1.pdf?page=128

    # 《太乙金镜式经》卷五基福、大游、小游不属当前四计模块，四库扫描第2册4～15页 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=4

    # 《太乙金镜式经》卷六临津问道、狮子反掷假例所得破年月日时未实现；白云卷空四库扫描第2册37页确作第二局，所列武德、寅、主7客13却属第一局，原例局号与课盘不合 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=37

    # 《太乙金镜式经》卷六猛虎相拒假例阳遁7局，四库扫描第2册38页，以504-10-21古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=38

    def test_猛虎相拒假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 10 21\n")
        self.assertIn("第1纪，甲子元第7局，阳遁", 输出)
        self.assertIn("太乙：艮3宫", 输出)

    # 《太乙金镜式经》卷六雷公入水假例阳遁13局，四库扫描第2册39页，以504-10-27古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=39

    def test_雷公入水假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 10 27\n")
        self.assertIn("第1纪，甲子元第13局，阳遁", 输出)
        self.assertIn("太乙：兑6宫", 输出)
        self.assertIn("文昌：太炅（巽），计神：寅，始击：太阳（辰）", 输出)
        self.assertIn("主算：18，主大将：8宫，主参将：4宫", 输出)
        self.assertIn("客算：19，客大将：9宫，客参将：7宫", 输出)

    # 《太乙金镜式经》卷六白龙得云假例阳遁22局，四库扫描第2册40～41页，以504-11-05古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=40

    def test_白龙得云假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 11 05\n")
        self.assertIn("第1纪，甲子元第22局，阳遁", 输出)
        self.assertIn("太乙：巽9宫", 输出)
        self.assertIn("文昌：阴德（乾），计神：巳，始击：天道（未）", 输出)
        self.assertIn("主算：16，主大将：6宫，主参将：8宫", 输出)
        self.assertIn("客算：30，客大将：3宫，客参将：9宫", 输出)

    # 《太乙金镜式经》卷六回军无言假例阳遁28局，四库扫描第2册42页，以504-11-11古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=42

    def test_回军无言假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 11 11\n")
        self.assertIn("第1纪，甲子元第28局，阳遁", 输出)
        self.assertIn("太乙：离2宫", 输出)
        self.assertIn("文昌：吕申（寅），计神：亥，始击：太炅（巽）", 输出)
        self.assertIn("主算：14，主大将：4宫，主参将：2宫", 输出)
        self.assertIn("客算：9，客大将：9宫，客参将：7宫", 输出)

    # 《太乙金镜式经》卷七景祐元年积10154950，比本脚本金钥匙岁计少1，缺该积年算内外及上元换算起例，四库扫描第2册50页 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=50

    # 《太乙金镜式经》卷七十精、阳九百六及卷八分野未实现，四库扫描第2册50～66、68～77页 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=50

    # 《太乙金镜式经》卷九敌国动静假例阴遁52局，四库扫描第2册92页，以2026-06-29卯时代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=92

    def test_敌国动静假例(self):
        输出 = 运行("太乙.py", "4\n2026 06 29 05\n")
        self.assertIn("第3纪，丙子元第52局，阴遁", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：阳德（丑），计神：巳，始击：太簇（酉）", 输出)
        self.assertIn("客算：7，客大将：7宫，客参将：1宫", 输出)

    # 《太乙金镜式经》卷九敌使言虚实假例阳遁25局，四库扫描第2册93页，以504-11-08古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=93

    def test_敌使言虚实假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 11 08\n")
        self.assertIn("第1纪，甲子元第25局，阳遁", 输出)
        self.assertIn("太乙：乾1宫", 输出)
        self.assertIn("文昌：地主（子），计神：寅，始击：大义（亥）", 输出)
        self.assertIn("客算：40，客大将：4宫，客参将：2宫", 输出)

    # 《太乙金镜式经》卷九敌国有无间谍假例阳遁2局，四库扫描第2册94页，以504-10-16古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=94

    def test_敌国有无间谍假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 10 16\n")
        self.assertIn("第1纪，甲子元第2局，阳遁", 输出)
        self.assertIn("太乙：乾1宫", 输出)
        self.assertIn("文昌：太簇（酉），计神：丑，始击：阴主（戌）", 输出)
        self.assertIn("客算：1，客大将：1宫", 输出)

    # 《太乙金镜式经》卷九敌来方面假例阳遁8局，四库扫描第2册95～96页，以504-10-22古日计代表相同纪元局式 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=95

    def test_敌来方面假例(self):
        输出 = 运行("太乙.py", "3\n2\n504 10 22\n")
        self.assertIn("第1纪，甲子元第8局，阳遁", 输出)
        self.assertIn("太乙：艮3宫", 输出)
        self.assertIn("文昌：阳德（丑），计神：未，始击：大武（坤）", 输出)
        self.assertIn("客算：22", 输出)

    # 《太乙金镜式经》卷十假例所得巡狩方向、灾月及域名厄会年不属当前四计输出，四库扫描第2册106～114页 https://commons.wikimedia.org/wiki/File:SSID-12326978_太乙金鏡式經_2.pdf?page=106
