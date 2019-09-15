import requests
import json

key='AIzaSyBuNaNWHNyEkh0eXdSzWqowMjz6NSNhhuk'
mode='driving'
source = 'silicon park,jankalayan nagar,malad west'
destination = 'LT road,borivali west' 
url='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+source+'&destinations='+destination+'&departure_time=now&key=AIzaSyCpqF94lCsSRaLVRh7w-Q7mT09Aobg1ecc'

print(url)
