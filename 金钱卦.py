from secrets import randbelow
from 易卦 import 卦名


爻位 = ("初", "二", "三", "四", "五", "上")
算法 = input("选择金钱卦算法（1 《增删卜易》；2 《祛疑说》所记朱熹反旧法）：").strip()
if 算法 == "1":
    算法名 = "《增删卜易》一背单、两背拆"
    爻名 = ("交（老阴）", "单（少阳）", "拆（少阴）", "重（老阳）")
    爻画 = ("⚋ ×", "⚊", "⚋", "⚊ ○")
    爻数 = (6, 7, 8, 9)
elif 算法 == "2":
    算法名 = "《祛疑说》所记朱熹反旧法"
    爻名 = ("重（老阳）", "拆（少阴）", "单（少阳）", "交（老阴）")
    爻画 = ("⚊ ○", "⚋", "⚊", "⚋ ×")
    爻数 = (9, 8, 7, 6)
else:
    raise ValueError("须选择1或2")
print("所选算法：" + 算法名)

取数 = input("输入六次投钱的背数（初爻至上爻，0～3，用空格分隔）；\n或直接回车模拟掷三钱六次：")

if not 取数.strip():
    背数 = tuple(sum(randbelow(2) for _ in range(3)) for _ in range(6))
else:
    try:
        背数 = tuple(map(int, 取数.split()))
    except ValueError:
        raise ValueError("须输入六个0～3之间的背数") from None
    if len(背数) != 6 or any(n < 0 or n > 3 for n in 背数):
        raise ValueError("须输入六个0～3之间的背数")

本卦 = tuple(爻数[n] for n in 背数)
动位 = tuple(i for i, n in enumerate(背数) if n in (0, 3))
变卦 = tuple(1 - n % 2 if n in (6, 9) else n % 2 for n in 本卦)

print("投钱结果（从上爻至初爻）：")
for i in range(5, -1, -1):
    n = 背数[i]
    print(f"{爻位[i]}爻：{n}背，{爻数[n]}，{爻名[n]} {爻画[n]}")

print("本卦：" + 卦名(本卦))
print("动爻：" + ("、".join(爻位[i] + "爻" for i in 动位) if 动位 else "无"))
print("变卦：" + (卦名(变卦) if 动位 else "无（静卦）"))
