import streamlit as st
import ecdf
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
    a = st.file_uploader("前屆試題檔")
    b = st.file_uploader("應屆試題檔")
    c = st.file_uploader("共同題檔")
    agree = st.checkbox('執行')
    if a and b and c and agree:
        former = st.sidebar.slider('前屆答對題數', 1, 110, 30)
        st.markdown('<p class="title-font">Demo version</p>', unsafe_allow_html=True)
        [fig, corr] = ecdf.equalize_pltly(former)
        st.write(fig)
        st.markdown(f'<p class="big-font">對應到應屆的答對題數為 {corr} 題</p>', unsafe_allow_html=True)
    else:
        st.write("請放入資料")
            


if __name__ == '__main__':
    main()