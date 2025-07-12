import streamlit as st
from screens.auth.login_page import login_page_func
from screens.outer_dashboard import main_page_bl
from screens.auth.signup_page import signup_page_func
from screens.main_dashboard import main_page_afterlogin
from screens.sessionstate_folder.session_state import *

if st.session_state.page=="outer_dashboard":
    main_page_bl()
elif st.session_state.logged_in==True:
    main_page_afterlogin()
else:
    if st.session_state.page=="signup":
        signup_page_func()
    else:
        login_page_func()

if __name__=="__main__":
    pass
