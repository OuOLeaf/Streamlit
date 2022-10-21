import streamlit as st
import ecdf

def main():
    st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
.title-font {
    font-size:30px !important;
}</style>""", unsafe_allow_html=True)
    former = st.sidebar.slider('前屆答對題數', 1, 110, 30)
    st.markdown('<p class="title-font">Demo version</p>', unsafe_allow_html=True)
    [fig, corr] = ecdf.equalize_pltly(former)
    st.write(fig)
   
    st.markdown(f'<p class="big-font">對應到應屆的答對題數為 {corr} 題</p>', unsafe_allow_html=True)
   
            


if __name__ == '__main__':
    main()