import streamlit as st

st.title('Hello Sujit')

st.header("Header")
st.subheader('Subheader')
st.text('Start the ')
st.markdown(""" # h1 tag
## h2 tag
### h3 tga
:moon:<br>
:sunglasses:            
             """)

# if st.button('Subscribe'):
#     st.write('Thank u for your support')

# name = st.text_input('Name')
# st.write(name)

# st.date_input("enter a date")

# st.time_input('enter a time')

# st.checkbox('youacceptthe iandc',value=False)

st.sidebar.selectbox('Select anumber ',[1,2,3,4,5])