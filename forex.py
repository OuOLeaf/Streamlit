import pandas as pd
import numpy as np
from girth.synthetic import create_synthetic_irt_dichotomous
from girth import twopl_mml, ability_mle, rasch_conditional, \
    ability_map, rasch_jml, rasch_mml, ability_eap, tag_missing_data
import matplotlib.pyplot as plt
import plotly.graph_objects as go
# ---------------------------------------------------------
# 讀取兩次考試與共同題資料檔，pre = 前次；now = 本次，common = 共同題
def forEx_fig(pd_data_pre, pd_data_now, pd_data_common):
    # dir = 'D:/Dropbox/Andy/金融考試標準化設置/02_RASCH/forEx/' # 資料檔暗鎖所在目錄
    file_pre = 'exchange(19).xlsx'
    file_now = 'exchange(20).xlsx'
    # file_common = 'common_items_19_20.xlsx'
    # pd_data_pre = pd.read_excel(dir+file_pre, header=None)
    # pd_data_now = pd.read_excel(dir+file_now, header=None)
    raw_data_pre = np.array(pd_data_pre)
    raw_data_now = np.array(pd_data_now)

    test_answer_pre = raw_data_pre[0, 1:] # 前次考試正確答案
    answered_data_pre = raw_data_pre[3:, 1:] # 前次考試考生答案
    J_pre, I_pre = answered_data_pre.shape # 前次考生人數，題目數

    test_answer_now = raw_data_now[0, 1:]# 本次考試正確答案
    answered_data_now = raw_data_now[3:, 1:] # 本次考試考生答案
    J_now, I_now = answered_data_now.shape # 本次考生人數，題目數

    common_items = np.array(pd_data_common)
    common_items_pre = common_items[:, 0] # 前次考試的共同題題號
    common_items_now = common_items[:, 1] # 本次考試的共同題題號

    Tmp = np.tile(test_answer_pre, (J_pre, 1))
    # data_pre = np.multiply((Tmp.T == answered_data_pre.T), 1) # I_pre x J_pre
    data_pre = (Tmp.T == answered_data_pre.T) # 對答案（前次答題結果）
    Tmp = np.tile(test_answer_now, (J_now, 1))
    # data_now = np.multiply((Tmp.T == answered_data_now.T), 1) # I_now x J_now
    data_now = (Tmp.T == answered_data_now.T) # 對答案（本次答題結果）
    correctly_answered_pre = data_pre.mean(axis = 0) # 前次考試答對率
    correctly_answered_now = data_now.mean(axis = 0) # 本次考試答對率
    # -------------------------------------------------------------
    common_data_pre = data_pre[common_items_pre-1, :] # 共同題答題結果（前次）
    common_data_now = data_now[common_items_now-1, :] # 共同題答題結果（本次）
    common_data = np.c_[common_data_pre, common_data_now]  # 共同題答題結果（合併）

    # 兩屆考試結果合併成一個矩陣：n x m, n=前次題數（剔除共同題）+共同題數+本次題數（剔除共同題）， m 人數=前次考生+本次考生
    data_pre_without_common = np.delete(data_pre, common_items_pre-1, axis = 0) # 前次考試剔除共同題後的結果
    data_pre_without_common_ext = np.c_[data_pre_without_common, \
        -99999 * np.ones((I_pre-len(common_items_pre), J_now))].astype(int) # 前次考試剔除共同題後剩餘的答題的結果 + 遺失資料以 -99999 填補（for 本屆考生）
    data_now_without_common = np.delete(data_now, common_items_now-1, axis = 0)  # 本次考試剔除共同題後剩餘的答題結果
    data_now_without_common_ext = np.c_[-99999 * np.ones((I_pre-len(common_items_pre), J_pre)), \
        data_now_without_common].astype(int) # 遺失資料（for 前屆考生） + 本次考試剔除共同題後的結果

    data_final = np.r_[data_pre_without_common_ext, common_data, data_now_without_common_ext]

    # --- 估計題目 difficulties 與考生 ability
    discrimination = 1 * np.ones(data_final.shape[0]) # 固定 discrimination=1.7
    estimates = rasch_mml(data_final, discrimination=1, options=None) 
    # estimates = rasch_conditional(data_final, discrimination=1.7, options=None) 
    difficulty_estimates = estimates['Difficulty'] # 題目 difficulties
    discrimination_estimates = estimates['Discrimination'] # 題目鑑別度（已固定）
    # 考生 ability
    ability_estimates = ability_eap(data_final, difficulty_estimates, discrimination_estimates, options=None)
    # 繪圖：考生 ability vs. 答對率
    # fig = plt.figure(figsize=(9,6))
    # fig, ax = plt.subplots(1,1, figsize=(9,6))
    # plt.scatter(ability_estimates, np.r_[correctly_answered_pre, correctly_answered_now], marker = '.')
    # ax.scatter(ability_estimates[0:J_pre], correctly_answered_pre, marker = 's', color = 'r', alpha = 0.3, label=file_pre)
    # ax.scatter(ability_estimates[J_pre:], correctly_answered_now, marker = 's', color = 'g', alpha = 0.3, label=file_now)
    # plt.xlabel("Examinee's ability"), plt.ylabel('correctly answered %')
    # plt.grid('True')
    # plt.legend()
    # plt.title('Rasch: Maximum Marginal Likelihood')
    # plt.show()

    ## plotly
    fig = go.Figure()
    # straight lines
    ldict = dict(color = 'purple', width = 3)
    # curve
    fig.add_trace(go.Scatter(x = ability_estimates[0:J_pre], y = correctly_answered_pre, opacity = 0.7, mode = "markers", name = "前屆"))
    fig.add_trace(go.Scatter(x = ability_estimates[J_pre:], y = correctly_answered_now, opacity = 0.7, mode = "markers", name = "應屆"))
    # layout(ticks, grid)
    xdict = {'tickmode' : "array"
            ,'tickfont': dict(size = 15)
            ,'showgrid' : False
            ,'zeroline':False}
    
    ydict = {'tickmode' : "array"
            ,'tickfont': dict(size = 15)
            ,'showgrid' : False
            ,'zeroline':False}
    
    # Edit the layout
    fig.update_layout(xaxis_title='能力',
                      yaxis_title='正確題數',
                      xaxis = xdict,
                      yaxis = ydict,
                      xaxis_range = [-2.5, 2.5],
                      yaxis_range = [-0.1, 1],
                      showlegend=True,
                      margin = dict(l = 90, r = 20, t = 20, b = 60),
                      autosize = False,
                      width = 700,
                      height = 550,
                      font = dict(size = 15))
    return(fig)

