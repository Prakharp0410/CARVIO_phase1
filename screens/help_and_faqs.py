import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

button_css="""<style>
button.st-emotion-cache-1rwb540.e1e4lema2 {
    background: green;
}</style>"""

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

background_css="""
<style>
section.stMain.st-emotion-cache-z4kicb.elbt1zu1 {
    background-image:url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
}
.stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
    color: white;
    max-width: 100%;
}
</style>
""" 

expander_css="""
<style>
.st-emotion-cache-4rp1ik:hover {
    color: white;
    border-style: groove;
    border-color: white;
    border-radius: 15px;
    opacity: 0.8;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
summary.st-emotion-cache-4rp1ik.eah1tn13 {
    margin-top: 20px;
}
</style>"""

help_title=""" <h1> HELP AND FAQs</h1>
<style>
h1{
    color: white;
    font-size: 60px;
    text-align: center;
    position:relative;
}
</style>
"""

def help_and_faqs_page():
    st.markdown(remove_header_footer, unsafe_allow_html=True)
    st.markdown(background_css, unsafe_allow_html=True)
    st.markdown(expander_css, unsafe_allow_html=True)
    st.markdown(button_css, unsafe_allow_html=True)

    back_dashboard_button=st.button("Back to dashboard")
    if back_dashboard_button:                           #back to dashboard 
       st.session_state.page="home_page"
       st.session_state.current_page="none"
       st.rerun() 
    
    st.markdown(help_title, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True) 
    st.markdown("""
    

    
    <h2 style='color:white; font-size:40px; text-align:center;'>Frequently Asked Questions</h2>
    <p style='color:white; font-size:20px; text-decoration:underline'>
        Here are some common questions and answers to help you navigate our car rental service.</p>
    """, unsafe_allow_html=True)


    # Example FAQs
    faqs = {
            "How does the car rental process work?":
        "Choose your rental dates, select a car category, provide personal details, confirm booking with payment, then pick up and enjoy your rental.",
    
    "How do I select rental dates ?":
        "Specify your pick-up and drop-off dates and times, and visit our showroom to pick up the car at the desired time.",
    
    "How do I choose the right car for my needs?":
        "Select from vehicle types like hatchback, sedan(Luxury), or SUVs based on your trip duration, passengers, and preferences.",
    
    "Can I book a rental car online?":
        "Yes, you can book online through our website or app, selecting your car and rental dates.",
    
    "What information do I need to provide when booking?":
        "You'll need to provide your full name and contact details while signing up only.",
    
    "How do I confirm my booking?":
        "After payment, you will see whether your payment was successful or not.",
    
    "Can I modify or cancel my booking?":
        "Modification or cancellation policies vary; check with your rental provider or contact customer support.",
    
    "What happens at car pick-up?":
        "Present your confirmation, inspect the vehicle, and familiarize yourself with its features before driving off.",
    
    "How is the rental cost calculated?":
        "Costs depend on vehicle type, rental duration, and any additional services or fees.",
    
    "Can I rent a car for a short period like a few hours?":
        "No, you have to book for atleast a day.",
    
    "Are there options for airport pick-up and drop-off?":
        "Yes, contact our management and they will arrange this for you.",
    
    "What should I do if I want to rent multiple cars?":
        "Make separate bookings for each vehicle as per your requirements.",
    
    "What are the typical steps to return a rental car?":
        "Return the car by clicking on the button on our website after dropping the vehicle, inspect the vehicle with staff, settle any extra charges, and obtain a receipt at our showroom.",
    
    "How can I leave feedback or review a rental?":
        "After your rental period, you can submit reviews after returning on the return page on the website or app to share your experience.",
    
    "What support is available during my rental?":
        "You can easily contact the showroom.The contact no. is: 95670249793"

    }

    for question, answer in faqs.items():
        with st.expander(question, expanded=False):
            st.markdown("<br>", unsafe_allow_html=True)  # Add space before the answer
            st.write(answer)
