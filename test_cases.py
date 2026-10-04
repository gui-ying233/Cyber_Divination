import subprocess
import sys
import unittest
from pathlib import Path


目录 = Path(__file__).resolve().parent


def 运行(脚本: str, 输入: str) -> str:
    return subprocess.run(
        [sys.executable, "-B", str(目录 / 脚本)],
        input=输入,
        text=True,
        capture_output=True,
        check=True,
        cwd=目录,
        timeout=5,
    ).stdout


class 古籍占例(unittest.TestCase):
    # 《梅花易数》卷一“西林寺牌额占” https://zh.wikisource.org/wiki/梅花易數/卷一#西林寺牌額占
    def test_西林寺牌额(self):
        初占 = 运行("梅花易数.py", "7 8\n")
        改额 = 运行("梅花易数.py", "7 10\n")
        self.assertIn("䷖ 山地剥\n\t变卦为：䷳ 艮为山", 初占)
        self.assertIn("䷨ 山泽损\n\t变卦为：䷼ 风泽中孚", 改额)

    # 《梅花易数》卷一“今日动静如何”实占 https://zh.wikisource.org/wiki/梅花易數/卷一#今日動靜如何
    def test_今日动静如何(self):
        输出 = 运行("梅花易数.py", "8 5\n")
        self.assertIn("䷭ 地风升\n\t变卦为：䷊ 地天泰", 输出)

    # 《增删卜易》辰月戊申占父病；背数按所载爻画及占卦法换算 https://zh.wikisource.org/wiki/增刪卜易/9 https://www.shidianguji.com/book/XYXZSBY/chapter/1laba3s8ovar2
    def test_辰月戊申占父病(self):
        钱卦 = 运行("金钱卦.py", "1\n1 1 1 3 1 1\n")
        纳甲 = 运行("六爻纳甲.py", "7 7 7 9 7 7\n戊\n1\n")
        self.assertIn("本卦：䷀ 乾为天", 钱卦)
        self.assertIn("动爻：四爻", 钱卦)
        self.assertIn("变卦：䷈ 风天小畜", 钱卦)
        self.assertIn("主卦：䷀ 乾为天（乾宫，属金，世6应3）", 纳甲)
        self.assertIn("变卦：䷈ 风天小畜", 纳甲)
        self.assertIn("四爻 玄武 官鬼 壬午 ⚊ ○", 纳甲)
        self.assertIn("→ 父母 辛未", 纳甲)

    # 《增删卜易》“六合章”四次实占；背数按所载爻画换算 https://zh.wikisource.org/wiki/增刪卜易/19
    def test_六合章四次实占(self):
        占例 = (
            ("申月丙子占出门", "3 2 1 0 2 2", "9 8 7 6 8 8", "丙", "䷣ 地火明夷", "䷽ 雷山小过", "初爻、四爻", "世4应1"),
            ("未月丁巳占悔婚", "3 2 1 1 2 1", "9 8 7 7 8 7", "丁", "䷝ 离为火", "䷷ 火山旅", "初爻", "世6应3"),
            ("卯月甲寅占风水", "0 1 2 3 1 2", "6 7 8 9 7 8", "甲", "䷮ 泽水困", "䷻ 水泽节", "初爻、四爻", "世1应4"),
            ("卯月丁巳争田水", "3 2 3 3 2 3", "9 8 9 9 8 9", "丁", "䷝ 离为火", "䷁ 坤为地", "初爻、三爻、四爻、上爻", "世6应3"),
        )
        for 事, 背数, 爻数, 日干, 本卦, 变卦, 动爻, 世应 in 占例:
            with self.subTest(事=事):
                钱卦 = 运行("金钱卦.py", f"1\n{背数}\n")
                纳甲 = 运行("六爻纳甲.py", f"{爻数}\n{日干}\n1\n")
                self.assertIn(f"本卦：{本卦}", 钱卦)
                self.assertIn(f"变卦：{变卦}", 钱卦)
                self.assertIn(f"动爻：{动爻}", 钱卦)
                self.assertIn(f"主卦：{本卦}", 纳甲)
                self.assertIn(f"变卦：{变卦}", 纳甲)
                self.assertIn(世应, 纳甲)

    # 《太乙金钥匙》续集嘉靖四十年辛酉岁、戊戌月、丁未日、庚戌时占例 https://www.shidianguji.com/zh/book/NGJ89241199902106666022/chapter/1lq8dkylq3yn8
    def test_嘉靖四十年太乙四计(self):
        占例 = (
            ("1\n1561\n", ("庚子元第22局", "巽9宫", "文昌：阴德（乾）", "主算：16", "客算：30")),
            ("2\n1561\n11\n", ("壬子元第47局", "巽9宫", "文昌：高丛（卯）", "主算：4", "客算：8")),
            ("3\n1\n1\n44\n", ("甲子元第44局", "坎8宫", "文昌：阳德（丑）", "主算：33", "客算：14")),
            ("4\n1\n74\n11\n", ("戊子元第23局", "巽9宫", "文昌：阴德（乾）", "主算：16", "客算：23")),
        )
        for 输入, 结果 in 占例:
            with self.subTest(输入=输入):
                输出 = 运行("太乙.py", 输入)
                for 字样 in 结果:
                    self.assertIn(字样, 输出)

    # 《太乙金镜式经》卷一梁天监三年甲申六月八日积日例 https://zh.wikisource.org/wiki/太乙金鏡式經_(四庫全書本)/卷01
    def test_梁天监三年太乙日计(self):
        输出 = 运行("太乙.py", "3\n2\n707501061\n")
        self.assertIn("庚子元第45局", 输出)
        self.assertIn("太乙：坎8宫", 输出)
        self.assertIn("文昌：和德（艮）", 输出)
