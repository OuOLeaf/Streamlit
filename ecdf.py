#%%
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# 中文字顯示
#%%
def data(former):
    # data points
    n = 110
    x = np.linspace(0, 100, 1000)
    y1 = norm.cdf(x, loc = 50, scale = 15) * n
    y2 = norm.cdf(x, loc = 45, scale = 13) * n
    
    # lines
    ability = norm.ppf(former/n, loc = 50, scale = 15)
    corr = norm.cdf(ability , loc = 45, scale = 13) * n
    lx = np.linspace(-5, ability, 1000)
    vx = [ability] * 1000
    ly1 = [former] * 1000
    ly2 = [corr] * 1000
    vy = np.linspace(-5, corr, 1000)

    # ticks
    yls = [0, 55, 110]
    yls.append(round(corr, 1))
    yls.append(round(former, 1))
    xls = [0, 20, 40, 60, 80, 100]
    # xls.append(round(ability, 1))

    return [[x, y1, y2, xls, yls], [lx, vx, vy, ly1, ly2, corr, ability]]
#%%
#%%
# plotly
import plotly.graph_objects as go
def equalize_pltly(former):
    # loading data
    info = data(former)
    x, y1, y2, xls, yls = info[0] 
    lx, vx, vy, ly1, ly2, corr, ability = info[1] 

    # initialize graph
    fig = go.Figure()

    # straight lines
    ldict = dict(color = 'purple', width = 3)
    fig.add_trace(go.Scatter(x = lx, y = ly1, opacity=0.5, line = ldict, showlegend=False))
    fig.add_trace(go.Scatter(x = lx, y = ly2, opacity=0.5, line = ldict, showlegend=False))
    fig.add_trace(go.Scatter(x = vx, y = vy,  opacity=0.5, line = ldict, showlegend=False))
    
    # curves
    c1dict = dict(color = 'blue', width = 4)
    c2dict = dict(color = 'orange', width = 4)
    fig.add_trace(go.Scatter(x = x, y = y1, opacity=0.8, name = "前屆", line = c1dict))
    fig.add_trace(go.Scatter(x = x, y = y2, opacity=0.8, name = "應屆", line = c2dict))
    
    
    # layout(ticks, grid)
    xdict = {'tickmode' : "array"
            ,'tickvals': xls
            ,'tickfont': dict(size = 15)
            ,'showgrid' : False
            ,'zeroline':False}
    
    ydict = {'tickmode' : "array"
            ,'tickvals': yls
            ,'tickfont': dict(size = 15)
            ,'showgrid' : False
            ,'zeroline':False}
    
    # Edit the layout
    fig.update_layout(xaxis_title='能力',
                      yaxis_title='正確題數',
                      xaxis = xdict,
                      yaxis = ydict,
                      xaxis_range = [0, 100],
                      yaxis_range = [-2, 110],
                      showlegend=True,
                      margin = dict(l = 90, r = 20, t = 20, b = 60),
                      autosize = False,
                      width = 700,
                      height = 550,
                      font = dict(size = 15))
    # rotate ticks
    # fig.update_xaxes(tickangle=30)
    # ticks
    
    return [fig, round(corr, 1), round(ability, 2)]

equalize_pltly(23)[0]
#%%
# matplotlib function
def equalize_mpl(former):
    # loading data
    info = data(former)
    x, y1, y2, xls, yls = info[0] 
    lx, vx, vy, ly1, ly2, corr = info[1] 
    
    fig, ax = plt.subplots(1,1)
    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
   
    # straight lines
    plt.plot(lx, ly1, color = "red", alpha = 0.3)
    plt.plot(lx, ly2, color = "red", alpha = 0.3)
    plt.plot(vx, vy, color = "red", alpha = 0.3)

    # curves
    ax.plot(x, y1, label = "前屆", lw = 3, alpha = 0.9)
    ax.plot(x, y2, label = "應屆", lw = 3, alpha = 0.9)
    
    # label and ticks
    plt.ylabel("答對題數", fontsize = 14)
    plt.xlabel("能力", fontsize = 14)
    plt.xlim(0,102)
    plt.ylim(0,112)
    plt.legend(loc = "lower right")
    plt.yticks(sorted(yls))
    ax.set_yticklabels(map(str, sorted(yls)))
    plt.xticks(sorted(xls))
    ax.set_xticklabels(map(str, sorted(xls)))
    
    return [fig, round(corr, 1)]

