import streamlit as st

st.title("🦍我的第一个streamLit应用🦄",help="第一章的主要内容")
st.header("第二行")
st.subheader("嘻嘻")
st.text("Hello World")

python_code='''print("hello world")
a=1
b=2
print(a+b)
'''

st.code(python_code,line_numbers=True)

st.markdown("# 一级标题")
st.markdown("## 二级标题")
st.markdown("### 三级标题")
st.markdown("#### 四级标题")

st.markdown("嘻嘻")
st.markdown(":red[嘻嘻]")

st.markdown("*嘻嘻*")
st.markdown("**嘻嘻**")
st.markdown("***嘻嘻***")
