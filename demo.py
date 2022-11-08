import streamlit as st
import ecdf
import forex
import pandas as pd
def fun():
    st.write('fun click')
    return 0
def main():
    st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
.title-font {
    font-size:30px !important;
}</style>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        a = st.file_uploader("前屆作答檔")
        b = st.file_uploader("應屆作答檔")
        c = st.file_uploader("共同題檔")
    with col2:
        e = st.file_uploader("前屆答案檔")
        f = st.file_uploader("應屆答案檔")

    agree = st.checkbox('執行')
    dir = 'D:/Dropbox/Andy/金融考試標準化設置/02_RASCH/forEx/' # 資料檔暗鎖所在目錄
    file_pre = 'exchange(19).xlsx'
    file_now = 'exchange(20).xlsx'
    file_common = 'common_items_19_20.xlsx'
    
    
    if agree:
        pd_data_pre = pd.read_excel(a, header=None)
        pd_data_now = pd.read_excel(b, header=None)
        pd_data_common = pd.read_excel(c)
        former = st.sidebar.slider('前屆答對題數', 1, 110, 30)
        kind = st.sidebar.selectbox("考試種類", ["外匯交易", "金融基測", "CFP"])
        st.markdown('<p class="title-font">Demo version</p>', unsafe_allow_html=True)
        fig, corr, ability = ecdf.equalize_pltly(former)
        st.write(fig)
        st.markdown(f'<p class="big-font">對應到應屆的答對題數為 {corr} 題<br>能力值為 {ability}</p>', unsafe_allow_html=True)
        f = forex.forEx_fig(pd_data_pre, pd_data_now, pd_data_common)
        st.write(f)
    else:
        st.write("請放入資料")
            


if __name__ == '__main__':
    main()