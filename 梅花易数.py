from datetime import datetime
from zhdate import ZhDate

先天八卦 = (7, 3, 5, 1, 6, 2, 4, 0)

六十四卦 = (
    "坤为地", "地雷复", "地水师", "地泽临", "地山谦", "地火明夷", "地风升", "地天泰",
    "雷地豫", "震为雷", "雷水解", "雷泽归妹", "雷山小过", "雷火丰", "雷风恒", "雷天大壮",
    "水地比", "水雷屯", "坎为水", "水泽节", "水山蹇", "水火既济", "水风井", "水天需",
    "泽地萃", "泽雷随", "泽水困", "兑为泽", "泽山咸", "泽火革", "泽风大过", "泽天夬",
    "山地剥", "山雷颐", "山水蒙", "山泽损", "艮为山", "山火贲", "山风蛊", "山天大畜",
    "火地晋", "火雷噬嗑", "火水未济", "火泽睽", "火山旅", "离为火", "火风鼎", "火天大有",
    "风地观", "风雷益", "风水涣", "风泽中孚", "风山渐", "风火家人", "巽为风", "风天小畜",
    "天地否", "天雷无妄", "天水讼", "天泽履", "天山遁", "天火同人", "天风姤", "乾为天"
)

今时 = (
    int(str(ZhDate.from_datetime(datetime.now()))[2:6]) % 12 - 3 if int(str(ZhDate.from_datetime(
        datetime.now()))[2:6]) % 12 > 3 else int(str(ZhDate.from_datetime(datetime.now()))[2:6]) % 12 + 9,
    int(str(ZhDate.from_datetime(datetime.now()))[7:9]),
    int(str(ZhDate.from_datetime(datetime.now()))[10:12]),
    (int((int(datetime.now().strftime("%H")) - 7) % 24 / 2) + 2) % 12
)


def 年月日时起卦() -> str:
    上卦 = 先天八卦[sum(今时[:3]) % 8 - 1]

    下卦 = 先天八卦[sum(今时) % 8 - 1]

    动爻 = sum(今时) % 6
    if 动爻:
        return 六十四卦[int(bin(上卦)[2:].zfill(3) + bin(下卦)[2:].zfill(3), 2)
                    ^ int(bin(1 << 动爻 - 1)[2:], 2)]
    else:
        return 六十四卦[int(bin(上卦)[2:].zfill(3) + bin(下卦)[2:].zfill(3), 2)]


def 以数起卦(n: tuple[int]) -> str:
    上卦 = 先天八卦[n[0] % 8 - 1]

    下卦 = 先天八卦[n[1] % 8 - 1]

    动爻 = sum(n) % 6
    if 动爻:
        return 六十四卦[int(bin(上卦)[2:].zfill(3) + bin(下卦)[2:].zfill(3), 2)
                    ^ int(bin(1 << 动爻 - 1)[2:], 2)]
    else:
        return 六十四卦[int(bin(上卦)[2:].zfill(3) + bin(下卦)[2:].zfill(3), 2)]


取数 = str(input("输入2个自然数，用空格分隔；\n或直接回车以使用当前年月日时起卦："))

if len(取数) == 0:
    print(年月日时起卦())
elif len(tuple(map(int, 取数.split(" ")))) == 2 and all(_ >= 0 for _ in tuple(map(int, 取数.split(" ")))):
    print(以数起卦(tuple(map(int, 取数.split(" ")))))
else:
    print("输入应当为空或两个自然数")
