import streamlit as st

st.set_page_config(page_title='个简历生成器')
st.title('个人简历生成器')
st.text('使用streamlit生成简历')

c1,c2 = st.columns([1,2])
with c1:
    user_name = st.text_input('姓名')
    zhiwei = st.text_input('职位')
    phone = st.text_input('电话')
    emil = st.text_input('邮箱')
    csrq = st.date_input("出生日期", value=None)  
    st.text('性别')
    xb = st.radio('选择性别',
                  ['男', '女', '其他'],
                  horizontal=True,
                  label_visibility='hidden'
                  )
    xueli = st.selectbox(
                        '选择学历',
                        ['本科', '硕士', '博士'],
                        label_visibility='collapsed'
                        )
    st.text('语言能力')
    yy = st.multiselect(
                        '选择你的语言能力',
                        ['北京', '太原', '临汾', '南京', '杭州', '西安'],
                        )
    st.text('技能')
    jn = st.multiselect(
                        '选择你的技能',
                        ['睡觉', '摸鱼', '当老板', '打架', '干饭', '滴滴'],
                        )
    st.text('工作经验')
    jy = st.slider('工作经验', 0, 33, 1)
    st.text('期望薪资（年）')
    xz = st.slider(
                        '选择薪资范围',
                        0, 500000, (0, 3000)
                        )    
    jj = st.text_area(label='个人简介：', placeholder='请输入个人简介')
    time = st.time_input('最佳联系时间')
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="avatar")
with c2:
    st.title(user_name)
    st.text('职位：'+ zhiwei)
    st.text('电话：'+ phone)
    st.text('邮箱：'+ emil)
    st.text('出生日期：')
    st.text(csrq)
    st.text('性别：'+ xb)
    st.text('学历：'+ xueli)
    st.text('语言能力：')
    st.text(yy)
    st.text('技能：')
    st.text(jn)
    st.text('经验：')
    st.text(jy)
    st.text('期望薪资：')
    st.text(xz)
    st.text('个人简介：'+ jj)
    st.text('最佳联系时间：')
    st.text(time)
