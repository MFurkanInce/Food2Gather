import streamlit as st
from User import UserFactory
from Authentication import Authenticator


main = st.container()
result = st.container()

with main:
    st.title('Food2Gather')
    member = st.button('Member')


with result:
   if member:
       test = Authenticator()

       user1 = UserFactory('Member')
       st.write(user1.show_info())
       user1.type = "premium"
       st.write(user1.show_info())


       sub = st.button('Subscribe')
       user1.buy_membership('gold')
       st.write(user1.show_info())