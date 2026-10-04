from vendor.zhdate.zhdate import ZhDate
from datetime import datetime
from 历法 import 公历时刻

六神: tuple[str, ...] = ("大安", "留连", "速喜", "赤口", "小吉", "空亡")


def 入卦(n: tuple[int, ...], 算法: str) -> str:
    return 六神[(sum(n) - len(n) + (1 if 算法 == "2" else 0)) % 6]


算法 = input("选择算法：1《玉匣记》（正月初一子时大安）；2《多能鄙事》（正月初一子时留连）：")
if 算法 not in ("1", "2"):
    raise ValueError("请输入1或2选择算法")

取数 = str(input("输入任意个数，用空格分隔；\n或直接回车以公历时刻起卦："))

if len(取数) == 0:
    时刻 = 公历时刻(input("输入公历年月日时（北京时间，如2026 10 04 13；回车为当前时刻）："), True)
    try:
        农历 = ZhDate.from_datetime(datetime(时刻.year, 时刻.month, 时刻.day))
    except (IndexError, ValueError) as 错误:
        raise ValueError("该公历日期超出ZhDate支持的农历范围") from 错误
    今时: tuple[int, ...] = (农历.lunar_month, 农历.lunar_day, (时刻.hour + 1) // 2 % 12 + 1)
    print(入卦(今时, 算法))
elif (数 := tuple(map(int, 取数.split()))) and any(_ > 0 for _ in 数) and all(_ >= 0 for _ in 数):
    print(入卦(数, 算法))
else:
    print("输入数不得全部为0或包含负数")
