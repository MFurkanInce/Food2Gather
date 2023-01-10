import streamlit as st
from User import UserFactory
from Authentication import Authenticator


main = st.container()
result = st.container()
chat = st.button('chat')

with main:
    st.title('Food2Gather')
    member = st.button('Member')


with result:
   test = Authenticator()

   user1 = UserFactory('Member')
   st.write(user1.show_info())
   user1.membership = "premium"
   st.write(user1.show_info())

   option = st.selectbox('select',('bronze', 'silver', 'gold', 'diamond'))
   user1.buy_membership(option)
   st.write(user1.show_info())


if chat:
    st.write(user1.talk_chatbot())