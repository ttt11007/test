import streamlit as st
import pandas as pd

#标题
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
#定义数据
data={
    '日期':['2025.12.18','2025.12.20','2025.12.22'],
    '任务':['学生档案','课程管理系统','数据图展示'],
    '状态':['✅完成','🕐进行中','❌未完成'],
    '难度':['⭐⭐','⭐⭐','⭐⭐⭐⭐⭐⭐']
}
#转换数据帧
df=pd.DataFrame(data)
#显示数据
st.text('静态表')
st.table(df)
st.text('动态表')
st.dataframe(df)
st.subheader('🔐最新代码成果')
#代码存储
python_code='''print("hello world")
a=1
b=2
print(a+b)
'''
#显示代码块
st.code(python_code,line_numbers=True)
st.markdown(':green[ing:]下一个任务进行中...')
st.markdown(':green[next:]数据图展示')
st.markdown(':green[last_time:]2025.12.18 15:33:23')
st.text('系统状态：在线 | 连接状态：已加密')

