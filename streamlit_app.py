import streamlit as st

st.title("streamlit App Test")
st.header("최은주")
st.info('정보를 알려드립니다.')
st.code('''
print("우리는")
''')
col1, col2, col3 = st.columns(3)
col1.metric("temperature","70","1.2")
