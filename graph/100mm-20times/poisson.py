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

input_csv = pd.read_csv("C:\\uec\\基礎科学実験A\\04\\BSEA1_04_MeasureRadiation\\graph\\100mm-20times\\count-distribution-100mm-20times.csv", header=None)

fig = plt.figure(dpi=200)

x1 = 6.5
x2 = 23.5
y1 = 0
y2 = 8

plt.xlim(x1, x2)
plt.ylim(y1, y2)

plt.bar(input_csv[0], input_csv[1], 0.5, color="gray", edgecolor="black")

# for i in range(5):
#     plt.text(x1 + (x2 - x1) * 0.95, y1 + (y2 - y1) * 0.9 - i * 0.04, text[i], ha="right")

plt.xticks([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

plt.xlabel(r"計数値$\ N$")
plt.ylabel(r"出現回数$\ n$")

plt.tight_layout()

plt.show()