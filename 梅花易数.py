from datetime import datetime
from zhdate import ZhDate
from 易卦 import 六十四卦

时刻 = datetime.now()
农历 = ZhDate.from_datetime(datetime(时刻.year, 时刻.month, 时刻.day))
今时: tuple[int, int, int, int] = (
    (农历.lunar_year - 4) % 12 + 1,
    农历.lunar_month,
    农历.lunar_day,
    (时刻.hour + 1) // 2 % 12 + 1,
)


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
    input("输入2个自然数，用空格分隔；\n或直接回车以使用当前年月日时起卦：")
)

if len(取数) == 0:
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
