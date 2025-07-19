# session_state.py - auto generated file
import streamlit as st
from filehandling.rentals_io import load_all_rentals

all_rentals=load_all_rentals()

if "page" not in st.session_state:
    st.session_state.page="outer_dashboard"

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if "username" not in st.session_state:
    st.session_state.username=""

if"current_page" not in st.session_state:
    st.session_state.current_page="none"

if "email" not in st.session_state:
    st.session_state.email="xyz"

if "rate" not in st.session_state:
    st.session_state.rate=0

if "duration" not in st.session_state:
    st.session_state.duration=0

if "car_name" not in st.session_state:
    st.session_state.car_name="none"

if "car_brand" not in st.session_state:
    st.session_state.car_brand="none"

if "car_type" not in st.session_state:
    st.session_state.car_type="none"

if "car_fuel_type" not in st.session_state:
    st.session_state.car_fuel_type="none"

if "car_image" not in st.session_state:
    st.session_state.car_image="none"

if "car_no" not in st.session_state:
    st.session_state.car_no="none"

if "car_color" not in st.session_state:
    st.session_state.car_color="none"

if "start_rental" not in st.session_state:
    st.session_state.start_rental="none"

if "end_rental" not in st.session_state:
    st.session_state.end_rental="none"

if "car_available" not in st.session_state:
    st.session_state.car_available=True    

if "car_returned" not in st.session_state:
    st.session_state.car_returned=None

if "total_amount" not in st.session_state:
    st.session_state.total_amount=0

if "rental_id" not in st.session_state:
    if len(all_rentals) == 0:
        st.session_state.rental_id = 1
    else:
        st.session_state.rental_id = max(rental["rental_id"] for rental in all_rentals) + 1


def for_signup():
    st.session_state.page="signup"

def for_login():
    st.session_state.page="login"

def for_logout():
    st.session_state.page="login"
    st.session_state.logged_in=False

def already_logged_in(username_text):
     st.session_state.logged_in=True
     st.session_state.page="home_page"
     st.session_state.username=username_text

def rent_page_ss():
    st.session_state.current_page="rent_car"

def billing_summary_ss():
    st.session_state.current_page="billing_summary"

def my_rentals_ss():
    st.session_state.current_page="my_rentals"

def return_car_ss():
    st.session_state.current_page="return_car"

def save_for_billing_ss(rate_of_car,duration_in_days,
                        car_name,car_brand,
                        car_type,car_fuel_type,car_image,car_number,car_color,
                        start_rental,end_rental):
    st.session_state.rate=rate_of_car
    st.session_state.duration=duration_in_days
    st.session_state.car_name=car_name
    st.session_state.car_brand=car_brand
    st.session_state.car_type=car_type
    st.session_state.car_fuel_type=car_fuel_type
    st.session_state.car_image=car_image
    st.session_state.car_no=car_number
    st.session_state.car_color=car_color
    st.session_state.start_date=start_rental
    st.session_state.end_date=end_rental

def help_page_ss():
    st.session_state.current_page="help_and_faqs"

    