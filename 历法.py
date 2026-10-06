from datetime import date, datetime, timedelta, timezone
from fractions import Fraction
from vendor.lunar_python.lunar_python import Solar
from vendor.lunar_python.lunar_python.util import ShouXingUtil

天干 = "甲乙丙丁戊己庚辛壬癸"
地支 = "子丑寅卯辰巳午未申酉戌亥"
中气月将 = {"雨水": "亥", "春分": "戌", "谷雨": "酉", "小满": "申", "夏至": "未", "大暑": "午", "处暑": "巳", "秋分": "辰", "霜降": "卯", "小雪": "寅", "冬至": "丑", "DONG_ZHI": "丑", "大寒": "子"}
节月 = {"大雪": 1, "DA_XUE": 1, "小寒": 2, "XIAO_HAN": 2, "立春": 3, "LI_CHUN": 3, "惊蛰": 4, "JING_ZHE": 4, "清明": 5, "立夏": 6, "芒种": 7, "小暑": 8, "立秋": 9, "白露": 10, "寒露": 11, "立冬": 12}


def 公历时刻(文本: str, 需时辰: bool = False) -> datetime:
    if not 文本.strip():
        return datetime.now(timezone(timedelta(hours=8))).replace(tzinfo=None)
    try:
        数 = [int(项) for 项 in 文本.replace("-", " ").replace(":", " ").replace("T", " ").split()]
        if len(数) == 3 and 需时辰:
            数.append(int(input("输入北京时间小时（0～23）：")))
        if len(数) not in (3, 4, 5):
            raise ValueError
        return datetime(数[0], 数[1], 数[2], 数[3] if len(数) > 3 else 12, 数[4] if len(数) > 4 else 0)
    except ValueError as 错误:
        raise ValueError("请输入公历年 月 日，可加小时、分钟，例如2026 10 04 13 30") from 错误


def 儒略日(时刻: datetime) -> float:
    return 时刻.toordinal() + 1721424.5 + (时刻.hour + 时刻.minute / 60 + 时刻.second / 3600) / 24


def 日干支(日期: date) -> str:
    序 = (日期.toordinal() + 14) % 60
    return 天干[序 % 10] + 地支[序 % 12]


def 时支(时刻: datetime) -> str:
    return 地支[(时刻.hour + 1) // 2 % 12]


def 历书中气(时刻: datetime) -> list[tuple[float, str]]:
    已过: list[tuple[float, str]] = []
    for 年 in (时刻.year, 时刻.year + 1):
        if 1106 <= 时刻.year < 1136:
            天, 余 = divmod((28613460 + 年 - 1100) * 2662626 % 437400, 7290)
            日期 = date(年 - 1, 12, 1)
            日期 += timedelta(days=((15 + 天) - (日期.toordinal() + 14)) % 60)
            冬至 = Fraction(2 * 日期.toordinal() + 3442849, 2) + Fraction(余, 7290)
            气策 = 15 + Fraction(6371, 29160)
        elif 1384 <= 时刻.year < 1645:
            冬至 = Fraction("2226545.5375") + (年 - 1384) * Fraction("365.2425")
            气策 = Fraction("365.2425") / 24
        else:
            return []
        已过.extend((float(冬至 + 2 * 序 * 气策), 支) for 序, 支 in enumerate("丑子亥戌酉申未午巳辰卯寅"))
    return 已过


def 月将(时刻: datetime, 古历: bool = False) -> str:
    儒略 = 儒略日(时刻)
    if 古历:
        中气 = 历书中气(时刻)
        if 中气:
            return max((气日, 支) for 气日, 支 in 中气 if 气日 <= 儒略)[1]
    历 = Solar.fromJulianDay(儒略).getLunar()
    已过: list[tuple[float, str]] = []
    for 名称, 节气 in 历.getJieQiTable().items():
        if 名称 not in 中气月将:
            continue
        气日 = 节气.getJulianDay()
        if 古历:
            气日 = ShouXingUtil.calcQi(气日 - 2451545) + 2451544.5
        if 气日 <= 儒略:
            已过.append((气日, 中气月将[名称]))
    if not 已过:
        raise ValueError("无法计算该时刻的月将")
    return max(已过)[1]


def 节月序(时刻: datetime) -> tuple[int, int]:
    儒略 = 儒略日(时刻)
    历 = Solar.fromJulianDay(儒略).getLunar()
    已过 = [(节气.getJulianDay(), 节月[名称]) for 名称, 节气 in 历.getJieQiTable().items() if 名称 in 节月 and 节气.getJulianDay() <= 儒略]
    if not 已过:
        raise ValueError("无法计算该时刻的节月")
    节日, 月序 = max(已过)
    年 = date.fromordinal(int(节日 + 0.5) - 1721425).year + (月序 == 1)
    return 年, 月序


def 二至积日(时刻: datetime) -> tuple[str, int]:
    儒略 = 儒略日(时刻)
    历 = Solar.fromJulianDay(儒略).getLunar()
    已过 = [(节气.getJulianDay(), "阴" if 名称 == "夏至" else "阳") for 名称, 节气 in 历.getJieQiTable().items() if 名称 in ("夏至", "冬至", "DONG_ZHI") and 节气.getJulianDay() <= 儒略]
    if not 已过:
        raise ValueError("无法计算该时刻的二至")
    二至日, 遁 = max(已过)
    日期 = date.fromordinal(int(二至日 + 0.5) - 1721425)
    甲子 = 日期 - timedelta(days=(日期.toordinal() + 14) % 60)
    return 遁, (时刻.date() - 甲子).days + 1
