import streamlit as st
st.set_page_config(page_title='相册网站')

image_url =[
    {
        'url':'https://img95.699pic.com/photo/60027/3798.jpg_wh860.jpg',
        'text':'老鹰'
        },
    {
        'url':'http://pic1.bbzhi.com/dongwubizhi/jingcaishunjian-quweidongwubizhi/animal_hd_fun_animals_1920x1200_1830_11.jpg',
        'text':'小熊猫'
        },
    {
        'url':'https://img.shetu66.com/2023/08/24/1692861034607396.jpg',
        'text':'鹦鹉'
        },

    ]
if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.image(image_url[st.session_state['ind']]['url'],caption=image_url[st.session_state['ind']]['text'])

c1,c2=st.columns(2)

def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(image_url)

def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(image_url)

with c1:
    st.button('上一张',use_container_width=True,on_click=lastImg)

with c2:
    st.button('下一张',use_container_width=True,on_click=nextImg)
