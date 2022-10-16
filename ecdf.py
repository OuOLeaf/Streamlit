
# 安裝過要套件要放進資料夾 pipreqs --encoding=utf8 .\test
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# 中文字顯示

def equalize(former):
    n = 110
    fig, ax = plt.subplots(1,1)
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    x = np.linspace(0, 100, 1000)
    y1 = norm.cdf(x, loc = 50, scale = 15) * n
    y2 = norm.cdf(x, loc = 45, scale = 13) * n
    plt.ylabel("答對題數", fontsize = 14)
    plt.xlabel("能力", fontsize = 14)
    # lines
    ability = norm.ppf(former/n, loc = 50, scale = 15)
    corr = norm.cdf(ability , loc = 45, scale = 13) * n
    lx = np.linspace(0, ability, 1000)
    vx = [ability] * 1000
    ly1 = [former] * 1000
    ly2 = [corr] * 1000
    vy = np.linspace(0, corr, 1000)
    plt.plot(lx, ly1, color = "red", alpha = 0.3)
    plt.plot(lx, ly2, color = "red", alpha = 0.3)
    plt.plot(vx, vy, color = "red", alpha = 0.3)
    # curves
    ax.plot(x, y1, label = "前屆", lw = 3, alpha = 0.9)
    ax.plot(x, y2, label = "應屆", lw = 3, alpha = 0.9)
    
    yls = [0, 55, 110]
    yls.append(round(corr, 1))
    yls.append(round(former, 1))

    xls = [0, 20, 40, 60, 80, 100]
    xls.append(round(ability, 1))
    

    plt.xlim(0,102)
    plt.ylim(0,112)
    plt.legend(loc = "lower right")
    plt.yticks(sorted(yls))
    ax.set_yticklabels(map(str, sorted(yls)))
    plt.xticks(sorted(xls))
    ax.set_xticklabels(map(str, sorted(xls)))
    
    return [fig, round(corr, 1)]
