import streamlit as st
st.set_page_config(page_title='音乐播放器')

music_url =[
    {
        'musicurl':'https://music.163.com/song/media/outer/url?id=27789126.mp3',
        'imgurl':'https://p1.music.126.net/ueVw7Occk8bQnBpZWeaHjw==/1319413953400034.jpg?param=130y130',
        'text':'年轻的战场-张杰'
        },
    {
        'musicurl':'https://music.163.com/song/media/outer/url?id=64985.mp3',
        'imgurl':'https://p1.music.126.net/Qs7rthgurYD-OISrms8hng==/109951166050592954.jpg?param=130y130',
        'text':'只是近黄昏-陈奕迅'
        },
    {
        'musicurl':'https://music.163.com/song/media/outer/url?id=386425.mp3',
        'imgurl':'https://p1.music.126.net/z5jrOL-OSXWKfQjyPJas8w==/109951163093838994.jpg?param=130y130',
        'text':'听不到-五月天'
        },

    ]
if 'ind' not in st.session_state:
    st.session_state['ind']=0

c1,c2=st.columns([1,2])

def lastMusic():
    st.session_state['ind']=(st.session_state['ind']-1) % len(music_url)

def nextMusic():
    st.session_state['ind']=(st.session_state['ind']+1) % len(music_url)

with c1:
    st.image(music_url[st.session_state['ind']]['imgurl'])
    

with c2:
    st.subheader(music_url[st.session_state['ind']]['text'])

    st.audio(music_url[st.session_state['ind']]['musicurl'])
    
    c11,c22=st.columns(2)

    with c11:
        st.button('上一首',use_container_width=True,on_click=lastMusic)
    with c22:
        st.button('下一首',use_container_width=True,on_click=nextMusic)
