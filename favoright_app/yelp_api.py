# frontend ==calls==> localhost:8000/get_me_data/some_info ==calls==> some_api.com/some_info&my_api_key=whatever 
# ==reponds==> your data (in django) ==responds==> your data (in front end) (edite
# frontend --> url route(backend localhost) --->   view handler ----> .py file --> call api ---> return data ---> back to frontend --> render data…. is this close ?
 
 
from django.http import HttpResponse
import requests
import os
from dotenv import load_dotenv
load_dotenv()
 

API_KEY= os.getenv("YELP_API_KEY")
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {
    "Authorization": 'bearer %s' % API_KEY
}


def get_yelp_data(location, term, radius):
    PARAMETERS = {
        "location":location,
        "term":term,
        "radius":radius,
        "limit":20
    }

    response = requests.get(url=ENDPOINT,params=PARAMETERS, headers=HEADERS)

    return response