# 繪製排序後的線圖
# fig = plt.figure(figsize=(9,6))
# ability_estimates_pre = ability_estimates[0:J_pre]
# ability_estimates_now = ability_estimates[J_pre:]
# tmp = np.argsort(ability_estimates_pre)
# ability_estimates_sort_pre = np.take_along_axis(ability_estimates_pre, tmp, axis = -1)
# correctly_answered_sort_pre = np.take_along_axis(correctly_answered_pre, tmp, axis = -1)
# tmp = np.argsort(ability_estimates_now)
# ability_estimates_sort_now = np.take_along_axis(ability_estimates_now, tmp, axis = -1)
# correctly_answered_sort_now = np.take_along_axis(correctly_answered_now, tmp, axis = -1)

# plt.plot(ability_estimates_sort_pre, correctly_answered_sort_pre, \
#     linestyle = '--', linewidth = 3, color = 'r', alpha = 0.5, label=file_pre)
# plt.plot(ability_estimates_sort_now, correctly_answered_sort_now, \
#     color = 'g', alpha = 1, label=file_now)
# plt.xlabel("Examinee's ability"), plt.ylabel('correctly answered %')
# plt.grid('True')
# plt.legend()
# plt.title('Rasch: Maximum Marginal Likelihood')

# # 繪製答題正確率的前後屆對照線
# boundary_pre = 73/110
# a = np.where(correctly_answered_sort_pre >= boundary_pre)
# # b = np.where(correctly_answered_sort_pre <= boundary_pre)
# c = ability_estimates_sort_pre[a][0]
# d = np.where(ability_estimates_sort_now >= c)
# boundary_now = correctly_answered_sort_now[d][0]
# plt.axhline(y = boundary_pre, color = 'r', linestyle = '-')
# plt.axhline(y = boundary_now, color = 'g', linestyle = '-')
# plt.axvline(x = c, color = 'r', linestyle = '-')
# plt.show()
# print('The boundary for the current test: {}'.format(boundary_now*110))