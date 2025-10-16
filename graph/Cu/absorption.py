import matplotlib.pyplot as plt
import matplotlib_fontja
import pandas as pd
import numpy as np
import math

plt.rcParams["font.family"] = "MS Mincho"
plt.rcParams["font.size"] = 15

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = "black"
plt.rcParams["legend.markerscale"] = 5
plt.rcParams["lines.linewidth"] = 1
plt.rcParams["lines.linestyle"] = "-"
plt.rcParams["lines.marker"] = ""

input_csv = pd.read_csv("C:\\uec\\基礎科学実験A\\04\\BSEA1_04_MeasureRadiation\\graph\\Cu\\absorption-Cu.csv", header=None)

fig = plt.figure(dpi=200)

x1 = 0
x2 = 0.14
y1 = 0
y2 = 2.5

plt.xlim(x1, x2)
plt.ylim(y1, y2)

x = np.array(input_csv[0])
y = np.array(input_csv[1])
err = [input_csv[1] - input_csv[2], input_csv[3] - input_csv[1]]

plt.errorbar(x, y, yerr=err, capsize=5, fmt="o", markersize=5, ecolor="black", elinewidth=1, markeredgecolor="black", color="black")

slope, intercept = np.polyfit(x, y, 1)
xmin, xmax = plt.xlim()
x_fit = np.array([xmin, xmax])
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, color='black', label=f'最小二乗法による直線 (LSM Line)\ny = {slope:.2f}x + {intercept:.2f}')

rho = 8.96
a = float(f"{slope:.2f}") * 10
mu = -a / math.log10(math.e)
mum = mu / rho

print("傾き=", a, "cm^-1")
print("mu=", mu, "cm^-1")
print("mum=", mum, "cm^2/g")

# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

plt.xlabel(r"$\mathrm{Cu}$箔の厚さ$\ x_\mathrm{Cu}/\mathrm{mm}$")
plt.ylabel(r"計数値の対数$\ \log_{10}\overline{N}_\beta$")

plt.tight_layout()

plt.show()