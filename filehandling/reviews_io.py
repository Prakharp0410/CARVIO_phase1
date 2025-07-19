import json

file="D:/PROJECT/CARVIO_v1/data/reviews.json"

def load_reviews():
    try:
        with open(file,"r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_reviews(reviews):
    with open(file,"w") as f:
        json.dump(reviews,f,indent=4)

def add_review(username, car_name,car_brand,start_date,end_date,review,rating_from_5):
    all_reviews=load_reviews()
    new_review={
        "username": username,
        "car name": car_name,
        "car brand": car_brand,
        "Start Date": start_date,
        "End Date" : end_date,
        "reviews by user": review,
        "rating"  : rating_from_5
    }
    all_reviews.append(new_review)
    save_reviews(all_reviews)
