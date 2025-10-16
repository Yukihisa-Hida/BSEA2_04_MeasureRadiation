import matplotlib.pyplot as plt
import matplotlib_fontja
import pandas as pd

plt.rcParams["font.family"] = "MS Mincho"
plt.rcParams["font.size"] = 15

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = "black"
plt.rcParams["legend.markerscale"] = 5
plt.rcParams["lines.linewidth"] = 0
plt.rcParams["lines.linestyle"] = ""
plt.rcParams["lines.marker"] = "."

input_csv = pd.read_csv("C:\\uec\\基礎科学実験A\\04\\BSEA1_04_MeasureRadiation\\graph\\30mm-300times\\count-distribution-30mm-300times.csv", header=None)

fig = plt.figure(dpi=200)

x1 = 19.5
x2 = 51.5
y1 = 0
y2 = 0.125

plt.xlim(x1, x2)
plt.ylim(y1, y2)

plt.bar(input_csv[0], input_csv[1], 0.5, color="gray", edgecolor="black")

plt.plot(input_csv[0], input_csv[2], color="black", markeredgecolor="black", markersize=10)

text = [
    r"ゲート時間$\ 1\mathrm{s}$",
    r"回数$300$回",
    r"$\overline{N}=33.39$",
    r"$\sigma=6.12$",
    r"$\sqrt{\overline{N}}=5.78$",
]

for i in range(5):
    plt.text(x1 + (x2 - x1) * 0.95, y1 + (y2 - y1) * 0.9 - i * 0.014, text[i], ha="right")

plt.xticks([20, 25, 30, 35, 40, 45, 50])

plt.xlabel(r"計数値$\ N$")
plt.ylabel(r"出現確率$\ n_N/\sum n_N$")

plt.tight_layout()

plt.show()