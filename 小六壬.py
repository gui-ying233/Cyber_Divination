from zhdate import ZhDate
from datetime import datetime
from re import findall

六神: tuple[str, ...] = ("大安", "留连", "速喜", "赤口", "小吉", "空亡")
今时: tuple[int, ...] = (
    int(
        findall(
            r"农历\d\d\d\d年(\d\d?)月\d\d?日", str(ZhDate.from_datetime(datetime.now()))
        )[0]
    ),
    int(
        findall(
            r"农历\d\d\d\d年\d\d?月(\d\d?)日", str(ZhDate.from_datetime(datetime.now()))
        )[0]
    ),
    (int((int(datetime.now().strftime("%H")) - 7) % 24 / 2) + 2) % 12,
)


def 入卦(n: tuple[int, ...]) -> str:
    return 六神[(sum(n) - len(n)) % 6]


取数 = str(input("输入任意个数，用空格分隔；\n或直接回车以使用当前月日时起卦："))

if len(取数) == 0:
    print(入卦(今时))
elif any(_ > 0 for _ in tuple(map(int, 取数.split(" ")))):
    print(入卦(tuple(map(int, 取数.split(" ")))))
else:
    print("输入数不得全部为0")
