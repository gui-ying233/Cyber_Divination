import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《太乙金钥匙》本卷成化乙巳年积10155402，仅记纪年，以1485年中代表该岁检验积年，不指占日 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkvlnkx7u

    def test_成化乙巳太乙积年(self):
        输出 = 运行("太乙.py", "1\n1485 07 01\n")
        self.assertIn("岁计：积10155402", 输出)

    # 《太乙金钥匙》本卷临津问道起兵例明称“似如”，卦运、大游、小游等亦不属当前四计输出 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkvlnkx7u

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

    # 《太乙金镜式经》卷一梁天监三年六月八日积707501061、太乙八宫和德；四库影像第八叶上核字，儒略7月5日即本脚本公历7月7日 https://www.shidianguji.com/zh/book/SK1615/chapter/1l9lir71os7ce https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷01

    def test_梁天监三年太乙日计(self):
        输出 = 运行("太乙.py", "3\n2\n504 07 07\n")
        self.assertIn("庚子元第45局", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：和德（艮）", 输出)

    # 《太乙金镜式经》卷一开元十八年含元殿问答未给占时课盘，十月五日庚申例明称“假” https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷01

    # 《太乙金镜式经》卷二帝王纪年及卷三阴阳七十二局是立成表， https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷02 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷03

    # 《太乙金镜式经》卷三阳39主25、阳50主6，四库扫描111、112页同，按投算起例应35、16；该本立成表与起例不合 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=111

    # 《太乙金镜式经》卷三阴11客36、阴15客29、阴25主21、阴26主31、阴27主39，四库扫描117至119页同；与起例推数不合 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=117

    # 《太乙金镜式经》卷三阴37客目大威、阴43大武38、阴44太簇31，四库扫描120、121页同；按计神加和德应大武25、大神1、大武38；该本立成表与起例不合 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=120

    # 《太乙金镜式经》卷三阴46客算一、阴70主算三十二，四库扫描121、124页明确如此，电子表误录二、二十二，代码按原起例相符 https://commons.wikimedia.org/wiki/File:CADAL06056494_太乙金鏡式經·卷一~卷四.djvu?page=121

    # 《太乙金镜式经》卷四三门、主客、出师等是术式条文及假令，不是具年实占记录 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷04

    # 《太乙金镜式经》卷五基福、大游、小游不属当前四计模块 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷05

    # 《太乙金镜式经》卷六将兵课式以“假令”设例，未记具体实占年日 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷06

    # 《太乙金镜式经》卷七景祐元年积10154950，比本脚本金钥匙岁计少1，缺该积年算内外及上元换算起例 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷07

    # 《太乙金镜式经》卷七十精、阳九百六及卷八分野未实现，卷九、十“假令”课式亦非具年实占 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷07 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷08 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷09 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷10
