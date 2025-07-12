import json


file="D:/car_rental_system/data/rental_history.json"

def load_all_rentals():
    with open(file, "r") as f:
        return json.load(f)

def save_rentals(rentals):
    with open(file, "w") as f:
        json.dump(rentals,f,indent=4)

def add_rentals(username,car_name,car_brand,car_no,start_date,
                end_date,duration,returned,total_amount,
                car_image):
    all_rentals=load_all_rentals()
    
    new_rental={
        "username": username,
        "car name": car_name,
        "car brand": car_brand,
        "car no"   : car_no,
        "rental start": start_date.isoformat(),
        "rental end": end_date.isoformat(),
        "duration": duration,
        "returned": returned,
        "total_amount": total_amount,
        "car_image": car_image
      }
    all_rentals.append(new_rental)
    save_rentals(all_rentals)

def show_user_current_rentals(username_text):
     all_rentals=load_all_rentals()
     current_rentals=[rental for rental in all_rentals if rental["username"]==username_text
               and rental["returned"]==False]
     return current_rentals

def show_user_past_rentals(username_text):
     all_rentals=load_all_rentals()
     past_rentals=[rental for rental in all_rentals if rental["username"]==username_text
                   and rental["returned"]==True]
     return past_rentals

def mark_returned(username, car_no,returned):
    all_rentals=load_all_rentals()
    for r in all_rentals:
        if(r["username"]==username and r["car no"]== car_no):
                r["returned"]=returned
                break
    save_rentals(all_rentals)

def empty_rentals_json():
     with open(file, "w") as f:
          json.dump([],f)