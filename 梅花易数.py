from datetime import datetime
from zhdate import ZhDate
from re import findall

六十四卦 = (
    "䷁ 坤为地", "䷖ 山地剥", "䷇ 水地比", "䷓ 风地观", "䷏ 雷地豫", "䷢ 火地晋", "䷬ 泽地萃", "䷋ 天地否",
    "䷎ 地山谦", "䷳ 艮为山", "䷦ 水山蹇", "䷴ 风山渐", "䷽ 雷山小过", "䷷ 火山旅", "䷞ 泽山咸", "䷠ 天山遁",
    "䷆ 地水师", "䷃ 山水蒙", "䷜ 坎为水", "䷺ 风水涣", "䷧ 雷水解", "䷿ 火水未济", "䷮ 泽水困", "䷅ 天水讼",
    "䷭ 地风升", "䷑ 山风蛊", "䷯ 水风井", "䷸ 巽为风", "䷟ 雷风恒", "䷱ 火风鼎", "䷛ 泽风大过", "䷫ 天风姤",
    "䷗ 地雷复", "䷚ 山雷颐", "䷂ 水雷屯", "䷩ 风雷益", "䷲ 震为雷", "䷔ 火雷噬嗑", "䷐ 泽雷随", "䷘ 天雷无妄",
    "䷣ 地火明夷", "䷕ 山火贲", "䷾ 水火既济", "䷤ 风火家人", "䷶ 雷火丰", "䷝ 离为火", "䷰ 泽火革", "䷌ 天火同人",
    "䷒ 地泽临", "䷨ 山泽损", "䷻ 水泽节", "䷼ 风泽中孚", "䷵ 雷泽归妹", "䷥ 火泽睽", "䷹ 兑为泽", "䷉ 天泽履",
    "䷊ 地天泰", "䷙ 山天大畜", "䷄ 水天需", "䷈ 风天小畜", "䷡ 雷天大壮", "䷍ 火天大有", "䷪ 泽天夬", "䷀ 乾为天"
)

今时 = (
    int(str(ZhDate.from_datetime(datetime.now()))[2:6]) % 12 - 3 if int(str(ZhDate.from_datetime(
        datetime.now()))[2:6]) % 12 > 3 else int(str(ZhDate.from_datetime(datetime.now()))[2:6]) % 12 + 9,
    int(findall(r'年(\d\d?)月', str(ZhDate.from_datetime(datetime.now())))[0]),
    int(findall(r'月(\d\d?)日', str(
        ZhDate.from_datetime(datetime.now())))[0]),
    (int((int(datetime.now().strftime("%H")) - 7) % 24 / 2) + 2) % 12
)


def 年月日时起卦() -> str:
    上卦 = (8 - sum(今时[:3]) % 8) % 8
    下卦 = (8 - sum(今时) % 8) % 8
    动爻 = sum(今时) % 6

    print(六十四卦[int(bin(下卦)[2:].zfill(3) + bin(上卦)[2:].zfill(3), 2)], end="\n\t")
    if 动爻:
        print("变卦为：" + 六十四卦[int(bin(int(bin(上卦)[2:].zfill(3)[::-1] + bin(下卦)
              [2:].zfill(3)[::-1], 2) ^ 1 << 动爻 - 1)[2:].zfill(6)[::-1], 2)])
    else:
        print("无变卦")


def 以数起卦(n: tuple[int]) -> str:
    上卦 = (8 - n[0] % 8) % 8
    下卦 = (8 - n[1] % 8) % 8
    动爻 = sum(n) % 6

    print(六十四卦[int(bin(下卦)[2:].zfill(3) + bin(上卦)[2:].zfill(3), 2)], end="\n\t")
    if 动爻:
        print("变卦为：" + 六十四卦[int(bin(int(bin(上卦)[2:].zfill(3)[::-1] + bin(下卦)
              [2:].zfill(3)[::-1], 2) ^ 1 << 动爻 - 1)[2:].zfill(6)[::-1], 2)])
    else:
        print("无变卦")


取数 = str(input("输入2个自然数，用空格分隔；\n或直接回车以使用当前年月日时起卦："))

if len(取数) == 0:
    年月日时起卦()
elif len(tuple(map(int, 取数.split(" ")))) == 2 and all(_ >= 0 for _ in tuple(map(int, 取数.split(" ")))):
    以数起卦(tuple(map(int, 取数.split(" "))))
else:
    print("输入应当为空或两个自然数")
