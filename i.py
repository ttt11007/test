import streamlit as st
import pandas as pd

st.image('https://img95.699pic.com/photo/50134/4384.jpg_wh860.jpg')
tab1, tab2, tab3,tab4, tab5 = st.tabs(['首页','个人简历生成器','动物档案','南宁美食数据','数字档案'])
   
with tab1:
    st.title("主页")
    st.image('https://ts3.tc.mm.bing.net/th/id/OIP-C.FN5OQm4S7c9M8bgXBVgmlAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3')
    st.write("1111111111111111111122222222222222222222222223333333333333333333344444444444444444444")

with tab2:
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


with tab3:
    st.title("动物档案")
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

with tab4:
    st.title("南宁美食数据")
    data = {
        '月份':['01月', '02月', '03月','04月', '05月', '06月','07月', '08月', '09月','10月', '11月', '12月'],
        '1号门店':[200, 150, 180,120, 160, 123,150, 100, 220,110, 100, 160],
        '2号门店':[120, 160, 123,150, 100, 220,110, 100, 160,150,130,125],
        '3号门店':[110, 100, 160,120, 160, 123,60,123,114,125,145,87],
        '4号门店':[90, 99, 110,150, 100, 220,110,130,160,99,100,160],
        '5号门店':[150, 100, 220,120, 160, 123,110, 100, 160,160,112,124],
    }

    df = pd.DataFrame(data)

    index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='序号')
    
    df.index = index

    st.header("门店数据")
    
    st.write(df)
    
    st.header("折线图")

    st.line_chart(df, x='月份')

    df.set_index('月份', inplace=True)

    map_data={
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }

    mapd=pd.DataFrame(map_data)

    st.map(mapd)

    st.header("餐厅评分")

    fen_data={
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
         "评分": [4.2, 4.5, 4.0, 4.7, 4.3]
    }

    df1 = pd.DataFrame(fen_data)

    index = pd.Series([1, 2, 3,4,5], name='评分')

    df1.index = index

    st.bar_chart(df1, x='餐厅')

    st.header("用餐高峰")

    can_data = {
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
        '12点':[200, 150, 180,90, 160],
        '13点':[100, 140, 110,150, 180],
        '14点':[220, 170, 160,140, 110],
        '15点':[230, 120, 190,110,150],
        '16点':[150, 90, 130,110,150],
        '17点':[120, 130, 150,90, 160],
        '18点':[110, 50, 110,150, 180,],
        '19点':[90, 160, 120,140, 110]
    }

    df2 = pd.DataFrame(can_data)

    index = pd.Series([1, 2, 3,4,5], name='12点')

    df2.index = index

    st.area_chart(df2, x='餐厅')

with tab5:
    st.title('小韦的档案')
    st.header('😀基础信息')
    st.text('学生id：007')
    st.markdown('注册时间：:green[2025.12.18] | 精神状态：正常')
    st.markdown('当前教室：:green[实训楼710] | 安全等级：绝密')
    st.header('🔑详细信息')
    st.subheader('💰收入情况')
    st.metric(label="当日收入", value="6666", delta="666")
    st.subheader('💯成绩信息')
    c1, c2, c3 = st.columns(3)
    c1.metric(label="语文", value="110", delta="10")
    c2.metric(label="数学", value="120", delta="20")
    c3.metric(label="英语", value="119", delta="19")
    st.header('📜今日任务')

    data={
        '日期':['2025.12.18','2025.12.20','2025.12.22'],
        '任务':['学生档案','课程管理系统','数据图展示'],
        '状态':['✅完成','🕐进行中','❌未完成'],
        '难度':['⭐⭐','⭐⭐','⭐⭐⭐⭐⭐⭐']
    }

    df=pd.DataFrame(data)

    st.text('静态表')
    st.table(df)
    st.text('动态表')
    st.dataframe(df)
    st.subheader('🔐最新代码成果')

    python_code='''print("hello world")
        a=1
        b=2
        print(a+b)
    '''

    st.code(python_code,line_numbers=True)
    st.markdown(':green[ing:]下一个任务进行中...')
    st.markdown(':green[next:]数据图展示')
    st.markdown(':green[last_time:]2025.12.18 15:33:23')
    st.text('系统状态：在线 | 连接状态：已加密')


