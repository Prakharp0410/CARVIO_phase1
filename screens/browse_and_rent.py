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
section.stMain.st-emotion-cache-4rsbii.e4man111 {
    background-image:url(https://mobiag.com/wp-content/uploads/2019/06/car-rental-fleet.jpg);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
}
</style>
""" 

font_color="""<style>
.stHorizontalBlock.st-emotion-cache-rra9ig.e1msl4mp2 {
    color: white;
}
p {
    color: white;
}
     </style>"""

button_css="""
<style>
div.stButton > button {
    background-color: #2E86AB;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    background-color: #FF8C00;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 140, 0, 0.3);
}
div.stButton > button:active {
    transform: translateY(0px);
}
</style>
"""

select_bar_css="""
<style>
.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am {
    width: 100%;
}
div[data-testid="stSelectbox"] > div {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
}
div[data-testid="stSelectbox"] label {
    color: white !important;
    font-weight: 500;
}
</style>
"""

car_card_css = """
<style>

.car-image-container {
    width: 100%;
    height: 300px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f0f0f0;
    border-radius: 10px;
    margin-bottom: 15px;
    border: 2px solid #2E86AB;
}
.car-title {
    color: #2E86AB;
    font-family: 'Roboto', sans-serif;
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 10px;
    text-align: center;
}
.car-detail {
    color: white;
    margin-bottom: 5px;
    font-size: 14px;
}
.car-detail strong {
    color: #FF8C00;
}
.filter-title {
    color: white;
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 15px;
    text-align: center;
}
</style>
"""

def rent_car_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True) #remove_header
    
    back_dashboard_button=st.button("Back to dashboard")
    if back_dashboard_button:                           #back to dashboard 
       st.session_state.page="home_page"
       st.session_state.current_page="none"
       st.rerun()
   
    st.markdown(making_max_width, unsafe_allow_html=True) #making width:100%
    st.markdown(background_css, unsafe_allow_html=True)  #background-black
    st.markdown(font_color, unsafe_allow_html=True)  # font color
    st.markdown(button_css,unsafe_allow_html=True)  #butons_css
    st.markdown(select_bar_css,unsafe_allow_html=True)  #selectbar_css
    st.markdown(car_card_css, unsafe_allow_html=True)  #car_card_css
    st.markdown(rent_your_car_title, unsafe_allow_html=True)  #title
    
    def filter():                                        #filter function
       st.markdown('<h3 class="filter-title" style="color: white" >Filters</h3>', unsafe_allow_html=True)
       col1,col2=st.columns(2)
       with col1:
        car_type_selected=st.selectbox("Car type", ["All","SUV","Sedan","MPV","Hatchback"])
       with col2:
        fuel_type_Selectd=st.selectbox("Fuel type", ["All","Petrol","Diesel","CNG"])
       return car_type_selected,fuel_type_Selectd

    def display_cars(cars_per_row=2):              #to display car in a grid format
        car_type_selected,fuel_type_selected=filter()
        cars=load_cars()
        if car_type_selected!="All":
            cars=[car for car in cars if car["Car_type"]==car_type_selected]
        if fuel_type_selected!="All":
            cars=[car for car in cars if car["Fuel Type"]==fuel_type_selected]
        for i in range(0,len(cars),cars_per_row):
            cols=st.columns(cars_per_row)
            for idx, car in enumerate(cars[i:i+cars_per_row]):
              with cols[idx]:
                with st.container():
                    st.markdown(
      f"""
       <div class="car-image-container">
             <img src="{car['image']}" style="width:100%; height:100%; object-fit:cover;">
      </div>
    """,
    unsafe_allow_html=True,)
          
                    text_col1,text_col2=st.columns([1.5,1])
                    today=date.today()
                    start_date=date.today()
                    end_date=date.today()
                    with text_col1:
                        st.markdown(f'<h2 class="car-title">{car["Brand"]}  {car["Name"]}</h2>',unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Car No</strong>: {car["Car_no"]}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Type</strong>: {car["Car_type"]}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Mileage</strong>: {car["Mileage"]} km/l</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Age</strong>: {car["car_age"]} years</p>', unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                        start_date=st.date_input("Start from", today, key=car['car_age'])
                    with text_col2:
                        st.markdown("<br><br>", unsafe_allow_html=True) 
                        st.markdown(f'<p class="car-detail"><strong>AC</strong>: {"Yes" if car["AC"] else "No"}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Color</strong>: {car["color"]}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Rate per day</strong>: ₹{car["rate_per_day"]}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Fuel Type</strong>: {car["Fuel Type"]}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="car-detail"><strong>Available</strong>: {"Yes" if car["available"] else "No"}</p>', unsafe_allow_html=True)
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
                    
                    st.markdown('</div>', unsafe_allow_html=True)
     
    display_cars()