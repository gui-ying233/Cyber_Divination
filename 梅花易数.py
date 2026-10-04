from datetime import datetime
from vendor.zhdate.zhdate import ZhDate
from 易卦 import 六十四卦
from 历法 import 公历时刻

def reverse3(n: int) -> int:
    return ((n & 0b001) << 2) | ((n & 0b010)) | ((n & 0b100) >> 2)


def reverse6(n: int) -> int:
    return (
        ((n & 0b000001) << 5)
        | ((n & 0b000010) << 3)
        | ((n & 0b000100) << 1)
        | ((n & 0b001000) >> 1)
        | ((n & 0b010000) >> 3)
        | ((n & 0b100000) >> 5)
    )


取数: str = str(
    input("输入2个自然数，用空格分隔；\n或直接回车以公历时刻起卦：")
)

if len(取数) == 0:
    时刻 = 公历时刻(input("输入公历年月日时（北京时间，如2026 10 04 13；回车为当前时刻）："), True)
    try:
        农历 = ZhDate.from_datetime(datetime(时刻.year, 时刻.month, 时刻.day))
    except (IndexError, ValueError) as 错误:
        raise ValueError("该公历日期超出ZhDate支持的农历范围") from 错误
    今时: tuple[int, int, int, int] = ((农历.lunar_year - 4) % 12 + 1, 农历.lunar_month, 农历.lunar_day, (时刻.hour + 1) // 2 % 12 + 1)
    上卦, 下卦, 动爻 = (
        (8 - sum(今时[:3]) % 8) % 8,
        (8 - sum(今时) % 8) % 8,
        sum(今时) % 6 or 6,
    )
elif (
    (数 := tuple(map(int, 取数.split())))
    and len(数) == 2
    and all(_ >= 0 for _ in 数)
):
    上卦, 下卦, 动爻 = (8 - 数[0] % 8) % 8, (8 - 数[1] % 8) % 8, sum(数) % 6 or 6
else:
    raise ValueError("输入应当为空或两个自然数")

print(六十四卦[下卦 << 3 | 上卦], end="\n\t")
print(
    "变卦为："
    + 六十四卦[
        reverse6(((reverse3(上卦) << 3) | reverse3(下卦)) ^ (1 << (动爻 - 1)))
    ]
)
