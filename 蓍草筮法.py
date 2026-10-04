from secrets import randbelow
from 易卦 import 卦名


算法 = input("选择蓍草算法（1 三变皆挂；2 首变挂一、后二变不挂）：").strip()
if 算法 not in ("1", "2"):
    raise ValueError("须选择1或2")
print("所选算法：" + ("三变皆挂（朱熹）" if 算法 == "1" else "首变挂一、后二变不挂（郭雍）"))

爻数: list[int] = []
for 爻位 in range(6):
    策数 = 49
    归奇: list[int] = []
    for 变 in range(3):
        挂策 = 1 if 算法 == "1" or 变 == 0 else 0
        左策 = randbelow(策数 - 1 - 挂策) + 1 + 挂策
        右策 = 策数 - 左策
        左策 -= 挂策
        左奇 = 左策 % 4 or 4
        右奇 = 右策 % 4 or 4
        归奇.append(挂策 + 左奇 + 右奇)
        策数 -= 归奇[-1]

    爻 = 策数 // 4
    爻数.append(爻)
    print(
        f"{'初二三四五上'[爻位]}爻：归奇 {归奇[0]}、{归奇[1]}、{归奇[2]}；"
        f"余 {策数} 策，为 {爻}（{('老阴', '少阳', '少阴', '老阳')[爻 - 6]}）"
    )

本卦 = tuple(数 % 2 for 数 in 爻数)
变卦 = tuple(1 - 阴阳 if 数 in (6, 9) else 阴阳 for 数, 阴阳 in zip(爻数, 本卦))
print(f"本卦：{卦名(本卦)}")
print(f"之卦：{卦名(变卦)}" if 本卦 != 变卦 else "无动爻")
