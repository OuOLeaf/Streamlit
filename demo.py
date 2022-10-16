import streamlit as st
import ecdf

 

def main():

    with st.container():
        st.file_uploader("共同題檔", type=(["tsv","csv","txt","tab","xlsx","xls"]))
        st.file_uploader("當屆試題檔", type=(["tsv","csv","txt","tab","xlsx","xls"]))
        st.file_uploader("應屆試題檔", type=(["tsv","csv","txt","tab","xlsx","xls"]))
    check = st.checkbox("執行")
    if check:
        former = st.slider("前屆答對題數", 1, 110, 0)
        st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
    }
    .title-font {
        font-size:30px !important;
    }</style>""", unsafe_allow_html=True)
        st.markdown('<p class="title-font">Demo version</p>', unsafe_allow_html=True)
        [fig, corr] = ecdf.equalize(former)
        st.write(fig)
    
        st.markdown(f'<p class="big-font">對應到應屆的答對題數為 {corr} 題</p>', unsafe_allow_html=True)
        


if __name__ == '__main__':
    main()

