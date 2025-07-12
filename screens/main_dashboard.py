import streamlit as st
import base64
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from screens.sessionstate_folder.session_state import *
from screens.browse_and_rent import rent_car_page
from screens.billing_summary import billing_page
from screens.my_rentals import my_rentals_page_function
from screens.return_and_review import return_and_review_page
from screens.help_and_faqs import help_and_faqs_page

remove_header_footer = """     
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hide the orange loading progress bar */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* Remove top padding to avoid white space */
        .block-container {
            padding-top: 0rem !important;
        }
    </style>
"""

making_max_width="""
      <style>   
  .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
    max-width: 100%;
    }
    </style>
    """
def main_page_afterlogin():
    st.markdown(remove_header_footer,unsafe_allow_html=True)   #removes header and footer
    st.markdown(making_max_width,unsafe_allow_html=True)       #sets max width of the page
    
    
    if st.session_state.current_page == "rent_car":           
        rent_car_page()                             #rent your car page 
  
    elif st.session_state.current_page=="billing_summary":
        billing_page()                              #billing summary page
    
    elif st.session_state.current_page=="my_rentals":
        my_rentals_page_function()                  #my rentals page
    
    elif st.session_state.current_page=="return_car":
         return_and_review_page()                #return and review page

    elif st.session_state.current_page=="help_and_faqs":
         help_and_faqs_page()                #help and faqs page

    elif st.session_state.page=="home_page": 
        col0,col1,col2,col3,col4,col5=st.columns(6)
        with col0:
            log_out_button=st.button("Log Out", key="btn1")
            if log_out_button:
                for_logout() #sets sesion_state.page=login
                st.rerun()
        with col1:
            rent_page_button=st.button("Rent a car")    
            if rent_page_button: 
                rent_page_ss()
                st.rerun() # This sets st.session_state.current_page to "rent_car"  
        with col2:
            billing_summary_button=st.button("Billing")  
            if billing_summary_button:
                   billing_summary_ss()  # This sets st.session_state.current_page to "billing_summary"
                   st.rerun()
        with col3:    
            my_rentals_button=st.button("My Rentals")
            if my_rentals_button:
                 my_rentals_ss()   # This sets st.session_state.current_page to "my_rentals"
                 st.rerun()
        with col4:    
            return_button=st.button("Return car")
            if return_button:
                return_car_ss()
                st.rerun()
        with col5:    
            help_button=st.button("Help and FAQs")
            if help_button:
                 help_page_ss()
                 st.rerun()


        
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
        
        car_animation = """
        <style>
        .car-container {
            position: relative;
            width: 100%;
            height: 100px;
            background: transparent;
            overflow: hidden;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .car {
            position: absolute;
            left: 0;
            top: 30px;
            font-size: 48px;
            transition: left 4s linear;
            animation: moveCar 10s linear infinite;
        }
        @keyframes moveCar {
            0%   { left: 0; }
            50% { left: 80%; }
        }
        </style>
        <div class="car-container">
            <div class="car">🚗</div>
        </div>
        """
       # st.markdown(car_animation, unsafe_allow_html=True)
    
        username=st.session_state.get("username", "User")

        st.markdown(f"""       
                    <h1 style='color:white'> Welcome to CARVIO</h1>
                    <div class="h2h">
                    <h2>{username}</h2>
                    </div>
                    <h3 style='color:white'> Your Car, Your Pace, Your Savings</h3>    """,
                    unsafe_allow_html=True)  #The main text on dashboard
    
        st.markdown( """<style> 
                       .h2h{
                        color:beige;  
                    }
                    </style>""", unsafe_allow_html=True) #Username CSS
        

        st.markdown("""    
                    <style>
                    div.stButton > button{
                    background-color: green;
                    color:white;
                    top:0px;
                    width:150px;
                    }
                    div.stButton > button:hover{
                    background-color: red ;
                    color: white;
                    }
                    </style>
                    """, unsafe_allow_html=True)  #main dashboard buttons css
 

 


