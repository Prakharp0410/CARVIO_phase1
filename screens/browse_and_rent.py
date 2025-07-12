import streamlit as st
import os
import sys
from datetime import date

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from filehandling.cars_io import save_cars,load_cars,update_cars
from screens.sessionstate_folder.session_state import *

making_max_width=""" <style>     
                      .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.elbt1zu4 {
                         max-width: 100%;
                           }
                      </style> """

rent_your_car_title="""<div class="heading">
                      <h1>RENT YOUR CAR</h1>
                    </div> 
                    <style>
                    .heading{
                    color:white;
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-size:250px;
                    }
                    h1#rent-your-car {
                            font-size: 70px;
                        }       
                    </style>
                            """


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
</style>
""" 

font_color="""<style>
.stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03 {
    color: white;
}
p {
    color: white;
}
     </style>"""

button_css="""
<style>
button.st-emotion-cache-1rwb540.e1e4lema2 {
                background-color: green;
                color: white;
               }   
button.st-emotion-cache-1rwb540.e1e4lema2 : hover {
                background-color: red;
                color: white;
               }   

                        </style> """

select_bar_css="""
                    <style>
                        .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am {
    width: 70%;
} </style>

    """

def rent_car_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True) #remove_header
    st.markdown(making_max_width, unsafe_allow_html=True) #making width:100%
    st.markdown(background_css, unsafe_allow_html=True)  #background-black
    st.markdown(font_color, unsafe_allow_html=True)  # font color
    st.markdown(button_css,unsafe_allow_html=True)  #butons_css
    st.markdown(select_bar_css,unsafe_allow_html=True)  #selectbar_css
    
    back_dashboard_button=st.button("Back to dashboard")
    if back_dashboard_button:                           #back to dashboard 
       st.session_state.page="home_page"
       st.session_state.current_page="none"
       st.rerun()
    
    st.markdown(rent_your_car_title, unsafe_allow_html=True)  #title
       
    def filter():                                        #filter function
       st.markdown("<h3 style='color:white'> Filters</h3>" ,unsafe_allow_html=True)
       col1,col2=st.columns(2)
       with col1:
        st.selectbox("Car type", ["SUV","Sedan","MPV","Hatchback"])
       with col2:
        st.selectbox("Fuel type", ["Petrol","Diesel","CNG"])


    def display_cars(cars_per_row=2):              #to display car in a grid format
        filter()
        cars=load_cars()
        for i in range(0,len(cars),cars_per_row):
            cols=st.columns(cars_per_row)
            for idx, car in enumerate(cars[i:i+cars_per_row]):
              with cols[idx]:
                with st.container():
                    st.markdown(
      f"""
       <div style="width:500px; height:300px;
            overflow:hidden; display:flex; 
            align-items:center; justify-content:center; 
            background:#eee; border-radius:8px; margin-bottom:8px;">
             <img src="{car['image']}" style="width:100%; height:100%; object-fit:cover;">
      </div>
    """,
    unsafe_allow_html=True,)
          
                    text_col1,text_col2=st.columns([1.5,1])
                    today=date.today()
                    start_date=date.today()
                    end_date=date.today()
                    with text_col1:
                        st.markdown(f"<h2 style='font-family:Roboto'>{car['Brand']}  {car['Name']}</h2>",unsafe_allow_html=True)
                        st.markdown(f"**Car No**: {car['Car_no']}")
                        st.markdown(f"**Type**: {car['Car_type']}")
                        st.markdown(f"**Mileage**: {car['Mileage']} km/l")
                        st.markdown(f"**Age**:{car['car_age']} years")
                        st.markdown("<br>", unsafe_allow_html=True)
                        start_date=st.date_input("Start from", today, key=car['car_age'])
                    with text_col2:
                        st.markdown("<br><br>", unsafe_allow_html=True) 
                        st.markdown(f"**AC**: {'Yes' if car['AC'] else 'No'}")
                        st.markdown(f"**Color**: {car['color']}")
                        st.markdown(f"**Rate per day**: ₹{car['rate_per_day']}")
                        st.markdown(f"**Fuel Type**: {car['Fuel Type']}")
                        st.markdown(f"**Available**: {'Yes' if car['available'] else 'No'}")
                        end_date=st.date_input("End till", today, key=car['Name'])
                        duration_of_days=((end_date-start_date).days+1)
                    rent_button=st.button(f"Rent this car", 
                                              key=car["Car_no"],
                                              type="secondary")    
                    if rent_button:
                        if(car["available"]==False):
                           st.error("The car is already rented")
                        else:
                           st.success(f"You selected {car['Brand']} {car['Name']}")
                           save_for_billing_ss(car['rate_per_day'],duration_of_days,  #saving car info in session state
                                            car['Name'],car['Brand'],
                                            car['Car_type'],car['Fuel Type'],car['image'], 
                                            car['Car_no'],car['color'],start_date,end_date)  
     
    display_cars()          