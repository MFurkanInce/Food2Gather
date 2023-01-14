import streamlit as st
from User import UserFactory
from DataBaseClass import DataBaseClass

main = st.container()
result = st.container()
member = st.button('member')
chat = st.button('chat')

with main:
    st.title('Food2Gather')

    DB = DataBaseClass()
    DB.create_default_db()

with result:
    name = st.text_input('Enter name of the member')
    user1 = UserFactory('Member')
    user1.name = name

    option = st.selectbox('select', ('bronze', 'silver', 'gold', 'diamond'))

    user1.buy_membership(option)

    st.write(user1.show_info())

    if chat:
        st.write(user1.talk_chatbot())

