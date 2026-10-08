import unittest

from . import 运行


class 古籍占例(unittest.TestCase):
    # 《绘图增广玉匣记》扫叶山房本影202“李淳风六壬时课”，假如三月初五辰时，小吉 https://archive.org/details/20241205_20241205_0310/page/n201/mode/1up

    def test_玉匣记三月初五辰时(self):
        输出 = 运行("小六壬.py", "1\n3 5 5\n")
        self.assertTrue(输出.endswith("小吉\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一留连上起子时 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一子时(self):
        输出 = 运行("小六壬.py", "2\n1 1 1\n")
        self.assertTrue(输出.endswith("留连\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一丑时速喜 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一丑时(self):
        输出 = 运行("小六壬.py", "2\n1 1 2\n")
        self.assertTrue(输出.endswith("速喜\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一寅时赤口 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一寅时(self):
        输出 = 运行("小六壬.py", "2\n1 1 3\n")
        self.assertTrue(输出.endswith("赤口\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一卯时小吉 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一卯时(self):
        输出 = 运行("小六壬.py", "2\n1 1 4\n")
        self.assertTrue(输出.endswith("小吉\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一辰时空亡 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一辰时(self):
        输出 = 运行("小六壬.py", "2\n1 1 5\n")
        self.assertTrue(输出.endswith("空亡\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一巳时大安 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一巳时(self):
        输出 = 运行("小六壬.py", "2\n1 1 6\n")
        self.assertTrue(输出.endswith("大安\n"))

    # 《多能鄙事》卷八“小六壬课时”，正月初一午时又为留连 https://upload.wikimedia.org/wikipedia/commons/f/f0/Shanghai_多能鄙事十二卷.pdf#page=196

    def test_多能鄙事正月初一午时(self):
        输出 = 运行("小六壬.py", "2\n1 1 7\n")
        self.assertTrue(输出.endswith("留连\n"))
