
import streamlit as st
import base64
from filehandling.user_io import *
from screens.sessionstate_folder.session_state import for_signup, already_logged_in


def validate_login(username, password):
    
    if not username or not password:
        st.error("Username and password cannot be the empty")
        return False 
    users=load_users()
    if username in users and users[username]["password"]==password:
        return True
    else:
        st.error("Invalid username or password. Create an account first!!")
        return False


def login_page_func():
    def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
             data = f.read()
            return base64.b64encode(data).decode()

    def set_background(png_file):
            bin_str = get_base64_of_bin_file(png_file)
            page_bg_img = f'''
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
    set_background("D:/PROJECT/CARVIO_v1/static/image/bgimage_final.png")
   
    st.markdown("""
                <style>
                .st-emotion-cache-bfgnao p, .st-emotion-cache-bfgnao ol, .st-emotion-cache-bfgnao ul, .st-emotion-cache-bfgnao dl, .st-emotion-cache-bfgnao li {
    font-size: inherit;
    color: white;}
                
                   </style> """,
        unsafe_allow_html=True) #for the text_input font
    
    st.title("Log In")
    username_text=st.text_input("Enter your Username:")
    password_text=st.text_input("Enter the password:")
    login_button=st.button("Login")
    if login_button:
        login1=validate_login(username_text,password_text)    #function called from above
        if login1:
            st.success("Logged in Successfully")
            already_logged_in(username_text)         #home page session state
            st.session_state.username=username_text
            st.rerun()
    signup_button=st.button("Sign Up")
    if signup_button: 
        for_signup()
        st.rerun()
    