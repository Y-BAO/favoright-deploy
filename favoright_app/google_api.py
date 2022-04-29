 
 
import requests
import os
from dotenv import load_dotenv
 
load_dotenv()


print(os.getenv("GOOGLE_MAP_API_KEY"))

API_KEY = os.getenv("GOOGLE_MAP_API_KEY")

def get_google_map_view(address):
    response =  f"https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={address}"
    return response 
    