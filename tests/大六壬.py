import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《六壬断案》韩太守祈雪，《断案新编》现代书影第10页（印002）题己酉十一月初四己卯寅将；该日为戊申丑将，十月初四才是己卯寅将 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=10

    # 《六壬断案》元集天时十二月戊申子将申时占晴雨，书影题目及断语均未载占年 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=13

    # 《六壬断案》元集天时浙江大旱，九月十五癸丑日辰将辰时，未载占年，未取得对应书影 https://daizhige.org/易藏/术数/六壬断案.html

    # 《六壬断案》元集宅墓第1案张九翁占宅，《断案新编》PDF16 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=16
    def test_张九翁占宅(self):
        输出 = 运行("大六壬.py", "1128 10 11 13\n1\n1\n")
        self.assertIn("庚寅日，天罡辰将加未时", 输出)
        self.assertIn("初传：巳 勾陈 官鬼", 输出)
        self.assertIn("中传：寅 螣蛇 妻财", 输出)
        self.assertIn("末传：亥 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第2案叶助教占宅，《断案新编》PDF19 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=19
    def test_叶助教占宅(self):
        输出 = 运行("大六壬.py", "1128 02 15 13\n1\n1\n")
        self.assertIn("辛卯日，神后子将加未时", 输出)
        self.assertIn("初传：卯 玄武 妻财", 输出)
        self.assertIn("中传：申 朱雀 兄弟", 输出)
        self.assertIn("末传：丑 白虎 父母", 输出)

    # 《六壬断案》元集宅墓第3案邵三翁占宅，《断案新编》PDF22 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=22
    def test_邵三翁占宅(self):
        输出 = 运行("大六壬.py", "1128 10 02 21\n1\n1\n")
        self.assertIn("辛巳日，天罡辰将加亥时", 输出)
        self.assertIn("初传：卯 天后 妻财", 输出)
        self.assertIn("中传：申 天空 兄弟", 输出)
        self.assertIn("末传：丑 螣蛇 父母", 输出)

    # 《六壬断案》邵秀才，《断案新编》现代书影第25页（印032）题己酉二月乙巳戌将亥时，年日与戌将不合；先干不重位取辰卯寅 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=25

    # 《六壬断案》元集宅墓第5案邵巡检占宅，《断案新编》PDF28 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=28
    def test_邵巡检占宅(self):
        输出 = 运行("大六壬.py", "1128 08 02 03\n1\n1\n")
        self.assertIn("庚辰日，胜光午将加寅时", 输出)
        self.assertIn("初传：辰 玄武 父母", 输出)
        self.assertIn("中传：申 螣蛇 兄弟", 输出)
        self.assertIn("末传：子 青龙 子孙", 输出)

    # 《六壬断案》元集宅墓第6案任三翁占宅，《断案新编》PDF31 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=31
    def test_任三翁占宅(self):
        输出 = 运行("大六壬.py", "1128 12 22 15\n1\n1\n")
        self.assertIn("壬寅日，大吉丑将加申时", 输出)
        self.assertIn("初传：子 白虎 兄弟", 输出)
        self.assertIn("中传：巳 贵人 妻财", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)

    # 《六壬断案》元集宅墓第7案邵伯达占宅基，《断案新编》PDF34 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=34
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

    # 《六壬断案》元集郑宣义占宅，书影只载八月癸丑巳将丑时；辛亥造酒房和己酉交易不能唯一确定占年 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=40

    # 《六壬断案》元集宅墓第10案王德卿占宅，《断案新编》PDF43 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=43
    def test_王德卿占宅(self):
        输出 = 运行("大六壬.py", "1128 11 02 05\n1\n1\n")
        self.assertIn("壬子日，太冲卯将加卯时", 输出)
        self.assertIn("初传：亥 天空 兄弟", 输出)
        self.assertIn("中传：子 青龙 兄弟", 输出)
        self.assertIn("末传：卯 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第11案童得松占宅，《断案新编》PDF46 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=46
    def test_童得松占宅(self):
        输出 = 运行("大六壬.py", "1129 07 10 01\n1\n1\n")
        self.assertIn("壬戌日，小吉未将加丑时", 输出)
        self.assertIn("初传：巳 太阴 妻财", 输出)
        self.assertIn("中传：亥 勾陈 兄弟", 输出)
        self.assertIn("末传：巳 太阴 妻财", 输出)

    # 《六壬断案》元集宅墓第12案徐八公据夜贵版和“卯子息爻乘夜贵”断语核对；另本天将作昼贵，儒略历七月九日为本脚本公历七月十六日 https://shuyuan.zhiming.life/read/大六壬断案(亨集)/9 https://tianyugong.com/liurenduanan/ 《断案新编》PDF49为昼贵图 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=49
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

    # 《六壬断案》元集刘将仕占宅，《断案新编》PDF52原注六月朔未交小暑，故以五月论 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=52
    def test_刘将仕占宅(self):
        输出 = 运行("大六壬.py", "1129 06 26 05\n1\n1\n")
        self.assertIn("戊申日，小吉未将加卯时", 输出)
        self.assertIn("初传：辰 玄武 兄弟", 输出)
        self.assertIn("中传：申 青龙 子孙", 输出)
        self.assertIn("末传：子 螣蛇 妻财", 输出)

    # 《六壬断案》元集宅墓第14案；《断案新编》现代书影第55页（印092）记己酉二月戊子戌将巳时，古历平气清明当日傍晚交节，巳时仍为二月节月 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=55
    def test_何丞务占宅(self):
        输出 = 运行("大六壬.py", "1129 04 07 09\n1\n1\n")
        self.assertIn("戊子日，河魁戌将加巳时", 输出)
        self.assertIn("初传：巳 太常 父母", 输出)
        self.assertIn("中传：戌 六合 兄弟", 输出)
        self.assertIn("末传：卯 太阴 官鬼", 输出)

    # 《六壬断案》元集宅墓第15案任太公占宅，《断案新编》PDF58 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=58
    def test_任太公占宅(self):
        输出 = 运行("大六壬.py", "1128 02 10 07\n1\n1\n")
        self.assertIn("丙戌日，神后子将加辰时", 输出)
        self.assertIn("初传：酉 太阴 妻财", 输出)
        self.assertIn("中传：巳 天空 兄弟", 输出)
        self.assertIn("末传：丑 朱雀 子孙", 输出)

    # 《六壬断案》元集宅墓第16案王解元占宅，《断案新编》PDF61 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=61
    def test_王解元占宅(self):
        输出 = 运行("大六壬.py", "1129 04 12 13\n1\n1\n")
        self.assertIn("癸巳日，河魁戌将加未时", 输出)
        self.assertIn("初传：申 六合 父母", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：寅 玄武 子孙", 输出)

    # 《六壬断案》元集宅墓第17案何宣义占宅，《断案新编》PDF64 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=64
    def test_何宣义占宅(self):
        输出 = 运行("大六壬.py", "1129 04 12 17\n1\n1\n")
        self.assertIn("癸巳日，河魁戌将加酉时", 输出)
        self.assertIn("初传：未 勾陈 官鬼", 输出)
        self.assertIn("中传：申 青龙 父母", 输出)
        self.assertIn("末传：酉 天空 父母", 输出)

    # 《六壬断案》元集林承务占宅，《断案新编》PDF67记辛卯午将辰时，末传酉乘六合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=67
    def test_林承务占宅(self):
        输出 = 运行("大六壬.py", "1129 08 08 07\n1\n1\n")
        self.assertIn("辛卯日，胜光午将加辰时", 输出)
        self.assertIn("初传：巳 天后 官鬼", 输出)
        self.assertIn("中传：未 螣蛇 父母", 输出)
        self.assertIn("末传：酉 六合 兄弟", 输出)

    # 《六壬断案》元集宅墓第19案冯修职占宅，《断案新编》PDF70 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=70
    def test_冯修职占宅(self):
        输出 = 运行("大六壬.py", "1128 06 08 05\n1\n1\n")
        self.assertIn("乙酉日，传送申将加卯时", 输出)
        self.assertIn("初传：未 青龙 妻财", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：巳 白虎 子孙", 输出)

    # 《六壬断案》元集宅墓第20案叶油饼店主占宅，《断案新编》PDF73 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=73
    def test_叶油饼店主占宅(self):
        输出 = 运行("大六壬.py", "1128 07 21 17\n1\n1\n")
        self.assertIn("戊辰日，小吉未将加酉时", 输出)
        self.assertIn("初传：丑 天空 兄弟", 输出)
        self.assertIn("中传：亥 太常 妻财", 输出)
        self.assertIn("末传：酉 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第21案童秀才，清抄公开书影第26幅明确戊申三月十一乙未戌将丑时，与课图相合，不需反推占时 https://www.yeshuxiang.com/72732.html
    def test_童秀才占宅(self):
        输出 = 运行("大六壬.py", "1128 04 19 02\n1\n1\n")
        self.assertIn("乙未日，河魁戌将加丑时", 输出)
        self.assertIn("初传：丑 青龙 妻财", 输出)
        self.assertIn("中传：戌 朱雀 妻财", 输出)
        self.assertIn("末传：未 天后 妻财", 输出)

    # 《六壬断案》元集宅墓第22案何七秀才占宅，《断案新编》PDF79 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=79
    def test_何七秀才占宅(self):
        输出 = 运行("大六壬.py", "1128 03 19 11\n1\n1\n")
        self.assertIn("甲子日，登明亥将加午时", 输出)
        self.assertIn("初传：子 螣蛇 父母", 输出)
        self.assertIn("中传：巳 太常 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》元集宅墓第23案某占家宅，《断案新编》PDF82 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=82
    def test_某占家宅(self):
        输出 = 运行("大六壬.py", "1128 10 05 21\n1\n1\n")
        self.assertIn("甲申日，天罡辰将加亥时", 输出)
        self.assertIn("初传：子 青龙 父母", 输出)
        self.assertIn("中传：巳 太阴 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》郁氏女，《断案新编》现代书影第85页（印152）完整作申将戌时；丙辰1076五月初八为癸亥，且该年无丁亥申将 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=85

    # 《六壬断案》元集宅墓第25案邵三公占宅，《断案新编》PDF88 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=88
    def test_邵三公占宅(self):
        输出 = 运行("大六壬.py", "1129 01 31 00\n1\n1\n")
        self.assertIn("壬午日，神后子将加子时", 输出)
        self.assertIn("初传：亥 太常 兄弟", 输出)
        self.assertIn("中传：午 六合 妻财", 输出)
        self.assertIn("末传：子 玄武 兄弟", 输出)

    # 《六壬断案》元集江文老占宅，书影只载七月十五丁酉午将辰时；依弁言邵氏1065～1133年生卒范围日历唯一得1128-08-19，占年为反推 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=91
    # def test_江文老占家宅(self):
    #     输出 = 运行("大六壬.py", "1128 08 19 07\n1\n1\n")
    #     self.assertIn("丁酉日，胜光午将加辰时", 输出)
    #     self.assertIn("初传：酉 朱雀 妻财", 输出)
    #     self.assertIn("中传：亥 贵人 官鬼", 输出)
    #     self.assertIn("末传：丑 太阴 子孙", 输出)

    # 《六壬断案》元集宅墓第27案徐大夫占宅，《断案新编》PDF94 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=94
    def test_徐大夫占宅(self):
        输出 = 运行("大六壬.py", "1128 02 10 13\n1\n1\n")
        self.assertIn("丙戌日，神后子将加未时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：丑 太阴 子孙", 输出)
        self.assertIn("末传：午 青龙 兄弟", 输出)

    # 《六壬断案》元集宅墓第28案郭德占家宅，《断案新编》PDF97 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=97
    def test_郭德占家宅(self):
        输出 = 运行("大六壬.py", "1129 07 02 11\n1\n1\n")
        self.assertIn("甲寅日，小吉未将加午时", 输出)
        self.assertIn("初传：辰 六合 妻财", 输出)
        self.assertIn("中传：巳 勾陈 子孙", 输出)
        self.assertIn("末传：午 青龙 子孙", 输出)

    # 《六壬断案》元集宅墓第29案叶助教占家宅，《断案新编》PDF100 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=100
    def test_叶助教占家宅(self):
        输出 = 运行("大六壬.py", "1129 03 03 11\n1\n1\n")
        self.assertIn("癸丑日，登明亥将加午时", 输出)
        self.assertIn("初传：午 螣蛇 妻财", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：辰 天后 官鬼", 输出)

    # 《六壬断案》元集宅墓第30案童三十四公占宅，《断案新编》PDF103 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=103
    def test_童三十四公占宅(self):
        输出 = 运行("大六壬.py", "1129 08 25 05\n1\n1\n")
        self.assertIn("戊申日，太乙巳将加卯时", 输出)
        self.assertIn("初传：子 天后 妻财", 输出)
        self.assertIn("中传：寅 螣蛇 官鬼", 输出)
        self.assertIn("末传：辰 六合 兄弟", 输出)

    # 《六壬断案》元集汪四六公占宅，《断案新编》PDF106记己酉壬午日辰将申时 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=106
    def test_汪四六公占宅(self):
        输出 = 运行("大六壬.py", "1129 09 28 15\n1\n1\n")
        self.assertIn("壬午日，天罡辰将加申时", 输出)
        self.assertIn("初传：戌 白虎 官鬼", 输出)
        self.assertIn("中传：午 天后 妻财", 输出)
        self.assertIn("末传：寅 六合 子孙", 输出)

    # 《六壬断案》元集伊伯廷；《断案新编》现代书影第109页（印200）記己酉丙午卯将申时，按古历气法取卯将 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=109
    def test_伊伯廷占宅(self):
        输出 = 运行("大六壬.py", "1129 10 22 15\n2\n1\n1\n")
        self.assertIn("丙午日，太冲卯将加申时", 输出)
        self.assertIn("初传：子 螣蛇 官鬼", 输出)
        self.assertIn("中传：未 太常 子孙", 输出)
        self.assertIn("末传：寅 六合 父母", 输出)

    # 《六壬断案》元集正月丁卯子将卯时占宅，书影题目及断语均未载占年 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=112

    # 《六壬断案》元集汪解元占宅基，书影补全己酉二月朔庚戌亥将酉时，图酉时用昼贵 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=115
    def test_汪解元占宅基(self):
        输出 = 运行("大六壬.py", "1129 02 28 17\n1\n2\n")
        self.assertIn("庚戌日，登明亥将加酉时", 输出)
        self.assertIn("初传：子 天后 子孙", 输出)
        self.assertIn("中传：寅 螣蛇 妻财", 输出)
        self.assertIn("末传：辰 六合 父母", 输出)
        self.assertIn("一课：庚上戌，玄武", 输出)
        self.assertIn("二课：戌上子，天后", 输出)
        self.assertIn("三课：戌上子，天后", 输出)
        self.assertIn("四课：子上寅，螣蛇", 输出)

    # 《六壬断案》元集癸酉巳将申时占宅，书影题目及断语均未载占年 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=118

    # 《六壬断案》元集正月己巳占宅，书影题午将酉时而课图为子加酉；占年未载 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=121

    # 《六壬断案》元集郑三公；《断案新编》现代书影第124页（印230）记己酉正月二十三壬寅子将寅时，按古历气法取子将 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=124
    def test_郑三公占坟地(self):
        输出 = 运行("大六壬.py", "1129 02 20 03\n2\n1\n1\n")
        self.assertIn("壬寅日，神后子将加寅时", 输出)
        self.assertIn("初传：戌 青龙 官鬼", 输出)
        self.assertIn("中传：申 白虎 父母", 输出)
        self.assertIn("末传：午 玄武 妻财", 输出)

    # 《六壬断案》元集徐承务；《断案新编》现代书影第127页（印236）记己酉九月癸卯辰将卯时，九月按节月成立，图用夜贵；孟子翔引录本第97页另排昼贵 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=127
    def test_徐承务占坟地(self):
        输出 = 运行("大六壬.py", "1129 10 19 05\n1\n3\n")
        self.assertIn("癸卯日，天罡辰将加卯时", 输出)
        self.assertIn("初传：辰 螣蛇 官鬼", 输出)
        self.assertIn("中传：巳 朱雀 妻财", 输出)
        self.assertIn("末传：午 六合 妻财", 输出)

    # 《六壬断案》元集刘秘教占宅，六月初一戊申日与第13案同日，课图可独立复盘，《断案新编》PDF130 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=130
    def test_刘秘教占宅(self):
        输出 = 运行("大六壬.py", "1129 06 26 17\n1\n1\n")
        self.assertIn("戊申日，小吉未将加酉时", 输出)
        self.assertIn("初传：丑 天空 兄弟", 输出)
        self.assertIn("中传：亥 太常 妻财", 输出)
        self.assertIn("末传：酉 太阴 子孙", 输出)

    # 《六壬断案》元集郭仲起；《断案新编》现代书影第133页（印248）明确未将寅时，与课图相合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C/%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=133
    def test_郭仲起占宅(self):
        输出 = 运行("大六壬.py", "1129 07 02 03\n1\n1\n")
        self.assertIn("甲寅日，小吉未将加寅时", 输出)
        self.assertIn("初传：子 青龙 父母", 输出)
        self.assertIn("中传：巳 太阴 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)

    # 《六壬断案》亨集应贡元占前程，《断案新编》PDF136 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=136
    def test_应贡元占前程(self):
        输出 = 运行("大六壬.py", "1128 07 30 13\n1\n1\n")
        self.assertIn("丁丑日，胜光午将加未时", 输出)
        self.assertIn("初传：子 螣蛇 官鬼", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：戌 天后 子孙", 输出)
        self.assertIn("一课：丁上午，白虎", 输出)
        self.assertIn("二课：午上巳，天空", 输出)
        self.assertIn("三课：丑上子，螣蛇", 输出)
        self.assertIn("四课：子上亥，贵人", 输出)

    # 《六壬断案》亨集何秀才占应试，《断案新编》PDF139 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=139
    def test_何秀才占应试(self):
        输出 = 运行("大六壬.py", "1129 01 29 17\n1\n1\n")
        self.assertIn("庚辰日，神后子将加酉时", 输出)
        self.assertIn("初传：寅 白虎 妻财", 输出)
        self.assertIn("中传：巳 太阴 官鬼", 输出)
        self.assertIn("末传：申 螣蛇 兄弟", 输出)
        self.assertIn("一课：庚上亥，勾陈", 输出)
        self.assertIn("二课：亥上寅，白虎", 输出)
        self.assertIn("三课：辰上未，贵人", 输出)
        self.assertIn("四课：未上戌，六合", 输出)

    # 《六壬断案》亨集应秀才同课占前程，仅称与何秀才同课，程注又明言月将不同，未载该次年月日时；《断案新编》PDF142 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=142

    # 《六壬断案》亨集徐将仕占前程，《断案新编》PDF145 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=145
    def test_徐将仕占前程(self):
        输出 = 运行("大六壬.py", "1128 07 21 09\n1\n1\n")
        self.assertIn("戊辰日，小吉未将加巳时", 输出)
        self.assertIn("初传：申 白虎 子孙", 输出)
        self.assertIn("中传：戌 玄武 兄弟", 输出)
        self.assertIn("末传：子 天后 妻财", 输出)
        self.assertIn("一课：戊上未，天空", 输出)
        self.assertIn("二课：未上酉，太常", 输出)
        self.assertIn("三课：辰上午，青龙", 输出)
        self.assertIn("四课：午上申，白虎", 输出)

    # 《六壬断案》亨集徐教授占前程 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=148
    def test_徐教授占前程(self):
        输出 = 运行("大六壬.py", "1128 03 21 15\n2\n1\n1\n")
        self.assertIn("丙寅日，登明亥将加申时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：寅 玄武 父母", 输出)
        self.assertIn("一课：丙上申，六合", 输出)
        self.assertIn("二课：申上亥，贵人", 输出)
        self.assertIn("三课：寅上巳，天空", 输出)
        self.assertIn("四课：巳上申，六合", 输出)

    # 《六壬断案》亨集杨秀才占前程，《断案新编》PDF151 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=151
    def test_杨秀才占前程(self):
        输出 = 运行("大六壬.py", "1129 02 28 07\n1\n1\n")
        self.assertIn("庚戌日，登明亥将加辰时", 输出)
        self.assertIn("初传：戌 六合 父母", 输出)
        self.assertIn("中传：巳 太常 官鬼", 输出)
        self.assertIn("末传：子 螣蛇 子孙", 输出)
        self.assertIn("一课：庚上卯，太阴", 输出)
        self.assertIn("二课：卯上戌，六合", 输出)
        self.assertIn("三课：戌上巳，太常", 输出)
        self.assertIn("四课：巳上子，螣蛇", 输出)

    # 《六壬断案》亨集应秀才己卯日占前程，仅载己卯日、午将、丑时，未载占年；《断案新编》PDF154 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=154

    # 《六壬断案》亨集叶助教占前程，《精抄历代六壬占验汇选》卷2戊寅日原稿明载建炎己酉五月，公开书影第7页 https://d.zixueguoxue.com/2022/04/1650441050-f06417473b12f17.pdf#page=7
    def test_叶助教占前程(self):
        输出 = 运行("大六壬.py", "1129 05 27 13\n1\n1\n")
        self.assertIn("戊寅日，传送申将加未时", 输出)
        self.assertIn("初传：辰 六合 兄弟", 输出)
        self.assertIn("中传：巳 勾陈 父母", 输出)
        self.assertIn("末传：午 青龙 父母", 输出)
        self.assertIn("一课：戊上午，青龙", 输出)
        self.assertIn("二课：午上未，天空", 输出)
        self.assertIn("三课：寅上卯，朱雀", 输出)
        self.assertIn("四课：卯上辰，六合", 输出)

    # 《六壬断案》亨集伊秀才占科试，《断案新编》PDF160 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=160
    def test_伊秀才占科试(self):
        输出 = 运行("大六壬.py", "1128 07 16 09\n1\n1\n1\n1\n")
        self.assertIn("癸亥日，小吉未将加巳时", 输出)
        self.assertIn("初传：丑 太常 官鬼", 输出)
        self.assertIn("中传：卯 太阴 子孙", 输出)
        self.assertIn("末传：巳 贵人 妻财", 输出)
        self.assertIn("一课：癸上卯，太阴", 输出)
        self.assertIn("二课：卯上巳，贵人", 输出)
        self.assertIn("三课：亥上丑，太常", 输出)
        self.assertIn("四课：丑上卯，太阴", 输出)

    # 《六壬断案》亨集应寺簿占前程，《断案新编》PDF163 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=163
    def test_应寺簿占前程(self):
        输出 = 运行("大六壬.py", "1129 07 25 07\n1\n1\n")
        self.assertIn("丁丑日，胜光午将加辰时", 输出)
        self.assertIn("初传：酉 朱雀 妻财", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：丑 太阴 子孙", 输出)
        self.assertIn("一课：丁上酉，朱雀", 输出)
        self.assertIn("二课：酉上亥，贵人", 输出)
        self.assertIn("三课：丑上卯，太常", 输出)
        self.assertIn("四课：卯上巳，天空", 输出)

    # 《六壬断案》亨集占升迁，《精抄历代六壬占验汇选》卷2丙子日原稿冯知丞同课 https://img.xiandtang.com/i/2024/11/15/精抄历代六壬占验汇选_95.jpg
    def test_冯知丞占升迁(self):
        输出 = 运行("大六壬.py", "1129 11 21 01\n1\n1\n")
        self.assertIn("丙子日，太冲卯将加丑时", 输出)
        self.assertIn("初传：辰 青龙 子孙", 输出)
        self.assertIn("中传：午 六合 兄弟", 输出)
        self.assertIn("末传：申 螣蛇 妻财", 输出)
        self.assertIn("一课：丙上未，朱雀", 输出)
        self.assertIn("二课：未上酉，贵人", 输出)
        self.assertIn("三课：子上寅，白虎", 输出)
        self.assertIn("四课：寅上辰，青龙", 输出)

    # 《六壬断案》亨集赵将仕占武试, 十二月按节月，公历1129-01-29尚未交春，《断案新编》PDF169 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=169
    def test_赵将仕占武试(self):
        输出 = 运行("大六壬.py", "1129 01 29 00\n1\n1\n")
        self.assertIn("庚辰日，神后子将加子时", 输出)
        self.assertIn("初传：申 天后 兄弟", 输出)
        self.assertIn("中传：寅 青龙 妻财", 输出)
        self.assertIn("末传：巳 朱雀 官鬼", 输出)

    # 《六壬断案》亨集邹大官人占弓马，《断案新编》PDF172 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=172
    def test_邹大官人占弓马(self):
        输出 = 运行("大六壬.py", "1129 04 27 15\n1\n1\n")
        self.assertIn("戊申日，从魁酉将加申时", 输出)
        self.assertIn("初传：戌 玄武 兄弟", 输出)
        self.assertIn("中传：酉 太常 子孙", 输出)
        self.assertIn("末传：午 青龙 父母", 输出)
        self.assertIn("一课：戊上午，青龙", 输出)
        self.assertIn("二课：午上未，天空", 输出)
        self.assertIn("三课：申上酉，太常", 输出)
        self.assertIn("四课：酉上戌，玄武", 输出)

    # 《六壬断案》亨集龚县尉占前程，《断案新编》PDF175 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=175
    def test_龚县尉占前程(self):
        输出 = 运行("大六壬.py", "1129 11 27 03\n1\n1\n")
        self.assertIn("壬午日，功曹寅将加寅时", 输出)
        self.assertIn("初传：亥 太常 兄弟", 输出)
        self.assertIn("中传：午 六合 妻财", 输出)
        self.assertIn("末传：子 玄武 兄弟", 输出)
        self.assertIn("一课：壬上亥，太常", 输出)
        self.assertIn("二课：亥上亥，太常", 输出)
        self.assertIn("三课：午上午，六合", 输出)
        self.assertIn("四课：午上午，六合", 输出)

    # 《六壬断案》亨集郭巡辖占赴任，《断案新编》PDF178 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=178
    def test_郭巡辖占赴任(self):
        输出 = 运行("大六壬.py", "1129 04 27 00\n1\n1\n")
        self.assertIn("戊申日，从魁酉将加子时", 输出)
        self.assertIn("初传：寅 青龙 官鬼", 输出)
        self.assertIn("中传：亥 太常 妻财", 输出)
        self.assertIn("末传：申 天后 子孙", 输出)
        self.assertIn("一课：戊上寅，青龙", 输出)
        self.assertIn("二课：寅上亥，太常", 输出)
        self.assertIn("三课：申上巳，朱雀", 输出)
        self.assertIn("四课：巳上寅，青龙", 输出)

    # 《六壬断案》亨集徐学士占前程，《断案新编》PDF181 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=181
    def test_徐学士占前程(self):
        输出 = 运行("大六壬.py", "1128 03 19 09\n1\n1\n1\n")
        self.assertIn("甲子日，登明亥将加巳时", 输出)
        self.assertIn("初传：寅 天后 兄弟", 输出)
        self.assertIn("中传：申 青龙 官鬼", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)
        self.assertIn("一课：甲上申，青龙", 输出)
        self.assertIn("二课：申上寅，天后", 输出)
        self.assertIn("三课：子上午，白虎", 输出)
        self.assertIn("四课：午上子，螣蛇", 输出)

    # 《六壬断案》亨集谢省元占赴省试，《断案新编》PDF184 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=184
    def test_谢省元占赴省试(self):
        输出 = 运行("大六壬.py", "1129 11 09 03\n1\n1\n")
        self.assertIn("甲子日，太冲卯将加寅时", 输出)
        self.assertIn("初传：辰 六合 妻财", 输出)
        self.assertIn("中传：巳 朱雀 子孙", 输出)
        self.assertIn("末传：午 螣蛇 子孙", 输出)
        self.assertIn("一课：甲上卯，勾陈", 输出)
        self.assertIn("二课：卯上辰，六合", 输出)
        self.assertIn("三课：子上丑，天空", 输出)
        self.assertIn("四课：丑上寅，青龙", 输出)

    # 《六壬断案》亨集赵公占子国子监试，只载己酉辛巳子将亥时，1129-01-30与1130-01-25均可，未载占月；《断案新编》PDF187 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=187

    # 《六壬断案》亨集邵二十一公占孙前程，程注按年岁推戊申，未直载占年月日时，不能把前案公历日期移来；《断案新编》PDF190 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=190

    # 《六壬断案》亨集何知丞占赴任，《断案新编》PDF193 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=193
    def test_何知丞占赴任(self):
        输出 = 运行("大六壬.py", "1129 01 02 13\n1\n1\n")
        self.assertIn("癸丑日，大吉丑将加未时", 输出)
        self.assertIn("初传：未 朱雀 官鬼", 输出)
        self.assertIn("中传：丑 太常 官鬼", 输出)
        self.assertIn("末传：未 朱雀 官鬼", 输出)
        self.assertIn("一课：癸上未，朱雀", 输出)
        self.assertIn("二课：未上丑，太常", 输出)
        self.assertIn("三课：丑上未，朱雀", 输出)
        self.assertIn("四课：未上丑，太常", 输出)

    # 《六壬断案》亨集陈学谕占前程，《断案新编》PDF196 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=196
    def test_陈学谕占前程(self):
        输出 = 运行("大六壬.py", "1128 10 05 21\n1\n1\n")
        self.assertIn("甲申日，天罡辰将加亥时", 输出)
        self.assertIn("初传：子 青龙 父母", 输出)
        self.assertIn("中传：巳 太阴 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)
        self.assertIn("一课：甲上未，贵人", 输出)
        self.assertIn("二课：未上子，青龙", 输出)
        self.assertIn("三课：申上丑，天空", 输出)
        self.assertIn("四课：丑上午，天后", 输出)

    # 《六壬断案》亨集施主簿占前程，《断案新编》PDF199 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=199
    def test_施主簿占前程(self):
        输出 = 运行("大六壬.py", "1128 10 17 01\n1\n1\n")
        self.assertIn("丙申日，天罡辰将加丑时", 输出)
        self.assertIn("初传：申 螣蛇 妻财", 输出)
        self.assertIn("中传：亥 太阴 官鬼", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)
        self.assertIn("一课：丙上申，螣蛇", 输出)
        self.assertIn("二课：申上亥，太阴", 输出)
        self.assertIn("三课：申上亥，太阴", 输出)
        self.assertIn("四课：亥上寅，白虎", 输出)

    # 《六壬断案》亨集邵梓材占前程，书影仍记戊申九月二十一壬寅辰将酉时；该日1128-10-23定气与纪元历皆卯将，原日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=202

    # 《六壬断案》亨集邓省干占前程，书影仍记戊申九月二十一壬寅辰将未时；该日1128-10-23定气与纪元历皆卯将，原日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=205

    # 《六壬断案》亨集江司户占官职, 寅时课图用昼贵，《断案新编》PDF208 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=208
    def test_江司户占官职(self):
        输出 = 运行("大六壬.py", "1128 11 08 03\n1\n2\n")
        self.assertIn("戊午日，太冲卯将加寅时", 输出)
        self.assertIn("初传：寅 螣蛇 官鬼", 输出)
        self.assertIn("中传：午 青龙 父母", 输出)
        self.assertIn("末传：午 青龙 父母", 输出)
        self.assertIn("一课：戊上午，青龙", 输出)
        self.assertIn("二课：午上未，天空", 输出)
        self.assertIn("三课：午上未，天空", 输出)
        self.assertIn("四课：未上申，白虎", 输出)

    # 《六壬断案》亨集冯机宜占前程，《断案新编》PDF211 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=211
    def test_冯机宜占前程(self):
        输出 = 运行("大六壬.py", "1129 11 21 19\n1\n1\n")
        self.assertIn("丙子日，太冲卯将加戌时", 输出)
        self.assertIn("初传：巳 太常 兄弟", 输出)
        self.assertIn("中传：戌 螣蛇 子孙", 输出)
        self.assertIn("末传：卯 天空 父母", 输出)
        self.assertIn("一课：丙上戌，螣蛇", 输出)
        self.assertIn("二课：戌上卯，天空", 输出)
        self.assertIn("三课：子上巳，太常", 输出)
        self.assertIn("四课：巳上戌，螣蛇", 输出)

    # 《六壬断案》亨集刘运干占前程，《断案新编》PDF214 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=214
    def test_刘运干占前程(self):
        输出 = 运行("大六壬.py", "1128 11 05 13\n1\n1\n")
        self.assertIn("乙卯日，太冲卯将加未时", 输出)
        self.assertIn("初传：未 白虎 妻财", 输出)
        self.assertIn("中传：卯 六合 兄弟", 输出)
        self.assertIn("末传：亥 天后 父母", 输出)
        self.assertIn("一课：乙上子，贵人", 输出)
        self.assertIn("二课：子上申，太常", 输出)
        self.assertIn("三课：卯上亥，天后", 输出)
        self.assertIn("四课：亥上未，白虎", 输出)

    # 《六壬断案》亨集郑子云占前程，《断案新编》PDF219 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=219
    def test_郑子云占前程(self):
        输出 = 运行("大六壬.py", "1128 11 05 07\n1\n1\n")
        self.assertIn("乙卯日，太冲卯将加辰时", 输出)
        self.assertIn("初传：丑 螣蛇 妻财", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：亥 天后 父母", 输出)
        self.assertIn("一课：乙上卯，六合", 输出)
        self.assertIn("二课：卯上寅，朱雀", 输出)
        self.assertIn("三课：卯上寅，朱雀", 输出)
        self.assertIn("四课：寅上丑，螣蛇", 输出)

    # 《六壬断案》亨集何上舍占前程 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=222
    def test_何上舍占前程(self):
        输出 = 运行("大六壬.py", "1128 11 11 13\n1\n1\n")
        self.assertIn("辛酉日，太冲卯将加未时", 输出)
        self.assertIn("初传：巳 螣蛇 官鬼", 输出)
        self.assertIn("中传：丑 青龙 父母", 输出)
        self.assertIn("末传：酉 玄武 兄弟", 输出)
        self.assertIn("二课：午上寅，勾陈", 输出)
        self.assertIn("三课：酉上巳，螣蛇", 输出)
        self.assertIn("一课：辛上午，贵人", 输出)
        self.assertIn("四课：巳上丑，青龙", 输出)

    # 《六壬断案》亨集童七秀才占前程，《断案新编》PDF225 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=225
    def test_童七秀才占前程(self):
        输出 = 运行("大六壬.py", "1128 07 10 13\n1\n1\n")
        self.assertIn("丁巳日，小吉未将加未时", 输出)
        self.assertIn("初传：巳 天空 兄弟", 输出)
        self.assertIn("中传：申 玄武 妻财", 输出)
        self.assertIn("末传：寅 六合 父母", 输出)
        self.assertIn("一课：丁上未，太常", 输出)
        self.assertIn("二课：未上未，太常", 输出)
        self.assertIn("三课：巳上巳，天空", 输出)
        self.assertIn("四课：巳上巳，天空", 输出)

    # 《六壬断案》亨集陈主簿占官任, 课图按《六壬指南》涉害先孟取午，《断案新编》PDF228 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=228
    def test_陈主簿占官任(self):
        输出 = 运行("大六壬.py", "1129 11 25 07\n1\n1\n2\n")
        self.assertIn("庚辰日，功曹寅将加辰时", 输出)
        self.assertIn("初传：午 青龙 官鬼", 输出)
        self.assertIn("中传：辰 六合 父母", 输出)
        self.assertIn("末传：寅 螣蛇 妻财", 输出)
        self.assertIn("一课：庚上午，青龙", 输出)
        self.assertIn("二课：午上辰，六合", 输出)
        self.assertIn("三课：辰上寅，螣蛇", 输出)
        self.assertIn("四课：寅上子，天后", 输出)

    # 《六壬断案》亨集徐通判占赴任，书影仍题戊申十二月壬辰丑将；该年壬辰日无丑将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=231

    # 《六壬断案》亨集钱通判占前程，《断案新编》PDF234 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=234
    def test_钱通判占前程(self):
        输出 = 运行("大六壬.py", "1129 01 29 09\n1\n1\n1\n")
        self.assertIn("庚辰日，神后子将加巳时", 输出)
        self.assertIn("初传：午 白虎 官鬼", 输出)
        self.assertIn("中传：丑 贵人 父母", 输出)
        self.assertIn("末传：申 青龙 兄弟", 输出)
        self.assertIn("一课：庚上卯，太阴", 输出)
        self.assertIn("二课：卯上戌，六合", 输出)
        self.assertIn("三课：辰上亥，朱雀", 输出)
        self.assertIn("四课：亥上午，白虎", 输出)

    # 《六壬断案》亨集时监院占迁转，《断案新编》PDF237 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=237
    def test_时监院占迁转(self):
        输出 = 运行("大六壬.py", "1129 01 30 17\n1\n1\n")
        self.assertIn("辛巳日，神后子将加酉时", 输出)
        self.assertIn("初传：申 天空 兄弟", 输出)
        self.assertIn("中传：亥 玄武 子孙", 输出)
        self.assertIn("末传：寅 贵人 妻财", 输出)
        self.assertIn("一课：辛上丑，天后", 输出)
        self.assertIn("二课：丑上辰，朱雀", 输出)
        self.assertIn("三课：巳上申，天空", 输出)
        self.assertIn("四课：申上亥，玄武", 输出)

    # 《六壬断案》亨集陈上舍占科举，《断案新编》PDF240 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=240
    def test_陈上舍占科举(self):
        输出 = 运行("大六壬.py", "1129 02 17 13\n1\n1\n")
        self.assertIn("己亥日，神后子将加未时", 输出)
        self.assertIn("初传：巳 白虎 父母", 输出)
        self.assertIn("中传：戌 朱雀 兄弟", 输出)
        self.assertIn("末传：卯 玄武 官鬼", 输出)
        self.assertIn("一课：己上子，贵人", 输出)
        self.assertIn("二课：子上巳，白虎", 输出)
        self.assertIn("三课：亥上辰，太常", 输出)
        self.assertIn("四课：辰上酉，六合", 输出)

    # 《六壬断案》亨集欧阳秘教占秋试，《断案新编》PDF243 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=243
    def test_欧阳秘教占秋试(self):
        输出 = 运行("大六壬.py", "1129 07 27 19\n1\n1\n1\n")
        self.assertIn("己卯日，胜光午将加戌时", 输出)
        self.assertIn("初传：未 天后 兄弟", 输出)
        self.assertIn("中传：卯 白虎 官鬼", 输出)
        self.assertIn("末传：亥 六合 妻财", 输出)
        self.assertIn("一课：己上卯，白虎", 输出)
        self.assertIn("二课：卯上亥，六合", 输出)
        self.assertIn("三课：卯上亥，六合", 输出)
        self.assertIn("四课：亥上未，天后", 输出)

    # 《六壬断案》亨集徐秀才占秋试，《断案新编》PDF246 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=246
    def test_徐秀才占秋试(self):
        输出 = 运行("大六壬.py", "1129 03 12 15\n1\n1\n")
        self.assertIn("壬戌日，登明亥将加申时", 输出)
        self.assertIn("初传：辰 天后 官鬼", 输出)
        self.assertIn("中传：未 朱雀 官鬼", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)
        self.assertIn("一课：壬上寅，玄武", 输出)
        self.assertIn("二课：寅上巳，贵人", 输出)
        self.assertIn("三课：戌上丑，太常", 输出)
        self.assertIn("四课：丑上辰，天后", 输出)

    # 《六壬断案》亨集何知录占前程，《断案新编》PDF249 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=249
    def test_何知录占前程(self):
        输出 = 运行("大六壬.py", "1128 06 09 13\n1\n1\n")
        self.assertIn("丙戌日，传送申将加未时", 输出)
        self.assertIn("初传：亥 贵人 官鬼", 输出)
        self.assertIn("中传：子 天后 官鬼", 输出)
        self.assertIn("末传：丑 太阴 子孙", 输出)
        self.assertIn("一课：丙上午，青龙", 输出)
        self.assertIn("二课：午上未，勾陈", 输出)
        self.assertIn("三课：戌上亥，贵人", 输出)
        self.assertIn("四课：亥上子，天后", 输出)

    # 《六壬断案》亨集童学生占前程, 程注古本明载己酉三月十七日，《断案新编》PDF252 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=252
    def test_童学生占前程(self):
        输出 = 运行("大六壬.py", "1129 04 14 09\n1\n1\n")
        self.assertIn("乙未日，河魁戌将加巳时", 输出)
        self.assertIn("初传：巳 白虎 子孙", 输出)
        self.assertIn("中传：戌 朱雀 妻财", 输出)
        self.assertIn("末传：卯 玄武 兄弟", 输出)
        self.assertIn("一课：乙上酉，六合", 输出)
        self.assertIn("二课：酉上寅，太阴", 输出)
        self.assertIn("三课：未上子，贵人", 输出)
        self.assertIn("四课：子上巳，白虎", 输出)

    # 《六壬断案》亨集盖判院占前程，《断案新编》PDF255 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=255
    def test_盖判院占前程(self):
        输出 = 运行("大六壬.py", "1129 06 30 00\n1\n1\n")
        self.assertIn("壬子日，小吉未将加子时", 输出)
        self.assertIn("初传：午 玄武 妻财", 输出)
        self.assertIn("中传：丑 朱雀 官鬼", 输出)
        self.assertIn("末传：申 白虎 父母", 输出)
        self.assertIn("一课：壬上午，玄武", 输出)
        self.assertIn("二课：午上丑，朱雀", 输出)
        self.assertIn("三课：子上未，太常", 输出)
        self.assertIn("四课：未上寅，螣蛇", 输出)

    # 《六壬断案》亨集应解元占前程, 午时课图用夜贵，《断案新编》PDF258 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=258
    def test_应解元占前程(self):
        输出 = 运行("大六壬.py", "1129 01 27 11\n1\n3\n")
        self.assertIn("戊寅日，神后子将加午时", 输出)
        self.assertIn("初传：寅 白虎 官鬼", 输出)
        self.assertIn("中传：申 螣蛇 子孙", 输出)
        self.assertIn("末传：寅 白虎 官鬼", 输出)
        self.assertIn("一课：戊上亥，勾陈", 输出)
        self.assertIn("二课：亥上巳，太阴", 输出)
        self.assertIn("三课：寅上申，螣蛇", 输出)
        self.assertIn("四课：申上寅，白虎", 输出)

    # 《六壬断案》亨集方县尉占前程, 程注古本明载己酉五月初一，《断案新编》PDF261 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=261
    def test_方县尉占前程(self):
        输出 = 运行("大六壬.py", "1129 05 27 07\n1\n1\n")
        self.assertIn("戊寅日，传送申将加辰时", 输出)
        self.assertIn("初传：丑 贵人 兄弟", 输出)
        self.assertIn("中传：午 白虎 父母", 输出)
        self.assertIn("末传：酉 勾陈 子孙", 输出)
        self.assertIn("一课：戊上酉，勾陈", 输出)
        self.assertIn("二课：酉上丑，贵人", 输出)
        self.assertIn("三课：寅上午，白虎", 输出)
        self.assertIn("四课：午上戌，六合", 输出)

    # 《六壬断案》亨集仪上舍占前程，仅载辛巳日、申将、寅时，未载占年；《断案新编》PDF264 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=264

    # 《六壬断案》亨集毛主簿占前程，《断案新编》PDF267 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=267
    def test_毛主簿占前程(self):
        输出 = 运行("大六壬.py", "1128 06 10 11\n1\n1\n")
        self.assertIn("丁亥日，传送申将加午时", 输出)
        self.assertIn("初传：酉 朱雀 妻财", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：丑 太阴 子孙", 输出)
        self.assertIn("一课：丁上酉，朱雀", 输出)
        self.assertIn("二课：酉上亥，贵人", 输出)
        self.assertIn("三课：亥上丑，太阴", 输出)
        self.assertIn("四课：丑上卯，太常", 输出)

    # 《六壬断案》亨集王法司占前程，《断案新编》PDF270 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=270
    def test_王法司占前程(self):
        输出 = 运行("大六壬.py", "1128 07 07 19\n1\n1\n")
        self.assertIn("甲寅日，小吉未将加戌时", 输出)
        self.assertIn("初传：丑 天空 妻财", 输出)
        self.assertIn("中传：亥 太常 父母", 输出)
        self.assertIn("末传：亥 太常 父母", 输出)
        self.assertIn("一课：甲上亥，太常", 输出)
        self.assertIn("二课：亥上申，天后", 输出)
        self.assertIn("三课：寅上亥，太常", 输出)
        self.assertIn("四课：亥上申，天后", 输出)

    # 《六壬断案》亨集赵监务占赴任, 原注己酉正月初二，未交春仍题戊申，《断案新编》PDF273 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=273
    def test_赵监务占赴任(self):
        输出 = 运行("大六壬.py", "1129 01 30 07\n1\n1\n")
        self.assertIn("辛巳日，神后子将加辰时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：寅 勾陈 妻财", 输出)
        self.assertIn("末传：戌 太常 父母", 输出)
        self.assertIn("一课：辛上午，贵人", 输出)
        self.assertIn("二课：午上寅，勾陈", 输出)
        self.assertIn("三课：巳上丑，青龙", 输出)
        self.assertIn("四课：丑上酉，玄武", 输出)

    # 《六壬断案》亨集赵知县占前程，《断案新编》PDF276 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=276
    def test_赵知县占前程(self):
        输出 = 运行("大六壬.py", "1128 12 15 13\n1\n1\n")
        self.assertIn("乙未日，功曹寅将加未时", 输出)
        self.assertIn("初传：午 天空 子孙", 输出)
        self.assertIn("中传：丑 天后 妻财", 输出)
        self.assertIn("末传：申 勾陈 官鬼", 输出)
        self.assertIn("一课：乙上亥，螣蛇", 输出)
        self.assertIn("二课：亥上午，天空", 输出)
        self.assertIn("三课：未上寅，太阴", 输出)
        self.assertIn("四课：寅上酉，六合", 输出)

    # 《六壬断案》亨集韩省干占岁中事, 原载己酉元旦，《断案新编》PDF279 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=279
    def test_韩省干占岁中事(self):
        输出 = 运行("大六壬.py", "1129 01 29 21\n1\n1\n")
        self.assertIn("庚辰日，神后子将加亥时", 输出)
        self.assertIn("初传：午 螣蛇 官鬼", 输出)
        self.assertIn("中传：未 贵人 父母", 输出)
        self.assertIn("末传：申 天后 兄弟", 输出)
        self.assertIn("一课：庚上酉，太阴", 输出)
        self.assertIn("二课：酉上戌，玄武", 输出)
        self.assertIn("三课：辰上巳，朱雀", 输出)
        self.assertIn("四课：巳上午，螣蛇", 输出)

    # 《六壬断案》亨集伊知县占赴任，《断案新编》PDF282 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=282
    def test_伊知县占赴任(self):
        输出 = 运行("大六壬.py", "1129 07 11 21\n1\n1\n1\n")
        self.assertIn("癸亥日，小吉未将加亥时", 输出)
        self.assertIn("初传：未 太常 官鬼", 输出)
        self.assertIn("中传：卯 贵人 子孙", 输出)
        self.assertIn("末传：亥 勾陈 兄弟", 输出)
        self.assertIn("一课：癸上酉，天空", 输出)
        self.assertIn("二课：酉上巳，太阴", 输出)
        self.assertIn("三课：亥上未，太常", 输出)
        self.assertIn("四课：未上卯，贵人", 输出)

    # 《六壬断案》亨集童巡检占前程，书影仍题己酉八月丁未午将；八月初一丁未是1129-08-24，定气与纪元历皆巳将 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=285

    # 《六壬断案》亨集应汝言占前程, 月将按宋纪元历气法取卯，《断案新编》PDF288 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=288
    def test_应汝言占前程(self):
        输出 = 运行("大六壬.py", "1129 10 23 03\n2\n1\n1\n")
        self.assertIn("丁未日，太冲卯将加寅时", 输出)
        self.assertIn("初传：申 螣蛇 妻财", 输出)
        self.assertIn("中传：酉 贵人 妻财", 输出)
        self.assertIn("末传：戌 天后 子孙", 输出)
        self.assertIn("一课：丁上申，螣蛇", 输出)
        self.assertIn("二课：申上酉，贵人", 输出)
        self.assertIn("三课：未上申，螣蛇", 输出)
        self.assertIn("四课：申上酉，贵人", 输出)

    # 《六壬断案》亨集姜子安占前程，《断案新编》PDF291 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=291
    def test_姜子安占前程(self):
        输出 = 运行("大六壬.py", "1129 10 25 00\n1\n1\n")
        self.assertIn("己酉日，太冲卯将加子时", 输出)
        self.assertIn("初传：卯 青龙 官鬼", 输出)
        self.assertIn("中传：午 朱雀 父母", 输出)
        self.assertIn("末传：酉 天后 子孙", 输出)
        self.assertIn("一课：己上戌，太阴", 输出)
        self.assertIn("二课：戌上丑，白虎", 输出)
        self.assertIn("三课：酉上子，太常", 输出)
        self.assertIn("四课：子上卯，青龙", 输出)

    # 《六壬断案》亨集童知丞占在任，《断案新编》PDF294 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=294
    def test_童知丞占在任(self):
        输出 = 运行("大六壬.py", "1129 11 24 01\n1\n1\n")
        self.assertIn("己卯日，功曹寅将加丑时", 输出)
        self.assertIn("初传：辰 勾陈 兄弟", 输出)
        self.assertIn("中传：巳 六合 父母", 输出)
        self.assertIn("末传：午 朱雀 父母", 输出)
        self.assertIn("一课：己上申，贵人", 输出)
        self.assertIn("二课：申上酉，天后", 输出)
        self.assertIn("三课：卯上辰，勾陈", 输出)
        self.assertIn("四课：辰上巳，六合", 输出)

    # 《六壬断案》亨集赵主簿占前程，《断案新编》PDF297 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=297
    def test_赵主簿占前程(self):
        输出 = 运行("大六壬.py", "1129 10 27 09\n1\n1\n")
        self.assertIn("辛亥日，太冲卯将加巳时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：辰 朱雀 父母", 输出)
        self.assertIn("末传：寅 勾陈 妻财", 输出)
        self.assertIn("一课：辛上申，太阴", 输出)
        self.assertIn("二课：申上午，贵人", 输出)
        self.assertIn("三课：亥上酉，玄武", 输出)
        self.assertIn("四课：酉上未，天后", 输出)

    # 《六壬断案》亨集陈殿院占谪官，甲申秋壬辰巳将在1104年无匹配，原年日将不合；《断案新编》PDF300 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=300

    # 《六壬断案》亨集李大夫占银网事，《精抄历代六壬占验汇选》卷1甲子日原稿明载大观己丑十二月，1109年甲子日无子将，原年日将不合 https://d.zixueguoxue.com/2022/04/1650441050-f06417473b12f17.pdf#page=3

    # 《六壬断案》亨集姜伯达占前程, 宋本更正未将寅时 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=306
    def test_姜伯达占前程(self):
        输出 = 运行("大六壬.py", "1129 07 01 03\n1\n1\n")
        self.assertIn("癸丑日，小吉未将加寅时", 输出)
        self.assertIn("初传：午 玄武 妻财", 输出)
        self.assertIn("中传：亥 勾陈 兄弟", 输出)
        self.assertIn("末传：辰 天后 官鬼", 输出)
        self.assertIn("一课：癸上午，玄武", 输出)
        self.assertIn("二课：午上亥，勾陈", 输出)
        self.assertIn("三课：丑上午，玄武", 输出)
        self.assertIn("四课：午上亥，勾陈", 输出)

    # 《六壬断案》亨集冯干办占前程, 书影明记己酉正月 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=309
    def test_冯干办占前程(self):
        输出 = 运行("大六壬.py", "1129 02 12 11\n1\n1\n1\n")
        self.assertIn("甲午日，神后子将加午时", 输出)
        self.assertIn("初传：寅 天后 兄弟", 输出)
        self.assertIn("中传：申 青龙 官鬼", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)
        self.assertIn("一课：甲上申，青龙", 输出)
        self.assertIn("二课：申上寅，天后", 输出)
        self.assertIn("三课：午上子，螣蛇", 输出)
        self.assertIn("四课：子上午，白虎", 输出)

    # 《六壬断案》亨集邓十八官人占漕试，《断案新编》PDF312 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=312
    def test_邓十八官人占漕试(self):
        输出 = 运行("大六壬.py", "1129 04 27 01\n1\n1\n")
        self.assertIn("戊申日，从魁酉将加丑时", 输出)
        self.assertIn("初传：子 青龙 妻财", 输出)
        self.assertIn("中传：申 螣蛇 子孙", 输出)
        self.assertIn("末传：辰 玄武 兄弟", 输出)
        self.assertIn("一课：戊上丑，天空", 输出)
        self.assertIn("二课：丑上酉，朱雀", 输出)
        self.assertIn("三课：申上辰，玄武", 输出)
        self.assertIn("四课：辰上子，青龙", 输出)

    # 《六壬断案》亨集刘干运占前程，《断案新编》PDF315 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=315
    def test_刘干运占前程(self):
        输出 = 运行("大六壬.py", "1129 06 26 03\n1\n1\n")
        self.assertIn("戊申日，小吉未将加寅时", 输出)
        self.assertIn("初传：卯 太常 官鬼", 输出)
        self.assertIn("中传：申 螣蛇 子孙", 输出)
        self.assertIn("末传：丑 天空 兄弟", 输出)
        self.assertIn("一课：戊上戌，六合", 输出)
        self.assertIn("二课：戌上卯，太常", 输出)
        self.assertIn("三课：申上丑，天空", 输出)
        self.assertIn("四课：丑上午，天后", 输出)

    # 《六壬断案》利集何三公占终身，《断案新编》PDF318 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=318
    def test_何三公占终身(self):
        输出 = 运行("大六壬.py", "1128 07 19 03\n1\n1\n")
        self.assertIn("丙寅日，小吉未将加寅时", 输出)
        self.assertIn("初传：子 六合 官鬼", 输出)
        self.assertIn("中传：巳 太常 兄弟", 输出)
        self.assertIn("末传：戌 螣蛇 子孙", 输出)
        self.assertIn("一课：丙上戌，螣蛇", 输出)
        self.assertIn("二课：戌上卯，天空", 输出)
        self.assertIn("三课：寅上未，太阴", 输出)
        self.assertIn("四课：未上子，六合", 输出)

    # 《六壬断案》利集袁知镇占终身，书影仍题戊申十一月戊戌丑将；该年戊戌日无丑将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=321

    # 《六壬断案》利集王解元占终身，《断案新编》PDF324 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=324
    def test_王解元占终身(self):
        输出 = 运行("大六壬.py", "1128 02 11 03\n1\n1\n")
        self.assertIn("丁亥日，神后子将加寅时", 输出)
        self.assertIn("初传：酉 贵人 妻财", 输出)
        self.assertIn("中传：未 太阴 子孙", 输出)
        self.assertIn("末传：巳 太常 兄弟", 输出)
        self.assertIn("一课：丁上巳，太常", 输出)
        self.assertIn("二课：巳上卯，天空", 输出)
        self.assertIn("三课：亥上酉，贵人", 输出)
        self.assertIn("四课：酉上未，太阴", 输出)

    # 《六壬断案》利集邵木匠占本身，书影题戊申十一月一日壬子卯将；生卒范围内1068-11-16、1128-11-02均合日将，却都不合十一月初一，无法唯一反推日期 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=327

    # 《六壬断案》利集傅清卿占平生，《断案新编》PDF330 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=330
    def test_傅清卿占平生(self):
        输出 = 运行("大六壬.py", "1129 10 03 01\n1\n1\n")
        self.assertIn("丁亥日，天罡辰将加丑时", 输出)
        self.assertIn("初传：午 六合 兄弟", 输出)
        self.assertIn("中传：戌 天后 子孙", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)
        self.assertIn("一课：丁上戌，天后", 输出)
        self.assertIn("二课：戌上丑，太常", 输出)
        self.assertIn("三课：亥上寅，白虎", 输出)
        self.assertIn("四课：寅上巳，勾陈", 输出)

    # 《六壬断案》利集叶七秀才占平生，戊申十二月辛卯丑将在该年无匹配，原年日将不合；《断案新编》PDF333 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=333

    # 《六壬断案》利集傅大禄占平生，《断案新编》PDF336 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=336
    def test_傅大禄占平生(self):
        输出 = 运行("大六壬.py", "1129 02 12 05\n1\n1\n")
        self.assertIn("甲午日，神后子将加卯时", 输出)
        self.assertIn("初传：申 白虎 官鬼", 输出)
        self.assertIn("中传：巳 勾陈 子孙", 输出)
        self.assertIn("末传：寅 螣蛇 兄弟", 输出)
        self.assertIn("一课：甲上亥，太阴", 输出)
        self.assertIn("二课：亥上申，白虎", 输出)
        self.assertIn("三课：午上卯，朱雀", 输出)
        self.assertIn("四课：卯上子，天后", 输出)

    # 《六壬断案》利集王知县占身位，《断案新编》PDF339 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=339
    def test_王知县占身位(self):
        输出 = 运行("大六壬.py", "1128 06 07 01\n1\n1\n")
        self.assertIn("甲申日，传送申将加丑时", 输出)
        self.assertIn("初传：戌 六合 妻财", 输出)
        self.assertIn("中传：巳 太阴 子孙", 输出)
        self.assertIn("末传：子 青龙 父母", 输出)
        self.assertIn("一课：甲上酉，朱雀", 输出)
        self.assertIn("二课：酉上辰，玄武", 输出)
        self.assertIn("三课：申上卯，太常", 输出)
        self.assertIn("四课：卯上戌，六合", 输出)

    # 《六壬断案》利集何子重占平生，《断案新编》PDF342 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=342
    def test_何子重占平生(self):
        输出 = 运行("大六壬.py", "1129 02 12 05\n1\n1\n")
        self.assertIn("甲午日，神后子将加卯时", 输出)
        self.assertIn("初传：申 白虎 官鬼", 输出)
        self.assertIn("中传：巳 勾陈 子孙", 输出)
        self.assertIn("末传：寅 螣蛇 兄弟", 输出)
        self.assertIn("一课：甲上亥，太阴", 输出)
        self.assertIn("二课：亥上申，白虎", 输出)
        self.assertIn("三课：午上卯，朱雀", 输出)
        self.assertIn("四课：卯上子，天后", 输出)

    # 《六壬断案》利集姜子占向后，《断案新编》PDF345 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=345
    def test_姜子占向后(self):
        输出 = 运行("大六壬.py", "1129 10 25 01\n1\n1\n")
        self.assertIn("己酉日，太冲卯将加丑时", 输出)
        self.assertIn("初传：丑 白虎 兄弟", 输出)
        self.assertIn("中传：卯 青龙 官鬼", 输出)
        self.assertIn("末传：巳 六合 父母", 输出)
        self.assertIn("一课：己上酉，天后", 输出)
        self.assertIn("二课：酉上亥，玄武", 输出)
        self.assertIn("三课：酉上亥，玄武", 输出)
        self.assertIn("四课：亥上丑，白虎", 输出)

    # 《六壬断案》利集颜孔目占平生，《断案新编》PDF348 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=348
    def test_颜孔目占平生(self):
        输出 = 运行("大六壬.py", "1129 11 04 03\n1\n1\n")
        self.assertIn("己未日，太冲卯将加寅时", 输出)
        self.assertIn("初传：未 螣蛇 兄弟", 输出)
        self.assertIn("中传：申 贵人 子孙", 输出)
        self.assertIn("末传：申 贵人 子孙", 输出)
        self.assertIn("一课：己上申，贵人", 输出)
        self.assertIn("二课：申上酉，天后", 输出)
        self.assertIn("三课：未上申，贵人", 输出)
        self.assertIn("四课：申上酉，天后", 输出)

    # 《六壬断案》利集丁丑人占终身，《断案新编》PDF351 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=351
    def test_丁丑人占终身(self):
        输出 = 运行("大六壬.py", "1122 02 12 15\n1\n1\n")
        self.assertIn("丁巳日，神后子将加申时", 输出)
        self.assertIn("初传：酉 朱雀 妻财", 输出)
        self.assertIn("中传：丑 太阴 子孙", 输出)
        self.assertIn("末传：巳 天空 兄弟", 输出)
        self.assertIn("一课：丁上亥，贵人", 输出)
        self.assertIn("二课：亥上卯，太常", 输出)
        self.assertIn("三课：巳上酉，朱雀", 输出)
        self.assertIn("四课：酉上丑，太阴", 输出)

    # 《六壬断案》利集乙亥人占终身，《断案新编》PDF354 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=354
    def test_乙亥人占终身(self):
        输出 = 运行("大六壬.py", "1128 02 10 13\n1\n1\n")
        self.assertIn("丙戌日，神后子将加未时", 输出)
        self.assertIn("初传：申 六合 妻财", 输出)
        self.assertIn("中传：丑 太阴 子孙", 输出)
        self.assertIn("末传：午 青龙 兄弟", 输出)
        self.assertIn("一课：丙上戌，螣蛇", 输出)
        self.assertIn("二课：戌上卯，太常", 输出)
        self.assertIn("三课：戌上卯，太常", 输出)
        self.assertIn("四课：卯上申，六合", 输出)

    # 《六壬断案》利集壬午日占平生，仅载壬午日、亥将、酉时，未载占年；《断案新编》PDF357 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=357

    # 《六壬断案》利集徐成局占向后，《断案新编》PDF360 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=360
    def test_徐成局占向后(self):
        输出 = 运行("大六壬.py", "1129 03 29 03\n1\n1\n1\n")
        self.assertIn("己卯日，河魁戌将加寅时", 输出)
        self.assertIn("初传：未 天后 兄弟", 输出)
        self.assertIn("中传：卯 白虎 官鬼", 输出)
        self.assertIn("末传：亥 六合 妻财", 输出)
        self.assertIn("一课：己上卯，白虎", 输出)
        self.assertIn("二课：卯上亥，六合", 输出)
        self.assertIn("三课：卯上亥，六合", 输出)
        self.assertIn("四课：亥上未，天后", 输出)

    # 《六壬断案》利集行者占平生，徐成局案尾明载同日时有一行者占得此课，书影也载己酉三月初一 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=360
    def test_行者占平生(self):
        输出 = 运行("大六壬.py", "1129 03 29 03\n1\n1\n1\n")
        self.assertIn("己卯日，河魁戌将加寅时", 输出)
        self.assertIn("初传：未 天后 兄弟", 输出)
        self.assertIn("中传：卯 白虎 官鬼", 输出)
        self.assertIn("末传：亥 六合 妻财", 输出)

    # 《六壬断案》利集韩监仓占平生，书影末传辰乘天后 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=363
    def test_韩监仓占平生(self):
        输出 = 运行("大六壬.py", "1129 07 10 09\n1\n1\n")
        self.assertIn("壬戌日，小吉未将加巳时", 输出)
        self.assertIn("初传：子 白虎 兄弟", 输出)
        self.assertIn("中传：寅 玄武 子孙", 输出)
        self.assertIn("末传：辰 天后 官鬼", 输出)

    # 《六壬断案》利集刘监仓占年内，书影三传午辰寅 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=366
    def test_刘监仓占年内(self):
        输出 = 运行("大六壬.py", "1129 01 29 03\n1\n1\n2\n")
        self.assertIn("庚辰日，神后子将加寅时", 输出)
        self.assertIn("初传：午 螣蛇 官鬼", 输出)
        self.assertIn("中传：辰 六合 父母", 输出)
        self.assertIn("末传：寅 青龙 妻财", 输出)

    # 《六壬断案》利集唐丞务占一年，仅题戊申庚辰子将子时，未载占月；农年与节年口径可得不同日期；《断案新编》PDF369 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=369

    # 《六壬断案》利集祝省元占婚，《断案新编》PDF372 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=372
    def test_祝省元占婚(self):
        输出 = 运行("大六壬.py", "1129 03 29 07\n1\n1\n")
        self.assertIn("己卯日，河魁戌将加辰时", 输出)
        self.assertIn("初传：卯 玄武 官鬼", 输出)
        self.assertIn("中传：酉 六合 子孙", 输出)
        self.assertIn("末传：卯 玄武 官鬼", 输出)
        self.assertIn("一课：己上丑，天后", 输出)
        self.assertIn("二课：丑上未，青龙", 输出)
        self.assertIn("三课：卯上酉，六合", 输出)
        self.assertIn("四课：酉上卯，玄武", 输出)

    # 《六壬断案》利集孔七公占婚，《断案新编》PDF375 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=375
    def test_孔七公占婚(self):
        输出 = 运行("大六壬.py", "1129 12 08 21\n1\n1\n")
        self.assertIn("癸巳日，功曹寅将加亥时", 输出)
        self.assertIn("初传：申 青龙 父母", 输出)
        self.assertIn("中传：亥 太常 兄弟", 输出)
        self.assertIn("末传：寅 天后 子孙", 输出)
        self.assertIn("一课：癸上辰，螣蛇", 输出)
        self.assertIn("二课：辰上未，勾陈", 输出)
        self.assertIn("三课：巳上申，青龙", 输出)
        self.assertIn("四课：申上亥，太常", 输出)

    # 《六壬断案》利集李二伯占成亲，《断案新编》PDF378 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=378
    def test_李二伯占成亲(self):
        输出 = 运行("大六壬.py", "1129 12 15 13\n1\n1\n")
        self.assertIn("庚子日，功曹寅将加未时", 输出)
        self.assertIn("初传：戌 六合 父母", 输出)
        self.assertIn("中传：巳 太常 官鬼", 输出)
        self.assertIn("末传：子 螣蛇 子孙", 输出)
        self.assertIn("一课：庚上卯，太阴", 输出)
        self.assertIn("二课：卯上戌，六合", 输出)
        self.assertIn("三课：子上未，天空", 输出)
        self.assertIn("四课：未上寅，天后", 输出)

    # 《六壬断案》利集白生占产妇，《断案新编》PDF381 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=381
    def test_白生占产妇(self):
        输出 = 运行("大六壬.py", "1129 11 05 03\n1\n1\n")
        self.assertIn("庚申日，太冲卯将加寅时", 输出)
        self.assertIn("初传：亥 太常 子孙", 输出)
        self.assertIn("中传：酉 太阴 兄弟", 输出)
        self.assertIn("末传：酉 太阴 兄弟", 输出)
        self.assertIn("一课：庚上酉，太阴", 输出)
        self.assertIn("二课：酉上戌，玄武", 输出)
        self.assertIn("三课：申上酉，太阴", 输出)
        self.assertIn("四课：酉上戌，玄武", 输出)

    # 《六壬断案》利集翁秀才占子息，仅载丙申日、戌将、亥时，未载占年；《断案新编》PDF384 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=384

    # 《六壬断案》利集何解元占子嗣，《断案新编》PDF387 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=387
    def test_何解元占子嗣(self):
        输出 = 运行("大六壬.py", "1128 09 10 05\n1\n1\n")
        self.assertIn("己未日，太乙巳将加卯时", 输出)
        self.assertIn("初传：酉 六合 子孙", 输出)
        self.assertIn("中传：酉 六合 子孙", 输出)
        self.assertIn("末传：酉 六合 子孙", 输出)
        self.assertIn("一课：己上酉，六合", 输出)
        self.assertIn("二课：酉上亥，螣蛇", 输出)
        self.assertIn("三课：未上酉，六合", 输出)
        self.assertIn("四课：酉上亥，螣蛇", 输出)

    # 《六壬断案》利集张姓占远行，何解元案尾仅载同日同课；由原日巳将及独足酉酉酉反推卯时，占时为反推 https://daizhige.org/易藏/术数/六壬断案.html
    # def test_张姓占远行(self):
    #     输出 = 运行("大六壬.py", "1128 09 10 05\n1\n1\n")
    #     self.assertIn("己未日，太乙巳将加卯时", 输出)
    #     self.assertIn("初传：酉 六合 子孙", 输出)
    #     self.assertIn("中传：酉 六合 子孙", 输出)
    #     self.assertIn("末传：酉 六合 子孙", 输出)

    # 《六壬断案》利集季官人占过房子息，《断案新编》PDF390 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=390
    def test_季官人占过房子息(self):
        输出 = 运行("大六壬.py", "1129 11 06 11\n1\n1\n")
        self.assertIn("辛酉日，太冲卯将加午时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：卯 六合 妻财", 输出)
        self.assertIn("末传：子 天空 子孙", 输出)
        self.assertIn("一课：辛上未，天后", 输出)
        self.assertIn("二课：未上辰，朱雀", 输出)
        self.assertIn("三课：酉上午，贵人", 输出)
        self.assertIn("四课：午上卯，六合", 输出)

    # 《六壬断案》利集郭彦和占讨子, 书影四课酉乘青龙而三传酉乘贵人，取所载三传 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=393
    def test_郭彦和占讨子(self):
        输出 = 运行("大六壬.py", "1129 12 12 00\n1\n1\n")
        self.assertIn("丁酉日，功曹寅将加子时", 输出)
        self.assertIn("初传：酉 贵人 妻财", 输出)
        self.assertIn("中传：亥 太阴 官鬼", 输出)
        self.assertIn("末传：丑 太常 子孙", 输出)
        self.assertIn("二课：酉上亥，太阴", 输出)
        self.assertIn("三课：酉上亥，太阴", 输出)
        self.assertIn("四课：亥上丑，太常", 输出)

    # 《六壬断案》利集丁亥人占产，仅载丙辰日、午将、午时，未载占年；《断案新编》PDF396 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=396

    # 《六壬断案》利集乙丑日占产，仅载乙丑日、午将、申时，未载占年；《断案新编》PDF399 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=399

    # 《六壬断案》利集童监税占财产，书影题戌将丑时 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=402
    def test_童监税占财产(self):
        输出 = 运行("大六壬.py", "1128 04 19 01\n1\n1\n")
        self.assertIn("乙未日，河魁戌将加丑时", 输出)
        self.assertIn("初传：丑 青龙 妻财", 输出)
        self.assertIn("中传：戌 朱雀 妻财", 输出)
        self.assertIn("末传：未 天后 妻财", 输出)
        self.assertIn("一课：乙上丑，青龙", 输出)
        self.assertIn("二课：丑上戌，朱雀", 输出)
        self.assertIn("三课：未上辰，太常", 输出)
        self.assertIn("四课：辰上丑，青龙", 输出)

    # 《六壬断案》利集邹七丞务占求财，《断案新编》PDF408 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=408
    def test_邹七丞务占求财(self):
        输出 = 运行("大六壬.py", "1129 12 08 01\n1\n1\n")
        self.assertIn("癸巳日，功曹寅将加丑时", 输出)
        self.assertIn("初传：未 勾陈 官鬼", 输出)
        self.assertIn("中传：申 青龙 父母", 输出)
        self.assertIn("末传：酉 天空 父母", 输出)
        self.assertIn("一课：癸上寅，天后", 输出)
        self.assertIn("二课：寅上卯，贵人", 输出)
        self.assertIn("三课：巳上午，六合", 输出)
        self.assertIn("四课：午上未，勾陈", 输出)

    # 《六壬断案》利集林子成占养息，仅载乙亥日、戌将、午时，未载占年；《断案新编》PDF411 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=411

    # 《六壬断案》利集张公占店业，书影中传亥乘勾陈 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=415
    def test_张公占店业(self):
        输出 = 运行("大六壬.py", "1128 10 11 01\n1\n1\n")
        self.assertIn("庚寅日，天罡辰将加丑时", 输出)
        self.assertIn("初传：申 螣蛇 兄弟", 输出)
        self.assertIn("中传：亥 勾陈 子孙", 输出)
        self.assertIn("末传：寅 白虎 妻财", 输出)

    # 《六壬断案》利集曹八秀才占开店，《断案新编》PDF418 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=418
    def test_曹八秀才占开店(self):
        输出 = 运行("大六壬.py", "1129 12 14 17\n1\n1\n")
        self.assertIn("己亥日，功曹寅将加酉时", 输出)
        self.assertIn("初传：巳 玄武 父母", 输出)
        self.assertIn("中传：戌 朱雀 兄弟", 输出)
        self.assertIn("末传：卯 白虎 官鬼", 输出)
        self.assertIn("一课：己上子，勾陈", 输出)
        self.assertIn("二课：子上巳，玄武", 输出)
        self.assertIn("三课：亥上辰，太常", 输出)
        self.assertIn("四课：辰上酉，螣蛇", 输出)

    # 《六壬断案》利集张克用占买卖，仅载己未日、酉将、亥时，未载占年；《断案新编》PDF405 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=405

    # 《六壬断案》利集曹八秀才占进屋，《断案新编》PDF421 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=421
    def test_曹八秀才占进屋(self):
        输出 = 运行("大六壬.py", "1129 12 15 13\n1\n1\n")
        self.assertIn("庚子日，功曹寅将加未时", 输出)
        self.assertIn("初传：戌 六合 父母", 输出)
        self.assertIn("中传：巳 太常 官鬼", 输出)
        self.assertIn("末传：子 螣蛇 子孙", 输出)
        self.assertIn("一课：庚上卯，太阴", 输出)
        self.assertIn("二课：卯上戌，六合", 输出)
        self.assertIn("三课：子上未，天空", 输出)
        self.assertIn("四课：未上寅，天后", 输出)

    # 《六壬断案》利集水四哥占求财，《断案新编》PDF424 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=424
    def test_水四哥占求财(self):
        输出 = 运行("大六壬.py", "1129 12 17 15\n1\n1\n")
        self.assertIn("壬寅日，功曹寅将加申时", 输出)
        self.assertIn("初传：寅 玄武 子孙", 输出)
        self.assertIn("中传：申 六合 父母", 输出)
        self.assertIn("末传：寅 玄武 子孙", 输出)
        self.assertIn("一课：壬上巳，贵人", 输出)
        self.assertIn("二课：巳上亥，天空", 输出)
        self.assertIn("三课：寅上申，六合", 输出)
        self.assertIn("四课：申上寅，玄武", 输出)

    # 《六壬断案》利集刘五官占店，书影明题乙卯十月戊寅寅将；1075年无该日将，1135年该日为农历及节月十一月 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=427

    # 《六壬断案》利集甲申人占求财，书影明题丙辰五月十八丁酉申将；邵氏生卒范围丙辰为1076，日将唯一得1076-05-23农四月十二，日期为反推 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=430
    # def test_甲申人占求财(self):
    #     输出 = 运行("大六壬.py", "1076 05 23 13\n1\n1\n")
    #     self.assertIn("丁酉日，传送申将加未时", 输出)
    #     self.assertIn("初传：亥 贵人 官鬼", 输出)
    #     self.assertIn("中传：子 天后 官鬼", 输出)
    #     self.assertIn("末传：丑 太阴 子孙", 输出)

    # 《六壬断案》利集己巳人占求财，书影明题丙辰六月甲寅巳将；1076、1136两丙辰年均无甲寅巳将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=433

    # 《六壬断案》利集钱三郎占开店, 寅时课图用昼贵 https://daizhige.org/易藏/术数/六壬断案.html
    def test_钱三郎占开店(self):
        输出 = 运行("大六壬.py", "1129 10 02 03\n1\n2\n")
        self.assertIn("丙戌日，天罡辰将加寅时", 输出)
        self.assertIn("初传：子 天后 官鬼", 输出)
        self.assertIn("中传：寅 玄武 父母", 输出)
        self.assertIn("末传：辰 白虎 子孙", 输出)
        self.assertIn("一课：丙上未，勾陈", 输出)
        self.assertIn("二课：未上酉，朱雀", 输出)
        self.assertIn("三课：戌上子，天后", 输出)
        self.assertIn("四课：子上寅，玄武", 输出)

    # 《六壬断案》利集王县丞占官职，《断案新编》PDF436 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=436
    def test_王县丞占官职(self):
        输出 = 运行("大六壬.py", "1128 06 07 09\n1\n1\n")
        self.assertIn("甲申日，传送申将加巳时", 输出)
        self.assertIn("初传：申 青龙 官鬼", 输出)
        self.assertIn("中传：亥 朱雀 父母", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)
        self.assertIn("一课：甲上巳，太常", 输出)
        self.assertIn("二课：巳上申，青龙", 输出)
        self.assertIn("三课：申上亥，朱雀", 输出)
        self.assertIn("四课：亥上寅，天后", 输出)

    # 《六壬断案》利集汪五公占买卖，正文载与王县丞同月将日时，未直载该次占年；《断案新编》PDF436 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=436

    # 《六壬断案》利集刘判官占前程，《断案新编》PDF439 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=439
    def test_刘判官占前程(self):
        输出 = 运行("大六壬.py", "1128 08 05 05\n1\n1\n")
        self.assertIn("癸未日，胜光午将加卯时", 输出)
        self.assertIn("初传：辰 天后 官鬼", 输出)
        self.assertIn("中传：未 朱雀 官鬼", 输出)
        self.assertIn("末传：戌 青龙 官鬼", 输出)
        self.assertIn("一课：癸上辰，天后", 输出)
        self.assertIn("二课：辰上未，朱雀", 输出)
        self.assertIn("三课：未上戌，青龙", 输出)
        self.assertIn("四课：戌上丑，太常", 输出)

    # 《六壬断案》利集刘一翁代占身位，正文载与刘判官同月将日时，未直载该次占年；《断案新编》PDF443 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=443

    # 《六壬断案》利集何秀才占前程，《断案新编》PDF446 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=446
    def test_何秀才占前程(self):
        输出 = 运行("大六壬.py", "1128 06 20 07\n1\n1\n")
        self.assertIn("丁酉日，传送申将加辰时", 输出)
        self.assertIn("初传：亥 贵人 官鬼", 输出)
        self.assertIn("中传：卯 太常 父母", 输出)
        self.assertIn("末传：未 勾陈 子孙", 输出)
        self.assertIn("一课：丁上亥，贵人", 输出)
        self.assertIn("二课：亥上卯，太常", 输出)
        self.assertIn("三课：酉上丑，太阴", 输出)
        self.assertIn("四课：丑上巳，天空", 输出)

    # 《六壬断案》利集何学录占身宅，仅称与何秀才同课，未载该次年月日时；《断案新编》PDF449 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=449

    # 《六壬断案》利集周氏占交易，书影明题建炎五年；按1131年核，正月乙巳无亥将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=452

    # 《六壬断案》利集曹将仕占谋干, 课图按《六壬指南》涉害先孟取丑，《断案新编》PDF455 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=455
    def test_曹将仕占谋干(self):
        输出 = 运行("大六壬.py", "1129 12 18 07\n1\n1\n1\n2\n")
        self.assertIn("癸卯日，功曹寅将加辰时", 输出)
        self.assertIn("初传：丑 勾陈 官鬼", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：酉 太常 父母", 输出)
        self.assertIn("一课：癸上亥，天空", 输出)
        self.assertIn("二课：亥上酉，太常", 输出)
        self.assertIn("三课：卯上丑，勾陈", 输出)
        self.assertIn("四课：丑上亥，天空", 输出)

    # 《六壬断案》利集应秀才占出行，《断案新编》PDF458 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=458
    def test_应秀才占出行(self):
        输出 = 运行("大六壬.py", "1129 11 08 17\n1\n1\n")
        self.assertIn("癸亥日，太冲卯将加酉时", 输出)
        self.assertIn("初传：巳 太阴 妻财", 输出)
        self.assertIn("中传：亥 勾陈 兄弟", 输出)
        self.assertIn("末传：巳 太阴 妻财", 输出)
        self.assertIn("一课：癸上未，太常", 输出)
        self.assertIn("二课：未上丑，朱雀", 输出)
        self.assertIn("三课：亥上巳，太阴", 输出)
        self.assertIn("四课：巳上亥，勾陈", 输出)

    # 《六壬断案》利集李秀才访道士，仅载庚辰日、寅将、午时，未载占年；《断案新编》PDF461 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=461

    # 《六壬断案》利集管学正谒县尹，《断案新编》PDF464 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=464
    def test_管学正谒县尹(self):
        输出 = 运行("大六壬.py", "1129 12 09 19\n1\n1\n")
        self.assertIn("甲午日，功曹寅将加戌时", 输出)
        self.assertIn("初传：寅 白虎 兄弟", 输出)
        self.assertIn("中传：午 天后 子孙", 输出)
        self.assertIn("末传：戌 六合 妻财", 输出)
        self.assertIn("一课：甲上午，天后", 输出)
        self.assertIn("二课：午上戌，六合", 输出)
        self.assertIn("三课：午上戌，六合", 输出)
        self.assertIn("四课：戌上寅，白虎", 输出)

    # 《六壬断案》利集史某占访僧，仅载乙酉日、酉将、辰时，未载占年；《断案新编》PDF467 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=467

    # 《六壬断案》利集邵先生自占动静，据弁言治平2年生及案中64岁反推占年1128，原图用昼贵；《断案新编》PDF3、470 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=470
    # def test_邵先生自占动静(self):
    #     输出 = 运行("大六壬.py", "1128 11 06 00\n1\n2\n")
    #     self.assertIn("丙辰日，太冲卯将加子时，昼贵亥", 输出)
    #     self.assertIn("初传：申 六合 妻财", 输出)
    #     self.assertIn("中传：亥 贵人 官鬼", 输出)
    #     self.assertIn("末传：寅 玄武 父母", 输出)
    #     self.assertIn("一课：丙上申，六合", 输出)
    #     self.assertIn("二课：申上亥，贵人", 输出)
    #     self.assertIn("三课：辰上未，勾陈", 输出)
    #     self.assertIn("四课：未上戌，螣蛇", 输出)

    # 《六壬断案》利集丁巳人占出行，《断案新编》PDF473 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=473
    def test_丁巳人占出行(self):
        输出 = 运行("大六壬.py", "1129 02 12 11\n1\n1\n1\n")
        self.assertIn("甲午日，神后子将加午时", 输出)
        self.assertIn("初传：寅 天后 兄弟", 输出)
        self.assertIn("中传：申 青龙 官鬼", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)
        self.assertIn("一课：甲上申，青龙", 输出)
        self.assertIn("二课：申上寅，天后", 输出)
        self.assertIn("三课：午上子，螣蛇", 输出)
        self.assertIn("四课：子上午，白虎", 输出)

    # 《六壬断案》利集邵先生占相访，仅载戊辰日、子将、酉时，未载占年；《断案新编》PDF476 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=476

    # 《六壬断案》贞集黄秀才占行人，书影日干丁 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=479
    def test_黄秀才占行人(self):
        输出 = 运行("大六壬.py", "1128 03 12 13\n1\n1\n")
        self.assertIn("丁巳日，登明亥将加未时", 输出)
        self.assertIn("初传：酉 朱雀 妻财", 输出)
        self.assertIn("中传：丑 太阴 子孙", 输出)
        self.assertIn("末传：巳 天空 兄弟", 输出)
        self.assertIn("二课：亥上卯，太常", 输出)
        self.assertIn("三课：巳上酉，朱雀", 输出)
        self.assertIn("四课：酉上丑，太阴", 输出)
        self.assertIn("一课：丁上亥，贵人", 输出)

    # 《六壬断案》贞集王知县占新宰，书影仍题己丑十一月甲申子将；1109年甲申日无子将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=482

    # 《六壬断案》贞集戴仪占朝廷文字，《断案新编》PDF485 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=485
    def test_戴仪占朝廷文字(self):
        输出 = 运行("大六壬.py", "1118 07 21 09\n1\n1\n")
        self.assertIn("乙亥日，小吉未将加巳时", 输出)
        self.assertIn("初传：申 勾陈 官鬼", 输出)
        self.assertIn("中传：戌 朱雀 妻财", 输出)
        self.assertIn("末传：子 贵人 父母", 输出)
        self.assertIn("一课：乙上午，天空", 输出)
        self.assertIn("二课：午上申，勾陈", 输出)
        self.assertIn("三课：亥上丑，天后", 输出)
        self.assertIn("四课：丑上卯，玄武", 输出)

    # 《六壬断案》贞集某秀才望省试信，仅载甲戌日、酉将、卯时，未载占年；《断案新编》PDF488 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=488

    # 《六壬断案》贞集寺僧望州中文字，仅载辛亥日、申将、巳时，未载占年；《断案新编》PDF491 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=491

    # 《六壬断案》贞集张一公占州中文字，仅载辛卯日、亥将、寅时，未载占年；《断案新编》PDF494 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=494

    # 《六壬断案》贞集孟承务占幼童，《断案新编》PDF497 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=497
    def test_孟承务占幼童(self):
        输出 = 运行("大六壬.py", "1129 04 01 01\n1\n1\n")
        self.assertIn("壬午日，河魁戌将加丑时", 输出)
        self.assertIn("初传：巳 太阴 妻财", 输出)
        self.assertIn("中传：寅 螣蛇 子孙", 输出)
        self.assertIn("末传：亥 勾陈 兄弟", 输出)
        self.assertIn("一课：壬上申，白虎", 输出)
        self.assertIn("二课：申上巳，太阴", 输出)
        self.assertIn("三课：午上卯，贵人", 输出)
        self.assertIn("四课：卯上子，六合", 输出)

    # 《六壬断案》贞集王县丞占病，《断案新编》PDF500 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=500
    def test_王县丞占病(self):
        输出 = 运行("大六壬.py", "1128 07 07 05\n1\n1\n")
        self.assertIn("甲寅日，小吉未将加卯时", 输出)
        self.assertIn("初传：申 青龙 官鬼", 输出)
        self.assertIn("中传：午 白虎 子孙", 输出)
        self.assertIn("末传：午 白虎 子孙", 输出)
        self.assertIn("一课：甲上午，白虎", 输出)
        self.assertIn("二课：午上戌，六合", 输出)
        self.assertIn("三课：寅上午，白虎", 输出)
        self.assertIn("四课：午上戌，六合", 输出)

    # 《六壬断案》贞集徐孺人占病，《断案新编》PDF503 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=503
    def test_徐孺人占病(self):
        输出 = 运行("大六壬.py", "1128 06 16 05\n1\n1\n")
        self.assertIn("癸巳日，传送申将加卯时", 输出)
        self.assertIn("初传：午 螣蛇 妻财", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：辰 天后 官鬼", 输出)
        self.assertIn("一课：癸上午，螣蛇", 输出)
        self.assertIn("二课：午上亥，天空", 输出)
        self.assertIn("三课：巳上戌，青龙", 输出)
        self.assertIn("四课：戌上卯，太阴", 输出)

    # 《六壬断案》贞集伊秀才占父病，《断案新编》PDF506 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=506
    def test_伊秀才占父病(self):
        输出 = 运行("大六壬.py", "1129 12 11 03\n1\n1\n")
        self.assertIn("丙申日，功曹寅将加寅时", 输出)
        self.assertIn("初传：巳 勾陈 兄弟", 输出)
        self.assertIn("中传：申 螣蛇 妻财", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)
        self.assertIn("一课：丙上巳，勾陈", 输出)
        self.assertIn("二课：巳上巳，勾陈", 输出)
        self.assertIn("三课：申上申，螣蛇", 输出)
        self.assertIn("四课：申上申，螣蛇", 输出)

    # 《六壬断案》贞集张逸士占病，《断案新编》PDF509 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=509
    def test_张逸士占病(self):
        输出 = 运行("大六壬.py", "1128 10 11 01\n1\n1\n")
        self.assertIn("庚寅日，天罡辰将加丑时", 输出)
        self.assertIn("初传：申 螣蛇 兄弟", 输出)
        self.assertIn("中传：亥 勾陈 子孙", 输出)
        self.assertIn("末传：寅 白虎 妻财", 输出)
        self.assertIn("一课：庚上亥，勾陈", 输出)
        self.assertIn("二课：亥上寅，白虎", 输出)
        self.assertIn("三课：寅上巳，太阴", 输出)
        self.assertIn("四课：巳上申，螣蛇", 输出)

    # 《六壬断案》贞集叶八郎占医业，书影仍题戊申十二月辛卯丑将；该年辛卯日无丑将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=512

    # 《六壬断案》贞集樊郎中占项秀才病，《断案新编》PDF515 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=515
    def test_樊郎中占项秀才病(self):
        输出 = 运行("大六壬.py", "1129 11 09 15\n1\n1\n")
        self.assertIn("甲子日，太冲卯将加申时", 输出)
        self.assertIn("初传：寅 天后 兄弟", 输出)
        self.assertIn("中传：酉 勾陈 官鬼", 输出)
        self.assertIn("末传：辰 玄武 妻财", 输出)
        self.assertIn("一课：甲上酉，勾陈", 输出)
        self.assertIn("二课：酉上辰，玄武", 输出)
        self.assertIn("三课：子上未，天空", 输出)
        self.assertIn("四课：未上寅，天后", 输出)

    # 《六壬断案》贞集戊午日占病，《断案新编》PDF518 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=518
    def test_戊午日占病(self):
        输出 = 运行("大六壬.py", "1128 03 13 19\n1\n1\n")
        self.assertIn("戊午日，登明亥将加戌时", 输出)
        self.assertIn("初传：寅 青龙 官鬼", 输出)
        self.assertIn("中传：午 螣蛇 父母", 输出)
        self.assertIn("末传：午 螣蛇 父母", 输出)
        self.assertIn("一课：戊上午，螣蛇", 输出)
        self.assertIn("二课：午上未，贵人", 输出)
        self.assertIn("三课：午上未，贵人", 输出)
        self.assertIn("四课：未上申，天后", 输出)

    # 《六壬断案》贞集尹邦达占妻病，《断案新编》PDF521 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=521
    def test_尹邦达占妻病(self):
        输出 = 运行("大六壬.py", "1129 10 03 21\n1\n1\n")
        self.assertIn("丁亥日，天罡辰将加亥时", 输出)
        self.assertIn("初传：巳 太常 兄弟", 输出)
        self.assertIn("中传：戌 螣蛇 子孙", 输出)
        self.assertIn("末传：卯 天空 父母", 输出)
        self.assertIn("一课：丁上子，六合", 输出)
        self.assertIn("二课：子上巳，太常", 输出)
        self.assertIn("三课：亥上辰，白虎", 输出)
        self.assertIn("四课：辰上酉，贵人", 输出)

    # 《六壬断案》贞集叶解元占病，《断案新编》PDF524 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=524
    def test_叶解元占病(self):
        输出 = 运行("大六壬.py", "1130 08 04 09\n1\n1\n")
        self.assertIn("壬辰日，胜光午将加巳时", 输出)
        self.assertIn("初传：丑 太常 官鬼", 输出)
        self.assertIn("中传：寅 玄武 子孙", 输出)
        self.assertIn("末传：卯 太阴 子孙", 输出)
        self.assertIn("一课：壬上子，白虎", 输出)
        self.assertIn("二课：子上丑，太常", 输出)
        self.assertIn("三课：辰上巳，贵人", 输出)
        self.assertIn("四课：巳上午，螣蛇", 输出)

    # 《六壬断案》贞集韩省干占子病，《断案新编》PDF527 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=527
    def test_韩省干占子病(self):
        输出 = 运行("大六壬.py", "1130 08 11 13\n1\n1\n")
        self.assertIn("己亥日，胜光午将加未时", 输出)
        self.assertIn("初传：戌 太阴 兄弟", 输出)
        self.assertIn("中传：酉 玄武 子孙", 输出)
        self.assertIn("末传：申 太常 子孙", 输出)
        self.assertIn("一课：己上午，天空", 输出)
        self.assertIn("二课：午上巳，青龙", 输出)
        self.assertIn("三课：亥上戌，太阴", 输出)
        self.assertIn("四课：戌上酉，玄武", 输出)

    # 《六壬断案》贞集蒋六公占自身，《断案新编》PDF530 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=530
    def test_蒋六公占自身(self):
        输出 = 运行("大六壬.py", "1129 09 07 03\n1\n1\n")
        self.assertIn("辛酉日，太乙巳将加寅时", 输出)
        self.assertIn("初传：卯 螣蛇 妻财", 输出)
        self.assertIn("中传：午 勾陈 官鬼", 输出)
        self.assertIn("末传：酉 白虎 兄弟", 输出)
        self.assertIn("一课：辛上丑，天后", 输出)
        self.assertIn("二课：丑上辰，朱雀", 输出)
        self.assertIn("三课：酉上子，太阴", 输出)
        self.assertIn("四课：子上卯，螣蛇", 输出)

    # 《六壬断案》贞集蒋七婆占子病，《断案新编》PDF533 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=533
    def test_蒋七婆占子病(self):
        输出 = 运行("大六壬.py", "1129 09 07 15\n1\n1\n")
        self.assertIn("辛酉日，太乙巳将加申时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：卯 六合 妻财", 输出)
        self.assertIn("末传：子 天空 子孙", 输出)
        self.assertIn("一课：辛上未，天后", 输出)
        self.assertIn("二课：未上辰，朱雀", 输出)
        self.assertIn("三课：酉上午，贵人", 输出)
        self.assertIn("四课：午上卯，六合", 输出)

    # 《六壬断案》贞集庚辰日占病，仅载庚辰日、亥将、辰时，未载占年；《断案新编》PDF536 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=536

    # 《六壬断案》贞集丁巳日占病，仅载丁巳日、未将、寅时，未载占年；《断案新编》PDF539 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=539

    # 《六壬断案》贞集丙午日占病，仅载丙午日、子将、亥时，未载占年；《断案新编》PDF542 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=542

    # 《六壬断案》贞集己丑日占儿病，仅载己丑日、丑将、辰时，未载占年；《断案新编》PDF545 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=545

    # 《六壬断案》贞集吴四公占进畜，《断案新编》PDF548 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=548
    def test_吴四公占进畜(self):
        输出 = 运行("大六壬.py", "1129 11 08 07\n1\n1\n")
        self.assertIn("癸亥日，太冲卯将加辰时", 输出)
        self.assertIn("初传：戌 白虎 官鬼", 输出)
        self.assertIn("中传：酉 太常 父母", 输出)
        self.assertIn("末传：申 玄武 父母", 输出)
        self.assertIn("一课：癸上子，青龙", 输出)
        self.assertIn("二课：子上亥，天空", 输出)
        self.assertIn("三课：亥上戌，白虎", 输出)
        self.assertIn("四课：戌上酉，太常", 输出)

    # 《六壬断案》贞集王寺丞占取马，仅载丁亥日、戌将、卯时，未载占年；《断案新编》PDF551 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=551

    # 《六壬断案》贞集遂安官人占失马，仅载壬午日、丑将、卯时，未载占年；《断案新编》PDF554 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=554

    # 《六壬断案》贞集丁丑日占失马，仅载丁丑日、亥将、申时，未载占年；《断案新编》PDF557 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=557

    # 《六壬断案》贞集戊子日占失羊，仅载戊子日、酉将、寅时，未载占年；《断案新编》PDF560 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=560

    # 《六壬断案》贞集丁未日占失羊，仅载丁未日、未将、未时，未载占年；《断案新编》PDF563 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=563

    # 《六壬断案》贞集己卯日占失羊，仅载己卯日、亥将、未时，未载占年；《断案新编》PDF566 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=566

    # 《六壬断案》贞集甲辰日占失狗，仅载甲辰日、戌将、寅时，未载占年；《断案新编》PDF569 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=569

    # 《六壬断案》贞集辛亥日占失鸡，仅载辛亥日、子将、丑时，未载占年；《断案新编》PDF572 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=572

    # 《六壬断案》贞集某占捕逃犯, 课图按《六壬指南》涉害先孟取丑，《断案新编》PDF575 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=575
    def test_某占捕逃犯(self):
        输出 = 运行("大六壬.py", "1129 12 18 07\n1\n1\n1\n2\n")
        self.assertIn("癸卯日，功曹寅将加辰时", 输出)
        self.assertIn("初传：丑 勾陈 官鬼", 输出)
        self.assertIn("中传：亥 天空 兄弟", 输出)
        self.assertIn("末传：酉 太常 父母", 输出)
        self.assertIn("一课：癸上亥，天空", 输出)
        self.assertIn("二课：亥上酉，太常", 输出)
        self.assertIn("三课：卯上丑，勾陈", 输出)
        self.assertIn("四课：丑上亥，天空", 输出)

    # 《六壬断案》贞集李四官占失盗，仅载辛卯日、寅将、巳时，未载占年；《断案新编》PDF578 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=578

    # 《六壬断案》贞集官人占失婢，仅载甲寅日、卯将、丑时，未载占年；《断案新编》PDF581 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=581

    # 《六壬断案》贞集己酉日占失婢，仅载己酉日、酉将、未时，未载占年；《断案新编》PDF584 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=584

    # 《六壬断案》贞集己未日占失婢，仅载己未日、子将、戌时，未载占年；《断案新编》PDF587 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=587

    # 《六壬断案》贞集筵会占失银，仅载庚辰日、酉将、辰时，未载占年；《断案新编》PDF590 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=590

    # 《六壬断案》贞集其子再占失银，只载与前案同日酉将午时，前案也未载占年；《断案新编》PDF593 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=593

    # 《六壬断案》贞集某妇占失金环，仅载己丑日、寅将、戌时，未载占年；《断案新编》PDF596 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=596

    # 《六壬断案》贞集僧占失度牒，仅载辛卯日、酉将、辰时，未载占年；《断案新编》PDF599 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=599

    # 《六壬断案》贞集知县占失银物，仅载癸丑日、卯将、卯时，未载占年；《断案新编》PDF602 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=602

    # 《六壬断案》贞集庚午日占失银，仅载庚午日、子将、丑时，未载占年；《断案新编》PDF605 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=605

    # 《六壬断案》贞集庚午酉时再占，仅载庚午日、子将、酉时，未载占年；《断案新编》PDF608 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=608

    # 《六壬断案》贞集某占失船，仅载壬午日、丑将、卯时，未载占年；《断案新编》PDF611 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=611

    # 《六壬断案》贞集某占失麦面，仅载丁卯日、卯将、戌时，未载占年；《断案新编》PDF614 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=614

    # 《六壬断案》贞集童秀才占讼，《断案新编》PDF617 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=617
    def test_童秀才占讼(self):
        输出 = 运行("大六壬.py", "1128 08 19 07\n1\n1\n")
        self.assertIn("丁酉日，胜光午将加辰时", 输出)
        self.assertIn("初传：酉 朱雀 妻财", 输出)
        self.assertIn("中传：亥 贵人 官鬼", 输出)
        self.assertIn("末传：丑 太阴 子孙", 输出)
        self.assertIn("一课：丁上酉，朱雀", 输出)
        self.assertIn("二课：酉上亥，贵人", 输出)
        self.assertIn("三课：酉上亥，贵人", 输出)
        self.assertIn("四课：亥上丑，太阴", 输出)

    # 《六壬断案》贞集汪淑仪占讼，书影明题戊申辛丑戌将；该年辛丑日无戌将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=620

    # 《六壬断案》贞集陆孔目占讼，《断案新编》PDF623 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=623
    def test_陆孔目占讼(self):
        输出 = 运行("大六壬.py", "1129 11 05 09\n1\n1\n")
        self.assertIn("庚申日，太冲卯将加巳时", 输出)
        self.assertIn("初传：午 青龙 官鬼", 输出)
        self.assertIn("中传：辰 六合 父母", 输出)
        self.assertIn("末传：寅 螣蛇 妻财", 输出)
        self.assertIn("一课：庚上午，青龙", 输出)
        self.assertIn("二课：午上辰，六合", 输出)
        self.assertIn("三课：申上午，青龙", 输出)
        self.assertIn("四课：午上辰，六合", 输出)

    # 《六壬断案》贞集林文占讼，书影三传未卯亥与戌将加午天盘未亥卯不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=626

    # 《六壬断案》贞集祝秀才占讼，《断案新编》PDF629 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=629
    def test_祝秀才占讼(self):
        输出 = 运行("大六壬.py", "1129 10 01 05\n1\n1\n")
        self.assertIn("乙酉日，天罡辰将加卯时", 输出)
        self.assertIn("初传：亥 天后 父母", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：丑 螣蛇 妻财", 输出)
        self.assertIn("一课：乙上巳，青龙", 输出)
        self.assertIn("二课：巳上午，天空", 输出)
        self.assertIn("三课：酉上戌，太阴", 输出)
        self.assertIn("四课：戌上亥，天后", 输出)

    # 《六壬断案》贞集陆孔目占官事，《断案新编》PDF632 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=632
    def test_陆孔目占官事(self):
        输出 = 运行("大六壬.py", "1129 11 04 01\n1\n1\n")
        self.assertIn("己未日，太冲卯将加丑时", 输出)
        self.assertIn("初传：酉 天后 子孙", 输出)
        self.assertIn("中传：酉 天后 子孙", 输出)
        self.assertIn("末传：酉 天后 子孙", 输出)
        self.assertIn("一课：己上酉，天后", 输出)
        self.assertIn("二课：酉上亥，玄武", 输出)
        self.assertIn("三课：未上酉，天后", 输出)
        self.assertIn("四课：酉上亥，玄武", 输出)

    # 《六壬断案》贞集庚午日占讼，仅载庚午日、午将、未时，未载占年；《断案新编》PDF635 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=635

    # 《六壬断案》贞集乙未日占讼，仅载乙未日、未将、卯时，未载占年；《断案新编》PDF638 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=638

    # 《六壬断案》贞集打死人占解官，仅载辛丑日、子将、未时，未载占年；《断案新编》PDF641 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=641

    # 《六壬断案》贞集杀二人占决断，仅载壬辰日、酉将、寅时，未载占年；《断案新编》PDF644 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=644

    # 《六壬断案》贞集张大郎占官事，《断案新编》PDF647 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=647
    def test_张大郎占官事(self):
        输出 = 运行("大六壬.py", "1107 01 06 01\n1\n1\n")
        self.assertIn("辛酉日，大吉丑将加丑时", 输出)
        self.assertIn("初传：酉 白虎 兄弟", 输出)
        self.assertIn("中传：戌 太常 父母", 输出)
        self.assertIn("末传：未 青龙 父母", 输出)
        self.assertIn("一课：辛上戌，太常", 输出)
        self.assertIn("二课：戌上戌，太常", 输出)
        self.assertIn("三课：酉上酉，白虎", 输出)
        self.assertIn("四课：酉上酉，白虎", 输出)

    # 《六壬断案》贞集沈保正占役事，《断案新编》PDF650 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=650
    def test_沈保正占役事(self):
        输出 = 运行("大六壬.py", "1129 11 10 19\n1\n1\n")
        self.assertIn("乙丑日，太冲卯将加戌时", 输出)
        self.assertIn("初传：寅 天空 兄弟", 输出)
        self.assertIn("中传：未 天后 妻财", 输出)
        self.assertIn("末传：子 勾陈 父母", 输出)
        self.assertIn("一课：乙上酉，螣蛇", 输出)
        self.assertIn("二课：酉上寅，天空", 输出)
        self.assertIn("三课：丑上午，太阴", 输出)
        self.assertIn("四课：午上亥，六合", 输出)

    # 《六壬断案》贞集沈四公争保正，书影明题戊申七月二十三乙巳午将；该日1128-08-27定气与纪元历皆巳将 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=653

    # 《六壬断案》贞集潘道士占住持，仅载戊戌日、戌将、寅时，未载占年；《断案新编》PDF656 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=656

    # 《六壬断案》贞集长老常占，书影仍题己丑二月癸丑酉将；1109年癸丑日无酉将，原年日将不合 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=659

    # 《六壬断案》贞集壬子日占求酒，仅载壬子日、申将、亥时，未载占年；《断案新编》PDF662 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=662

    # 《六壬断案》贞集蔡京占长星，原案未载占年，原注崇宁五年丙戌的彗星史事推1106年，四月辛未酉将唯一得1106-05-21，日期为反推 https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E5%A4%A7%E5%85%AD%E5%A3%AC%E6%96%AD%E6%A1%88%E6%96%B0%E7%BC%96_%E9%82%B5%E5%BD%A6%E5%92%8C.pdf#page=665
    # def test_蔡京占长星(self):
    #     输出 = 运行("大六壬.py", "1106 05 21 03\n1\n1\n1\n")
    #     self.assertIn("辛未日，从魁酉将加寅时", 输出)
    #     self.assertIn("初传：酉 青龙 兄弟", 输出)
    #     self.assertIn("中传：辰 太阴 父母", 输出)
    #     self.assertIn("末传：亥 六合 子孙", 输出)

    # 《精抄历代六壬占验汇选》卷1丙寅日吴公望问终身，原稿以康熙24年五月初七丙寅申将酉时的生辰演课 https://img.xiandtang.com/i/2024/11/15/精抄历代六壬占验汇选_35.jpg
    def test_吴公望生辰占终身(self):
        输出 = 运行("大六壬.py", "1685 06 08 17\n1\n1\n")
        self.assertIn("丙寅日，传送申将加酉时", 输出)
        self.assertIn("初传：子 玄武 官鬼", 输出)
        self.assertIn("中传：亥 太阴 官鬼", 输出)
        self.assertIn("末传：戌 天后 子孙", 输出)
        self.assertIn("一课：丙上辰，青龙", 输出)
        self.assertIn("二课：辰上卯，天空", 输出)
        self.assertIn("三课：寅上丑，太常", 输出)
        self.assertIn("四课：丑上子，玄武", 输出)

    # 《精抄历代六壬占验汇选》卷2丙子日孙兴功占赵福星升迁，原稿注“辰时必错当是卯时” https://img.xiandtang.com/i/2024/11/15/精抄历代六壬占验汇选_98.jpg
    def test_孙兴功占赵福星升迁(self):
        输出 = 运行("大六壬.py", "1648 05 03 05\n1\n1\n")
        self.assertIn("丙子日，从魁酉将加卯时", 输出)
        self.assertIn("初传：午 青龙 兄弟", 输出)
        self.assertIn("中传：子 天后 官鬼", 输出)
        self.assertIn("末传：午 青龙 兄弟", 输出)
        self.assertIn("一课：丙上亥，贵人", 输出)
        self.assertIn("二课：亥上巳，天空", 输出)
        self.assertIn("三课：子上午，青龙", 输出)
        self.assertIn("四课：午上子，天后", 输出)

    # 《精抄历代六壬占验汇选》卷2丁丑日王得俊占前程，原稿建炎己酉闰八月丁丑巳将酉时 https://img.xiandtang.com/i/2024/11/15/精抄历代六壬占验汇选_101.jpg
    def test_王得俊占前程(self):
        输出 = 运行("大六壬.py", "1129 09 23 17\n1\n1\n1\n")
        self.assertIn("丁丑日，太乙巳将加酉时", 输出)
        self.assertIn("初传：巳 太常 兄弟", 输出)
        self.assertIn("中传：丑 勾陈 子孙", 输出)
        self.assertIn("末传：酉 贵人 妻财", 输出)
        self.assertIn("一课：丁上卯，天空", 输出)
        self.assertIn("二课：卯上亥，朱雀", 输出)
        self.assertIn("三课：丑上酉，贵人", 输出)
        self.assertIn("四课：酉上巳，太常", 输出)

    # 《精抄历代六壬占验汇选》卷4乙未日司化南占何官，原稿戊子六月乙未未将卯时，公开书影第11页 https://d.zixueguoxue.com/2022/04/1650441050-f06417473b12f17.pdf#page=11
    def test_司化南占何官(self):
        输出 = 运行("大六壬.py", "1648 07 21 05\n1\n1\n")
        self.assertIn("乙未日，小吉未将加卯时", 输出)
        self.assertIn("初传：亥 螣蛇 父母", 输出)
        self.assertIn("中传：卯 玄武 兄弟", 输出)
        self.assertIn("末传：未 青龙 妻财", 输出)
        self.assertIn("一课：乙上申，勾陈", 输出)
        self.assertIn("二课：申上子，贵人", 输出)
        self.assertIn("三课：未上亥，螣蛇", 输出)
        self.assertIn("四课：亥上卯，玄武", 输出)

    # 《景祐六壬神定经》起贵条文未记具年实占；王仁俊《神定经纂》稿本第23页录乙己 https://upload.wikimedia.org/wikipedia/commons/a/ad/NLC892-411999030028-142313_%E6%AD%A3%E5%AD%B8%E5%A0%82%E9%9B%9C%E8%91%97_%E7%AC%AC18%E5%86%8A.pdf#page=23

    # 《六壬大全》课经元首甲子日子将卯时假设例，上图书影PDF第243页；2027-02-14仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=243
    def test_元首甲子起例(self):
        输出 = 运行("大六壬.py", "2027 02 14 05\n1\n1\n")
        self.assertIn("甲子日，神后子将加卯时", 输出)
        self.assertIn("初传：午 青龙", 输出)
        self.assertIn("中传：卯 朱雀", 输出)
        self.assertIn("末传：子 天后", 输出)

    # 《六壬大全》八卷本卷3课经范蠡占郑妃生产，PDF244记四月丁丑日子时申将，未载占年 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=244

    # 《六壬大全》课经观月经七月乙酉日午将寅时假设例，上图书影PDF第245页明记申子辰；2030-08-18仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=245
    def test_候来旬拆身乙酉例(self):
        输出 = 运行("大六壬.py", "2030 08 18 03\n1\n1\n")
        self.assertIn("乙酉日，胜光午将加寅时", 输出)
        self.assertRegex(输出, r"(?m)^初传：申 ")
        self.assertRegex(输出, r"(?m)^中传：子 ")
        self.assertRegex(输出, r"(?m)^末传：辰 ")

    # 《六壬大全》课经重审丙戌日申将巳时假设例，上图书影PDF第248页；2031-06-15仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=248
    def test_重审丙戌起例(self):
        输出 = 运行("大六壬.py", "2031 06 15 09\n1\n1\n")
        self.assertIn("丙戌日，传送申将加巳时", 输出)
        self.assertIn("初传：申 六合", 输出)
        self.assertIn("中传：亥 贵人", 输出)
        self.assertIn("末传：寅 玄武", 输出)

    # 《六壬大全》八卷本卷3课经李司马，PDF248记乙亥日辰时酉将，未载占年 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=248

    # 《六壬大全》课经知一壬辰日辰将巳时假设例，上图书影PDF第251页；2034-10-03仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=251
    def test_知一壬辰起例(self):
        输出 = 运行("大六壬.py", "2034 10 03 09\n1\n1\n")
        self.assertIn("壬辰日，天罡辰将加巳时", 输出)
        self.assertIn("初传：戌 白虎", 输出)
        self.assertIn("中传：酉 太常", 输出)
        self.assertIn("末传：申 玄武", 输出)

    # 《六壬大全》课经涉害正月丁卯日亥将丑时假设例，上图书影PDF第254页；2026-02-22仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=254
    def test_涉害丁卯起例(self):
        输出 = 运行("大六壬.py", "2026 02 22 01\n1\n1\n1\n")
        self.assertIn("丁卯日，登明亥将加丑时", 输出)
        self.assertIn("初传：亥 朱雀", 输出)
        self.assertIn("中传：酉 贵人", 输出)
        self.assertIn("末传：未 太阴", 输出)

    # 《六壬大全》课经见机四月庚子日申将戌时假设例，上图书影PDF第254页；2026-05-26仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=254
    def test_见机庚子起例(self):
        输出 = 运行("大六壬.py", "2026 05 26 19\n1\n1\n1\n")
        self.assertIn("庚子日，传送申将加戌时", 输出)
        self.assertIn("初传：午 螣蛇", 输出)
        self.assertIn("中传：辰 六合", 输出)
        self.assertIn("末传：寅 青龙", 输出)

    # 《六壬大全》课经察微庚戌日申将辰时假设例，上图书影PDF第255页；2026-06-05仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=255
    def test_察微庚戌起例(self):
        输出 = 运行("大六壬.py", "2026 06 05 07\n1\n1\n1\n")
        self.assertIn("庚戌日，传送申将加辰时", 输出)
        self.assertIn("初传：辰 玄武", 输出)
        self.assertIn("中传：申 青龙", 输出)
        self.assertIn("末传：子 螣蛇", 输出)

    # 《六壬大全》课经缀瑕六月甲午日午将辰时假设例，上图书影PDF第255–256页；2034-08-06仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=255
    def test_缀瑕甲午起例(self):
        输出 = 运行("大六壬.py", "2034 08 06 07\n1\n1\n1\n")
        self.assertIn("甲午日，胜光午将加辰时", 输出)
        self.assertIn("初传：辰 六合", 输出)
        self.assertIn("中传：午 青龙", 输出)
        self.assertIn("末传：申 白虎", 输出)

    # 《六壬大全》课经比用乙卯日子将寅时假设例，上图书影PDF第256页；2026-02-10仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=256
    def test_比用乙卯起例(self):
        输出 = 运行("大六壬.py", "2026 02 10 03\n1\n1\n1\n")
        self.assertIn("乙卯日，神后子将加寅时", 输出)
        self.assertIn("初传：亥 玄武", 输出)
        self.assertIn("中传：酉 天后", 输出)
        self.assertIn("末传：未 螣蛇", 输出)

    # 《六壬大全》课经观月经甲辰日亥将卯时假设例，上图书影PDF第256、258页明记子申辰；2029-03-15仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=258
    def test_涉害甲辰起例(self):
        输出 = 运行("大六壬.py", "2029 03 15 05\n1\n1\n1\n")
        self.assertIn("甲辰日，登明亥将加卯时", 输出)
        self.assertRegex(输出, r"(?m)^初传：子 ")
        self.assertRegex(输出, r"(?m)^中传：申 ")
        self.assertRegex(输出, r"(?m)^末传：辰 ")

    # 《六壬大全》课经蒿矢壬辰日申将巳时假设例，上图书影PDF第260页；2032-06-15仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=260
    def test_蒿矢壬辰起例(self):
        输出 = 运行("大六壬.py", "2032 06 15 09\n1\n1\n")
        self.assertIn("壬辰日，传送申将加巳时", 输出)
        self.assertIn("初传：戌 青龙", 输出)
        self.assertIn("中传：丑 太常", 输出)
        self.assertIn("末传：辰 天后", 输出)

    # 《六壬大全》课经弹射壬申日亥将申时假设例，上图书影PDF第260页；2026-02-27仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=260
    def test_弹射壬申起例(self):
        输出 = 运行("大六壬.py", "2026 02 27 15\n1\n1\n")
        self.assertIn("壬申日，登明亥将加申时", 输出)
        self.assertIn("初传：巳 贵人", 输出)
        self.assertIn("中传：申 六合", 输出)
        self.assertIn("末传：亥 天空", 输出)

    # 《六壬大全》课经虎视戊申日辰将卯时假设例，上图书影PDF第265页；2026-10-01仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=265
    def test_虎视戊申起例(self):
        输出 = 运行("大六壬.py", "2026 10 01 05\n1\n1\n")
        self.assertIn("戊申日，天罡辰将加卯时", 输出)
        self.assertIn("初传：戌 玄武", 输出)
        self.assertIn("中传：酉 太常", 输出)
        self.assertIn("末传：午 青龙", 输出)

    # 《六壬大全》课经冬蛇丁丑日丑将辰时假设例，上图书影PDF第265页；2026-01-03仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=265
    def test_冬蛇丁丑起例(self):
        输出 = 运行("大六壬.py", "2026 01 03 07\n1\n1\n")
        self.assertIn("丁丑日，大吉丑将加辰时", 输出)
        self.assertIn("初传：子 螣蛇", 输出)
        self.assertIn("中传：辰 青龙", 输出)
        self.assertIn("末传：戌 天后", 输出)

    # 《六壬大全》课经观月经乙未日寅将辰时假设例，上图书影PDF第267页；2031-12-21仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=267
    def test_冬蛇乙未起例(self):
        输出 = 运行("大六壬.py", "2031 12 21 07\n1\n1\n")
        self.assertIn("乙未日，功曹寅将加辰时", 输出)
        self.assertRegex(输出, r"(?m)^初传：亥 ")
        self.assertRegex(输出, r"(?m)^中传：寅 ")
        self.assertRegex(输出, r"(?m)^末传：巳 ")

    # 《六壬大全》课经别责丙辰日辰将卯时假设例，上图书影PDF第269页；2026-10-09仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=269
    def test_别责丙辰起例(self):
        输出 = 运行("大六壬.py", "2026 10 09 05\n1\n1\n")
        self.assertIn("丙辰日，天罡辰将加卯时", 输出)
        self.assertIn("初传：亥 贵人", 输出)
        self.assertIn("中传：午 青龙", 输出)
        self.assertIn("末传：午 青龙", 输出)

    # 《六壬大全》课经八专甲寅日丑将辰时假设例，上图书影PDF第270页；2030-01-19仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=270
    def test_八专甲寅起例(self):
        输出 = 运行("大六壬.py", "2030 01 19 07\n1\n1\n")
        self.assertIn("甲寅日，大吉丑将加辰时", 输出)
        self.assertIn("初传：丑 贵人", 输出)
        self.assertIn("中传：亥 太阴", 输出)
        self.assertIn("末传：亥 太阴", 输出)

    # 《六壬大全》课经帷簿丁未日辰将丑时假设例，上图书影PDF第271页；2026-09-30仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=271
    def test_帷簿丁未起例(self):
        输出 = 运行("大六壬.py", "2026 09 30 01\n1\n1\n")
        self.assertIn("丁未日，天罡辰将加丑时", 输出)
        self.assertIn("初传：亥 太阴", 输出)
        self.assertIn("中传：戌 天后", 输出)
        self.assertIn("末传：戌 天后", 输出)

    # 《六壬大全》课经独足己未日酉将未时假设例，上图书影PDF第271页；2031-05-19仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=271
    def test_独足己未起例(self):
        输出 = 运行("大六壬.py", "2031 05 19 13\n1\n1\n")
        self.assertIn("己未日，从魁酉将加未时", 输出)
        self.assertIn("初传：酉 六合", 输出)
        self.assertIn("中传：酉 六合", 输出)
        self.assertIn("末传：酉 六合", 输出)

    # 《六壬大全》课经观月经庚申日亥将申时假设例，上图书影PDF第273页；2032-03-15仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=273
    def test_八专庚申起例(self):
        输出 = 运行("大六壬.py", "2032 03 15 15\n1\n1\n")
        self.assertIn("庚申日，登明亥将加申时", 输出)
        self.assertRegex(输出, r"(?m)^初传：丑 ")
        self.assertRegex(输出, r"(?m)^中传：亥 ")
        self.assertRegex(输出, r"(?m)^末传：亥 ")

    # 《六壬大全》课经观月经己未日亥将酉时假设例，上图书影PDF第273页；2031-03-20仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=273
    def test_独脚己未起例(self):
        输出 = 运行("大六壬.py", "2031 03 20 17\n1\n1\n")
        self.assertIn("己未日，登明亥将加酉时", 输出)
        self.assertRegex(输出, r"(?m)^初传：酉 ")
        self.assertRegex(输出, r"(?m)^中传：酉 ")
        self.assertRegex(输出, r"(?m)^末传：酉 ")

    # 《六壬大全》课经伏吟癸巳日午将午时假设例，上图书影PDF第276页；2031-08-21仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=276
    def test_伏吟癸巳起例(self):
        输出 = 运行("大六壬.py", "2031 08 21 11\n1\n1\n")
        self.assertIn("癸巳日，胜光午将加午时", 输出)
        self.assertIn("初传：丑 勾陈", 输出)
        self.assertIn("中传：戌 白虎", 输出)
        self.assertIn("末传：未 太阴", 输出)

    # 《六壬大全》课经自任丙辰日申将申时假设例，上图书影PDF第276页；2026-06-11仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=276
    def test_自任丙辰起例(self):
        输出 = 运行("大六壬.py", "2026 06 11 15\n1\n1\n")
        self.assertIn("丙辰日，传送申将加申时", 输出)
        self.assertIn("初传：巳 天空", 输出)
        self.assertIn("中传：申 玄武", 输出)
        self.assertIn("末传：寅 六合", 输出)

    # 《六壬大全》课经自信丁丑日未将未时假设例，上图书影PDF第277页；2026-07-02仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=277
    def test_自信丁丑起例(self):
        输出 = 运行("大六壬.py", "2026 07 02 13\n1\n1\n")
        self.assertIn("丁丑日，小吉未将加未时", 输出)
        self.assertIn("初传：丑 朱雀", 输出)
        self.assertIn("中传：戌 天后", 输出)
        self.assertIn("末传：未 太常", 输出)

    # 《六壬大全》课经杜传壬辰日酉将酉时假设例，上图书影PDF第278页原图用昼贵；2026-05-18仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=278
    def test_杜传壬辰起例(self):
        输出 = 运行("大六壬.py", "2026 05 18 17\n1\n2\n")
        self.assertIn("壬辰日，从魁酉将加酉时", 输出)
        self.assertIn("初传：亥 天空", 输出)
        self.assertIn("中传：辰 螣蛇", 输出)
        self.assertIn("末传：戌 白虎", 输出)

    # 《六壬大全》课经返吟庚戌日申将寅时假设例，上图书影PDF第282页；2026-06-05仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=282
    def test_返吟庚戌起例(self):
        输出 = 运行("大六壬.py", "2026 06 05 03\n1\n1\n")
        self.assertIn("庚戌日，传送申将加寅时", 输出)
        self.assertIn("初传：寅 白虎", 输出)
        self.assertIn("中传：申 螣蛇", 输出)
        self.assertIn("末传：寅 白虎", 输出)

    # 《六壬大全》课经井栏正月辛丑日亥将巳时假设例，上图书影PDF第282页；2029-03-12仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=282
    def test_井栏辛丑起例(self):
        输出 = 运行("大六壬.py", "2029 03 12 09\n1\n1\n")
        self.assertIn("辛丑日，登明亥将加巳时", 输出)
        self.assertIn("初传：亥 青龙", 输出)
        self.assertIn("中传：未 螣蛇", 输出)
        self.assertIn("末传：辰 太阴", 输出)

    # 《六壬大全》课经返吟观月经丁未日亥将巳时假设例，上图书影PDF第283页；2029-03-18仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=283
    def test_返吟丁未起例(self):
        输出 = 运行("大六壬.py", "2029 03 18 09\n1\n1\n")
        self.assertIn("丁未日，登明亥将加巳时", 输出)
        self.assertRegex(输出, r"(?m)^初传：巳 ")
        self.assertRegex(输出, r"(?m)^中传：丑 ")
        self.assertRegex(输出, r"(?m)^末传：丑 ")

    # 《六壬大全》课经返吟观月经己未日同亥将巳时例假设例，上图书影PDF第283页；2031-03-20仅为原日将时的等价公历输入 https://commons.wikimedia.org/wiki/File:Shanghai_六壬大全八卷.pdf?page=283
    def test_返吟己未起例(self):
        输出 = 运行("大六壬.py", "2031 03 20 09\n1\n1\n")
        self.assertIn("己未日，登明亥将加巳时", 输出)
        self.assertRegex(输出, r"(?m)^初传：巳 ")
        self.assertRegex(输出, r"(?m)^中传：丑 ")
        self.assertRegex(输出, r"(?m)^末传：丑 ")

    # 《御定六壬直指》卷上起例及七百二十立式不是实占，所引指南等占验须回原案核对；贵表及昼夜界已核故宫本第8页 https://upload.wikimedia.org/wikipedia/commons/d/dd/GGZBCK417_%E5%BE%A1%E5%AE%9A%E5%85%AD%E5%A3%AC%E7%9B%B4%E6%8C%87.pdf#page=8

    # 《御定六壬直指》辛卯第一课明确卯子午，并注毕法用卯子卯；这是伏吟互刑异法，具年傅姓案另见指南 https://upload.wikimedia.org/wikipedia/commons/d/dd/GGZBCK417_%E5%BE%A1%E5%AE%9A%E5%85%AD%E5%A3%AC%E7%9B%B4%E6%8C%87.pdf#page=227

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

    # 《六壬指南》庚寅五月问雨，1925年国图扫描第129页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=129
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

    # 《六壬指南》李庚续弦，1925年国图扫描第133页；原刻己丑五月癸酉酉时、课图申将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=133

    # 《六壬指南》东宫田妃六甲，1925年国图扫描第133页；原刻丁丑十月癸丑酉时，图作返吟卯将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=133

    # 《六壬指南》江右傅姓六甲，1925年国图扫描第134页；原刻庚辰三月辛卯戌时、伏吟戌将；原题日将与课图不合（定气、旧历气法）；图卯子卯明确采用循环刑法 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=134

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

    # 《六壬指南》陆夺翼占考试，1925年国图扫描第138页；原图丑时用昼贵 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=138
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

    # 《六壬指南》孙兴功占乡试，1925年国图扫描第139、140页；原题记本日辰、酉两课，第140页只列辰时伏吟图，断语先时发用未与图巳不合，酉课未列完整图 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=139

    # 《六壬指南》孙兴功辰时占乡试，1925年国图扫描第140页；原刻辰时图用夜贵 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=140
    def test_孙兴功辰时占乡试(self):
        输出 = 运行("大六壬.py", "1648 10 10 08\n1\n3\n")
        self.assertIn("丙辰日，天罡辰将加辰时", 输出)
        self.assertIn("初传：巳 勾陈 兄弟", 输出)
        self.assertIn("中传：申 螣蛇 妻财", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)

    # 《六壬指南》何伴鹤代占兄弟乡试，1925年国图扫描第140页；原刻丁卯八月乙巳申时，课图反推辰将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=140

    # 《六壬指南》张盛美门生会试，1925年国图扫描第141页；原刻丁丑正月己巳巳时并明写子将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=141

    # 《六壬指南》王继廉代占会试，1925年国图扫描第142页；原刻甲戌二月戊辰辰时、返吟戌将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=142

    # 《六壬指南》宫子玄占会试，1925年国图扫描第142页；课图在第143页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=142
    def test_宫子玄占会试(self):
        输出 = 运行("大六壬.py", "1643 03 20 06\n1\n1\n")
        self.assertIn("乙丑日，登明亥将加卯时", 输出)
        self.assertIn("初传：巳 青龙 子孙", 输出)
        self.assertIn("中传：丑 螣蛇 妻财", 输出)
        self.assertIn("末传：酉 玄武 官鬼", 输出)

    # 《六壬指南》孙大宜占会试，1925年国图扫描第143页；原刻丁丑二月癸未午时，课图反推戌将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=143

    # 《六壬指南》陈公明占会试，1925年国图扫描第144页；原刻戊辰八月甲戌亥时，课图反推未将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=144

    # 《六壬指南》刘若宜占会试，1925年国图扫描第144页；原刻丁丑二月乙未日戌时，按大统历平气日春分前取亥将 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=144
    def test_刘若宜占会试(self):
        输出 = 运行("大六壬.py", "1637 03 21 19\n2\n1\n1\n")
        self.assertIn("乙未日，登明亥将加戌时", 输出)
        self.assertIn("初传：酉 天后 官鬼", 输出)
        self.assertIn("中传：戌 太阴 妻财", 输出)
        self.assertIn("末传：亥 玄武 父母", 输出)

    # 《六壬指南》吴克孝占会试，1925年国图扫描第145页；原刻丁丑二月乙未日巳时，按大统历平气日春分前取亥将 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=145
    def test_吴克孝占会试(self):
        输出 = 运行("大六壬.py", "1637 03 21 09\n2\n1\n1\n")
        self.assertIn("乙未日，登明亥将加巳时", 输出)
        self.assertIn("初传：戌 朱雀 妻财", 输出)
        self.assertIn("中传：辰 太常 妻财", 输出)
        self.assertIn("末传：戌 朱雀 妻财", 输出)

    # 《六壬指南》王旋官代占升迁，1925年国图扫描第146页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=146
    def test_王旋官代占升迁(self):
        输出 = 运行("大六壬.py", "1631 04 11 14\n1\n1\n")
        self.assertIn("甲申日，河魁戌将加未时", 输出)
        self.assertIn("初传：申 青龙 官鬼", 输出)
        self.assertIn("中传：亥 朱雀 父母", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)

    # 《六壬指南》蔡熙阳占杨司马罢官，1925年国图扫描第147页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=147
    def test_蔡熙阳占杨司马罢官(self):
        输出 = 运行("大六壬.py", "1637 08 21 09\n1\n1\n1\n")
        self.assertIn("戊辰日，胜光午将加巳时", 输出)
        self.assertIn("初传：寅 螣蛇 官鬼", 输出)
        self.assertIn("中传：午 青龙 父母", 输出)
        self.assertIn("末传：午 青龙 父母", 输出)

    # 《六壬指南》汪仙民邵无奇占马康庄入相，1925年国图扫描第147页；原刻戊辰十二月庚寅辰时、图反推寅将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=147

    # 《六壬指南》杨方壶占仕途，1925年国图扫描第148页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=148
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

    # 《六壬指南》阮实夫代占温首揆，1925年国图扫描第150页；原刻丁丑四月丙申日酉时，按大统历平气日小满前取酉将 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=150
    def test_阮实夫代占温首揆(self):
        输出 = 运行("大六壬.py", "1637 05 21 17\n2\n1\n1\n")
        self.assertIn("丙申日，从魁酉将加酉时", 输出)
        self.assertIn("初传：巳 勾陈 兄弟", 输出)
        self.assertIn("中传：申 螣蛇 妻财", 输出)
        self.assertIn("末传：寅 白虎 父母", 输出)

    # 《六壬指南》陆金吾占陈东明出师，1925年国图扫描第150页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=150
    def test_陆金吾占陈东明出师(self):
        输出 = 运行("大六壬.py", "1636 03 12 05\n1\n1\n")
        self.assertIn("辛巳日，登明亥将加卯时", 输出)
        self.assertIn("初传：午 贵人 官鬼", 输出)
        self.assertIn("中传：寅 勾陈 妻财", 输出)
        self.assertIn("末传：戌 太常 父母", 输出)

    # 《六壬指南》阮胤平占入相，1925年国图扫描第151页；原刻丁丑八月己未辰时、图反推巳将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=151

    # 《六壬指南》仇庸足占功名，1925年国图扫描第152页；原刻辛未四月己未辰时、图反推申将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=152

    # 《六壬指南》陈龙正占钱士升入相，1925年国图扫描第153页；原刻癸酉七月甲寅申时、图反推午将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=153

    # 《六壬指南》贺中怜代占周首揆，1925年国图扫描第153页；原图返吟涉害取地盘孟位 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=153
    def test_贺中怜代占周首揆(self):
        输出 = 运行("大六壬.py", "1633 03 11 09\n1\n1\n2\n")
        self.assertIn("甲子日，登明亥将加巳时", 输出)
        self.assertIn("初传：寅 天后 兄弟", 输出)
        self.assertIn("中传：申 青龙 官鬼", 输出)
        self.assertIn("末传：寅 天后 兄弟", 输出)

    # 《六壬指南》孙兴功占赵福星升迁，1925年国图扫描第154页；原刻戊子四月丙子辰时、返吟戌将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=154

    # 《六壬指南》阮胤平占李括苍入相，1925年国图扫描第155页；原刻丁丑七月甲戌巳时、图反推午将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=155

    # 《六壬指南》阮胤平占袁郑枚卜，1925年国图扫描第156页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=156
    def test_阮胤平占袁郑枚卜(self):
        输出 = 运行("大六壬.py", "1637 09 18 09\n1\n1\n")
        self.assertIn("丙申日，太乙巳将加巳时", 输出)
        self.assertIn("初传：巳 天空 兄弟", 输出)
        self.assertIn("中传：申 玄武 妻财", 输出)
        self.assertIn("末传：寅 六合 父母", 输出)

    # 《六壬指南》陈公明占黄虎山功名，1925年国图扫描第156页；原刻甲申十月；依年日时及课图卯将反推1644-10-26九月廿六 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=156
    # def test_陈公明占黄虎山功名(self):
    #     输出 = 运行("大六壬.py", "1644 10 26 21\n1\n1\n")
    #     self.assertIn("辛亥日，太冲卯将加亥时", 输出)
    #     self.assertIn("初传：未 白虎 父母", 输出)
    #     self.assertIn("中传：亥 六合 子孙", 输出)
    #     self.assertIn("末传：卯 天后 妻财", 输出)

    # 《六壬指南》刘一纯占梁司马冢宰，1925年国图扫描第157页；原刻辛未四月丁酉卯时、图反推戌将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=157

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
        输出 = 运行("大六壬.py", "1638 03 22 09\n1\n1\n1\n")
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

    # 《六壬指南》司化南占何官，1925年国图扫描第162页；原刻戊子六月乙未未时、图反推亥将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=162

    # 《六壬指南》涂松亭占彭南溟升迁，1925年国图扫描第162页；原刻丁卯正月；依年日时及课图子将反推1628-01-30丁卯十二月廿四 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=162
    # def test_涂松亭占彭南溟升迁(self):
    #     输出 = 运行("大六壬.py", "1628 01 30 05\n1\n1\n")
    #     self.assertIn("丁巳日，神后子将加卯时", 输出)
    #     self.assertIn("初传：亥 贵人 官鬼", 输出)
    #     self.assertIn("中传：申 玄武 妻财", 输出)
    #     self.assertIn("末传：巳 天空 兄弟", 输出)

    # 《六壬指南》潘云从占郑潜奄升迁，1925年国图扫描第163页；原刻庚辰正月丁丑卯时，四课反推亥将而三传写寅卯辰；按四课下贼应巳丑酉，与原题从革相合，原图四课与三传栏不合 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=163

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

    # 《六壬指南》孙兴功仕扬占功名，1925年国图扫描第165页；原刻辛巳七月己未酉时、图反推寅将；原题日将与课图不合（定气、旧历气法）；图末传卯乘太阴亦与所排贵人序不合 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=165

    # 《六壬指南》胡道台令乔中军索占，1925年国图扫描第166页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=166
    def test_胡道台令乔中军索占(self):
        输出 = 运行("大六壬.py", "1648 08 21 21\n1\n1\n")
        self.assertIn("丙寅日，胜光午将加亥时", 输出)
        self.assertIn("初传：子 六合 官鬼", 输出)
        self.assertIn("中传：未 太阴 子孙", 输出)
        self.assertIn("末传：寅 青龙 父母", 输出)

    # 《六壬指南》蔡熙阳推吴淞总戎，1925年国图扫描第167页；原刻戊寅二月丙午戌时、图反推卯将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=167

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

    # 《六壬指南》方潜夫奉诏进京，1925年国图扫描第170页；原刻壬午十月辛未午时、图为丑将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=170

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

    # 《六壬指南》寇道台占仕途，1925年国图扫描第173页；原刻癸酉六月戊寅未时伏吟；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=173

    # 《六壬指南》江半石占钦差，1925年国图扫描第174页；原刻己巳二月乙巳巳时，课图反推戌将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=174

    # 《六壬指南》胡尹占巡按差，1925年国图扫描第175页；原刻辛卯二月戊子日午时，1651-03-01为二月初十，按原纪年、日、将、时核盘 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=175
    def test_胡尹占巡按差(self):
        输出 = 运行("大六壬.py", "1651 03 01 11\n1\n1\n")
        self.assertIn("戊子日，登明亥将加午时", 输出)
        self.assertIn("初传：巳 太常 父母", 输出)
        self.assertIn("中传：戌 六合 兄弟", 输出)
        self.assertIn("末传：卯 太阴 官鬼", 输出)

    # 《六壬指南》张维枢占章奏，1925年国图扫描第176页；原刻己巳正月己未午时、四课反推丑将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=176

    # 《六壬指南》董兑之代董玄宰辞大宗伯，1925年国图扫描第177页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=177
    def test_董兑之代董玄宰辞大宗伯(self):
        输出 = 运行("大六壬.py", "1633 08 14 19\n1\n1\n")
        self.assertIn("庚子日，胜光午将加戌时", 输出)
        self.assertIn("初传：子 青龙 子孙", 输出)
        self.assertIn("中传：申 螣蛇 兄弟", 输出)
        self.assertIn("末传：辰 玄武 父母", 输出)

    # 《六壬指南》刘退斋占何如人，1925年国图扫描第177页；原刻丁丑八月壬寅卯时、四课反推巳将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=177

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

    # 《六壬指南》王旋官占上疏，1925年国图扫描第179页；原刻辛未六月癸卯日卯时，1631-06-29为六月初一；原课涉害按地盘孟仲季取用 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=179
    def test_王旋官占上疏(self):
        输出 = 运行("大六壬.py", "1631 06 29 05\n1\n1\n2\n")
        self.assertIn("癸卯日，小吉未将加卯时", 输出)
        self.assertIn("初传：酉 勾陈 父母", 输出)
        self.assertIn("中传：丑 太常 官鬼", 输出)
        self.assertIn("末传：巳 贵人 妻财", 输出)

    # 《六壬指南》刘退斋请假省亲，1925年国图扫描第180页；丁丑四月丁酉巳时，《明史》大统原式小满在当日13:47，巳时仍为酉将 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=180
    def test_刘退斋请假省亲(self):
        输出 = 运行("大六壬.py", "1637 05 22 09\n2\n1\n1\n")
        self.assertIn("丁酉日，从魁酉将加巳时", 输出)
        self.assertIn("初传：亥 贵人 官鬼", 输出)
        self.assertIn("中传：卯 太常 父母", 输出)
        self.assertIn("末传：未 勾陈 子孙", 输出)

    # 《六壬指南》沈云生占回奏，1925年国图扫描第181页；原刻癸酉二月丁丑午时、四课反推亥将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=181

    # 《六壬指南》孙三杰代丁科长守科失红本，1925年国图扫描第182页；原刻丁丑十一月丁亥申时、返吟寅将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=182

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

    # 《六壬指南》冯允升被逮求占，1925年国图扫描第184页；原刻丙子三月；依年日时及课图戌将反推1636-03-26二月二十 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=184
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

    # 《六壬指南》埂子街甲午客袖占，1925年国图扫描第185页；原刻壬午七月甲午午时、图反推巳将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=185

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

    # 《六壬指南》吴振缨被逮索占，1925年国图扫描第188页；原刻丙子二月乙酉巳时、图反推戌将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=188

    # 《六壬指南》盛顺被逮进京，1925年国图扫描第189页；原刻癸未七月丁未未时、图反推辰将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=189

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

    # 《六壬指南》谭懋芳李父母被逮，1925年国图扫描第191页；原题丁丑十一月丁亥日戊申时，四课却为癸未辰时；依原年及课图日将时反推1638-01-03十一月十九 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=191
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

    # 《六壬指南》建龙寺丽天索占，1925年国图扫描第194页；原刻丙寅四月丙寅寅时、图反推酉将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=194

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

    # 《六壬指南》弯子街二人占子逃，1925年国图扫描第196页；原刻庚寅四月乙酉日巳时，1650-05-02为四月初二，按原纪年、日、将、时核盘 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=196
    def test_弯子街二人占子逃(self):
        输出 = 运行("大六壬.py", "1650 05 02 09\n1\n1\n")
        self.assertIn("乙酉日，从魁酉将加巳时", 输出)
        self.assertIn("初传：申 勾陈 官鬼", 输出)
        self.assertIn("中传：子 贵人 父母", 输出)
        self.assertIn("末传：辰 太常 妻财", 输出)

    # 《六壬指南》李六生问燕京安危，1925年国图扫描第197页；原课图卯发用，断语作戌发用 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=197
    def test_李六生问燕京安危(self):
        输出 = 运行("大六壬.py", "1644 05 08 07\n1\n1\n")
        self.assertIn("庚申日，从魁酉将加辰时", 输出)
        self.assertIn("初传：卯 太阴 妻财", 输出)
        self.assertIn("中传：丑 贵人 父母", 输出)
        self.assertIn("末传：丑 贵人 父母", 输出)

    # 《六壬指南》田百原闻睢州兵变，扫描第197、198页原题戊午日丙申时与图干丙不合；图用子将，按图丙午旧历为子将 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=197

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

    # 《六壬指南》王总兵闻大同兵变，扫描第200页原刻五月；辛巳亥将对应1649-03-04正月廿二 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=200
    # def test_王总兵闻大同兵变(self):
    #     输出 = 运行("大六壬.py", "1649 03 04 05\n1\n1\n")
    #     self.assertIn("辛巳日，登明亥将加卯时", 输出)
    #     self.assertIn("初传：午 贵人 官鬼", 输出)
    #     self.assertIn("中传：寅 勾陈 妻财", 输出)
    #     self.assertIn("末传：戌 太常 父母", 输出)

    # 《六壬指南》武昌城池安危，1925年国图扫描第201页；己丑三月是诸友出示晋戴洋旧课的时间，原占未记具体年日 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=201

    # 《六壬指南》扬城被围，1925年国图扫描第202页；原题庚申年；原课图日将时可对应甲申1644-06-17五月十三，原年与该反推日期不合 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=202
    # def test_扬城被围(self):
    #     输出 = 运行("大六壬.py", "1644 06 17 09\n1\n1\n")
    #     self.assertIn("庚子日，传送申将加巳时", 输出)
    #     self.assertIn("初传：午 白虎 官鬼", 输出)
    #     self.assertIn("中传：酉 勾陈 兄弟", 输出)
    #     self.assertIn("末传：子 螣蛇 子孙", 输出)

    # 《六壬指南》卞孟井问真定安危，1925年国图扫描第202页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=202
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

    # 《六壬指南》辛未四月兵警，1925年国图扫描第206页；原图丙子酉将酉时伏吟，1631年丙子均不在酉将期；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=206

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

    # 《六壬指南》倪子玄占父到京，1925年国图扫描第209页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=209
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

    # 《六壬指南》张奉初为观初占病，1925年国图扫描第211页；原刻辛巳九月；依年日时及课图午将反推1641-08-19七月十三，原图丑时用昼贵 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=211
    # def test_张奉初为观初占病(self):
    #     输出 = 运行("大六壬.py", "1641 08 19 01\n1\n2\n")
    #     self.assertIn("丁亥日，胜光午将加丑时", 输出)
    #     self.assertIn("初传：巳 天空 兄弟", 输出)
    #     self.assertIn("中传：戌 螣蛇 子孙", 输出)
    #     self.assertIn("末传：卯 太常 父母", 输出)

    # 《六壬指南》张奉初案后匿名人复占，仅录未亥卯三传及白虎发用，未记占时与完整课图 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=211

    # 《六壬指南》张澹宁占病，1925年国图扫描第212页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=212
    def test_张澹宁占病(self):
        输出 = 运行("大六壬.py", "1639 07 23 07\n1\n1\n1\n")
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

    # 《六壬指南》楠姓为董晋侯占病，1925年国图扫描第213页；辛卯二月丁未卯时按历书中气日为戌将，原题八专，三传与逐课取克相合 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=213
    def test_楠姓为董晋侯占病(self):
        输出 = 运行("大六壬.py", "1651 03 20 05\n2\n1\n1\n1\n")
        self.assertIn("丁未日，河魁戌将加卯时", 输出)
        self.assertIn("初传：酉 太阴 妻财", 输出)
        self.assertIn("中传：辰 青龙 子孙", 输出)
        self.assertIn("末传：亥 贵人 官鬼", 输出)

    # 《六壬指南》王养吾占妻病，1925年国图扫描第214页；原刻乙丑十月辛亥午时、图反推卯将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=214

    # 《六壬指南》刘一纯占病，1925年国图扫描第215页；原刻辛未正月；依年日时及课图亥将反推1631-03-06二月初四 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=215
    # def test_刘一纯占病(self):
    #     输出 = 运行("大六壬.py", "1631 03 06 13\n1\n1\n")
    #     self.assertIn("戊申日，登明亥将加未时", 输出)
    #     self.assertIn("初传：辰 玄武 兄弟", 输出)
    #     self.assertIn("中传：申 青龙 子孙", 输出)
    #     self.assertIn("末传：子 螣蛇 妻财", 输出)

    # 《六壬指南》陈惟一占扬州道台病，1925年国图扫描第216页；原刻己丑八月；依年日时及伏吟午将反推1649-07-31六月廿二 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=216
    # def test_陈惟一占扬州道台病(self):
    #     输出 = 运行("大六壬.py", "1649 07 31 11\n1\n1\n")
    #     self.assertIn("庚戌日，胜光午将加午时", 输出)
    #     self.assertIn("初传：申 白虎 兄弟", 输出)
    #     self.assertIn("中传：寅 螣蛇 妻财", 输出)
    #     self.assertIn("末传：巳 勾陈 官鬼", 输出)

    # 《六壬指南》程孝延代郑姓占病，1925年国图扫描第217页；原刻己丑八月乙未巳时、图反推午将；原题日将与课图不合（定气、旧历气法） https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=217

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

    # 《六壬指南》敏若夜闻鸦鸣，1925年国图扫描第219页；原刻己丑三月乙丑日亥时，1649-04-17为三月初六，按原纪年、日、将、时核盘 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=219
    def test_敏若夜闻鸦鸣(self):
        输出 = 运行("大六壬.py", "1649 04 17 21\n1\n1\n")
        self.assertIn("乙丑日，河魁戌将加亥时", 输出)
        self.assertIn("初传：子 太常 父母", 输出)
        self.assertIn("中传：亥 玄武 父母", 输出)
        self.assertIn("末传：戌 太阴 妻财", 输出)

    # 《六壬指南》吴三占天宁寺夜惊，1925年国图扫描第220页；课图在第221页 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=220
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

    # 《六壬指南》陈开子司化南射覆文书，1925年国图扫描第223页；图在第224页，用昼贵与地盘孟位涉害，原文另论东方朔本课亥酉未 https://commons.wikimedia.org/wiki/File:NLC416-12jh005348-45347_六壬指南.pdf?page=223
    def test_陈开子司化南射覆文书(self):
        输出 = 运行("大六壬.py", "1650 06 30 17\n1\n2\n2\n")
        self.assertIn("甲申日，小吉未将加酉时", 输出)
        self.assertIn("初传：午 青龙 子孙", 输出)
        self.assertIn("中传：辰 六合 妻财", 输出)
        self.assertIn("末传：寅 螣蛇 兄弟", 输出)
