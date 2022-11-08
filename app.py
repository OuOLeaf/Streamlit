import streamlit as st
import ecdf
import forex
import pandas as pd
import openxyl
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

    a = st.file_uploader("前屆作答檔")
    b = st.file_uploader("應屆作答檔")
    c = st.file_uploader("共同題檔")

    agree = st.checkbox('執行')
    dir = './' 
    file_pre = 'exchange(19).xlsx'
    file_now = 'exchange(20).xlsx'
    file_common = 'common_items_19_20.xlsx'
    
    
    if agree:
        pd_data_pre = pd.read_excel(a, header=None)
        pd_data_now = pd.read_excel(b, header=None)
        pd_data_common = pd.read_excel(c)
        f = forex.forEx_fig(pd_data_pre, pd_data_now, pd_data_common)
        st.write(f)
    else:
        st.write("請放入資料")
            


if __name__ == '__main__':
    main()