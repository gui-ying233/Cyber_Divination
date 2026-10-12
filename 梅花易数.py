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
    input("输入上卦、下卦两个自然数；加时取动爻可再输入时数（子1至亥12），用空格分隔；\n或输入原载年月日时四数（年、时按子1至亥12），可加第五个附加数；\n已知卦象与动爻可输入上、下卦序数 / 动爻，例如1 8 / 1；\n或直接回车以公历时刻起卦：")
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
elif "/" in 取数:
    卦数文本, 爻数文本 = 取数.split("/")
    卦数 = tuple(map(int, 卦数文本.split()))
    动爻 = int(爻数文本)
    if len(卦数) != 2 or not all(1 <= _ <= 8 for _ in 卦数) or not 1 <= 动爻 <= 6:
        raise ValueError("请输入上、下卦序数 / 动爻；卦序1～8，动爻1～6")
    上卦, 下卦 = (8 - 卦数[0]) % 8, (8 - 卦数[1]) % 8
elif (
    (数 := tuple(map(int, 取数.split())))
    and (len(数) == 2 or len(数) == 3 and 1 <= 数[2] <= 12)
    and all(_ >= 0 for _ in 数)
):
    上卦, 下卦, 动爻 = (8 - 数[0] % 8) % 8, (8 - 数[1] % 8) % 8, sum(数) % 6 or 6
elif (
    (len(数) == 4 or len(数) == 5)
    and 1 <= 数[0] <= 12
    and 1 <= 数[1] <= 12
    and 1 <= 数[2] <= 30
    and 1 <= 数[3] <= 12
    and all(_ >= 0 for _ in 数)
):
    年月日数 = sum(数[:3]) + (数[4] if len(数) == 5 else 0)
    总数 = 年月日数 + 数[3]
    上卦, 下卦, 动爻 = (8 - 年月日数 % 8) % 8, (8 - 总数 % 8) % 8, 总数 % 6 or 6
else:
    raise ValueError("请输入两个自然数及可选时数，或原载年月日时数及可选附加数；年、月、时1～12，日1～30")

print(六十四卦[下卦 << 3 | 上卦], end="\n\t")
print(
    "变卦为："
    + 六十四卦[
        reverse6(((reverse3(上卦) << 3) | reverse3(下卦)) ^ (1 << (动爻 - 1)))
    ]
)
