import os
import json

file="D:/PROJECT/CARVIO_v1/data/cars.json"


def load_cars():
    with open(file, "r") as f:
        return json.load(f)

def save_cars(cars):
    with open(file, "w") as f:
        json.dump(cars, f, indent=4)

def update_cars(car_name,car_no,available):
            cars=load_cars()
            updated=0
            for car in cars:
                if (car["Name"]==car_name and car["Car_no"]==car_no):
                     car["available"]=available
                     updated=1
                     break
            if updated==1:
                 save_cars(cars)

# def reset_all_cars_available():
#     cars = load_cars()
#     for car in cars:
#         car["available"] = True
#     save_cars(cars)
