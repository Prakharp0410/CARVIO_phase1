
    
import streamlit as st
from filehandling.user_io import *
from screens.sessionstate_folder.session_state import for_login
import base64


def signup(username,password,fname,lname,email,phone_number):
    if not password or not username:       
        st.error("username and password cannot be empty")
        return False

    if len(username)<5:                         #for username validation
        st.error("username must be of 5 or more characters")
        return False
    if password:                                #for password validation
       password_set=set("!@%^&*")
    upper=0
    lower=0
    number=0
    special=0
    for c in password:
            if c.isupper():
               upper+=1
            elif c.islower():
                lower+=1
            elif c.isdigit():
                number+=1
            elif c in password_set:
                special+=1
    if not(upper>0 and lower>0 and number>0 and special>0):       
            st.error("Please enter atleast 1 UPPERCASE,lowercase,special character and a number in password")
            return False
    if len(password)<5:                   
            st.error("Password must be of more than 5 characters")
            return False
    if "@" not in email:                   #for email validation
            st.error("Invalid email")
            return False
    first,second=email.split('@')       
    if not first or not second:
            st.error("Invalid Email")
            return False
    if not phone_number.isdigit():       #for phone number validation
            st.error("Phone number can only contain digits")
            return False
    if len(str(phone_number))!=10:
            st.error("Phone number can only contain 10 digits")
            return False
    users=load_users()
    if username in users:
          st.error("Username already exists")
          return False
    users[username]={
        "fname":fname,
        "lname":lname,
        "email":email,
        "password": password,
        "phone_number": phone_number
        }
    save_users(users)
    return True


def signup_page_func():

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
    set_background("D:/car_rental_system/static/image/bgimage_final.png")
  
    st.markdown("""   
                <style>
    .st-emotion-cache-bfgnao p, .st-emotion-cache-bfgnao ol,
    .st-emotion-cache-bfgnao ul, .st-emotion-cache-bfgnao dl, 
    .st-emotion-cache-bfgnao li {
                        font-size: inherit;
                        color: white;
                                }  

                </style>
                """,
         unsafe_allow_html=True)  #for the text-box headings

    st.title("Sign Up")
    fname_text=st.text_input("First name:", placeholder="Akash")
    lname_text=st.text_input("Last name:", placeholder="Patel")
    email_text=st.text_input("Email:", placeholder="Example: yz@gmail.com")
    username_text=st.text_input("Enter your username:",
                                 placeholder="Username must not be less than 5 chaacters")
    password_text=st.text_input("Enter your password:", 
                                type="password",
                                placeholder=
                                "Must contain atleast one special case,Uppecase,Lowercase and digit")
    phone_number=st.text_input("Enter your phone:")
    signup_button=st.button("Sign up")
    if signup_button:
     signup1=signup(username_text,password_text,        #signup function called from above
                    fname_text,lname_text,
                    email_text,phone_number)
     if signup1:
        st.success("Fab!!, Your account has been created")
        st.button("Go to login page", on_click=for_login)

    st.button("Already exists?", on_click=for_login)